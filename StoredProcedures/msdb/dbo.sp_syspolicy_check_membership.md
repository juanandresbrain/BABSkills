# dbo.sp_syspolicy_check_membership

**Database:** msdb  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_syspolicy_check_membership"]
    SP --> NoRefs(["No table dependencies detected"])
```

## Table Dependencies

_No table references detected automatically._

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[sp_syspolicy_check_membership]
@role sysname,
@raiserror bit = 1
AS
BEGIN
	-- make sure that the caller is dbo or @role
	IF ( IS_MEMBER(@role) != 1 AND USER_ID() != 1)
	BEGIN
		IF (@raiserror = 1)
		BEGIN
			RAISERROR(15003, -1, -1, @role);
		END
		RETURN 15003;
	END
	
	RETURN 0;
END

dbo,sp_syspolicy_configure,CREATE PROCEDURE [dbo].[sp_syspolicy_configure]
    @name sysname,
    @value sql_variant
AS
BEGIN
	DECLARE @retval_check int;
	EXECUTE @retval_check = [dbo].[sp_syspolicy_check_membership] 'PolicyAdministratorRole'
	IF (0 != @retval_check)
	BEGIN
		RETURN @retval_check
	END

    DECLARE @value_type sysname;
    
    IF (@name=N'Enabled')
    BEGIN
        SET @value_type = CONVERT(sysname, SQL_VARIANT_PROPERTY(@value, 'BaseType'));
        IF (@value_type != 'int')
        BEGIN
            RAISERROR (34021, -1, -1, @name, @value_type);
            RETURN 34021;
        END
       
        EXEC msdb.[dbo].[sp_syspolicy_set_config_enabled] @value;
    END
    ELSE 
    IF (@name = N'HistoryRetentionInDays')
    BEGIN
        SET @value_type = CONVERT(sysname, SQL_VARIANT_PROPERTY(@value, 'BaseType'));
        IF (@value_type != 'int')
        BEGIN
            RAISERROR (34021, -1, -1, @name, @value_type);
            RETURN 34021;
        END
        
        EXEC msdb.[dbo].[sp_syspolicy_set_config_history_retention] @value;
    END
    ELSE
    IF (@name=N'LogOnSuccess')
    BEGIN
        SET @value_type = CONVERT(sysname, SQL_VARIANT_PROPERTY(@value, 'BaseType'));
        IF (@value_type != 'int')
        BEGIN
            RAISERROR (34021, -1, -1, @name, @value_type);
            RETURN 34021;
        END
       
        EXEC msdb.[dbo].[sp_syspolicy_set_log_on_success] @value;
    END
    ELSE 
    BEGIN
        RAISERROR(34020, -1, -1, @name);
        RETURN 34020;
    END
    
    RETURN 0;
END

dbo,sp_syspolicy_create_job,CREATE PROCEDURE [dbo].[sp_syspolicy_create_job] 
@schedule_uid uniqueidentifier,
@is_enabled bit = 0,
@jobID uniqueidentifier OUTPUT
AS
BEGIN
	DECLARE @retval_check int;
	EXECUTE @retval_check = [dbo].[sp_syspolicy_check_membership] 'PolicyAdministratorRole'
	IF ( 0!= @retval_check)
	BEGIN
		RETURN @retval_check
	END

	DECLARE @job_name sysname

	-- create unique job name
	SET @job_name = N'syspolicy_check_schedule_' + LEFT(CONVERT(nvarchar(100), @schedule_uid), 100) 
	WHILE (EXISTS (SELECT * FROM msdb..sysjobs WHERE name = @job_name))
	BEGIN
		SET @job_name = N'syspolicy_check_schedule_' + LEFT(CONVERT(nvarchar(91), @schedule_uid), 91) + '_' + RIGHT(STR(FLOOR(RAND() * 100000000)),8) 
	END

	EXEC  msdb.dbo.sp_add_job @job_name=@job_name, 
			@enabled=@is_enabled, 
			@notify_level_eventlog=0, 
			@notify_level_email=2, 
			@notify_level_netsend=2, 
			@notify_level_page=2, 
			@delete_level=0, 
			@category_id=0, -- [Uncategorized (Local)]
			@job_id = @jobID OUTPUT

	EXEC msdb.dbo.sp_add_jobserver @job_name=@job_name, @server_name = @@servername

    EXEC msdb.dbo.sp_add_jobstep 
            @job_id=@jobID, 
			@step_name=N'Verify that automation is enabled.', 
		    @step_id=1, 
		    @cmdexec_success_code=0, 
		    @on_fail_action=1, 
		    @on_fail_step_id=0, 
		    @retry_attempts=0, 
		    @retry_interval=0, 
		    @os_run_priority=0, 
		    @subsystem=N'TSQL', 
		    @command=N'IF (msdb.dbo.fn_syspolicy_is_automation_enabled() != 1)
        BEGIN
            RAISERROR(34022, 16, 1)
        END', 
		    @database_name=N'master', 
		    @flags=0

	DECLARE @command nvarchar(max)
	SET @command = [dbo].[fn_syspolicy_get_ps_command] (@schedule_uid)

	EXEC msdb.dbo.sp_add_jobstep 
            @job_id=@jobID, 
			@step_name=N'Evaluate policies.', 
			@step_id=2, 
			@cmdexec_success_code=0, 
			@on_success_action=1, 
			@on_fail_action=2, 
			@retry_attempts=0, 
			@retry_interval=0, 
			@os_run_priority=0, 
			@subsystem=N'PowerShell', 
			@command=@command, 
			@flags=0

    EXEC msdb.dbo.sp_update_jobstep 
            @job_id = @jobID, 
            @step_id = 1, 
            @on_success_action=4, 
            @on_success_step_id=2 

	DECLARE @schedule_id int
	SELECT @schedule_id = schedule_id from msdb.dbo.sysschedules where schedule_uid = @schedule_uid

	EXEC msdb.dbo.sp_attach_schedule @job_name = @job_name, @schedule_id = @schedule_id
END

dbo,sp_syspolicy_create_purge_job,CREATE PROCEDURE [dbo].[sp_syspolicy_create_purge_job]
AS
BEGIN
DECLARE @retval_check int;
EXECUTE @retval_check = [dbo].[sp_syspolicy_check_membership] 'PolicyAdministratorRole';
IF ( 0!= @retval_check)
BEGIN
	RETURN @retval_check;
END

-- create a policy history retention maintenance job
-- first check if this job already exists 
IF EXISTS (SELECT * 
            FROM msdb.dbo.syspolicy_configuration c
            WHERE c.name = 'PurgeHistoryJobGuid')
BEGIN
    RETURN;
END

BEGIN TRANSACTION;
DECLARE @ReturnCode INT;
SELECT @ReturnCode = 0;
DECLARE @job_name sysname;
-- create unique job name
SET @job_name = N'syspolicy_purge_history';
WHILE (EXISTS (SELECT * FROM msdb..sysjobs WHERE name = @job_name))
BEGIN
	SET @job_name = N'syspolicy_purge_history_' + RIGHT(STR(FLOOR(RAND() * 100000000)),8);
END

DECLARE @sa_account_name sysname
SET @sa_account_name = SUSER_Name(0x1)

DECLARE @jobId BINARY(16);
EXEC @ReturnCode =  msdb.dbo.sp_add_job 
        @job_name=@job_name, 
		@enabled=1, 
		@notify_level_eventlog=0, 
		@notify_level_email=0, 
		@notify_level_netsend=0, 
		@notify_level_page=0, 
		@delete_level=0, 
		@owner_login_name=@sa_account_name, 
		@job_id = @jobId OUTPUT;
IF (@@ERROR <> 0 OR @ReturnCode <> 0) GOTO QuitWithRollback;

EXEC @ReturnCode = msdb.dbo.sp_add_jobstep 
        @job_id=@jobId, 
        @step_name=N'Verify that automation is enabled.', 
		@step_id=1, 
		@cmdexec_success_code=0, 
		@on_success_action=3, 
		@on_success_step_id=0, 
		@on_fail_action=1, 
		@on_fail_step_id=0, 
		@retry_attempts=0, 
		@retry_interval=0, 
		@os_run_priority=0, 
		@subsystem=N'TSQL', 
		@command=N'IF (msdb.dbo.fn_syspolicy_is_automation_enabled() != 1)
        BEGIN
            RAISERROR(34022, 16, 1)
        END', 
		@database_name=N'master', 
		@flags=0;
IF (@@ERROR <> 0 OR @ReturnCode <> 0) GOTO QuitWithRollback

EXEC @ReturnCode = msdb.dbo.sp_add_jobstep 
        @job_id=@jobId, 
        @step_name=N'Purge history.', 
		@step_id=2, 
		@cmdexec_success_code=0, 
		@on_success_action=3, 
		@on_success_step_id=0, 
		@on_fail_action=2, 
		@on_fail_step_id=0, 
		@retry_attempts=0, 
		@retry_interval=0, 
		@os_run_priority=0, 
		@subsystem=N'TSQL', 
		@command=N'EXEC msdb.dbo.sp_syspolicy_purge_history', 
		@database_name=N'master', 
		@flags=0;
IF (@@ERROR <> 0 OR @ReturnCode <> 0) GOTO QuitWithRollback;

DECLARE @command nvarchar(1000);
SET @command = N'if (''$(ESCAPE_SQUOTE(INST))'' -eq ''MSSQLSERVER'') {$a = ''\DEFAULT''} ELSE {$a = ''''};
(Get-Item SQLSERVER:\SQLPolicy\$(ESCAPE_NONE(SRVR))$a).EraseSystemHealthPhantomRecords()'

EXEC @ReturnCode = msdb.dbo.sp_add_jobstep 
        @job_id=@jobId, 
        @step_name=N'Erase Phantom System Health Records.', 
		@step_id=3, 
		@cmdexec_success_code=0, 
		@on_success_action=1, 
		@on_success_step_id=0, 
		@on_fail_action=2, 
		@on_fail_step_id=0, 
		@retry_attempts=0, 
		@retry_interval=0, 
		@os_run_priority=0, 
		@subsystem=N'PowerShell', 
		@command=@command, 
		@database_name=N'master', 
		@flags=0;
IF (@@ERROR <> 0 OR @ReturnCode <> 0) GOTO QuitWithRollback;

EXEC @ReturnCode = msdb.dbo.sp_update_job @job_id = @jobId, @start_step_id = 1;
IF (@@ERROR <> 0 OR @ReturnCode <> 0) GOTO QuitWithRollback;

EXEC @ReturnCode = msdb.dbo.sp_add_jobserver @job_id = @jobId, @server_name = @@SERVERNAME;
IF (@@ERROR <> 0 OR @ReturnCode <> 0) GOTO QuitWithRollback;

-- run this job every day at 2AM
EXEC @ReturnCode = msdb.dbo.sp_add_jobschedule 
        @job_id=@jobId, 
        @name=N'syspolicy_purge_history_schedule', 
		@enabled=1, 
		@freq_type=4, 
		@freq_interval=1, 
		@freq_subday_type=1, 
		@freq_subday_interval=0, 
		@freq_relative_interval=0, 
		@freq_recurrence_factor=0, 
		@active_start_date=20080101, 
		@active_end_date=99991231, 
		@active_start_time=20000, 
		@active_end_time=235959;
IF (@@ERROR <> 0 OR @ReturnCode <> 0) GOTO QuitWithRollback;

INSERT INTO [msdb].[dbo].[syspolicy_configuration_internal] (name, current_value)
VALUES (N'PurgeHistoryJobGuid', @jobId);

COMMIT TRANSACTION;
RETURN;

QuitWithRollback:
    IF (@@TRANCOUNT > 0) ROLLBACK TRANSACTION;
END

dbo,sp_syspolicy_delete_condition,CREATE PROCEDURE [dbo].[sp_syspolicy_delete_condition] 
@name sysname = NULL,
@condition_id int = NULL
AS
BEGIN
	DECLARE @retval_check int;
	EXECUTE @retval_check = [dbo].[sp_syspolicy_check_membership] 'PolicyAdministratorRole'
	IF ( 0!= @retval_check)
	BEGIN
		RETURN @retval_check
	END

	DECLARE @retval              INT

    EXEC @retval = sp_syspolicy_verify_condition_identifiers @name, @condition_id OUTPUT
    IF (@retval <> 0)
        RETURN (1)

    IF EXISTS (SELECT * FROM msdb.dbo.syspolicy_policies WHERE condition_id = @condition_id)
    BEGIN
        RAISERROR(34012,-1,-1,'Condition','Policy')
        RETURN (1)
    END

    DELETE msdb.dbo.syspolicy_conditions_internal
    WHERE condition_id = @condition_id
    
    RETURN (0)
END

dbo,sp_syspolicy_delete_object_set,CREATE PROCEDURE [dbo].[sp_syspolicy_delete_object_set]
@object_set_name sysname = NULL,
@object_set_id int = NULL
AS
BEGIN
	DECLARE @retval_check int;
	EXECUTE @retval_check = [dbo].[sp_syspolicy_check_membership] 'PolicyAdministratorRole'
	IF ( 0!= @retval_check)
	BEGIN
		RETURN @retval_check
	END

	DECLARE @retval              INT

    EXEC @retval = sp_syspolicy_verify_object_set_identifiers @object_set_name, @object_set_id OUTPUT
    IF (@retval <> 0)
        RETURN (1)

    DELETE msdb.[dbo].[syspolicy_object_sets_internal] 
        WHERE object_set_id = @object_set_id

    RETURN (0)
END

dbo,sp_syspolicy_delete_policy,CREATE PROCEDURE [dbo].[sp_syspolicy_delete_policy] 
@name sysname = NULL,
@policy_id int = NULL
WITH EXECUTE AS OWNER
AS
BEGIN
	DECLARE @retval_check int;
	EXECUTE @retval_check = [dbo].[sp_syspolicy_check_membership] 'PolicyAdministratorRole'
	IF ( 0!= @retval_check)
	BEGIN
		RETURN @retval_check
	END

	DECLARE @retval              INT

    EXEC @retval = sp_syspolicy_verify_policy_identifiers @name, @policy_id OUTPUT
    IF (@retval <> 0)
        RETURN (1)

    DELETE msdb.dbo.syspolicy_policies_internal 
        WHERE policy_id = @policy_id

    RETURN (0)
END

dbo,sp_syspolicy_delete_policy_category,CREATE PROCEDURE [dbo].[sp_syspolicy_delete_policy_category]
@name sysname = NULL,
@policy_category_id int = NULL
AS
BEGIN
	DECLARE @retval_check int;
	EXECUTE @retval_check = [dbo].[sp_syspolicy_check_membership] 'PolicyAdministratorRole'
	IF ( 0!= @retval_check)
	BEGIN
		RETURN @retval_check
	END

	DECLARE @retval              INT

    EXEC @retval = sp_syspolicy_verify_policy_category_identifiers @name, @policy_category_id OUTPUT
    IF (@retval <> 0)
        RETURN (1)

    IF EXISTS (SELECT * FROM msdb.dbo.syspolicy_policy_category_subscriptions WHERE policy_category_id = @policy_category_id)
    BEGIN
        RAISERROR(34012,-1,-1,'Policy Category','Policy Subscription')
        RETURN (1)
    END


    IF EXISTS (SELECT * FROM msdb.dbo.syspolicy_policies WHERE policy_category_id = @policy_category_id)
    BEGIN
        RAISERROR(34012,-1,-1,'Policy Category','Policy')
        RETURN (1)
    END

    DELETE msdb.dbo.syspolicy_policy_categories_internal
    WHERE policy_category_id = @policy_category_id
    
    SET @retval = @@error
    RETURN @retval
END

dbo,sp_syspolicy_delete_policy_category_subscription,CREATE PROCEDURE [dbo].[sp_syspolicy_delete_policy_category_subscription] 
@policy_category_subscription_id int
WITH EXECUTE AS OWNER
AS
BEGIN
    DECLARE @old_policy_category_id INT
    SELECT @old_policy_category_id = policy_category_id 
        FROM dbo.syspolicy_policy_category_subscriptions 
        WHERE policy_category_subscription_id = @policy_category_subscription_id

    DECLARE @group_usage_count INT
    SELECT @group_usage_count = COUNT(name) 
        FROM syspolicy_policies pd 
        WHERE pd.policy_category_id = @old_policy_category_id

    DECLARE @subscription_group_usage_count INT
    SELECT @subscription_group_usage_count = COUNT(*) 
        FROM syspolicy_policy_category_subscriptions  
        WHERE policy_category_id = @old_policy_category_id

    SELECT @group_usage_count = @group_usage_count + @subscription_group_usage_count

    DELETE msdb.dbo.syspolicy_policy_category_subscriptions_internal 
        WHERE policy_category_subscription_id = @policy_category_subscription_id

    IF (@@ROWCOUNT = 0)
    BEGIN
        DECLARE @policy_category_subscription_id_as_char VARCHAR(36)
        SELECT @policy_category_subscription_id_as_char = CONVERT(VARCHAR(36), @policy_category_subscription_id)
        RAISERROR(14262, -1, -1, '@policy_category_subscription_id', @policy_category_subscription_id_as_char)
        RETURN(1) -- Failure
    END

    RETURN (0)
END

dbo,sp_syspolicy_delete_policy_execution_history,CREATE PROC [dbo].[sp_syspolicy_delete_policy_execution_history] 
 @policy_id int,
 @oldest_date datetime
AS
BEGIN
	DECLARE @retval_check int;
	EXECUTE @retval_check = [dbo].[sp_syspolicy_check_membership] 'PolicyAdministratorRole'
	IF ( 0!= @retval_check)
	BEGIN
		RETURN @retval_check
	END

    IF @oldest_date IS NULL
        BEGIN
        IF (@policy_id IS NULL)
            DELETE syspolicy_policy_execution_history_internal
        ELSE
            DELETE syspolicy_policy_execution_history_internal WHERE policy_id = @policy_id
        END
    ELSE
        BEGIN
        IF (@policy_id IS NULL)
            DELETE syspolicy_policy_execution_history_internal WHERE start_date < @oldest_date
        ELSE
            DELETE syspolicy_policy_execution_history_internal WHERE policy_id = @policy_id AND start_date < @oldest_date
        END
END

dbo,sp_syspolicy_delete_target_set,CREATE PROCEDURE [dbo].[sp_syspolicy_delete_target_set] 
@target_set_id int
AS
BEGIN
	DECLARE @retval_check int;
	EXECUTE @retval_check = [dbo].[sp_syspolicy_check_membership] 'PolicyAdministratorRole'
	IF ( 0!= @retval_check)
	BEGIN
		RETURN @retval_check
	END

	DELETE msdb.[dbo].[syspolicy_target_sets_internal] 
		WHERE target_set_id = @target_set_id
	
	IF (@@ROWCOUNT = 0)
	BEGIN
		DECLARE @target_set_id_as_char VARCHAR(36)
		SELECT @target_set_id_as_char = CONVERT(VARCHAR(36), @target_set_id)
		RAISERROR(14262, -1, -1, '@target_set_id', @target_set_id_as_char)
		RETURN (1)
	END

    RETURN (0)
END
```

