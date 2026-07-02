# dbo.sp_sqlagent_is_srvrolemember

**Database:** msdb  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_sqlagent_is_srvrolemember"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table references detected._

## Stored Procedure Code

```sql
CREATE PROCEDURE sp_sqlagent_is_srvrolemember
   @role_name sysname, @login_name sysname
AS
BEGIN
  DECLARE @is_member        INT
  SET NOCOUNT ON
  
  IF @role_name IS NULL OR @login_name IS NULL
    RETURN(0)
  
  SELECT @is_member = 0
  --IS_SRVROLEMEMBER works only if the login to be tested is provisioned with sqlserver
  if( @login_name = SUSER_SNAME())
    SELECT @is_member = IS_SRVROLEMEMBER(@role_name)
  else
    SELECT @is_member = IS_SRVROLEMEMBER(@role_name, @login_name)
    
  
  --try to impersonate. A try catch is used because we can have @name as NT groups also
  IF @is_member IS NULL
  BEGIN
    BEGIN TRY
      if( is_srvrolemember('sysadmin') = 1)
      begin
      EXECUTE AS LOGIN = @login_name -- impersonate 
        SELECT @is_member = IS_SRVROLEMEMBER(@role_name)  -- check role membership 
      REVERT -- revert back
      end
    END TRY
    BEGIN CATCH
      SELECT @is_member = 0
    END CATCH
  END
 
  RETURN ISNULL(@is_member,0)
END

dbo,sp_sqlagent_log_jobhistory,CREATE PROCEDURE sp_sqlagent_log_jobhistory
  @job_id               UNIQUEIDENTIFIER,
  @step_id              INT,
  @sql_message_id       INT = 0,
  @sql_severity         INT = 0,
  @message              NVARCHAR(4000) = NULL,
  @run_status           INT, -- SQLAGENT_EXEC_X code
  @run_date             INT,
  @run_time             INT,
  @run_duration         INT,
  @operator_id_emailed  INT = 0,
  @operator_id_netsent  INT = 0,
  @operator_id_paged    INT = 0,
  @retries_attempted    INT,
  @server               sysname = NULL,
  @session_id           INT = 0
AS
BEGIN
  DECLARE @retval              INT
  DECLARE @operator_id_as_char VARCHAR(10)
  DECLARE @step_name           sysname
  DECLARE @error_severity      INT

  SET NOCOUNT ON

  IF (@server IS NULL) OR (UPPER(@server collate SQL_Latin1_General_CP1_CS_AS) = '(LOCAL)')
    SELECT @server = UPPER(CONVERT(sysname, SERVERPROPERTY('ServerName')))

  -- Check authority (only SQLServerAgent can add a history entry for a job)
  EXECUTE @retval = sp_verify_jobproc_caller @job_id = @job_id, @program_name = N'SQLAgent%'
  IF (@retval <> 0)
    RETURN(@retval)

  -- NOTE: We raise all errors as informational (sev 0) to prevent SQLServerAgent from caching
  --       the operation (if it fails) since if the operation will never run successfully we
  --       don't want it to stay around in the operation cache.
  SELECT @error_severity = 0

  -- Check job_id
  IF (NOT EXISTS (SELECT *
                  FROM msdb.dbo.sysjobs_view
                  WHERE (job_id = @job_id)))
  BEGIN
    DECLARE @job_id_as_char      VARCHAR(36)
    SELECT @job_id_as_char = CONVERT(VARCHAR(36), @job_id)
    RAISERROR(14262, @error_severity, -1, 'Job', @job_id_as_char)
    RETURN(1) -- Failure
  END

  -- Check step id
  IF (@step_id <> 0) -- 0 means 'for the whole job'
  BEGIN
    SELECT @step_name = step_name
    FROM msdb.dbo.sysjobsteps
    WHERE (job_id = @job_id)
      AND (step_id = @step_id)
    IF (@step_name IS NULL)
    BEGIN
      DECLARE @step_id_as_char     VARCHAR(10)
      SELECT @step_id_as_char = CONVERT(VARCHAR, @step_id)
      RAISERROR(14262, @error_severity, -1, '@step_id', @step_id_as_char)
      RETURN(1) -- Failure
    END
  END
  ELSE
    SELECT @step_name = FORMATMESSAGE(14570)

  -- Check run_status
  IF (@run_status NOT IN (0, 1, 2, 3, 4, 5)) -- SQLAGENT_EXEC_X code
  BEGIN
    RAISERROR(14266, @error_severity, -1, '@run_status', '0, 1, 2, 3, 4, 5')
    RETURN(1) -- Failure
  END

  -- Check run_date
  EXECUTE @retval = sp_verify_job_date @run_date, '@run_date', 10
  IF (@retval <> 0)
    RETURN(1) -- Failure

  -- Check run_time
  EXECUTE @retval = sp_verify_job_time @run_time, '@run_time', 10
  IF (@retval <> 0)
    RETURN(1) -- Failure

  -- Check operator_id_emailed
  IF (@operator_id_emailed <> 0)
  BEGIN
    IF (NOT EXISTS (SELECT *
                    FROM msdb.dbo.sysoperators
                    WHERE (id = @operator_id_emailed)))
    BEGIN
      SELECT @operator_id_as_char = CONVERT(VARCHAR, @operator_id_emailed)
      RAISERROR(14262, @error_severity, -1, '@operator_id_emailed', @operator_id_as_char)
      RETURN(1) -- Failure
    END
  END

  -- Check operator_id_netsent
  IF (@operator_id_netsent <> 0)
  BEGIN
    IF (NOT EXISTS (SELECT *
                    FROM msdb.dbo.sysoperators
                    WHERE (id = @operator_id_netsent)))
    BEGIN
      SELECT @operator_id_as_char = CONVERT(VARCHAR, @operator_id_netsent)
      RAISERROR(14262, @error_severity, -1, '@operator_id_netsent', @operator_id_as_char)
      RETURN(1) -- Failure
    END
  END

  -- Check operator_id_paged
  IF (@operator_id_paged <> 0)
  BEGIN
    IF (NOT EXISTS (SELECT *
                    FROM msdb.dbo.sysoperators
                    WHERE (id = @operator_id_paged)))
    BEGIN
      SELECT @operator_id_as_char = CONVERT(VARCHAR, @operator_id_paged)
      RAISERROR(14262, @error_severity, -1, '@operator_id_paged', @operator_id_as_char)
      RETURN(1) -- Failure
    END
  END

  -- Insert the history row
  INSERT INTO msdb.dbo.sysjobhistory
         (job_id,
          step_id,
          step_name,
          sql_message_id,
          sql_severity,
          message,
          run_status,
          run_date,
          run_time,
          run_duration,
          operator_id_emailed,
          operator_id_netsent,
          operator_id_paged,
          retries_attempted,
          server)
  VALUES (@job_id,
          @step_id,
          @step_name,
          @sql_message_id,
          @sql_severity,
          @message,
          @run_status,
          @run_date,
          @run_time,
          @run_duration,
          @operator_id_emailed,
          @operator_id_netsent,
          @operator_id_paged,
          @retries_attempted,
          @server)

  -- Update sysjobactivity table 
  IF (@step_id = 0) --only update for job, not for each step
  BEGIN
    UPDATE msdb.dbo.sysjobactivity
    SET stop_execution_date = DATEADD(ms, -DATEPART(ms, GetDate()),  GetDate()),
        job_history_id = SCOPE_IDENTITY()
    WHERE
        session_id = @session_id AND job_id = @job_id
  END
  -- Special handling of replication jobs 
  DECLARE @job_name sysname
  DECLARE @category_id int
  SELECT  @job_name = name, @category_id = category_id from msdb.dbo.sysjobs 
   WHERE job_id = @job_id 
 
  -- If replicatio agents (snapshot, logreader, distribution, merge, and queuereader
  -- and the step has been canceled and if we are at the distributor.
  IF @category_id in (10,13,14,15,19) and @run_status = 3 and 
   object_id('MSdistributiondbs') is not null
  BEGIN
    -- Get the database
    DECLARE @database sysname
    SELECT @database = database_name from sysjobsteps where job_id = @job_id and 
   lower(subsystem) in (N'distribution', N'logreader','snapshot',N'merge',
      N'queuereader')
    -- If the database is a distribution database
    IF EXISTS (select * from MSdistributiondbs where name = @database)
    BEGIN
   DECLARE @proc nvarchar(500)
   SELECT @proc = quotename(@database) + N'.dbo.sp_MSlog_agent_cancel'
   EXEC @proc @job_id = @job_id, @category_id = @category_id, 
      @message = @message
    END  
  END

  -- Delete any history rows that are over the registry-defined limits
  IF (@step_id = 0) --only check once per job execution.
  BEGIN
    EXECUTE msdb.dbo.sp_jobhistory_row_limiter @job_id
  END

  RETURN(@@error) -- 0 means success
END

dbo,sp_sqlagent_notify,CREATE PROCEDURE sp_sqlagent_notify
  @op_type     NCHAR(1),                -- One of: J (Job action [refresh or start/stop]),
                                        --         S (Schedule action [refresh only])
                                        --         A (Alert action [refresh only]),
                                        --         G (Re-cache all registry settings),
                                        --         D (Dump job [or job schedule] cache to errorlog)
                                        --         P (Force an immediate poll of the MSX)
                                        --         L (Cycle log file)
                                        --         T (Test WMI parameters (namespace and query))
                                        --         M (DatabaseMail action [ refresh profile  associated with sql agent)
  @job_id      UNIQUEIDENTIFIER = NULL, -- JobID (for OpTypes 'J', 'S' and 'D')
  @schedule_id INT              = NULL, -- ScheduleID (for OpType 'S')
  @alert_id    INT              = NULL, -- AlertID (for OpType 'A')
  @action_type NCHAR(1)         = NULL, -- For 'J' one of: R (Run - no service check),
                                        --                 S (Start - with service check),
                                        --                 I (Insert),
                                        --                 U (Update),
                                        --                 D (Delete),
                                        --                 C (Stop [Cancel])
                                        -- For 'S' or 'A' one of: I (Insert),
                                        --                        U (Update),
                                        --                        D (Delete)
  @error_flag  INT              = 1,    -- Set to 0 to suppress the error from xp_sqlagent_notify if SQLServer agent is not running
  @wmi_namespace nvarchar(128) = NULL,
  @wmi_query     nvarchar(512) = NULL
AS
BEGIN



  DECLARE @retval         INT
  DECLARE @id_as_char     VARCHAR(10)
  DECLARE @job_id_as_char VARCHAR(36)
  DECLARE @nt_user_name   NVARCHAR(100)
   
  

  SET NOCOUNT ON

  SELECT @retval = 0 -- Success

  -- Make sure that we're dealing only with uppercase characters
  SELECT @op_type     = UPPER(@op_type collate SQL_Latin1_General_CP1_CS_AS)
  SELECT @action_type = UPPER(@action_type collate SQL_Latin1_General_CP1_CS_AS)

  -- Verify operation code
  IF (CHARINDEX(@op_type, N'JSAGDPLTM') = 0)
  BEGIN
    RAISERROR(14266, -1, -1, '@op_type', 'J, S, A, G, D, P, L, T, M')
    RETURN(1) -- Failure
  END

  -- Check the job id for those who use it
  IF (CHARINDEX(@op_type, N'JSD') <> 0)
  BEGIN
    IF (NOT ((@op_type = N'D' OR @op_type = N'S') AND (@job_id IS NULL))) -- For 'D' and 'S' job_id is optional
    BEGIN
      IF ((@job_id IS NULL) OR
          ((@action_type <> N'D') AND NOT EXISTS (SELECT *
                                                  FROM msdb.dbo.sysjobs_view
                                                  WHERE (job_id = @job_id))))
      BEGIN
        SELECT @job_id_as_char = CONVERT(VARCHAR(36), @job_id)
        RAISERROR(14262, -1, -1, '@job_id', @job_id_as_char)
        RETURN(1) -- Failure
      END
    END
  END

  -- Verify 'job' action parameters
  IF (@op_type = N'J')
  BEGIN
    SELECT @alert_id = 0
    IF (@schedule_id IS NULL) SELECT @schedule_id = 0

    -- The schedule_id (if specified) is the start step
    IF ((CHARINDEX(@action_type, N'RS') <> 0) AND (@schedule_id <> 0))
    BEGIN
      IF (NOT EXISTS (SELECT *
                      FROM msdb.dbo.sysjobsteps
                      WHERE (job_id = @job_id)
                        AND (step_id = @schedule_id)))
      BEGIN
        SELECT @id_as_char = ISNULL(CONVERT(VARCHAR, @schedule_id), '(null)')
        RAISERROR(14262, -1, -1, '@schedule_id', @id_as_char)
        RETURN(1) -- Failure
      END
    END
    ELSE
      SELECT @schedule_id = 0

    IF (CHARINDEX(@action_type, N'RSIUDC') = 0)
    BEGIN
      RAISERROR(14266, -1, -1, '@action_type', 'R, S, I, U, D, C')
      RETURN(1) -- Failure
    END
  END

  -- Verify 'schedule' action parameters
  IF (@op_type = N'S')
  BEGIN
    SELECT @alert_id = 0

    IF (CHARINDEX(@action_type, N'IUD') = 0)
    BEGIN
      RAISERROR(14266, -1, -1, '@action_type', 'I, U, D')
      RETURN(1) -- Failure
    END

    IF ((@schedule_id IS NULL) OR
        ((@action_type <> N'D') AND NOT EXISTS (SELECT *
                                                FROM msdb.dbo.sysschedules
                                                WHERE (schedule_id = @schedule_id))))
    BEGIN
      SELECT @id_as_char = ISNULL(CONVERT(VARCHAR, @schedule_id), '(null)')
      RAISERROR(14262, -1, -1, '@schedule_id', @id_as_char)
      RETURN(1) -- Failure
    END
  END

  -- Verify 'alert' action parameters
  IF (@op_type = N'A')
  BEGIN
    SELECT @job_id = 0x00
    SELECT @schedule_id = 0

    IF (CHARINDEX(@action_type, N'IUD') = 0)
    BEGIN
      RAISERROR(14266, -1, -1, '@action_type', 'I, U, D')
      RETURN(1) -- Failure
    END

    IF ((@alert_id IS NULL) OR
        ((@action_type <> N'D') AND NOT EXISTS (SELECT *
                                                FROM msdb.dbo.sysalerts
                                                WHERE (id = @alert_id))))
    BEGIN
      SELECT @id_as_char = ISNULL(CONVERT(VARCHAR, @alert_id), '(null)')
      RAISERROR(14262, -1, -1, '@alert_id', @id_as_char)
      RETURN(1) -- Failure
    END
  END

  -- Verify 'registry', 'job dump' and 'force MSX poll' , 'cycle log', dbmail profile refresh action parameters
  IF (CHARINDEX(@op_type, N'GDPLM') <> 0)
  BEGIN
    IF (@op_type <> N'D')
      SELECT @job_id = 0x00
    SELECT @alert_id = 0
    SELECT @schedule_id = 0
    SELECT @action_type = NULL
  END

  -- Parameters are valid, so now check execution permissions...

  -- For anything except a job (or schedule) action the caller must be SysAdmin, DBO, or DB_Owner
  IF (@op_type NOT IN (N'J', N'S'))
  BEGIN
    IF NOT ((ISNULL(IS_SRVROLEMEMBER(N'sysadmin'), 0) = 1) OR
            (ISNULL(IS_MEMBER(N'db_owner'), 0) = 1) OR
            (UPPER(USER_NAME() collate SQL_Latin1_General_CP1_CS_AS) = N'DBO'))
    BEGIN
      RAISERROR(14260, -1, -1)
      RETURN(1) -- Failure
    END
  END

  -- For a Job Action the caller must be SysAdmin, DBO, DB_Owner, or the job owner
  IF (@op_type = N'J')
  BEGIN
    IF NOT ((ISNULL(IS_SRVROLEMEMBER(N'sysadmin'), 0) = 1) OR
            (ISNULL(IS_MEMBER(N'db_owner'), 0) = 1) OR
            (UPPER(USER_NAME() collate SQL_Latin1_General_CP1_CS_AS) = N'DBO') OR
            (EXISTS (SELECT *
                     FROM msdb.dbo.sysjobs_view
                     WHERE (job_id = @job_id))))
    BEGIN
      RAISERROR(14252, -1, -1)
      RETURN(1) -- Failure
    END
  END

  --verify WMI parameters
  IF (@op_type = N'T')
  BEGIN
   SELECT @wmi_namespace = LTRIM(RTRIM(@wmi_namespace))
   SELECT @wmi_query = LTRIM(RTRIM(@wmi_query))  
    IF (@wmi_namespace IS NULL) or (@wmi_query IS NULL)
   BEGIN
          RAISERROR(14508, 16, 1)
          RETURN(1) -- Failure      
   END
  END

  -- Ok, let's do it...
  SELECT @nt_user_name = ISNULL(NT_CLIENT(), ISNULL(SUSER_SNAME(), FORMATMESSAGE(14205)))
  EXECUTE @retval = master.dbo.xp_sqlagent_notify @op_type, @job_id, @schedule_id, @alert_id, @action_type, @nt_user_name, @error_flag, @@trancount, @wmi_namespace, @wmi_query

  RETURN(@retval)
END

dbo,sp_sqlagent_probe_msx,CREATE PROCEDURE sp_sqlagent_probe_msx
  @server_name          sysname,  -- The name of the target server probing the MSX
  @local_time           NVARCHAR(100), -- The local time at the target server in the format YYYY/MM/DD HH:MM:SS
  @poll_interval        INT,           -- The frequency (in seconds) with which the target polls the MSX
  @time_zone_adjustment INT = NULL     -- The offset from GMT in minutes (may be NULL if unknown)
AS
BEGIN
  DECLARE @bad_enlistment        BIT
  DECLARE @blocking_instructions INT
  DECLARE @pending_instructions  INT

  SET NOCOUNT ON

  SELECT @server_name = UPPER(@server_name)
  SELECT @bad_enlistment = 0, @blocking_instructions = 0, @pending_instructions = 0

  UPDATE msdb.dbo.systargetservers
  SET last_poll_date = GETDATE(),
      local_time_at_last_poll = CONVERT(DATETIME, @local_time, 111),
      poll_interval = @poll_interval,
      time_zone_adjustment = ISNULL(@time_zone_adjustment, time_zone_adjustment)
  WHERE (UPPER(server_name) = @server_name)

  -- If the systargetservers entry is missing (and no DEFECT instruction has been posted)
  -- then the enlistment is bad
  IF (NOT EXISTS (SELECT 1
                  FROM msdb.dbo.systargetservers
                  WHERE (UPPER(server_name) = @server_name))) AND
     (NOT EXISTS (SELECT 1
                  FROM msdb.dbo.sysdownloadlist
                  WHERE (target_server = @server_name)
                    AND (operation_code = 7)
                    AND (object_type = 2)))
    SELECT @bad_enlistment = 1

  SELECT @blocking_instructions = COUNT(*)
  FROM msdb.dbo.sysdownloadlist
  WHERE (target_server = @server_name)
    AND (error_message IS NOT NULL)

  SELECT @pending_instructions = COUNT(*)
  FROM msdb.dbo.sysdownloadlist
  WHERE (target_server = @server_name)
    AND (error_message IS NULL)
    AND (status = 0)

  SELECT @bad_enlistment, @blocking_instructions, @pending_instructions
END

dbo,sp_sqlagent_refresh_job,CREATE PROCEDURE sp_sqlagent_refresh_job
  @job_id      UNIQUEIDENTIFIER = NULL,
  @server_name sysname          = NULL -- This parameter allows a TSX to use this SP when updating a job
AS
BEGIN
  DECLARE @server_id INT

  SET NOCOUNT ON

  IF (@server_name IS NULL) OR (UPPER(@server_name collate SQL_Latin1_General_CP1_CS_AS) = '(LOCAL)')
    SELECT @server_name = CONVERT(sysname, SERVERPROPERTY('ServerName'))

  SELECT @server_name = UPPER(@server_name)

  SELECT @server_id = server_id
  FROM msdb.dbo.systargetservers_view
  WHERE (UPPER(server_name) = ISNULL(@server_name, UPPER(CONVERT(sysname, SERVERPROPERTY('ServerName')))))

  SELECT @server_id = ISNULL(@server_id, 0)

  SELECT sjv.job_id,
         sjv.name COLLATE SQL_Latin1_General_CP1_CI_AS,
         sjv.enabled,
         sjv.start_step_id,
         owner = dbo.SQLAGENT_SUSER_SNAME(sjv.owner_sid),
         sjv.notify_level_eventlog,
         sjv.notify_level_email,
         sjv.notify_level_netsend,
         sjv.notify_level_page,
         sjv.notify_email_operator_id,
         sjv.notify_netsend_operator_id,
         sjv.notify_page_operator_id,
         sjv.delete_level,
         has_step = (SELECT COUNT(*)
                     FROM msdb.dbo.sysjobsteps sjst
                     WHERE (sjst.job_id = sjv.job_id)),
         sjv.version_number,
         last_run_date = ISNULL(sjs.last_run_date, 0),
         last_run_time = ISNULL(sjs.last_run_time, 0),
         sjv.originating_server,
         sjv.description COLLATE SQL_Latin1_General_CP1_CI_AS,
         agent_account = CASE sjv.owner_sid
              WHEN 0xFFFFFFFF THEN 1
              ELSE                 0
         END,
		 0 AS is_system
  FROM msdb.dbo.sysjobservers sjs,
       msdb.dbo.sysjobs_view  sjv
  WHERE ((@job_id IS NULL) OR (@job_id = sjv.job_id))
    AND (sjv.job_id = sjs.job_id)
    AND (sjs.server_id = @server_id)
  UNION 
  SELECT
	job_id,
	name COLLATE SQL_Latin1_General_CP1_CI_AS,
	enabled,
	start_step_id,
	N'sa'  AS [owner],
	notify_level_eventlog,
	0 AS notify_level_email,          -- notify_level_email
	0 AS notify_level_netsend,        -- notify_level_netsend
	0 AS notify_level_page,           -- notify_level_page
	0 AS notify_email_operator_id,    -- notify_email_operator_id
	0 AS notify_netsend_operator_id,  -- notify_netsend_operator_id
	0 AS notify_page_operator_id,     -- notify_page_operator_id
	delete_level,
	has_step = (SELECT COUNT(*)
                     FROM sys.fn_sqlagent_jobsteps(j.job_id, NULL) js
                     ),
	0 AS version_number,				-- version_number
	0 AS last_run_date,
	0 AS last_run_time,
	@server_name AS originating_server,
	description COLLATE SQL_Latin1_General_CP1_CI_AS,
	0 AS agent_account,
	1 AS is_system
  FROM sys.fn_sqlagent_jobs(NULL) j
  WHERE ((@job_id IS NULL) OR (@job_id = j.job_id))
  
  RETURN(@@error) -- 0 means success
END

dbo,sp_sqlagent_set_job_completion_state,CREATE PROCEDURE [dbo].[sp_sqlagent_set_job_completion_state]
    @job_id               UNIQUEIDENTIFIER,
    @last_run_outcome     TINYINT,
    @last_outcome_message NVARCHAR(4000),
    @last_run_date        INT,
    @last_run_time        INT,
    @last_run_duration    INT
AS
BEGIN
    -- Update last run date, time for specific job_id in local server
    UPDATE msdb.dbo.sysjobservers 
    SET last_run_outcome =  @last_run_outcome,
        last_outcome_message = @last_outcome_message,
        last_run_date = @last_run_date,
        last_run_time = @last_run_time,
        last_run_duration = @last_run_duration
    WHERE job_id  = @job_id
    AND server_id = 0
END

dbo,sp_sqlagent_set_jobstep_completion_state,CREATE PROCEDURE [dbo].[sp_sqlagent_set_jobstep_completion_state]
    @job_id                UNIQUEIDENTIFIER,
    @step_id               INT,
    @last_run_outcome      INT,
    @last_run_duration     INT,
    @last_run_retries      INT,
    @last_run_date         INT,
    @last_run_time         INT,
    @session_id            INT
AS
BEGIN
    -- Update job step completion state in sysjobsteps as well as sysjobactivity
    UPDATE [msdb].[dbo].[sysjobsteps]
    SET last_run_outcome      = @last_run_outcome,
        last_run_duration     = @last_run_duration,
        last_run_retries      = @last_run_retries,
        last_run_date         = @last_run_date, 
        last_run_time         = @last_run_time 
    WHERE job_id   = @job_id
    AND   step_id  = @step_id

    DECLARE @last_executed_step_date DATETIME 
    SET @last_executed_step_date = [msdb].[dbo].[agent_datetime](@last_run_date, @last_run_time)

    UPDATE [msdb].[dbo].[sysjobactivity]
    SET last_executed_step_date = @last_executed_step_date,
        last_executed_step_id   = @step_id
    WHERE job_id     = @job_id 
    AND   session_id = @session_id
END

dbo,sp_sqlagent_update_agent_xps,CREATE PROCEDURE sp_sqlagent_update_agent_xps
  @new_value        bit = 1  -- the new value for the "Agent XPs" configuration option.
AS
BEGIN
  declare @agent_enabled bit 
  declare @show_advanced bit 
  
  select @show_advanced = cast(value_in_use as bit) 
    from sys.configurations 
    where name = N'show advanced options' 
  
  select @agent_enabled = cast(value_in_use as bit) 
    from sys.configurations 
    where name = N'Agent XPs' 
    
  if @new_value <> @agent_enabled 
  begin 
    if 1 <> @show_advanced 
    begin 
      exec sys.sp_configure @configname = N'show advanced options', @configvalue = 1 
      reconfigure with override 
    end 
    
    exec sys.sp_configure @configname = N'Agent XPs', @configvalue = @new_value 
    reconfigure with override 
    if 1 <> @show_advanced 
    begin 
      exec sys.sp_configure @configname = N'show advanced options', @configvalue = 0 
      reconfigure with override 
    end 
  end
END

dbo,sp_sqlagent_update_jobactivity_next_scheduled_date,CREATE PROCEDURE [dbo].[sp_sqlagent_update_jobactivity_next_scheduled_date]
    @session_id            INT,
    @job_id                UNIQUEIDENTIFIER,
	@is_system             TINYINT = 0,
    @last_run_date         INT,
    @last_run_time         INT
AS
BEGIN
    IF(@is_system = 1)
    BEGIN
		-- TODO:: Call job activity update spec proc
		RETURN
    END

   DECLARE @next_scheduled_run_date DATETIME 
   SET @next_scheduled_run_date = NULL

   -- If last rundate and last runtime is not null then convert date, time to datetime
   IF (@last_run_date IS NOT NULL AND @last_run_time IS NOT NULL)
   BEGIN
        SET @next_scheduled_run_date = [msdb].[dbo].[agent_datetime](@last_run_date, @last_run_time) 
   END
   
   UPDATE [msdb].[dbo].[sysjobactivity]
   SET next_scheduled_run_date = @next_scheduled_run_date 
   WHERE session_id = @session_id 
   AND job_id = @job_id
END

dbo,sp_sqlagent_update_jobactivity_queued_date,CREATE PROCEDURE [dbo].[sp_sqlagent_update_jobactivity_queued_date]
    @session_id               INT,
    @job_id                   UNIQUEIDENTIFIER,
    @is_system             TINYINT = 0
AS
BEGIN
    IF(@is_system = 1)
    BEGIN
		-- TODO:: Call job activity update spec proc
		RETURN
    END
  
    UPDATE [msdb].[dbo].[sysjobactivity] 
    SET queued_date = DATEADD(ms, -DATEPART(ms, GETDATE()),  GETDATE()) 
    WHERE job_id = @job_id 
    AND session_id = @session_id
END

dbo,sp_sqlagent_update_jobactivity_requested_date,CREATE PROCEDURE [dbo].[sp_sqlagent_update_jobactivity_requested_date]
    @session_id               INT,
    @job_id                   UNIQUEIDENTIFIER,
    @is_system             TINYINT = 0,
    @run_requested_source_id  TINYINT
AS
BEGIN
    IF(@is_system = 1)
    BEGIN
		-- TODO:: Call job activity update spec proc
		RETURN
    END

    -- update sysjobactivity for user jobs
    UPDATE [msdb].[dbo].[sysjobactivity] 
    SET run_requested_date = DATEADD(ms, -DATEPART(ms, GETDATE()),  GETDATE()), 
        run_requested_source = CONVERT(SYSNAME, @run_requested_source_id), 
        queued_date = NULL, 
        start_execution_date = NULL, 
        last_executed_step_id = NULL, 
        last_executed_step_date = NULL, 
        stop_execution_date = NULL, 
        job_history_id = NULL, 
        next_scheduled_run_date = NULL 
    WHERE job_id = @job_id 
    AND session_id = @session_id
END

dbo,sp_sqlagent_update_jobactivity_start_execution_date,CREATE PROCEDURE [dbo].[sp_sqlagent_update_jobactivity_start_execution_date]
    @session_id               INT,
    @job_id                   UNIQUEIDENTIFIER,
    @is_system                TINYINT = 0,
    @begin_execution_date     INT,
    @begin_execution_time     INT
AS
BEGIN
    IF(@is_system = 1)
    BEGIN
		-- TODO:: Call job activity update spec proc
		RETURN
    END

   DECLARE @start_execution_date DATETIME 
   SET @start_execution_date = [msdb].[dbo].[agent_datetime](@begin_execution_date, @begin_execution_time) 
   
   UPDATE [msdb].[dbo].[sysjobactivity]
   SET start_execution_date = @start_execution_date
   WHERE session_id = @session_id 
   AND job_id = @job_id
END

dbo,sp_ssis_addfolder,CREATE PROCEDURE [dbo].[sp_ssis_addfolder]
  @parentfolderid uniqueidentifier,
  @name sysname,
  @folderid uniqueidentifier = NULL
AS
   --Check security
   IF (IS_MEMBER('db_ssisltduser')<>1) AND (IS_MEMBER('db_ssisadmin')<>1) AND (IS_SRVROLEMEMBER('sysadmin')<>1)
   BEGIN
       RAISERROR (14591, -1, -1, @name)
       RETURN 1  -- Failure
   END

   --// Security check passed, INSERT now
   INSERT INTO sysssispackagefolders (folderid, parentfolderid, foldername)
   VALUES (ISNULL(@folderid, NEWID()), @parentfolderid, @name)

dbo,sp_ssis_addlogentry,CREATE PROCEDURE [dbo].[sp_ssis_addlogentry]
  @event sysname,
  @computer nvarchar(128),
  @operator nvarchar(128),
  @source nvarchar(1024),
  @sourceid uniqueidentifier,
  @executionid uniqueidentifier,
  @starttime datetime,
  @endtime datetime,
  @datacode int,
  @databytes image,
  @message nvarchar(2048)
AS
  INSERT INTO sysssislog (
      event,
      computer,
      operator,
      source,
      sourceid,
      executionid,
      starttime,
      endtime,
      datacode,
      databytes,
      message )
  VALUES (
      @event,
      @computer,
      @operator,
      @source,
      @sourceid,
      @executionid,
      @starttime,
      @endtime,
      @datacode,
      @databytes,
      @message )
  RETURN 0

dbo,sp_ssis_checkexists,CREATE PROCEDURE [dbo].[sp_ssis_checkexists]
  @name sysname,
  @folderid uniqueidentifier
AS
  SET NOCOUNT ON
  SELECT TOP 1 1 FROM sysssispackages WHERE [name] = @name AND [folderid] = @folderid
  RETURN 0    -- SUCCESS

dbo,sp_ssis_deletefolder,CREATE PROCEDURE [dbo].[sp_ssis_deletefolder]
  @folderid uniqueidentifier
AS
   DECLARE @name  sysname
   DECLARE @count int

   IF @folderid = '00000000-0000-0000-0000-000000000000'
   BEGIN
      RAISERROR (14307, -1, -1, '00000000-0000-0000-0000-000000000000')
      RETURN 1  -- Failure
   END

   SELECT
       @name = [foldername]
   FROM
       sysssispackagefolders
   WHERE
       [folderid] = @folderid
   IF @name IS NOT NULL
   BEGIN
       --// The row exists, check security
       IF (IS_MEMBER('db_ssisadmin')<>1) AND (IS_SRVROLEMEMBER('sysadmin')<>1)
       BEGIN
           IF (IS_MEMBER('db_ssisltduser')<>1)
           BEGIN
               RAISERROR (14307, -1, -1, @name)
               RETURN 1  -- Failure
           END
       END
   END

   -- Get the number of packages in this folder
   SELECT
      @count = count(*)
   FROM
      sysssispackages
   WHERE
      [folderid] = @folderid

   -- Are there any packages in this folder
   IF @count > 0
   BEGIN
      -- Yes, do not delete
      RAISERROR (14593, -1, -1, @name)
      RETURN 1  -- Failure
   END

   -- Get the number of folders in this folder
   SELECT
      @count = count(*)
   FROM
      sysssispackagefolders
   WHERE
      [parentfolderid] = @folderid

   -- Are there any folders in this folder
   IF @count > 0
   BEGIN
      -- Yes, do not delete
      RAISERROR (14593, -1, -1, @name)
      RETURN 1  -- Failure
   END

   DELETE FROM sysssispackagefolders
   WHERE
       [folderid] = @folderid

dbo,sp_ssis_deletepackage,CREATE PROCEDURE [dbo].[sp_ssis_deletepackage]
  @name sysname,
  @folderid uniqueidentifier
AS
  DECLARE @sid varbinary(85)
  DECLARE @writerolesid varbinary(85)
  DECLARE @writerole nvarchar(128)
  SELECT
      @sid = [ownersid],
      @writerolesid = [writerolesid]
  FROM
      sysssispackages
  WHERE
      [name] = @name AND
      [folderid] = @folderid
  IF @sid IS NOT NULL
  BEGIN
      --// The row exists, check security
      IF @writerolesid IS NOT NULL
      BEGIN
          SELECT @writerole = [name] FROM sys.database_principals WHERE [type] = 'R' AND [sid] = @writerolesid
          IF @writerole IS NULL SET @writerole = 'db_ssisadmin'
      END
      IF @writerole IS NULL
      BEGIN
          IF (IS_MEMBER('db_ssisadmin')<>1) AND (IS_SRVROLEMEMBER('sysadmin')<>1)
          BEGIN
              IF (@sid<>SUSER_SID()) OR (IS_MEMBER('db_ssisltduser')<>1)
              BEGIN
                  RAISERROR (14307, -1, -1, @name)
                  RETURN 1  -- Failure
              END
          END
      END
      ELSE
      BEGIN
          -- If writerrole is set for this package, 
          -- Allow sysadmins and the members of writer role to delete this package
          IF (IS_MEMBER(@writerole)<>1)  AND (IS_SRVROLEMEMBER('sysadmin')<>1)
          BEGIN
              IF (@sid<>SUSER_SID()) OR (IS_MEMBER('db_ssisltduser')<>1)
              BEGIN
                  RAISERROR (14307, -1, -1, @name)
                  RETURN 1  -- Failure
              END
          END
      END
  END
  DELETE FROM sysssispackages
  WHERE
      [name] = @name AND
      [folderid] = @folderid

dbo,sp_ssis_getfolder,CREATE PROCEDURE [dbo].[sp_ssis_getfolder]
  @name sysname,
  @parentfolderid uniqueidentifier
AS
  SELECT
   folder.folderid,
   folder.foldername,
   folder.parentfolderid,
   parent.foldername
  FROM
      sysssispackagefolders folder 
  LEFT OUTER JOIN 
      sysssispackagefolders parent
  ON
      folder.parentfolderid = parent.folderid
  WHERE
      folder.foldername = @name AND
      (folder.parentfolderid = @parentfolderid OR 
      (@parentfolderid IS NULL AND folder.parentfolderid IS NULL))

dbo,sp_ssis_getpackage,CREATE PROCEDURE [dbo].[sp_ssis_getpackage]
  @name sysname,
  @folderid uniqueidentifier
AS
  DECLARE @sid varbinary(85)
  DECLARE @isencrypted bit
  DECLARE @readrolesid varbinary(85)
  DECLARE @readrole nvarchar(128)
  --// Check security, if the row exists
  SELECT @sid = [ownersid], @readrolesid = [readrolesid] FROM sysssispackages WHERE [name] = @name AND [folderid] = @folderid
  IF @sid IS NOT NULL
  BEGIN
      IF @readrolesid IS NOT NULL
      BEGIN
          SELECT @readrole = [name] FROM sys.database_principals WHERE [type] = 'R' AND [sid] = @readrolesid
          IF @readrole IS NULL SET @readrole = 'db_ssisadmin'
      END
      IF @readrole IS NOT NULL
      BEGIN
          IF (IS_MEMBER(@readrole)<>1) AND (IS_MEMBER('db_ssisadmin')<>1) AND (IS_SRVROLEMEMBER('sysadmin')<>1)
          BEGIN
              IF (IS_MEMBER('db_ssisltduser')<>1) OR (@sid<>SUSER_SID())
              BEGIN
                  RAISERROR (14307, -1, -1, @name)
                  RETURN 1  -- Failure
              END
          END
      END
      ELSE
      BEGIN
          IF (IS_MEMBER('db_ssisadmin')<>1) AND (IS_SRVROLEMEMBER('sysadmin')<>1) AND (IS_MEMBER('db_ssisoperator')<>1)
          BEGIN
              IF (IS_MEMBER('db_ssisltduser')<>1) OR (@sid<>SUSER_SID())
              BEGIN
                  RAISERROR (14586, -1, -1, @name)
                  RETURN 1  -- Failure
              END
          END
      END
  END

  SELECT
      packagedata
  FROM
      sysssispackages
  WHERE
      [name] = @name AND
      [folderid] = @folderid

dbo,sp_ssis_getpackageroles,CREATE PROCEDURE [dbo].[sp_ssis_getpackageroles]
  @name sysname,
  @folderid uniqueidentifier
AS
  DECLARE @readrolesid varbinary(85)
  DECLARE @writerolesid varbinary(85)
  DECLARE @readrole nvarchar(128)
  DECLARE @writerole nvarchar(128)
  SELECT
      @readrolesid = [readrolesid],
      @writerolesid = [writerolesid]
  FROM
      sysssispackages
  WHERE
      [name] = @name AND
      [folderid] = @folderid
  SELECT @readrole = [name] FROM sys.database_principals WHERE [type] = 'R' AND [sid] = @readrolesid
  SELECT @writerole = [name] FROM sys.database_principals WHERE [type] = 'R' AND [sid] = @writerolesid
  SELECT @readrole AS readrole, @writerole AS writerole

dbo,sp_ssis_listfolders,CREATE PROCEDURE [dbo].[sp_ssis_listfolders]
  @parentfolderid uniqueidentifier = NULL
AS
  SELECT
   folderid,
   parentfolderid,
   foldername
  FROM
      sysssispackagefolders
  WHERE
      [parentfolderid] = @parentfolderid OR 
      (@parentfolderid IS NULL AND [parentfolderid] IS NULL)
  ORDER BY 
      foldername

dbo,sp_ssis_listpackages,CREATE PROCEDURE [dbo].[sp_ssis_listpackages]
  @folderid uniqueidentifier
AS
  SELECT
      name,
      id,
      description,
      createdate,
      folderid,
      datalength(packagedata),
      vermajor,
      verminor,
      verbuild,
      vercomments,
      verid
  FROM
      sysssispackages
  WHERE
      [folderid] = @folderid
  ORDER BY
      name

dbo,sp_ssis_putpackage,CREATE PROCEDURE [dbo].[sp_ssis_putpackage]
  @name sysname,
  @id uniqueidentifier,
  @description nvarchar(1024),
  @createdate datetime,
  @folderid uniqueidentifier,
  @packagedata image,
  @packageformat int,
  @packagetype int,
  @vermajor int,
  @verminor int,
  @verbuild int,
  @vercomments nvarchar(1024),
  @verid uniqueidentifier
AS
  SET NOCOUNT ON
  DECLARE @sid varbinary(85)
  DECLARE @writerolesid varbinary(85)
  DECLARE @writerole nvarchar(128)
  --// Determine if we should INSERT or UPDATE
  SELECT @sid = [ownersid], @writerolesid = [writerolesid] FROM sysssispackages WHERE [name] = @name AND [folderid] = @folderid
  IF @sid IS NOT NULL
  BEGIN
      --// The row exists, check security
      IF @writerolesid IS NOT NULL
      BEGIN
          SELECT @writerole = [name] FROM sys.database_principals WHERE [type] = 'R' AND [sid] = @writerolesid
          IF @writerole IS NULL SET @writerole = 'db_ssisadmin'
      END
      IF @writerole IS NULL
      BEGIN
          IF (IS_MEMBER('db_ssisadmin')<>1) AND (IS_SRVROLEMEMBER('sysadmin')<>1)
          BEGIN
              IF (@sid<>SUSER_SID()) OR (IS_MEMBER('db_ssisltduser')<>1)
              BEGIN
                  RAISERROR (14307, -1, -1, @name)
                  RETURN 1  -- Failure
              END
          END
      END
      ELSE
      BEGIN
          IF (IS_MEMBER(@writerole)<>1) AND (IS_MEMBER('db_ssisadmin')<>1) AND (IS_SRVROLEMEMBER('sysadmin')<>1)
          BEGIN
              IF (@sid<>SUSER_SID()) OR (IS_MEMBER('db_ssisltduser')<>1)
              BEGIN
                  RAISERROR (14307, -1, -1, @name)
                  RETURN 1  -- Failure
              END
          END
      END
      --// Security check passed, UPDATE now
      UPDATE sysssispackages
      SET
          id = @id,
          description = @description,
          createdate = @createdate,
          packagedata = @packagedata,
          packageformat = @packageformat,
          packagetype = @packagetype,
          vermajor = @vermajor,
          verminor = @verminor,
          verbuild = @verbuild,
          vercomments = @vercomments,
          verid = @verid
      WHERE
          name = @name AND folderid = @folderid
  END
  ELSE
  BEGIN
      --// The row does not exist, check security
      IF (IS_MEMBER('db_ssisltduser')<>1) AND (IS_MEMBER('db_ssisadmin')<>1) AND (IS_SRVROLEMEMBER('sysadmin')<>1)
      BEGIN
          RAISERROR (14307, -1, -1, @name)
          RETURN 1  -- Failure
      END
      --// Security check passed, INSERT now
      INSERT INTO sysssispackages (
          name,
          id,
          description,
          createdate,
          folderid,
          ownersid,
          packagedata,
          packageformat,
          packagetype,
          vermajor,
          verminor,
          verbuild,
          vercomments,
          verid )
      VALUES (
          @name,
          @id,
          @description,
          @createdate,
          @folderid,
          SUSER_SID(),
          @packagedata,
          @packageformat,
          @packagetype,
          @vermajor,
          @verminor,
          @verbuild,
          @vercomments,
          @verid )
  END
  RETURN 0    -- SUCCESS

dbo,sp_ssis_renamefolder,CREATE PROCEDURE [dbo].[sp_ssis_renamefolder]
  @folderid uniqueidentifier,
  @name sysname
AS
   --Check security
   IF (IS_MEMBER('db_ssisltduser')<>1) AND (IS_MEMBER('db_ssisadmin')<>1) AND (IS_SRVROLEMEMBER('sysadmin')<>1)
   BEGIN
       RAISERROR (14591, -1, -1, @name)
       RETURN 1  -- Failure
   END

   --// Security check passed, INSERT now
   UPDATE sysssispackagefolders
   SET [foldername] = @name
   WHERE [folderid] = @folderid

dbo,sp_ssis_setpackageroles,CREATE PROCEDURE [dbo].[sp_ssis_setpackageroles]
  @name sysname,
  @folderid uniqueidentifier,
  @readrole nvarchar (128),
  @writerole nvarchar (128)
AS
  SET NOCOUNT ON
  DECLARE @sid varbinary(85)
  --// Determine if we should INSERT or UPDATE
  SELECT @sid = ownersid FROM sysssispackages WHERE name = @name AND folderid = @folderid
  IF @sid IS NOT NULL
  BEGIN
      --// The row exists, check security
      IF (IS_MEMBER('db_ssisadmin')<>1) AND (IS_SRVROLEMEMBER('sysadmin')<>1)
      BEGIN
          IF (@sid<>SUSER_SID())
          BEGIN
              RAISERROR (14307, -1, -1, @name)
              RETURN 1  -- Failure
          END
      END
      --// Security check passed, UPDATE now
      DECLARE @readrolesid varbinary(85)
      DECLARE @writerolesid varbinary(85)
      SELECT @readrolesid = [sid] FROM sys.database_principals WHERE [type] = 'R' AND [name] = @readrole
      SELECT @writerolesid = [sid] FROM sys.database_principals WHERE [type] = 'R' AND [name] = @writerole
      IF @readrolesid IS NULL AND @readrole IS NOT NULL
      BEGIN
          RAISERROR (15014, -1, -1, @readrole)
          RETURN 1
      END
      IF @writerolesid IS NULL AND @writerole IS NOT NULL
      BEGIN
          RAISERROR (15014, -1, -1, @writerole)
          RETURN 1
      END
      UPDATE sysssispackages
      SET
          [readrolesid] = @readrolesid,
          [writerolesid] = @writerolesid
      WHERE
          name = @name AND folderid = @folderid
  END
  ELSE
  BEGIN
      RAISERROR (14307, -1, -1, @name)
      RETURN 1  -- Failure
  END
  RETURN 0    -- SUCCESS

dbo,sp_start_job,CREATE PROCEDURE sp_start_job
  @job_name    sysname          = NULL,
  @job_id      UNIQUEIDENTIFIER = NULL,
  @error_flag  INT              = 1,    -- Set to 0 to suppress the error from sp_sqlagent_notify if SQLServerAgent is not running
  @server_name sysname          = NULL, -- The specific target server to start the [multi-server] job on
  @step_name   sysname          = NULL, -- The name of the job step to start execution with [for use with a local job only]
  @output_flag INT              = 1     -- Set to 0 to suppress the success message
AS
BEGIN
  DECLARE @job_id_as_char VARCHAR(36)
  DECLARE @retval         INT
  DECLARE @step_id        INT
  DECLARE @job_owner_sid  VARBINARY(85)

  SET NOCOUNT ON

  -- Remove any leading/trailing spaces from parameters
  SELECT @job_name    = LTRIM(RTRIM(@job_name))
  SELECT @server_name = UPPER(LTRIM(RTRIM(@server_name)))
  SELECT @step_name   = LTRIM(RTRIM(@step_name))

  -- Turn [nullable] empty string parameters into NULLs
  IF (@job_name = N'')    SELECT @job_name = NULL
  IF (@server_name = N'') SELECT @server_name = NULL
  IF (@step_name = N'')   SELECT @step_name = NULL

  EXECUTE @retval = sp_verify_job_identifiers '@job_name',
                                              '@job_id',
                                               @job_name OUTPUT,
                                               @job_id   OUTPUT,
                                               @owner_sid = @job_owner_sid OUTPUT
  IF (@retval <> 0)
    RETURN(1) -- Failure

  -- Check permissions beyond what's checked by the sysjobs_view
  -- SQLAgentReader role can see all jobs but
  -- cannot start/stop jobs they do not own
  IF (@job_owner_sid <> SUSER_SID()                      -- does not own the job
     AND (ISNULL(IS_SRVROLEMEMBER(N'sysadmin'), 0) = 0)     -- is not sysadmin
     AND (ISNULL(IS_MEMBER(N'SQLAgentOperatorRole'), 0) = 0))  -- is not SQLAgentOperatorRole
  BEGIN
   RAISERROR(14393, -1, -1);  
   RETURN(1) -- Failure
  END

  IF (NOT EXISTS (SELECT *
                  FROM msdb.dbo.sysjobservers
                  WHERE (job_id = @job_id)))
  BEGIN
    SELECT @job_id_as_char = CONVERT(VARCHAR(36), @job_id)
    RAISERROR(14256, -1, -1, @job_name, @job_id_as_char)
    RETURN(1) -- Failure
  END

  IF (EXISTS (SELECT *
              FROM msdb.dbo.sysjobservers
              WHERE (job_id = @job_id)
                AND (server_id = 0)))
  BEGIN
    -- The job is local, so start (run) the job locally

    -- Check the step name (if supplied)
    IF (@step_name IS NOT NULL)
    BEGIN
      SELECT @step_id = step_id
      FROM msdb.dbo.sysjobsteps
      WHERE (step_name = @step_name)
        AND (job_id = @job_id)

      IF (@step_id IS NULL)
      BEGIN
        RAISERROR(14262, -1, -1, '@step_name', @step_name)
        RETURN(1) -- Failure
      END
    END

    EXECUTE @retval = msdb.dbo.sp_sqlagent_notify @op_type     = N'J',
                                                  @job_id      = @job_id,
                                                  @schedule_id = @step_id, -- This is the start step
                                                  @action_type = N'S',
                                                  @error_flag  = @error_flag
    IF ((@retval = 0) AND (@output_flag = 1))
      RAISERROR(14243, 0, 1, @job_name)
  END
  ELSE
  BEGIN
    -- The job is a multi-server job

      -- Only sysadmin can start multi-server job
      IF (ISNULL(IS_SRVROLEMEMBER(N'sysadmin'), 0) <> 1)
      BEGIN
         RAISERROR(14397, -1, -1);
         RETURN(1) -- Failure
      END            

    -- Check target server name (if any)
    IF (@server_name IS NOT NULL)
    BEGIN
      IF (NOT EXISTS (SELECT *
                      FROM msdb.dbo.systargetservers
                      WHERE (UPPER(server_name) = @server_name)))
      BEGIN
        RAISERROR(14262, -1, -1, '@server_name', @server_name)
        RETURN(1) -- Failure
      END
    END

    -- Re-post the job if it's an auto-delete job
    IF ((SELECT delete_level
         FROM msdb.dbo.sysjobs
         WHERE (job_id = @job_id)) <> 0)
      EXECUTE @retval = msdb.dbo.sp_post_msx_operation 'INSERT', 'JOB', @job_id, @server_name

    -- Post start instruction(s)
    EXECUTE @retval = msdb.dbo.sp_post_msx_operation 'START', 'JOB', @job_id, @server_name
  END

  RETURN(@retval) -- 0 means success
END

dbo,sp_stop_job,CREATE PROCEDURE sp_stop_job
  @job_name           sysname          = NULL,
  @job_id             UNIQUEIDENTIFIER = NULL,
  @originating_server sysname          = NULL, -- So that we can stop ALL jobs that came from the given server
  @server_name        sysname        = NULL  -- The specific target server to stop the [multi-server] job on
AS
BEGIN
  DECLARE @job_id_as_char           VARCHAR(36)
  DECLARE @retval                   INT
  DECLARE @num_parameters           INT
  DECLARE @job_owner_sid         VARBINARY(85)
  
  SET NOCOUNT ON

  -- Remove any leading/trailing spaces from parameters
  SELECT @job_name           = LTRIM(RTRIM(@job_name))
  SELECT @originating_server = UPPER(LTRIM(RTRIM(@originating_server)))
  SELECT @server_name        = UPPER(LTRIM(RTRIM(@server_name)))

  -- Turn [nullable] empty string parameters into NULLs
  IF (@job_name           = N'') SELECT @job_name = NULL
  IF (@originating_server = N'') SELECT @originating_server = NULL
  IF (@server_name        = N'') SELECT @server_name = NULL

  -- We must have EITHER a job id OR a job name OR an originating server
  SELECT @num_parameters = 0
  IF (@job_id IS NOT NULL)
    SELECT @num_parameters = @num_parameters + 1
  IF (@job_name IS NOT NULL)
    SELECT @num_parameters = @num_parameters + 1
  IF (@originating_server IS NOT NULL)
    SELECT @num_parameters = @num_parameters + 1
  IF (@num_parameters <> 1)
  BEGIN
    RAISERROR(14232, -1, -1)
    RETURN(1) -- Failure
  END
  
  IF (@originating_server IS NOT NULL)
  BEGIN 
    -- Stop (cancel) ALL local jobs that originated from the specified server
    IF (NOT EXISTS (SELECT *
                    FROM msdb.dbo.sysjobs_view
                    WHERE (originating_server = @originating_server)))
    BEGIN
      RAISERROR(14268, -1, -1, @originating_server)
      RETURN(1) -- Failure
    END

    -- Check permissions beyond what's checked by the sysjobs_view
    -- SQLAgentReader role that can see all jobs but
    -- cannot start/stop jobs they do not own
    IF ((ISNULL(IS_SRVROLEMEMBER(N'sysadmin'), 0) = 0)          -- is not sysadmin
       AND (ISNULL(IS_MEMBER(N'SQLAgentOperatorRole'), 0) = 0)) -- is not SQLAgentOperatorRole
    BEGIN
       RAISERROR(14393, -1, -1);
       RETURN(1) -- Failure
    END

    DECLARE @total_counter   INT
    DECLARE @success_counter INT

    DECLARE stop_jobs CURSOR LOCAL
    FOR
    SELECT job_id
    FROM msdb.dbo.sysjobs_view
    WHERE (originating_server = @originating_server)

    SELECT @total_counter = 0, @success_counter = 0
    OPEN stop_jobs
    FETCH NEXT FROM stop_jobs INTO @job_id
    WHILE (@@fetch_status = 0)
    BEGIN
      SELECT @total_counter + @total_counter + 1
      EXECUTE @retval = msdb.dbo.sp_sqlagent_notify @op_type     = N'J',
                                                    @job_id      = @job_id,
                                                    @action_type = N'C'
      IF (@retval = 0)
        SELECT @success_counter = @success_counter + 1
      FETCH NEXT FROM stop_jobs INTO @job_id
    END
    RAISERROR(14253, 0, 1, @success_counter, @total_counter)
    DEALLOCATE stop_jobs

    RETURN(0) -- 0 means success
  END
  ELSE
  BEGIN
    -- Stop ONLY the specified job
    EXECUTE @retval = sp_verify_job_identifiers '@job_name',
                                                '@job_id',
                                                 @job_name OUTPUT,
                                                 @job_id   OUTPUT,
                                                 @owner_sid = @job_owner_sid OUTPUT
    IF (@retval <> 0)
      RETURN(1) -- Failure

    IF (NOT EXISTS (SELECT *
                    FROM msdb.dbo.sysjobservers
                    WHERE (job_id = @job_id)))
    BEGIN
      SELECT @job_id_as_char = CONVERT(VARCHAR(36), @job_id)
      RAISERROR(14257, -1, -1, @job_name, @job_id_as_char)
      RETURN(1) -- Failure
    END
    
    -- Check permissions beyond what's checked by the sysjobs_view
    -- SQLAgentReader role that can see all jobs but
    -- cannot start/stop jobs they do not own
    IF (@job_owner_sid <> SUSER_SID()                  -- does not own the job
       AND (ISNULL(IS_SRVROLEMEMBER(N'sysadmin'), 0) = 0)       -- is not sysadmin
       AND (ISNULL(IS_MEMBER(N'SQLAgentOperatorRole'), 0) = 0)) -- is not SQLAgentOperatorRole
    BEGIN
     RAISERROR(14393, -1, -1);
     RETURN(1) -- Failure
    END

    IF (EXISTS (SELECT *
                FROM msdb.dbo.sysjobservers
                WHERE (job_id = @job_id)
                  AND (server_id = 0)))
    BEGIN
      -- The job is local, so stop (cancel) the job locally
      EXECUTE @retval = msdb.dbo.sp_sqlagent_notify @op_type     = N'J',
                                                    @job_id      = @job_id,
                                                    @action_type = N'C'
      IF (@retval = 0)
        RAISERROR(14254, 0, 1, @job_name)
    END
    ELSE
    BEGIN
      -- The job is a multi-server job

      -- Only sysadmin can stop multi-server job
      IF (ISNULL(IS_SRVROLEMEMBER(N'sysadmin'), 0) <> 1)
      BEGIN
         RAISERROR(14397, -1, -1);
         RETURN(1) -- Failure
      END            

      -- Check target server name (if any)
      IF (@server_name IS NOT NULL)
      BEGIN
        IF (NOT EXISTS (SELECT *
                        FROM msdb.dbo.systargetservers
                        WHERE (UPPER(server_name) = @server_name)))
        BEGIN
          RAISERROR(14262, -1, -1, '@server_name', @server_name)
          RETURN(1) -- Failure
        END
      END

      -- Post the stop instruction(s)
      EXECUTE @retval = sp_post_msx_operation 'STOP', 'JOB', @job_id, @server_name
    END

    RETURN(@retval) -- 0 means success
  END

END

dbo,sp_syscollector_cleanup_collector,CREATE PROC [dbo].[sp_syscollector_cleanup_collector]
    @collection_set_id INT = NULL
AS
BEGIN
    IF (@collection_set_id IS NOT NULL)
    BEGIN
        DECLARE @retVal int
        EXEC @retVal = dbo.sp_syscollector_verify_collection_set @collection_set_id OUTPUT
        IF (@retVal <> 0)
        BEGIN
            RETURN (1)
        END
    END

    DECLARE @TranCounter INT
    SET @TranCounter = @@TRANCOUNT
    IF (@TranCounter > 0)
        SAVE TRANSACTION tran_cleanup_collection_set
    ELSE
        BEGIN TRANSACTION

    BEGIN TRY
    -- changing isolation level to repeatable to avoid any conflicts that may happen
    -- while running this stored procedure and sp_syscollector_start_collection_set concurrently
    SET TRANSACTION ISOLATION LEVEL REPEATABLE READ

    -- Security check (role membership)
    IF (NOT (ISNULL(IS_MEMBER(N'dc_admin'), 0) = 1) AND NOT (ISNULL(IS_MEMBER(N'db_owner'), 0) = 1))
    BEGIN
        REVERT
        RAISERROR(14677, -1, -1, 'dc_admin')
        RETURN (1)
    END

    -- Disable constraints
    -- this is done to make sure that constraint logic does not interfere with cleanup process
    ALTER TABLE dbo.syscollector_collection_sets_internal NOCHECK CONSTRAINT FK_syscollector_collection_sets_collection_sysjobs
    ALTER TABLE dbo.syscollector_collection_sets_internal NOCHECK CONSTRAINT FK_syscollector_collection_sets_upload_sysjobs

    -- Delete data collector jobs
    DECLARE @job_id uniqueidentifier
    DECLARE datacollector_jobs_cursor CURSOR LOCAL 
    FOR
        SELECT collection_job_id AS job_id FROM syscollector_collection_sets
        WHERE collection_job_id IS NOT NULL
        AND ( collection_set_id = @collection_set_id OR @collection_set_id IS NULL)
        UNION
        SELECT upload_job_id AS job_id FROM syscollector_collection_sets
        WHERE upload_job_id IS NOT NULL
        AND ( collection_set_id = @collection_set_id OR @collection_set_id IS NULL)

    OPEN datacollector_jobs_cursor
    FETCH NEXT FROM datacollector_jobs_cursor INTO @job_id
  
    WHILE (@@fetch_status = 0)
    BEGIN
        IF EXISTS ( SELECT COUNT(job_id) FROM sysjobs WHERE job_id = @job_id )
        BEGIN
            DECLARE @job_name sysname
            SELECT @job_name = name from sysjobs WHERE job_id = @job_id
            PRINT 'Removing job '+ @job_name
            EXEC dbo.sp_delete_job @job_id=@job_id, @delete_unused_schedule=0
        END
        FETCH NEXT FROM datacollector_jobs_cursor INTO @job_id
    END
    
    CLOSE datacollector_jobs_cursor
    DEALLOCATE datacollector_jobs_cursor

    -- Enable Constraints back
    ALTER TABLE dbo.syscollector_collection_sets_internal CHECK CONSTRAINT FK_syscollector_collection_sets_collection_sysjobs
    ALTER TABLE dbo.syscollector_collection_sets_internal CHECK CONSTRAINT FK_syscollector_collection_sets_upload_sysjobs


    -- Disable trigger on syscollector_collection_sets_internal
    -- this is done to make sure that trigger logic does not interfere with cleanup process
    EXEC('DISABLE TRIGGER syscollector_collection_set_is_running_update_trigger ON syscollector_collection_sets_internal')

    -- Set collection sets as not running state and update collect and upload jobs as null
    UPDATE syscollector_collection_sets_internal
    SET is_running = 0, 
        collection_job_id = NULL, 
        upload_job_id = NULL
    WHERE (collection_set_id = @collection_set_id OR @collection_set_id IS NULL)

    -- Enable back trigger on syscollector_collection_sets_internal
    EXEC('ENABLE TRIGGER syscollector_collection_set_is_running_update_trigger ON syscollector_collection_sets_internal')

    -- re-set collector config store if there is no enabled collector
    DECLARE @counter INT
    SELECT @counter= COUNT(is_running) 
    FROM syscollector_collection_sets_internal 
    WHERE is_running = 1

    IF (@counter = 0)  
    BEGIN
        UPDATE syscollector_config_store_internal
        SET parameter_value = 0
        WHERE parameter_name IN ('CollectorEnabled');

        UPDATE syscollector_config_store_internal
        SET parameter_value = NULL
        WHERE parameter_name IN ( 'MDWDatabase', 'MDWInstance' )
    END

    -- Delete collection set logs
    DELETE FROM syscollector_execution_log_internal
    WHERE (collection_set_id = @collection_set_id OR @collection_set_id IS NULL)

    IF (@TranCounter = 0)
    BEGIN
        COMMIT TRANSACTION
    END
    RETURN(0)
    END TRY
    BEGIN CATCH
        IF (@TranCounter = 0 OR XACT_STATE() = -1)
            ROLLBACK TRANSACTION
        ELSE IF (XACT_STATE() = 1)
            ROLLBACK TRANSACTION tran_cleanup_collection_set

        DECLARE @ErrorMessage   NVARCHAR(4000);
        DECLARE @ErrorSeverity  INT;
        DECLARE @ErrorState     INT;
        DECLARE @ErrorNumber    INT;
        DECLARE @ErrorLine      INT;
        DECLARE @ErrorProcedure NVARCHAR(200);
        SELECT @ErrorLine = ERROR_LINE(),
               @ErrorSeverity = ERROR_SEVERITY(),
               @ErrorState = ERROR_STATE(),
               @ErrorNumber = ERROR_NUMBER(),
               @ErrorMessage = ERROR_MESSAGE(),
               @ErrorProcedure = ISNULL(ERROR_PROCEDURE(), '-');
        RAISERROR (14684, @ErrorSeverity, -1 , @ErrorNumber, @ErrorSeverity, @ErrorState, @ErrorProcedure, @ErrorLine, @ErrorMessage);
        RETURN (1)
    END CATCH
END

dbo,sp_syscollector_configure_sql_dumper,CREATE PROCEDURE [dbo].[sp_syscollector_configure_sql_dumper]
    @collection_set_id        int = NULL,
    @name                    sysname = NULL,
    @dump_on_any_error      bit = NULL,                -- configure SQL dumper to dump on any SSIS errors
    @dump_on_codes          nvarchar(max) = NULL    -- configure SQL dumper to dump when we hit one of the specified SSIS errors. Set to N'' to remove the codes.
AS
BEGIN
    -- Security check (role membership)
    IF (NOT (ISNULL(IS_MEMBER(N'dc_admin'), 0) = 1) AND NOT (ISNULL(IS_MEMBER(N'db_owner'), 0) = 1))
    BEGIN
        RAISERROR(14677, -1, -1, 'dc_admin')
        RETURN(1) -- Failure
    END

    DECLARE @retVal int
    EXEC @retVal = dbo.sp_syscollector_verify_collection_set @collection_set_id OUTPUT, @name OUTPUT
    IF (@retVal <> 0)
        RETURN (1)

    DECLARE @is_running bit
    SELECT    @is_running = is_running
    FROM dbo.syscollector_collection_sets
    WHERE collection_set_id = @collection_set_id
    IF (@is_running = 1)
    BEGIN
        RAISERROR(14711, 0, 1)
    END

    IF (@dump_on_codes = N'')
    BEGIN
        UPDATE [dbo].[syscollector_collection_sets_internal]
        SET dump_on_codes = NULL
        WHERE @collection_set_id = collection_set_id
    END
    ELSE IF (@dump_on_codes IS NOT NULL)
    BEGIN
        UPDATE [msdb].[dbo].[syscollector_collection_sets_internal]
        SET dump_on_codes = @dump_on_codes
        WHERE @collection_set_id = collection_set_id
    END    

    IF (@dump_on_any_error IS NOT NULL)
    BEGIN
        UPDATE [msdb].[dbo].[syscollector_collection_sets_internal]
        SET dump_on_any_error = @dump_on_any_error
        WHERE @collection_set_id = collection_set_id
    END

    RETURN (0)
END

dbo,sp_syscollector_create_collection_item,CREATE PROCEDURE [dbo].[sp_syscollector_create_collection_item]
    @collection_set_id        int,
    @collector_type_uid        uniqueidentifier,
    @name                    sysname,
    @frequency                int = 5,                -- set by default to the minimum frequency
    @parameters                xml = NULL,
    @collection_item_id        int OUTPUT
AS
BEGIN
    DECLARE @TranCounter INT
    SET @TranCounter = @@TRANCOUNT
    IF (@TranCounter > 0)
        SAVE TRANSACTION tran_create_collection_item
    ELSE
        BEGIN TRANSACTION
    BEGIN TRY
        -- Security check (role membership)
        IF (NOT (ISNULL(IS_MEMBER(N'dc_admin'), 0) = 1) AND NOT (ISNULL(IS_MEMBER(N'db_owner'), 0) = 1))
        BEGIN
            RAISERROR(14677, -1, -1, 'dc_admin')
            RETURN (1)
        END

        DECLARE @is_system bit
        SELECT    @is_system = is_system
        FROM dbo.syscollector_collection_sets
        WHERE collection_set_id = @collection_set_id
        
        IF (@is_system = 1)
        BEGIN
            -- cannot update, delete, or add new collection items to a system collection set
            RAISERROR(14696, -1, -1);
            RETURN (1)
        END

        SET @name            = NULLIF(LTRIM(RTRIM(@name)), N'')
        IF (@name IS NULL) 
        BEGIN
            RAISERROR(21263, -1, -1, '@name')
            RETURN (1)
        END
        
        IF (@frequency < 5)
        BEGIN
            DECLARE @frequency_as_char VARCHAR(36)
            SELECT @frequency_as_char = CONVERT(VARCHAR(36), @frequency)
            RAISERROR(21405, 16, -1, @frequency_as_char, '@frequency', 5)
            RETURN (1)
        END

        IF (NOT EXISTS(SELECT * from dbo.syscollector_collector_types
            WHERE @collector_type_uid = collector_type_uid))
        BEGIN
            DECLARE @collector_type_uid_as_char VARCHAR(36)
            SELECT @collector_type_uid_as_char = CONVERT(VARCHAR(36), @collector_type_uid)
            RAISERROR(14262, -1, -1, '@collector_type_uid', @collector_type_uid_as_char)
            RETURN (1)
        END
        
        IF (NOT EXISTS(SELECT * from dbo.syscollector_collection_sets
            WHERE @collection_set_id = collection_set_id))
        BEGIN
            DECLARE @collection_set_id_as_char VARCHAR(36)
            SELECT @collection_set_id_as_char = CONVERT(VARCHAR(36), @collection_set_id)
            RAISERROR(14262, -1, -1, '@collection_set_id', @collection_set_id_as_char)
            RETURN (1)
        END

        DECLARE @is_running bit
        SELECT    @is_running = is_running
        FROM dbo.syscollector_collection_sets
        WHERE collection_set_id = @collection_set_id
        IF (@is_running = 1)
        BEGIN
            RAISERROR(14675, -1, -1, @name)
            RETURN (1)
        END

        IF (@parameters IS NULL)
        BEGIN
            DECLARE @parameter_schema xml
            SELECT @parameter_schema = parameter_schema FROM syscollector_collector_types WHERE collector_type_uid = @collector_type_uid
            IF (@parameter_schema IS NOT NULL)    -- only allows parameters to be null if the collector type has a null schema
            BEGIN
                RAISERROR(21263, -1, -1, '@parameters')
                RETURN (1)
            END
        END
        ELSE IF (LTRIM(RTRIM(CONVERT(nvarchar(max), @parameters))) <> N'') -- don't check if the parameters are empty string
        BEGIN
            EXEC dbo.sp_syscollector_validate_xml @collector_type_uid = @collector_type_uid, @parameters = @parameters
        END

        INSERT INTO [dbo].[syscollector_collection_items_internal]
        (
            collection_set_id,
            collector_type_uid,
            name,
            frequency,
            parameters
        )
        VALUES
        (
            @collection_set_id,
            @collector_type_uid,
            @name,
            @frequency,
            @parameters
        )

        SET @collection_item_id = SCOPE_IDENTITY()

        IF (@collection_item_id IS NULL)
        BEGIN
            DECLARE @collection_item_id_as_char VARCHAR(36)
            SELECT @collection_item_id_as_char = CONVERT(VARCHAR(36), @collection_item_id)
            RAISERROR(14262, -1, -1, '@collection_item_id', @collection_item_id_as_char)
            RETURN (1)
        END

        IF (@TranCounter = 0)
            COMMIT TRANSACTION
        RETURN (0)
    END TRY
    BEGIN CATCH
        IF (@TranCounter = 0 OR XACT_STATE() = -1)
            ROLLBACK TRANSACTION
        ELSE IF (XACT_STATE() = 1)
            ROLLBACK TRANSACTION tran_create_collection_item

        DECLARE @ErrorMessage   NVARCHAR(4000);
        DECLARE @ErrorSeverity  INT;
        DECLARE @ErrorState     INT;
        DECLARE @ErrorNumber    INT;
        DECLARE @ErrorLine      INT;
        DECLARE @ErrorProcedure NVARCHAR(200);
        SELECT @ErrorLine = ERROR_LINE(),
               @ErrorSeverity = ERROR_SEVERITY(),
               @ErrorState = ERROR_STATE(),
               @ErrorNumber = ERROR_NUMBER(),
               @ErrorMessage = ERROR_MESSAGE(),
               @ErrorProcedure = ISNULL(ERROR_PROCEDURE(), '-');

        RAISERROR (14684, @ErrorSeverity, -1 , @ErrorNumber, @ErrorSeverity, @ErrorState, @ErrorProcedure, @ErrorLine, @ErrorMessage);
        
        RETURN (1)
    END CATCH
END

dbo,sp_syscollector_create_collection_set,CREATE PROCEDURE [dbo].[sp_syscollector_create_collection_set]
    @name                        sysname,
    @target                        nvarchar(128) = NULL,
    @collection_mode            smallint = 0,    -- 0: cached, 1: non-cached
    @days_until_expiration      smallint = 730, -- two years
    @proxy_id                   int = NULL,     -- mutual exclusive; must specify either proxy_id or proxy_name to identify the proxy
    @proxy_name                    sysname = NULL,
    @schedule_uid               uniqueidentifier = NULL, 
    @schedule_name              sysname = NULL, -- mutual exclusive; must specify either schedule_uid or schedule_name to identify the schedule
    @logging_level                smallint = 1,
    @description                nvarchar(4000) = NULL,
    @collection_set_id            int OUTPUT,
    @collection_set_uid            uniqueidentifier = NULL OUTPUT
WITH EXECUTE AS OWNER -- 'MS_DataCollectorInternalUser'
AS
BEGIN
    DECLARE @TranCounter INT
    SET @TranCounter = @@TRANCOUNT
    IF (@TranCounter > 0)
        SAVE TRANSACTION tran_create_collection_set
    ELSE
        BEGIN TRANSACTION

    BEGIN TRY

    -- Security check (role membership)
    EXECUTE AS CALLER;
    IF (NOT (ISNULL(IS_MEMBER(N'dc_admin'), 0) = 1) AND NOT (ISNULL(IS_MEMBER(N'db_owner'), 0) = 1))
    BEGIN
        REVERT;
        RAISERROR(14677, -1, -1, 'dc_admin')
        RETURN (1)
    END
    REVERT;

    -- Remove any leading/trailing spaces from parameters
    SET @name                    = NULLIF(LTRIM(RTRIM(@name)), N'')
    SET @proxy_name                = NULLIF(LTRIM(RTRIM(@proxy_name)), N'')
    SET @schedule_name            = NULLIF(LTRIM(RTRIM(@schedule_name)), N'')
    SET @target                    = NULLIF(LTRIM(RTRIM(@target)), N'')
    SET @description            = LTRIM(RTRIM(@description))

    IF (@name IS NULL)
    BEGIN
        RAISERROR(21263, -1, -1, '@name')
        RETURN (1)
    END

    -- can't have both name and uid for the schedule
    IF (@schedule_uid IS NOT NULL) AND (@schedule_name IS NOT NULL)
    BEGIN
        RAISERROR(14373, -1, -1, '@schedule_uid', '@schedule_name')
        RETURN (1)
    END

    -- Execute the check for the schedule as caller to ensure only schedules owned by caller can be attached
    EXECUTE AS CALLER;

    DECLARE @schedule_id int
    IF (@schedule_uid IS NOT NULL)
    BEGIN
        SElECT @schedule_id = schedule_id FROM sysschedules_localserver_view WHERE @schedule_uid = schedule_uid
    
        IF (@schedule_id IS NULL)
        BEGIN
            DECLARE @schedule_uid_as_char VARCHAR(36)
            SELECT @schedule_uid_as_char = CONVERT(VARCHAR(36), @schedule_uid)
            REVERT;
            RAISERROR(14262, -1, -1, N'@schedule_uid', @schedule_uid_as_char)
            RETURN (1)
        END
    END
    ELSE IF (@schedule_name IS NOT NULL)
    BEGIN
        SELECT @schedule_id = schedule_id, @schedule_uid = schedule_uid FROM sysschedules_localserver_view WHERE name = @schedule_name 
    
        IF (@schedule_id IS NULL)
        BEGIN
            REVERT;
            RAISERROR(14262, -1, -1, N'@schedule_name', @schedule_name)
            RETURN (1)
        END
    END

    REVERT;

    -- if collection_mode is cached, make sure schedule_id is not null
    IF    (@collection_mode = 0 AND @schedule_id IS NULL)
    BEGIN
        RAISERROR(14683, -1, -1)    
        RETURN (1)
    END    

    IF (@proxy_id IS NOT NULL) OR (@proxy_name IS NOT NULL) 
    BEGIN
        -- check if the proxy exists
        EXEC sp_verify_proxy_identifiers '@proxy_name',
                                         '@proxy_id',
                                         @proxy_name OUTPUT,
                                         @proxy_id   OUTPUT

        -- check if proxy_id is granted to dc_admin
        IF (@proxy_id NOT IN (SELECT proxy_id 
                              FROM sysproxylogin 
                              WHERE sid = USER_SID(USER_ID('dc_admin'))
                              )
            )
        BEGIN
            RAISERROR(14719, -1, -1, N'dc_admin')
            RETURN (1)
        END
    END

    IF (@collection_mode < 0 OR @collection_mode > 1)
    BEGIN
        RAISERROR(14266, -1, -1, '@collection_mode', '0, 1')
        RETURN (1)
    END

    IF (@logging_level < 0 OR @logging_level > 2)
    BEGIN
        RAISERROR(14266, -1, -1, '@logging_level', '0, 1, or 2')
        RETURN (1)
    END

    IF (@collection_set_uid IS NULL)
    BEGIN
        SET @collection_set_uid = NEWID()
    END

    IF (@days_until_expiration < 0)
    BEGIN
        RAISERROR(14266, -1, -1, '@days_until_expiration', '>= 0')
        RETURN (1)
    END

    INSERT INTO [dbo].[syscollector_collection_sets_internal]
    (
        collection_set_uid,
        schedule_uid,
        name,
        target,
        is_running,
        proxy_id,
        is_system,
        upload_job_id,
        collection_job_id,
        collection_mode,
        logging_level,
        days_until_expiration,
        description
    )
    VALUES
    (
        @collection_set_uid,
        @schedule_uid,
        @name,
        @target,
        0,
        @proxy_id,
        0,
        NULL,
        NULL,
        @collection_mode,
        @logging_level,
        @days_until_expiration,
        @description
    )

    SET @collection_set_id = SCOPE_IDENTITY()

    IF (@collection_set_id IS NULL)
    BEGIN
        DECLARE @collection_set_id_as_char VARCHAR(36)
        SELECT @collection_set_id_as_char = CONVERT(VARCHAR(36), @collection_set_id)
        RAISERROR(14262, -1, -1, '@collection_set_id', @collection_set_id_as_char)
        RETURN (1)
    END

    IF (@TranCounter = 0)
        COMMIT TRANSACTION
    RETURN (0)

    END TRY
    BEGIN CATCH
        IF (@TranCounter = 0 OR XACT_STATE() = -1)
            ROLLBACK TRANSACTION
        ELSE IF (XACT_STATE() = 1)
            ROLLBACK TRANSACTION tran_create_collection_set

        DECLARE @ErrorMessage   NVARCHAR(4000);
        DECLARE @ErrorSeverity  INT;
        DECLARE @ErrorState     INT;
        DECLARE @ErrorNumber    INT;
        DECLARE @ErrorLine      INT;
        DECLARE @ErrorProcedure NVARCHAR(200);
        SELECT @ErrorLine = ERROR_LINE(),
               @ErrorSeverity = ERROR_SEVERITY(),
               @ErrorState = ERROR_STATE(),
               @ErrorNumber = ERROR_NUMBER(),
               @ErrorMessage = ERROR_MESSAGE(),
               @ErrorProcedure = ISNULL(ERROR_PROCEDURE(), '-');
        RAISERROR (14684, @ErrorSeverity, -1 , @ErrorNumber, @ErrorSeverity, @ErrorState, @ErrorProcedure, @ErrorLine, @ErrorMessage);

        RETURN (1)        
    END CATCH
END

dbo,sp_syscollector_create_collector_type,CREATE PROCEDURE [dbo].[sp_syscollector_create_collector_type]
    @collector_type_uid            uniqueidentifier = NULL OUTPUT,
    @name                        sysname,
    @parameter_schema            xml = NULL,
    @parameter_formatter        xml = NULL,
    @collection_package_id        uniqueidentifier,
    @upload_package_id            uniqueidentifier
AS
BEGIN
    DECLARE @TranCounter INT
    SET @TranCounter = @@TRANCOUNT
    IF (@TranCounter > 0)
        SAVE TRANSACTION tran_create_collector_type
    ELSE
        BEGIN TRANSACTION
    BEGIN TRY

    -- Security check (role membership)
    IF (NOT (ISNULL(IS_MEMBER(N'dc_admin'), 0) = 1) AND NOT (ISNULL(IS_MEMBER(N'db_owner'), 0) = 1))
    BEGIN
        RAISERROR(14677, -1, -1, 'dc_admin')
        RETURN (1)
    END

    SET @name                = NULLIF(LTRIM(RTRIM(@name)), N'')
    IF (@name IS NULL) 
    BEGIN
        RAISERROR(21263, -1, -1, '@name', @name)
        RETURN (1)
    END

    IF (@collector_type_uid IS NULL) 
    BEGIN
        SET @collector_type_uid = NEWID()
    END
    
    IF (NOT EXISTS(SELECT * from sysssispackages
        WHERE @collection_package_id = id))
    BEGIN
        DECLARE @collection_package_id_as_char VARCHAR(36)
        SELECT @collection_package_id_as_char = CONVERT(VARCHAR(36), @collection_package_id)
        RAISERROR(14262, -1, -1, '@collection_package_id', @collection_package_id_as_char)
        RETURN (1)
    END

    IF (NOT EXISTS(SELECT * from sysssispackages
        WHERE @upload_package_id = id))
    BEGIN
        DECLARE @upload_package_id_as_char VARCHAR(36)
        SELECT @upload_package_id_as_char = CONVERT(VARCHAR(36), @upload_package_id)
        RAISERROR(14262, -1, -1, '@upload_package_id', @upload_package_id_as_char)
        RETURN (1)
    END

    DECLARE @collection_package_name sysname
    DECLARE @collection_package_folderid uniqueidentifier
    DECLARE @upload_package_name sysname
    DECLARE @upload_package_folderid uniqueidentifier    

    SELECT 
        @collection_package_name = name,
        @collection_package_folderid = folderid
    FROM sysssispackages
    WHERE @collection_package_id = id

    SELECT 
        @upload_package_name = name,
        @upload_package_folderid = folderid
    FROM sysssispackages
    WHERE @upload_package_id = id

    DECLARE @schema_collection sysname
    IF (@parameter_schema IS NOT NULL)
    BEGIN
        SET @schema_collection = N'schema_collection_' + @name
        WHILE (EXISTS (SELECT * FROM sys.xml_schema_collections WHERE name = @schema_collection))
        BEGIN
            SET @schema_collection = LEFT(@schema_collection, 119) + '_' + RIGHT(STR(FLOOR(RAND() * 100000000)),8)
        END

        DECLARE @retVal int
        DECLARE @sql_string nvarchar(2048)
        DECLARE @param_definition nvarchar(16)
        SET @param_definition = N'@schema xml'
        SET @sql_string = N'CREATE XML SCHEMA COLLECTION ' + QUOTENAME(@schema_collection, '[') + N' AS @schema; '
        SET @sql_string = @sql_string + N'GRANT EXECUTE ON XML SCHEMA COLLECTION::[dbo].' + QUOTENAME(@schema_collection, '[') + N' TO dc_admin; ' 
        SET @sql_string = @sql_string + N'GRANT VIEW DEFINITION ON XML SCHEMA COLLECTION::[dbo].' + QUOTENAME(@schema_collection, '[') + N' TO dc_admin; '

        EXEC sp_executesql @sql_string, @param_definition, @schema = @parameter_schema
    END

    INSERT INTO [dbo].[syscollector_collector_types_internal]
    (
        collector_type_uid,
        name,
        parameter_schema,
        parameter_formatter,
        schema_collection,
        collection_package_name,
        collection_package_folderid,
        upload_package_name,
        upload_package_folderid
    )
    VALUES
    (
        @collector_type_uid,
        @name,
        @parameter_schema,
        @parameter_formatter,
        @schema_collection,
        @collection_package_name,
        @collection_package_folderid,
        @upload_package_name,
        @upload_package_folderid
    )

    IF (@TranCounter = 0)
        COMMIT TRANSACTION
    RETURN (0)
    END TRY
    BEGIN CATCH
        IF (@TranCounter = 0 OR XACT_STATE() = -1)
            ROLLBACK TRANSACTION
        ELSE IF (XACT_STATE() = 1)
            ROLLBACK TRANSACTION tran_create_collector_type

        DECLARE @ErrorMessage   NVARCHAR(4000);
        DECLARE @ErrorSeverity  INT;
        DECLARE @ErrorState     INT;
        DECLARE @ErrorNumber    INT;
        DECLARE @ErrorLine      INT;
        DECLARE @ErrorProcedure NVARCHAR(200);
        SELECT @ErrorLine = ERROR_LINE(),
               @ErrorSeverity = ERROR_SEVERITY(),
               @ErrorState = ERROR_STATE(),
               @ErrorNumber = ERROR_NUMBER(),
               @ErrorMessage = ERROR_MESSAGE(),
               @ErrorProcedure = ISNULL(ERROR_PROCEDURE(), '-');

        RAISERROR (14684, @ErrorSeverity, -1 , @ErrorNumber, @ErrorSeverity, @ErrorState, @ErrorProcedure, @ErrorLine, @ErrorMessage);

        RETURN (1)    
    END CATCH
END

dbo,sp_syscollector_create_jobs,CREATE PROCEDURE [dbo].[sp_syscollector_create_jobs]
    @collection_set_id        int,
    @collection_set_uid        uniqueidentifier,
    @collection_set_name    sysname,
    @proxy_id                int = NULL,
    @schedule_id            int = NULL,
    @collection_mode        smallint,
    @collection_job_id        uniqueidentifier OUTPUT,
    @upload_job_id            uniqueidentifier OUTPUT
AS
BEGIN
    SET NOCOUNT ON

    DECLARE @TranCounter INT
    SET @TranCounter = @@TRANCOUNT
    IF (@TranCounter > 0)
        SAVE TRANSACTION tran_syscollector_create_jobs
    ELSE
        BEGIN TRANSACTION

    BEGIN TRY

    -- job step names and commands shared between collection modes
    DECLARE @collection_set_id_as_char nvarchar(36)

    DECLARE @collection_step_command nvarchar(512)
    DECLARE @upload_step_command nvarchar(512)
    DECLARE @autostop_step_command nvarchar(512)
    DECLARE @purge_step_command nvarchar(1024)

    DECLARE @collection_step_name sysname
    DECLARE @upload_step_name sysname
    DECLARE @autostop_step_name sysname
    DECLARE @purge_step_name sysname

    DECLARE @job_name sysname
    DECLARE @job_id uniqueidentifier        
    DECLARE @description nvarchar(512)

    IF(@collection_set_id IS NOT NULL)
    BEGIN
        SET @collection_set_id_as_char = CONVERT(NVARCHAR(36), @collection_set_id)
        SET @collection_step_command = 
            N'dcexec -c -s ' + @collection_set_id_as_char + N' -i "$(ESCAPE_DQUOTE(MACH))\$(ESCAPE_DQUOTE(INST))"' + 
            N' -m ' + CONVERT(NVARCHAR(36), @collection_mode);
        SET @upload_step_command = 
            N'dcexec -u -s ' + @collection_set_id_as_char + N' -i "$(ESCAPE_DQUOTE(MACH))\$(ESCAPE_DQUOTE(INST))"';
        SET @autostop_step_command =
            N'exec dbo.sp_syscollector_stop_collection_set @collection_set_id=' + @collection_set_id_as_char 
            + N', @stop_collection_job = 0';  -- do not stop the collection job, otherwise you will abort yourself!
        SET @purge_step_command = 
            N'
            EXEC [dbo].[sp_syscollector_purge_collection_logs]
            '
    END

    -- verify that the proxy_id exists
    IF (@proxy_id IS NOT NULL)
    BEGIN
        DECLARE @proxy_name sysname
        DECLARE @retVal int
        -- this will throw an error of proxy_id does not exist
        EXEC @retVal = msdb.dbo.sp_verify_proxy_identifiers '@proxy_name', '@proxy_id', @proxy_name OUTPUT, @proxy_id OUTPUT
        IF (@retVal <> 0)
            RETURN (0)
    END

    -- add jobs, job steps and attach schedule separately for different modes
    IF (@collection_mode = 1)    -- non-cached mode
    BEGIN
        -- create 1 job and 2 steps, first for collection & upload, second for log purging
        SET @job_name = N'collection_set_' + @collection_set_id_as_char + '_noncached_collect_and_upload'
        SET @collection_step_name = @job_name + '_collect'
        SET @upload_step_name = @job_name + '_upload'
        SET @purge_step_name = @job_name + '_purge_logs'
        SET @description = N'Data Collector job for collection set ' + QUOTENAME(@collection_set_name)

        -- add agent job and job server
        EXEC dbo.sp_add_job 
            @job_name        = @job_name,
            @category_id    = 8, -- N'Data Collector'
            @enabled        = 0,
            @description    = @description,
            @job_id            = @job_id OUTPUT
        
        EXEC dbo.sp_add_jobserver
            @job_id            = @job_id,
            @server_name    = N'(local)'

        -- add both collect and upload job steps to the same job
        EXEC dbo.sp_add_jobstep
            @job_id                = @job_id,
            @step_name            = @collection_step_name,
            @subsystem            = 'CMDEXEC',
            @command            = @collection_step_command,
            @on_success_action    =  3,        -- go to the next job step (purge the log)
            @on_fail_action        =  2,        -- quit with failure
            @proxy_id            = @proxy_id,
            @flags              = 16        -- Write log to table (append to existing history)

        EXEC dbo.sp_add_jobstep
            @job_id                = @job_id,
            @step_name            = @purge_step_name,
            @subsystem            = 'TSQL',
            @database_name        = 'msdb',
            @command            = @purge_step_command,
            @on_success_action    =  3,        -- go to the next job step (upload)
            @on_fail_action        =  3,        -- go to the next job step (upload)
            @proxy_id            = NULL,
            @flags                = 16        -- write log to table (append to existing history)

        EXEC dbo.sp_add_jobstep
            @job_id                = @job_id,
            @step_name            = @upload_step_name,
            @subsystem            = 'CMDEXEC',
            @command            = @upload_step_command,
            @on_success_action    =  1,        -- quit with success
            @on_fail_action        =  2,        -- quit with failure
            @proxy_id            = @proxy_id,
            @flags              = 16        -- Write log to table (append to existing history)

        IF @schedule_id IS NOT NULL
        BEGIN
            -- attach the schedule
            EXEC dbo.sp_attach_schedule
                @job_id            = @job_id,
                @schedule_id    = @schedule_id
        END

        SET @upload_job_id = @job_id
        SET @collection_job_id = @job_id
    END

    IF (@collection_mode = 0) -- cached mode
    BEGIN
        -- create 2 jobs for collect and upload
        -- add to collect job an extra step that autostops collection called in case collect job fails
        DECLARE @upload_job_name        sysname
        DECLARE @collection_job_name    sysname
        SET @upload_job_name = N'collection_set_' + @collection_set_id_as_char + '_upload'
        SET @collection_job_name = N'collection_set_' + @collection_set_id_as_char + '_collection'

        SET @collection_step_name = @collection_job_name + '_collect'
        SET @autostop_step_name = @collection_job_name + '_autostop'
        SET @upload_step_name = @upload_job_name + '_upload'
        SET @purge_step_name = @upload_job_name + '_purge_logs'

        -- modify the collection step to pass in the stop event name passed in by agent
        SET @collection_step_command = @collection_step_command + N' -e $' + N'(ESCAPE_NONE(' + N'STOPEVENT))'

        -- add agent job and job server
        EXEC dbo.sp_add_job 
            @job_name        = @upload_job_name,
            @category_id    = 8, -- N'Data Collector'
            @enabled        = 0,
            @job_id            = @upload_job_id OUTPUT
        
        EXEC dbo.sp_add_jobserver
            @job_id            = @upload_job_id,
            @server_name    = N'(local)'

        EXEC dbo.sp_add_job 
            @job_name        = @collection_job_name,
            @category_id    = 8, -- N'Data Collector'
            @enabled        = 0,
            @job_id            = @collection_job_id OUTPUT

        EXEC dbo.sp_add_jobserver
            @job_id            = @collection_job_id,
            @server_name    = N'(local)'

        -- add upload job step to upload job and collection job
        -- step to collection job separately
        EXEC dbo.sp_add_jobstep
            @job_id                = @upload_job_id,
            @step_name            = @purge_step_name,
            @subsystem            = 'TSQL',
            @database_name        = 'msdb',
            @command            = @purge_step_command,
            @on_success_action    =  3,        -- go to next job step (upload)
            @on_fail_action        =  3,        -- go to next job step (upload)
            @proxy_id            = NULL,
            @flags                = 16        -- write log to table (append to existing history)

        EXEC dbo.sp_add_jobstep
            @job_id                = @upload_job_id,
            @step_name            = @upload_step_name,
            @subsystem            = 'CMDEXEC',
            @command            = @upload_step_command,
            @on_success_action    =  1,        -- quit with success
            @on_fail_action        =  2,        -- quit with failure
            @proxy_id            = @proxy_id

        EXEC dbo.sp_add_jobstep
            @job_id             = @collection_job_id,
            @step_name          = @collection_step_name,
            @subsystem          = 'CMDEXEC',
            @command            = @collection_step_command,
            @on_success_action  =  1,        -- quit with success
            @on_fail_action     =  3,        -- go to next job step (auto-stop)
                                             -- The retry logic will be applied to new collection sets only
            @retry_attempts     =  3,        -- in case a job step failed retry for 3 times
            @retry_interval     =  5,        -- 5 minutes wait between retry attempts
            @proxy_id           = @proxy_id,
            @flags              = 80 -- 16 (write log to table (append to existing history) 
                                     -- + 64 (create a stop event and pass it to the command line)

        EXEC dbo.sp_add_jobstep
            @job_id                = @collection_job_id,
            @step_name            = @autostop_step_name,
            @subsystem            = 'TSQL',
            @database_name        = 'msdb',
            @command            = @autostop_step_command,
            @on_success_action    =  2,        -- quit with failure
            @on_fail_action        =  2,        -- quit with failure
            @proxy_id            = NULL,
            @flags                = 16        -- write log to table (append to existing history)

        -- attach the input schedule to the upload job
        EXEC dbo.sp_attach_schedule
            @job_id            = @upload_job_id,
            @schedule_id    = @schedule_id

        -- attach the RunAsSQLAgentServiceStartSchedule to the collection job
        EXEC dbo.sp_attach_schedule
            @job_id            = @collection_job_id,
            @schedule_name    = N'RunAsSQLAgentServiceStartSchedule'
    END

    IF (@TranCounter = 0)
        COMMIT TRANSACTION
    RETURN (0)

    END TRY
    BEGIN CATCH
        IF (@TranCounter = 0 OR XACT_STATE() = -1)
            ROLLBACK TRANSACTION
        ELSE IF (XACT_STATE() = 1)
            ROLLBACK TRANSACTION tran_syscollector_create_jobs

        DECLARE @ErrorMessage   NVARCHAR(4000);
        DECLARE @ErrorSeverity  INT;
        DECLARE @ErrorState     INT;
        DECLARE @ErrorNumber    INT;
        DECLARE @ErrorLine      INT;
        DECLARE @ErrorProcedure NVARCHAR(200);
        SELECT @ErrorLine = ERROR_LINE(),
               @ErrorSeverity = ERROR_SEVERITY(),
               @ErrorState = ERROR_STATE(),
               @ErrorNumber = ERROR_NUMBER(),
               @ErrorMessage = ERROR_MESSAGE(),
               @ErrorProcedure = ISNULL(ERROR_PROCEDURE(), '-');

        RAISERROR (14684, @ErrorSeverity, -1 , @ErrorNumber, @ErrorSeverity, @ErrorState, @ErrorProcedure, @ErrorLine, @ErrorMessage);

        RETURN (1)
    END CATCH
END

dbo,sp_syscollector_create_tsql_query_collector,CREATE PROCEDURE [dbo].[sp_syscollector_create_tsql_query_collector]
    @collection_set_uid            uniqueidentifier,
    @collection_item_id            int,
    @collection_package_id        uniqueidentifier,
    @upload_package_id            uniqueidentifier
AS
BEGIN
    -- Security check (role membership)
    IF (NOT (ISNULL(IS_MEMBER(N'dc_operator'), 0) = 1) AND 
        NOT (ISNULL(IS_MEMBER(N'dc_proxy'), 0) = 1) AND 
        NOT (ISNULL(IS_MEMBER(N'db_owner'), 0) = 1))
    BEGIN
        RAISERROR(14677, -1, -1, 'dc_operator'' or ''dc_proxy')
        RETURN(1) -- Failure
    END

    DECLARE @errMsg VARCHAR(256)
    DECLARE @collection_set_id int
    SELECT @collection_set_id = s.collection_set_id
    FROM dbo.syscollector_collection_items i, dbo.syscollector_collection_sets s
    WHERE i.collection_item_id = @collection_item_id
    AND i.collector_type_uid = '302E93D1-3424-4be7-AA8E-84813ECF2419'
    AND s.collection_set_uid = @collection_set_uid

    -- Verify that the collection item exists of the correct type
    IF (@collection_set_id IS NULL)
    BEGIN        
        SELECT @errMsg = CONVERT(VARCHAR(36), @collection_set_uid) + ', ' + CONVERT(VARCHAR(36), @collection_item_id)
        RAISERROR(14262, -1, -1, '@collection_set_uid, @collection_item_id', @errMsg)
        RETURN(1)
    END

    -- Get the names and folder ids for the generated packages
    DECLARE @upload_package_name sysname
    DECLARE @upload_package_folder_id uniqueidentifier
    SELECT @upload_package_name = name, @upload_package_folder_id = folderid
    FROM sysssispackages
    WHERE id = @upload_package_id
    
    IF (@upload_package_name IS NULL) 
    BEGIN
        SELECT @errMsg = @upload_package_name + ', ' + CONVERT(VARCHAR(36), @upload_package_folder_id)
        RAISERROR(14262, -1, -1, '@upload_package_name, @upload_package_folder_id', @errMsg)
        RETURN(1)
    END

    DECLARE @collection_package_name sysname
    DECLARE @collection_package_folder_id uniqueidentifier
    SELECT @collection_package_name = name, @collection_package_folder_id = folderid
    FROM sysssispackages
    WHERE id = @collection_package_id
    
    IF (@collection_package_name IS NULL) 
    BEGIN
        SELECT @errMsg = @collection_package_name + ', ' + CONVERT(VARCHAR(36), @collection_package_folder_id)
        RAISERROR(14262, -1, -1, '@collection_package_name, @collection_package_folder_id', @errMsg)
        RETURN(1)
    END

    -- we need to allow dc_admin to delete these packages along with the collection set when 
    -- the set is deleted
    EXEC sp_ssis_setpackageroles @name = @upload_package_name, @folderid = @upload_package_folder_id, @readrole = NULL, @writerole = N'dc_admin'
    EXEC sp_ssis_setpackageroles @name = @collection_package_name, @folderid = @collection_package_folder_id, @readrole = NULL, @writerole = N'dc_admin'

    INSERT INTO [dbo].[syscollector_tsql_query_collector]
    (
        collection_set_uid,
        collection_set_id, 
        collection_item_id,
        collection_package_id,
        upload_package_id
    )
    VALUES
    (
        @collection_set_uid,
        @collection_set_id,
        @collection_item_id,
        @collection_package_id,
        @upload_package_id
    )
END

dbo,sp_syscollector_delete_collection_item,CREATE PROCEDURE [dbo].[sp_syscollector_delete_collection_item]
    @collection_item_id        int = NULL,
    @name                    sysname = NULL
AS
BEGIN
    -- Security check (role membership)
    IF (NOT (ISNULL(IS_MEMBER(N'dc_admin'), 0) = 1) AND NOT (ISNULL(IS_MEMBER(N'db_owner'), 0) = 1))
    BEGIN
        RAISERROR(14677, -1, -1, 'dc_admin')
        RETURN(1) -- Failure
    END

    DECLARE @retVal int
    EXEC @retVal = dbo.sp_syscollector_verify_collection_item @collection_item_id OUTPUT, @name OUTPUT
    IF (@retVal <> 0)
        RETURN (1)

    DECLARE @is_system          bit
    DECLARE @is_running         bit
    DECLARE @collection_set_id  int
    SELECT @is_running = s.is_running,
           @is_system = s.is_system,
           @collection_set_id = s.collection_set_id
    FROM dbo.syscollector_collection_sets s,
         dbo.syscollector_collection_items i
    WHERE i.collection_item_id = @collection_item_id
    AND s.collection_set_id = i.collection_set_id

    IF (@is_system = 1)
    BEGIN
        -- cannot update, delete, or add new collection items to a system collection set
        RAISERROR(14696, -1, -1);
        RETURN(1)
    END

    IF (@is_running = 1)
    BEGIN
        -- stop the collection set if it was running
        EXEC @retVal = sp_syscollector_stop_collection_set @collection_set_id = @collection_set_id
        IF (@retVal <> 0)
            RETURN (1)
    END

    -- all checks go, perform delete
    EXEC @retVal = sp_syscollector_delete_collection_item_internal @collection_item_id = @collection_item_id, @name = @name
    IF (@retVal <> 0)
        RETURN (1)
        
    RETURN (0)
END

dbo,sp_syscollector_delete_collection_item_internal,CREATE PROCEDURE [dbo].[sp_syscollector_delete_collection_item_internal]
    @collection_item_id         int,
    @name                       sysname
AS
BEGIN
    DECLARE @TranCounter INT
    SET @TranCounter = @@TRANCOUNT
    IF (@TranCounter > 0)
        SAVE TRANSACTION tran_delete_collection_item
    ELSE
        BEGIN TRANSACTION
    BEGIN TRY
        DELETE [dbo].[syscollector_collection_items_internal]
        WHERE collection_item_id = @collection_item_id
          AND name = @name

        IF (@TranCounter = 0)
            COMMIT TRANSACTION
        RETURN (0)
    END TRY
    BEGIN CATCH
        IF (@TranCounter = 0 OR XACT_STATE() = -1)
            ROLLBACK TRANSACTION
        ELSE IF (XACT_STATE() = 1)
            ROLLBACK TRANSACTION tran_delete_collection_item

        DECLARE @ErrorMessage   NVARCHAR(4000);
        DECLARE @ErrorSeverity  INT;
        DECLARE @ErrorState     INT;
        DECLARE @ErrorNumber    INT;
        DECLARE @ErrorLine      INT;
        DECLARE @ErrorProcedure NVARCHAR(200);
        SELECT @ErrorLine = ERROR_LINE(),
               @ErrorSeverity = ERROR_SEVERITY(),
               @ErrorState = ERROR_STATE(),
               @ErrorNumber = ERROR_NUMBER(),
               @ErrorMessage = ERROR_MESSAGE(),
               @ErrorProcedure = ISNULL(ERROR_PROCEDURE(), '-');

        RAISERROR (14684, @ErrorSeverity, -1 , @ErrorNumber, @ErrorSeverity, @ErrorState, @ErrorProcedure, @ErrorLine, @ErrorMessage);
        
        RETURN (1)
    END CATCH
END

dbo,sp_syscollector_delete_collection_set,CREATE PROCEDURE [dbo].[sp_syscollector_delete_collection_set]
    @collection_set_id            int = NULL,
    @name                        sysname = NULL
WITH EXECUTE AS OWNER -- 'MS_DataCollectorInternalUser'
AS
BEGIN
    -- Security check (role membership)
    EXECUTE AS CALLER;
    IF (NOT (ISNULL(IS_MEMBER(N'dc_admin'), 0) = 1) AND NOT (ISNULL(IS_MEMBER(N'db_owner'), 0) = 1))
    BEGIN
        REVERT;
        RAISERROR(14677, -1, -1, 'dc_admin')
        RETURN (1)
    END
    REVERT;

    DECLARE @retVal int
    EXEC @retVal = dbo.sp_syscollector_verify_collection_set @collection_set_id OUTPUT, @name OUTPUT
    IF (@retVal <> 0)
        RETURN (1)

    DECLARE @is_system            bit
    DECLARE @is_running            bit
    DECLARE @upload_job_id        uniqueidentifier
    DECLARE @collection_job_id    uniqueidentifier
    DECLARE @collection_mode    smallint
    SELECT    @is_running = is_running,
            @is_system = is_system,
            @upload_job_id = upload_job_id, 
            @collection_job_id = collection_job_id,
            @collection_mode = collection_mode
    FROM [dbo].[syscollector_collection_sets]
    WHERE collection_set_id = @collection_set_id

    IF (@is_system = 1)
    BEGIN
        -- cannot update, delete, or add new collection items to a system collection set
        RAISERROR(14696, -1, -1);
        RETURN (1)
    END

    IF (@is_running = 1)
    BEGIN
        EXEC @retVal = sp_syscollector_stop_collection_set @collection_set_id = @collection_set_id
        IF (@retVal <> 0)
            RETURN (1)
    END

    -- All checks are go
    -- Do the actual delete
    EXEC @retVal = sp_syscollector_delete_collection_set_internal
                        @collection_set_id = @collection_set_id, 
                        @name = @name,
                        @collection_job_id = @collection_job_id,
                        @upload_job_id = @upload_job_id,
                        @collection_mode = @collection_mode
    RETURN (0)
END

dbo,sp_syscollector_delete_collection_set_internal,CREATE PROCEDURE [dbo].[sp_syscollector_delete_collection_set_internal]
    @collection_set_id      int,
    @name                   sysname,
    @collection_job_id      uniqueidentifier,
    @upload_job_id          uniqueidentifier,
    @collection_mode        smallint
AS
BEGIN
    DECLARE @TranCounter int
    SET @TranCounter = @@TRANCOUNT
    IF (@TranCounter > 0)
        SAVE TRANSACTION tran_delete_collection_set
    ELSE
        BEGIN TRANSACTION
    
    BEGIN TRY
        -- clean log before deleting collection set
        DECLARE @log_id bigint
        SET @log_id = (SELECT TOP(1) log_id  FROM dbo.syscollector_execution_log WHERE collection_set_id = @collection_set_id)
        WHILE (@log_id IS NOT NULL)
        BEGIN
            EXEC dbo.sp_syscollector_delete_execution_log_tree @log_id = @log_id
            SET @log_id = (SELECT TOP(1) log_id  FROM dbo.syscollector_execution_log WHERE collection_set_id = @collection_set_id)
        END

        DECLARE @schedule_id    int
        SELECT @schedule_id = schedule_id
        FROM dbo.syscollector_collection_sets cs JOIN sysschedules_localserver_view sv
        ON (cs.schedule_uid = sv.schedule_uid)
        WHERE collection_set_id = @collection_set_id

        DELETE [dbo].[syscollector_collection_sets_internal]
        WHERE collection_set_id = @collection_set_id

        EXEC dbo.sp_syscollector_delete_jobs 
            @collection_job_id        = @collection_job_id,
            @upload_job_id            = @upload_job_id,
            @schedule_id            = @schedule_id,
            @collection_mode        = @collection_mode

        IF (@TranCounter = 0)
            COMMIT TRANSACTION
        RETURN (0)
    END TRY
    BEGIN CATCH
        IF (@TranCounter = 0 OR XACT_STATE() = -1)
            ROLLBACK TRANSACTION
        ELSE IF (XACT_STATE() = 1)
            ROLLBACK TRANSACTION tran_delete_collection_set

        DECLARE @ErrorMessage   NVARCHAR(4000);
        DECLARE @ErrorSeverity  INT;
        DECLARE @ErrorState     INT;
        DECLARE @ErrorNumber    INT;
        DECLARE @ErrorLine      INT;
        DECLARE @ErrorProcedure NVARCHAR(200);
        SELECT @ErrorLine = ERROR_LINE(),
               @ErrorSeverity = ERROR_SEVERITY(),
               @ErrorState = ERROR_STATE(),
               @ErrorNumber = ERROR_NUMBER(),
               @ErrorMessage = ERROR_MESSAGE(),
               @ErrorProcedure = ISNULL(ERROR_PROCEDURE(), '-');

        RAISERROR (14684, @ErrorSeverity, -1 , @ErrorNumber, @ErrorSeverity, @ErrorState, @ErrorProcedure, @ErrorLine, @ErrorMessage);
        
        RETURN (1)    
    END CATCH
END

dbo,sp_syscollector_delete_collector_type,CREATE PROCEDURE [dbo].[sp_syscollector_delete_collector_type]
    @collector_type_uid            uniqueidentifier = NULL,
    @name                        sysname = NULL
AS
BEGIN
    DECLARE @TranCounter INT
    SET @TranCounter = @@TRANCOUNT
    IF (@TranCounter > 0)
        SAVE TRANSACTION tran_delete_collector_type
    ELSE
        BEGIN TRANSACTION
    BEGIN TRY

    -- Security check (role membership)
    IF (NOT (ISNULL(IS_MEMBER(N'dc_admin'), 0) = 1) AND NOT (ISNULL(IS_MEMBER(N'db_owner'), 0) = 1))
    BEGIN
        RAISERROR(14677, -1, -1, 'dc_admin')
        RETURN (1)
    END
    
    DECLARE @retVal int
    EXEC @retVal = dbo.sp_syscollector_verify_collector_type @collector_type_uid OUTPUT, @name OUTPUT
    IF (@retVal <> 0)
        RETURN (1)

    IF (EXISTS(SELECT * from dbo.syscollector_collection_items
        WHERE @collector_type_uid = collector_type_uid))
    BEGIN
        RAISERROR(14673, -1, -1, @name)
        RETURN (1)
    END
    
    DECLARE @schema_collection sysname
        -- @sql_string should have enough buffer to include 2n+2 max size for QUOTENAME(@schema_collection).
    DECLARE @sql_string nvarchar(285)
    SET @schema_collection = (SELECT schema_collection 
                                FROM syscollector_collector_types_internal
                                WHERE @collector_type_uid = collector_type_uid)
    SET @sql_string = N'DROP XML SCHEMA COLLECTION ' + QUOTENAME(@schema_collection, '[');
    EXEC sp_executesql @sql_string

    DELETE [dbo].[syscollector_collector_types_internal]
    WHERE collector_type_uid = @collector_type_uid

    IF (@TranCounter = 0)
        COMMIT TRANSACTION
    RETURN (0)
    END TRY
    BEGIN CATCH
        IF (@TranCounter = 0 OR XACT_STATE() = -1)
            ROLLBACK TRANSACTION
        ELSE IF (XACT_STATE() = 1)
            ROLLBACK TRANSACTION tran_delete_collector_type

        DECLARE @ErrorMessage   NVARCHAR(4000);
        DECLARE @ErrorSeverity  INT;
        DECLARE @ErrorState     INT;
        DECLARE @ErrorNumber    INT;
        DECLARE @ErrorLine      INT;
        DECLARE @ErrorProcedure NVARCHAR(200);
        SELECT @ErrorLine = ERROR_LINE(),
               @ErrorSeverity = ERROR_SEVERITY(),
               @ErrorState = ERROR_STATE(),
               @ErrorNumber = ERROR_NUMBER(),
               @ErrorMessage = ERROR_MESSAGE(),
               @ErrorProcedure = ISNULL(ERROR_PROCEDURE(), '-');

        RAISERROR (14684, @ErrorSeverity, -1 , @ErrorNumber, @ErrorSeverity, @ErrorState, @ErrorProcedure, @ErrorLine, @ErrorMessage);
        
        RETURN (1)
    END CATCH
END

dbo,sp_syscollector_delete_execution_log_tree,CREATE PROCEDURE [dbo].[sp_syscollector_delete_execution_log_tree]
    @log_id BIGINT,
    @from_collection_set    BIT = 1
AS
BEGIN
    -- Security check (role membership)
    IF (NOT (ISNULL(IS_MEMBER(N'dc_operator'), 0) = 1) AND NOT (ISNULL(IS_MEMBER(N'db_owner'), 0) = 1))
    BEGIN
        RAISERROR(14677, -1, -1, 'dc_operator')
        RETURN(1) -- Failure
    END

    SET NOCOUNT ON;
    CREATE TABLE #log_ids (log_id BIGINT);
    
    WITH graph AS
    (
        SELECT log_id FROM dbo.syscollector_execution_log
        WHERE log_id = CASE @from_collection_set
            WHEN 1 THEN dbo.fn_syscollector_find_collection_set_root(@log_id)
            ELSE @log_id
        END
        UNION ALL
        SELECT leaf.log_id FROM dbo.syscollector_execution_log AS leaf
        INNER JOIN graph AS node ON (node.log_id = leaf.parent_log_id)
    )
    INSERT INTO #log_ids
    SELECT log_id
    FROM graph
    
    -- Delete all ssis log records pertaining to the selected logs
    DELETE FROM dbo.sysssislog
        FROM dbo.sysssislog AS s
        INNER JOIN dbo.syscollector_execution_log_internal AS l ON (l.package_execution_id = s.executionid)
        INNER JOIN #log_ids AS i ON i.log_id = l.log_id
        
    -- Then delete the actual logs
    DELETE FROM syscollector_execution_log_internal
        FROM syscollector_execution_log_internal AS l
        INNER Join #log_ids AS i ON i.log_id = l.log_id

    DROP TABLE #log_ids
    RETURN (0)
END

dbo,sp_syscollector_delete_jobs,CREATE PROCEDURE [dbo].[sp_syscollector_delete_jobs]
    @collection_job_id        uniqueidentifier,
    @upload_job_id            uniqueidentifier,
    @schedule_id            int = NULL,
    @collection_mode        smallint
AS
BEGIN
    -- delete the jobs corresponding to the collection set
    DECLARE @TranCounter INT
    SET @TranCounter = @@TRANCOUNT
    IF (@TranCounter > 0)
        SAVE TRANSACTION tran_syscollector_delete_jobs
    ELSE
        BEGIN TRANSACTION
    
    BEGIN TRY

    IF (@collection_mode = 1) -- non-cached mode
    BEGIN
        IF (@upload_job_id IS NOT NULL)
        BEGIN
            -- note, upload job id = collection job id in this mode
            IF (@schedule_id IS NOT NULL)
            BEGIN
                EXEC dbo.sp_detach_schedule
                    @job_id            = @upload_job_id, 
                    @schedule_id    = @schedule_id,
                    @delete_unused_schedule = 0
            END

            EXEC dbo.sp_delete_jobserver
                @job_id            = @upload_job_id,
                @server_name    = N'(local)'

            EXEC dbo.sp_delete_job 
                @job_id            = @upload_job_id
        END
    END
    ELSE -- cached mode
    BEGIN
        -- detach schedules, delete job servers, then delete jobs
        IF (@upload_job_id IS NOT NULL)
        BEGIN
            EXEC dbo.sp_detach_schedule
                @job_id            = @upload_job_id, 
                @schedule_id    = @schedule_id,
                @delete_unused_schedule = 0

            EXEC dbo.sp_delete_jobserver
                @job_id            = @upload_job_id,
                @server_name    = N'(local)'

            EXEC dbo.sp_delete_job 
                @job_id            = @upload_job_id
        END

        IF (@collection_job_id IS NOT NULL)
        BEGIN
            EXEC dbo.sp_detach_schedule
                @job_id            = @collection_job_id, 
                @schedule_name    = N'RunAsSQLAgentServiceStartSchedule',
                @delete_unused_schedule = 0

            EXEC dbo.sp_delete_jobserver
                @job_id            = @collection_job_id,
                @server_name    = N'(local)'

            EXEC dbo.sp_delete_job 
                @job_id            = @collection_job_id
        END
    END

    IF (@TranCounter = 0)
        COMMIT TRANSACTION
    RETURN (0)
    END TRY
    BEGIN CATCH
        IF (@TranCounter = 0 OR XACT_STATE() = -1)
            ROLLBACK TRANSACTION
        ELSE IF (XACT_STATE() = 1)
            ROLLBACK TRANSACTION tran_syscollector_delete_jobs

        DECLARE @ErrorMessage   NVARCHAR(4000);
        DECLARE @ErrorSeverity  INT;
        DECLARE @ErrorState     INT;
        DECLARE @ErrorNumber    INT;
        DECLARE @ErrorLine      INT;
        DECLARE @ErrorProcedure NVARCHAR(200);
        SELECT @ErrorLine = ERROR_LINE(),
               @ErrorSeverity = ERROR_SEVERITY(),
               @ErrorState = ERROR_STATE(),
               @ErrorNumber = ERROR_NUMBER(),
               @ErrorMessage = ERROR_MESSAGE(),
               @ErrorProcedure = ISNULL(ERROR_PROCEDURE(), '-');

        RAISERROR (14684, @ErrorSeverity, -1 , @ErrorNumber, @ErrorSeverity, @ErrorState, @ErrorProcedure, @ErrorLine, @ErrorMessage);
        
        RETURN (1)
    END CATCH
END

dbo,sp_syscollector_disable_collector,CREATE PROCEDURE [dbo].[sp_syscollector_disable_collector]
WITH EXECUTE AS OWNER -- 'MS_DataCollectorInternalUser'
AS
BEGIN
    -- Security check (role membership)
    EXECUTE AS CALLER;
    IF (NOT (ISNULL(IS_MEMBER(N'dc_operator'), 0) = 1) AND NOT (ISNULL(IS_MEMBER(N'db_owner'), 0) = 1))
    BEGIN
        REVERT;
        RAISERROR(14677, -1, -1, 'dc_operator')
        RETURN(1) -- Failure
    END
    REVERT;

    BEGIN TRANSACTION

    DECLARE @was_enabled int;

    SELECT @was_enabled = ISNULL(CONVERT(int, parameter_value),0)
    FROM [dbo].[syscollector_config_store_internal]
    WHERE parameter_name = 'CollectorEnabled'

    IF (@was_enabled <> 0)
    BEGIN

        UPDATE [dbo].[syscollector_config_store_internal]
        SET parameter_value = 0
        WHERE parameter_name = 'CollectorEnabled'

        DECLARE @collection_set_id INT
        DECLARE @collection_mode SMALLINT
        DECLARE @collection_job_id UNIQUEIDENTIFIER

        DECLARE collection_set_cursor CURSOR LOCAL FOR
            SELECT collection_set_id, collection_mode, collection_job_id
            FROM dbo.syscollector_collection_sets
            WHERE is_running = 1

        OPEN collection_set_cursor
        FETCH collection_set_cursor INTO @collection_set_id, @collection_mode, @collection_job_id

        WHILE @@FETCH_STATUS = 0 
        BEGIN
            -- If this collection set is running in cached mode, and the collection job is running, we need to stop the job explicitly here
            DECLARE @is_collection_job_running INT
            EXECUTE [dbo].[sp_syscollector_get_collection_set_execution_status]
                    @collection_set_id = @collection_set_id,
                    @is_collection_running = @is_collection_job_running OUTPUT    

            IF (@is_collection_job_running = 1
                AND @collection_mode = 0)           -- Cached mode
            BEGIN
                EXEC sp_stop_job @job_id = @collection_job_id
            END

            -- Now, disable the jobs and detach them from the upload schedules
            EXEC dbo.sp_syscollector_stop_collection_set_jobs @collection_set_id = @collection_set_id
            FETCH collection_set_cursor INTO @collection_set_id, @collection_mode, @collection_job_id
        END
        CLOSE collection_set_cursor
        DEALLOCATE collection_set_cursor

    END

    COMMIT TRANSACTION

END

dbo,sp_syscollector_enable_collector,CREATE PROCEDURE [dbo].[sp_syscollector_enable_collector]
WITH EXECUTE AS OWNER -- 'MS_DataCollectorInternalUser'
AS
BEGIN
    -- Security check (role membership)
    EXECUTE AS CALLER;
    IF (NOT (ISNULL(IS_MEMBER(N'dc_operator'), 0) = 1) AND NOT (ISNULL(IS_MEMBER(N'db_owner'), 0) = 1))
    BEGIN
        REVERT;
        RAISERROR(14677, -1, -1, 'dc_operator')
        RETURN(1) -- Failure
    END
    REVERT;

    -- check if SQL Server Agent is enabled
    DECLARE @agent_enabled int
    SELECT @agent_enabled = CAST(value_in_use AS int) FROM sys.configurations WHERE name = N'Agent XPs'
    IF @agent_enabled <> 1
    BEGIN
        RAISERROR(14699, -1, -1)
        RETURN (1) -- Failure
    END
    REVERT;

    BEGIN TRANSACTION

    DECLARE @was_enabled int;

    SELECT @was_enabled = ISNULL(CONVERT(int, parameter_value),0)
    FROM [dbo].[syscollector_config_store_internal]
    WHERE parameter_name = 'CollectorEnabled'

    IF (@was_enabled = 0)
    BEGIN

        UPDATE [dbo].[syscollector_config_store_internal]
        SET parameter_value = 1
        WHERE parameter_name = 'CollectorEnabled'

        DECLARE @collection_set_id int

        DECLARE collection_set_cursor CURSOR LOCAL FOR
            SELECT collection_set_id
            FROM dbo.syscollector_collection_sets
            WHERE is_running = 1

        OPEN collection_set_cursor
        FETCH collection_set_cursor INTO @collection_set_id

        WHILE @@FETCH_STATUS = 0 
        BEGIN
            EXEC dbo.sp_syscollector_start_collection_set_jobs @collection_set_id = @collection_set_id
            FETCH collection_set_cursor INTO @collection_set_id
        END

        CLOSE collection_set_cursor
        DEALLOCATE collection_set_cursor

    END

    COMMIT TRANSACTION

END
```

