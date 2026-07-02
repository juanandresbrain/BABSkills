# managed_backup.sp_backup_master_switch

**Database:** msdb  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["managed_backup.sp_backup_master_switch"]
    managed_backup_sp_add_task_command(["managed_backup.sp_add_task_command"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| managed_backup.sp_add_task_command |

## Stored Procedure Code

```sql
CREATE PROCEDURE managed_backup.sp_backup_master_switch 
	@new_state bit
AS
BEGIN
	IF NOT (HAS_PERMS_BY_NAME(null, null, 'ALTER ANY CREDENTIAL') = 1 AND 
            IS_ROLEMEMBER('db_backupoperator') = 1  AND
	    HAS_PERMS_BY_NAME('sp_delete_backuphistory', 'OBJECT', 'EXECUTE') = 1)
	BEGIN
	   RAISERROR(15247,-1,-1)	
	   RETURN;
	END

	IF @new_state IS NULL
	BEGIN
        RAISERROR (45204, 17, 1, N'@new_state', N'state for master switch');
		RETURN
	END

	EXEC managed_backup.sp_add_task_command @task_name = 'masterswitch', @additional_params = @new_state
END

managed_backup,sp_backup_on_demand,-- Do a backup on-demand by piggybacking on Smart Backup's backup mechanism.
-- @type can be either 'DATABASE' or 'LOG'
--
CREATE PROCEDURE managed_backup.sp_backup_on_demand
	@database_name SYSNAME,
	@type NVARCHAR(32)
AS
BEGIN
 	IF NOT (HAS_PERMS_BY_NAME(null, null, 'ALTER ANY CREDENTIAL') = 1 AND 
            IS_ROLEMEMBER('db_backupoperator') = 1)
	BEGIN
	   RAISERROR(15247,-1,-1)	
	   RETURN;
	END
	SET NOCOUNT ON

	IF (@database_name IS NULL) AND (@database_name = N'')
	BEGIN
        RAISERROR (45204, 17 ,1, N'@database_name', N'database name');
		RETURN
	END

	IF (UPPER(@type) <> 'DATABASE') AND (UPPER(@type) <> 'LOG')
	BEGIN
        RAISERROR (45206, 17, 2);
		RETURN
	END

	DECLARE @db_name_base64 NVARCHAR(MAX);
	DECLARE @input VARBINARY(MAX);
	DECLARE @params NVARCHAR(MAX);

	SET @input = CONVERT(VARBINARY(MAX), @database_name)
	SELECT @db_name_base64 = CAST(N'' as XML).value('xs:base64Binary(sql:variable("@input"))', 'NVARCHAR(MAX)')

	SELECT @params = N'backup_on_demand'+ N' ' + @db_name_base64 + N' ' + @type
	EXEC managed_backup.sp_add_task_command @task_name='backup', @additional_params = @params
END

managed_backup,sp_create_job,CREATE PROCEDURE managed_backup.sp_create_job
    @task_command		NVARCHAR(MAX),
    @task_job_id		UNIQUEIDENTIFIER = NULL OUTPUT,
    @task_job_step_id	UNIQUEIDENTIFIER = NULL OUTPUT
AS
BEGIN
    BEGIN TRANSACTION
    DECLARE @ReturnCode INT
    SELECT @ReturnCode = 0

    DECLARE @jobId BINARY(16)

    DECLARE @jobname NVARCHAR(MAX);
    SET @jobname = 'smart_admin_job_' + CONVERT(NVARCHAR(MAX), NEWID());

    EXEC @ReturnCode = msdb.dbo.sp_agent_add_job @job_name=@jobname, 
        @enabled = 1, 
        @delete_level = 0, 
        @description=N'smart_admin maintenance job.', 
        @job_id = @jobId OUTPUT
    
    IF (@@ERROR <> 0 OR @ReturnCode <> 0) 
    BEGIN
        GOTO QuitWithRollback
    END

    SET @task_job_id = @jobId;

    EXEC @ReturnCode = msdb.dbo.sp_agent_add_jobstep @job_id = @jobId, 
            @step_name=N'smart_admin job step', 
            @step_id=1, 
            @cmdexec_success_code=0, 
            @on_success_action=1, 
            @on_success_step_id=0, 
            @on_fail_action=2, 
            @on_fail_step_id=0, 
            @retry_attempts=0, 
            @retry_interval=0, 
            @os_run_priority=0, 
            @subsystem=N'smartadmin', 
            @command=@task_command, 
            @server=NULL, 
            @database_name=N'master', 
            @flags=48,
            @step_uid = @task_job_step_id OUTPUT

    IF (@@ERROR <> 0 OR @ReturnCode <> 0) GOTO QuitWithRollback

    COMMIT TRANSACTION
    GOTO EndSave
    QuitWithRollback:
    IF (@@TRANCOUNT > 0) 
    BEGIN
        ROLLBACK TRANSACTION
    END
    EndSave:
END
```

