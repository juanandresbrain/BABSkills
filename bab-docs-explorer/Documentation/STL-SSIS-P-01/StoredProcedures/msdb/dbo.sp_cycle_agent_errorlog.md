# dbo.sp_cycle_agent_errorlog

**Database:** msdb  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_cycle_agent_errorlog"]
    dbo_sp_sqlagent_notify(["dbo.sp_sqlagent_notify"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sp_sqlagent_notify |

## Stored Procedure Code

```sql
CREATE PROCEDURE sp_cycle_agent_errorlog
AS
BEGIN
   exec sp_sqlagent_notify N'L'
END

dbo,sp_delete_alert,CREATE PROCEDURE sp_delete_alert
  @name sysname
AS
BEGIN
  DECLARE @alert_id    INT
  DECLARE @return_code INT

  SET NOCOUNT ON

  -- Remove any leading/trailing spaces from parameters
  SELECT @name = LTRIM(RTRIM(@name))

  -- Only a sysadmin can do this
  IF ((ISNULL(IS_SRVROLEMEMBER(N'sysadmin'), 0) <> 1))
  BEGIN
    RAISERROR(15003, 16, 1, N'sysadmin')
    RETURN(1) -- Failure
  END

  -- Check if SQLServerAgent is in the process of starting
  EXECUTE @return_code = msdb.dbo.sp_is_sqlagent_starting
  IF (@return_code <> 0)
    RETURN(1) -- Failure

  -- Check if this Alert exists
  IF (NOT EXISTS (SELECT *
                  FROM msdb.dbo.sysalerts
                  WHERE (name = @name)))
  BEGIN
    RAISERROR(14262, 16, 1, '@name', @name)
    RETURN(1) -- Failure
  END

  -- Convert the Name to it's ID
  SELECT @alert_id = id
  FROM msdb.dbo.sysalerts
  WHERE (name = @name)

  BEGIN TRANSACTION

    -- Delete sysnotifications entries
    DELETE FROM msdb.dbo.sysnotifications
    WHERE (alert_id = @alert_id)

    -- Finally, do the actual DELETE
    DELETE FROM msdb.dbo.sysalerts
    WHERE (id = @alert_id)

  COMMIT TRANSACTION

  -- Notify SQLServerAgent of the change
  EXECUTE msdb.dbo.sp_sqlagent_notify @op_type     = N'A',
                                      @alert_id    = @alert_id,
                                      @action_type = N'D'
  RETURN(0) -- Success
END

dbo,sp_delete_all_msx_jobs,CREATE PROCEDURE sp_delete_all_msx_jobs
  @msx_server   sysname,
  @jobs_deleted INT = NULL OUTPUT
AS
BEGIN
  SET NOCOUNT ON

  -- Change server name to always reflect real servername or servername\instancename
  IF (UPPER(@msx_server collate SQL_Latin1_General_CP1_CS_AS) = '(LOCAL)')
    SELECT @msx_server = UPPER(CONVERT(sysname, SERVERPROPERTY('ServerName')))

  -- Delete all the jobs that originated from the MSX
  -- Note: This temp table is referenced by msdb.dbo.sp_delete_job_references
  CREATE TABLE #temp_jobs_to_delete (job_id UNIQUEIDENTIFIER NOT NULL, job_is_cached INT NOT NULL, owner_sid VARBINARY(85) NOT NULL)

  -- Table of msx schedules to delete
  DECLARE @temp_schedules_to_delete TABLE (schedule_id INT NOT NULL)  

  -- Non-sysadmins can only delete jobs they own. sysjobs_view returns all jobs
  -- for members of SQLAgentReaderRole and SQLAgentOperatorRole, but they should
  -- not be able to delete those jobs
  IF ((ISNULL(IS_SRVROLEMEMBER(N'sysadmin'), 0) = 1))
  BEGIN
   -- NOTE: The left outer-join here is to handle the [unlikely] case of missing sysjobservers rows
   INSERT INTO #temp_jobs_to_delete
   SELECT sjv.job_id, 
         CASE sjs.server_id WHEN 0 THEN 1 ELSE 0 END,
         sjv.owner_sid
   FROM msdb.dbo.sysjobs_view sjv
      LEFT OUTER JOIN msdb.dbo.sysjobservers sjs ON (sjv.job_id = sjs.job_id)
   WHERE (ISNULL(sjs.server_id, 0) = 0)
      AND (sjv.originating_server = @msx_server)
  END
  ELSE
  BEGIN
   -- NOTE: The left outer-join here is to handle the [unlikely] case of missing sysjobservers rows
   INSERT INTO #temp_jobs_to_delete
   SELECT sjv.job_id, 
         CASE sjs.server_id WHEN 0 THEN 1 ELSE 0 END,
         sjv.owner_sid
   FROM msdb.dbo.sysjobs_view sjv
      LEFT OUTER JOIN msdb.dbo.sysjobservers sjs ON (sjv.job_id = sjs.job_id)
   WHERE (ISNULL(sjs.server_id, 0) = 0)
      AND (sjv.originating_server = @msx_server)
      AND (sjv.owner_sid = SUSER_SID())
  END

  -- Must do this before deleting the job itself since sp_sqlagent_notify does a lookup on sysjobs_view
  EXECUTE msdb.dbo.sp_delete_job_references

  BEGIN TRANSACTION

    --Get the list of schedules to delete, these cant be deleted until the references are deleted in sysjobschedules
    INSERT INTO @temp_schedules_to_delete
    SELECT DISTINCT schedule_id 
    FROM   msdb.dbo.sysschedules
    WHERE (schedule_id IN 
            (SELECT schedule_id
            FROM msdb.dbo.sysjobschedules as js
           JOIN #temp_jobs_to_delete as tjd ON (js.job_id = tjd.job_id)))

    DELETE FROM msdb.dbo.sysjobschedules
    WHERE job_id IN (SELECT job_id FROM #temp_jobs_to_delete)

    --Now OK to delete the schedule
    DELETE FROM msdb.dbo.sysschedules
    WHERE schedule_id IN 
    (SELECT schedule_id
        FROM @temp_schedules_to_delete)
    
    DELETE FROM msdb.dbo.sysjobservers
    WHERE job_id IN (SELECT job_id FROM #temp_jobs_to_delete)
    
    DELETE FROM msdb.dbo.sysjobsteps
    WHERE job_id IN (SELECT job_id FROM #temp_jobs_to_delete)

    DELETE FROM msdb.dbo.sysjobs
    WHERE job_id IN (SELECT job_id FROM #temp_jobs_to_delete)

    DELETE FROM msdb.dbo.sysjobhistory
    WHERE job_id IN (SELECT job_id FROM #temp_jobs_to_delete)

   --Finally cleanup any orphaned sysschedules that were downloaded from the MSX
   DELETE msdb.dbo.sysschedules
   FROM msdb.dbo.sysschedules s
      JOIN msdb.dbo.sysoriginatingservers_view os ON (s.originating_server_id = os.originating_server_id)
   WHERE (os.originating_server = @msx_server)

  COMMIT TRANSACTION

  SELECT @jobs_deleted = COUNT(*)
  FROM #temp_jobs_to_delete

  DROP TABLE #temp_jobs_to_delete
END

dbo,sp_delete_backuphistory,CREATE   PROCEDURE sp_delete_backuphistory
  @oldest_date datetime
AS
BEGIN
  SET NOCOUNT ON

  DECLARE @backup_set_id TABLE      (backup_set_id INT)
  DECLARE @media_set_id TABLE       (media_set_id INT)
  DECLARE @restore_history_id TABLE (restore_history_id INT)

  INSERT INTO @backup_set_id (backup_set_id)
  SELECT DISTINCT backup_set_id
  FROM msdb.dbo.backupset
  WHERE backup_finish_date < @oldest_date

  INSERT INTO @media_set_id (media_set_id)
  SELECT DISTINCT media_set_id
  FROM msdb.dbo.backupset
  WHERE backup_finish_date < @oldest_date

  INSERT INTO @restore_history_id (restore_history_id)
  SELECT DISTINCT restore_history_id
  FROM msdb.dbo.restorehistory
  WHERE backup_set_id IN (SELECT backup_set_id
                          FROM @backup_set_id)

  BEGIN TRANSACTION

  DELETE FROM msdb.dbo.backupfile
  WHERE backup_set_id IN (SELECT backup_set_id
                          FROM @backup_set_id)
  IF (@@error > 0)
    GOTO Quit

  DELETE FROM msdb.dbo.backupfilegroup
  WHERE backup_set_id IN (SELECT backup_set_id
                          FROM @backup_set_id)
  IF (@@error > 0)
    GOTO Quit

  DELETE FROM msdb.dbo.restorefile
  WHERE restore_history_id IN (SELECT restore_history_id
                               FROM @restore_history_id)
  IF (@@error > 0)
    GOTO Quit

  DELETE FROM msdb.dbo.restorefilegroup
  WHERE restore_history_id IN (SELECT restore_history_id
                               FROM @restore_history_id)
  IF (@@error > 0)
    GOTO Quit

  DELETE FROM msdb.dbo.restorehistory
  WHERE restore_history_id IN (SELECT restore_history_id
                               FROM @restore_history_id)
  IF (@@error > 0)
    GOTO Quit

  DELETE FROM msdb.dbo.backupset
  WHERE backup_set_id IN (SELECT backup_set_id
                          FROM @backup_set_id)
  IF (@@error > 0)
    GOTO Quit

  DELETE msdb.dbo.backupmediafamily
  FROM msdb.dbo.backupmediafamily bmf
  WHERE bmf.media_set_id IN (SELECT media_set_id
                             FROM @media_set_id)
    AND ((SELECT COUNT(*)
          FROM msdb.dbo.backupset
          WHERE media_set_id = bmf.media_set_id) = 0)
  IF (@@error > 0)
    GOTO Quit

  DELETE msdb.dbo.backupmediaset
  FROM msdb.dbo.backupmediaset bms
  WHERE bms.media_set_id IN (SELECT media_set_id
                             FROM @media_set_id)
    AND ((SELECT COUNT(*)
          FROM msdb.dbo.backupset
          WHERE media_set_id = bms.media_set_id) = 0)
  IF (@@error > 0)
    GOTO Quit

  COMMIT TRANSACTION
  RETURN

Quit:
  ROLLBACK TRANSACTION

END

dbo,sp_delete_category,CREATE PROCEDURE sp_delete_category
  @class VARCHAR(8),  -- JOB or ALERT or OPERATOR
  @name  sysname
AS
BEGIN
  DECLARE @retval         INT
  DECLARE @category_id    INT
  DECLARE @category_class INT
  DECLARE @category_type  INT

  SET NOCOUNT ON

  -- Remove any leading/trailing spaces from parameters
  SELECT @class = LTRIM(RTRIM(@class))
  SELECT @name  = LTRIM(RTRIM(@name))

  EXECUTE @retval = sp_verify_category @class,
                                       NULL,
                                       NULL,
                                       @category_class OUTPUT,
                                       NULL
  IF (@retval <> 0)
    RETURN(1) -- Failure

  -- Check name
  SELECT @category_id = category_id,
         @category_type = category_type
  FROM msdb.dbo.syscategories
  WHERE (category_class = @category_class)
    AND (name = @name)
  IF (@category_id IS NULL)
  BEGIN
    RAISERROR(14262, -1, -1, '@name', @name)
    RETURN(1) -- Failure
  END

  -- Make sure that we're not deleting one of the permanent categories (id's 0 - 99)
  IF (@category_id < 100)
  BEGIN
    RAISERROR(14276, -1, -1, @name, @class)
    RETURN(1) -- Failure
  END

  BEGIN TRANSACTION

    -- Clean-up any Jobs that reference the deleted category
    UPDATE msdb.dbo.sysjobs
    SET category_id = CASE @category_type
                        WHEN 1 THEN 0 -- [Uncategorized (Local)]
                        WHEN 2 THEN 2 -- [Uncategorized (Multi-Server)]
                      END
    WHERE (category_id = @category_id)

    -- Clean-up any Alerts that reference the deleted category
    UPDATE msdb.dbo.sysalerts
    SET category_id = 98
    WHERE (category_id = @category_id)

    -- Clean-up any Operators that reference the deleted category
    UPDATE msdb.dbo.sysoperators
    SET category_id = 99
    WHERE (category_id = @category_id)

    -- Finally, delete the category itself
    DELETE FROM msdb.dbo.syscategories
    WHERE (category_id = @category_id)

  COMMIT TRANSACTION

  RETURN(0) -- Success
END

dbo,sp_delete_database_backuphistory,CREATE   PROCEDURE sp_delete_database_backuphistory
  @database_name sysname
AS
BEGIN
  SET NOCOUNT ON

  DECLARE @backup_set_id TABLE      (backup_set_id INT)
  DECLARE @media_set_id TABLE       (media_set_id INT)
  DECLARE @restore_history_id TABLE (restore_history_id INT)

  INSERT INTO @backup_set_id (backup_set_id)
  SELECT DISTINCT backup_set_id
  FROM msdb.dbo.backupset
  WHERE database_name = @database_name

  INSERT INTO @media_set_id (media_set_id)
  SELECT DISTINCT media_set_id
  FROM msdb.dbo.backupset
  WHERE database_name = @database_name

  INSERT INTO @restore_history_id (restore_history_id)
  SELECT DISTINCT restore_history_id
  FROM msdb.dbo.restorehistory
  WHERE backup_set_id IN (SELECT backup_set_id
                          FROM @backup_set_id)

  BEGIN TRANSACTION

  DELETE FROM msdb.dbo.backupfile
  WHERE backup_set_id IN (SELECT backup_set_id
                          FROM @backup_set_id)
  IF (@@error > 0)
    GOTO Quit

  DELETE FROM msdb.dbo.backupfilegroup
  WHERE backup_set_id IN (SELECT backup_set_id
                          FROM @backup_set_id)
  IF (@@error > 0)
    GOTO Quit

  DELETE FROM msdb.dbo.restorefile
  WHERE restore_history_id IN (SELECT restore_history_id
                               FROM @restore_history_id)
  IF (@@error > 0)
    GOTO Quit

  DELETE FROM msdb.dbo.restorefilegroup
  WHERE restore_history_id IN (SELECT restore_history_id
                               FROM @restore_history_id)
  IF (@@error > 0)
    GOTO Quit

  DELETE FROM msdb.dbo.restorehistory
  WHERE restore_history_id IN (SELECT restore_history_id
                               FROM @restore_history_id)
  IF (@@error > 0)
    GOTO Quit

  DELETE FROM msdb.dbo.backupset
  WHERE backup_set_id IN (SELECT backup_set_id
                          FROM @backup_set_id)
  IF (@@error > 0)
    GOTO Quit

  DELETE msdb.dbo.backupmediafamily
  FROM msdb.dbo.backupmediafamily bmf
  WHERE bmf.media_set_id IN (SELECT media_set_id
                             FROM @media_set_id)
    AND ((SELECT COUNT(*)
          FROM msdb.dbo.backupset
          WHERE media_set_id = bmf.media_set_id) = 0)
  IF (@@error > 0)
    GOTO Quit

  DELETE msdb.dbo.backupmediaset
  FROM msdb.dbo.backupmediaset bms
  WHERE bms.media_set_id IN (SELECT media_set_id
                             FROM @media_set_id)
    AND ((SELECT COUNT(*)
          FROM msdb.dbo.backupset
          WHERE media_set_id = bms.media_set_id) = 0)
  IF (@@error > 0)
    GOTO Quit

  COMMIT TRANSACTION
  RETURN

Quit:
  ROLLBACK TRANSACTION
END

dbo,sp_delete_dm_hadr_automatic_seeding_history,CREATE   PROCEDURE sp_delete_dm_hadr_automatic_seeding_history
  @oldest_date datetime
AS
BEGIN
  SET NOCOUNT ON

  DELETE FROM [msdb].[dbo].[dm_hadr_automatic_seeding_history]
  WHERE completion_time < @oldest_date
END

dbo,sp_delete_job,CREATE PROCEDURE sp_delete_job
  @job_id               UNIQUEIDENTIFIER = NULL, -- If provided should NOT also provide job_name
  @job_name             sysname          = NULL, -- If provided should NOT also provide job_id
  @originating_server      sysname         = NULL, -- Reserved (used by SQLAgent)
  @delete_history       BIT              = 1,    -- Reserved (used by SQLAgent)
  @delete_unused_schedule   BIT              = 1     -- For backward compatibility schedules are deleted by default if they are not 
                                        -- being used by another job. With the introduction of reusable schedules in V9 
                                        -- callers should set this to 0 so the schedule will be preserved for reuse.
AS
BEGIN
  DECLARE @current_msx_server sysname
  DECLARE @bMSX_job           BIT
  DECLARE @retval             INT
  DECLARE @local_machine_name sysname
  DECLARE @category_id        INT
  DECLARE @job_owner_sid      VARBINARY(85)
  
  SET NOCOUNT ON
  -- Remove any leading/trailing spaces from parameters
  SELECT @originating_server = UPPER(LTRIM(RTRIM(@originating_server)))

  -- Turn [nullable] empty string parameters into NULLs
  IF (@originating_server = N'') SELECT @originating_server = NULL

  -- Change server name to always reflect real servername or servername\instancename
  IF (@originating_server IS NOT NULL AND @originating_server = '(LOCAL)')
    SELECT @originating_server = UPPER(CONVERT(sysname, SERVERPROPERTY('ServerName')))

  IF ((@job_id IS NOT NULL) OR (@job_name IS NOT NULL))
  BEGIN
    EXECUTE @retval = sp_verify_job_identifiers '@job_name',
                                                '@job_id',
                                                 @job_name OUTPUT,
                                                 @job_id   OUTPUT,
                                                 @owner_sid = @job_owner_sid OUTPUT
    IF (@retval <> 0)
      RETURN(1) -- Failure

  END

  -- We need either a job name or a server name, not both
  IF ((@job_name IS NULL)     AND (@originating_server IS NULL)) OR
     ((@job_name IS NOT NULL) AND (@originating_server IS NOT NULL))
  BEGIN
    RAISERROR(14279, -1, -1)
    RETURN(1) -- Failure
  END

  -- Get category to see if it is a misc. replication agent. @category_id will be
  -- NULL if there is no @job_id.
  select @category_id = category_id from msdb.dbo.sysjobs where job_id = @job_id

  -- If job name was given, determine if the job is from an MSX
  IF (@job_id IS NOT NULL)
  BEGIN
    SELECT @bMSX_job = CASE UPPER(originating_server)
                         WHEN UPPER(CONVERT(sysname, SERVERPROPERTY('ServerName'))) THEN 0
                         ELSE 1
                       END
    FROM msdb.dbo.sysjobs_view
    WHERE (job_id = @job_id)
  END

  -- If server name was given, warn user if different from current MSX
  IF (@originating_server IS NOT NULL)
  BEGIN
    EXECUTE @retval = master.dbo.xp_getnetname @local_machine_name OUTPUT
    IF (@retval <> 0)
      RETURN(1) -- Failure

    IF ((@originating_server = UPPER(CONVERT(sysname, SERVERPROPERTY('ServerName')))) OR (@originating_server = UPPER(@local_machine_name)))
      SELECT @originating_server = UPPER(CONVERT(sysname, SERVERPROPERTY('ServerName')))

    EXECUTE master.dbo.xp_instance_regread N'HKEY_LOCAL_MACHINE',
                                           N'SOFTWARE\Microsoft\MSSQLServer\SQLServerAgent',
                                           N'MSXServerName',
                                           @current_msx_server OUTPUT,
                                           N'no_output'

    SELECT @current_msx_server = UPPER(@current_msx_server)
    -- If server name was given but it's not the current MSX, print a warning
    SELECT @current_msx_server = LTRIM(RTRIM(@current_msx_server))
    IF ((@current_msx_server IS NOT NULL) AND (@current_msx_server <> N'') AND (@originating_server <> @current_msx_server))
      RAISERROR(14224, 0, 1, @current_msx_server)
  END

  -- Check authority (only SQLServerAgent can delete a non-local job)
  IF (((@originating_server IS NOT NULL) AND (@originating_server <> UPPER(CONVERT(sysname, SERVERPROPERTY('ServerName'))))) OR (@bMSX_job = 1)) AND
     (PROGRAM_NAME() NOT LIKE N'SQLAgent%')
  BEGIN
    RAISERROR(14274, -1, -1)
    RETURN(1) -- Failure
  END
  
  -- Check permissions beyond what's checked by the sysjobs_view
  -- SQLAgentReader and SQLAgentOperator roles that can see all jobs
  -- cannot delete jobs they do not own
  IF (@job_id IS NOT NULL)
  BEGIN
   IF (@job_owner_sid <> SUSER_SID()                     -- does not own the job
       AND (ISNULL(IS_SRVROLEMEMBER(N'sysadmin'), 0) <> 1)) -- is not sysadmin
   BEGIN
     RAISERROR(14525, -1, -1);
     RETURN(1) -- Failure
    END
  END

  -- Do the delete (for a specific job)
  IF (@job_id IS NOT NULL)
  BEGIN
    -- Note: This temp table is referenced by msdb.dbo.sp_delete_job_references,
    -- so it cannot be declared as a local table.
    CREATE TABLE #temp_jobs_to_delete (job_id UNIQUEIDENTIFIER NOT NULL PRIMARY KEY CLUSTERED,
                                       job_is_cached INT NOT NULL)

    DECLARE @temp_schedules_to_delete TABLE (schedule_id INT NOT NULL)  

    INSERT INTO #temp_jobs_to_delete
    SELECT job_id, (SELECT COUNT(*)
                    FROM msdb.dbo.sysjobservers
                    WHERE (job_id = @job_id)
                      AND (server_id = 0))
    FROM msdb.dbo.sysjobs_view
    WHERE (job_id = @job_id)

    -- Check if we have any work to do
    IF (NOT EXISTS (SELECT *
                    FROM #temp_jobs_to_delete))
    BEGIN
      DROP TABLE #temp_jobs_to_delete
      RETURN(0) -- Success
    END

    -- Post the delete to any target servers (need to do this BEFORE
    -- deleting the job itself, but AFTER clearing all all pending
    -- download instructions).  Note that if the job is NOT a
    -- multi-server job then sp_post_msx_operation will catch this and
    -- will do nothing. Since it will do nothing that is why we need
    -- to NOT delete any pending delete requests, because that delete
    -- request might have been for the last target server and thus
    -- this job isn't a multi-server job anymore so posting the global
    -- delete would do nothing.
    DELETE FROM msdb.dbo.sysdownloadlist
    WHERE (object_id = @job_id)
      and (operation_code != 3) -- Delete
    EXECUTE msdb.dbo.sp_post_msx_operation 'DELETE', 'JOB', @job_id


    -- Must do this before deleting the job itself since sp_sqlagent_notify does a lookup on sysjobs_view
    -- Note: Don't notify agent in this call. It is done after the transaction is committed
    --       just in case this job is in the process of deleting itself
    EXECUTE msdb.dbo.sp_delete_job_references @notify_sqlagent = 0

    -- Delete all traces of the job
    BEGIN TRANSACTION

    DECLARE @err int

   --Get the schedules to delete before deleting records from sysjobschedules
    IF(@delete_unused_schedule = 1)
    BEGIN
        --Get the list of schedules to delete
        INSERT INTO @temp_schedules_to_delete
        SELECT DISTINCT schedule_id 
        FROM   msdb.dbo.sysschedules
        WHERE (schedule_id IN 
                (SELECT schedule_id
                FROM msdb.dbo.sysjobschedules
                WHERE (job_id = @job_id)))
    END


    DELETE FROM msdb.dbo.sysjobschedules
    WHERE job_id IN (SELECT job_id FROM #temp_jobs_to_delete)
    
    DELETE FROM msdb.dbo.sysjobservers
    WHERE job_id IN (SELECT job_id FROM #temp_jobs_to_delete)

    DELETE FROM msdb.dbo.sysjobsteps
    WHERE job_id IN (SELECT job_id FROM #temp_jobs_to_delete)

    DELETE FROM msdb.dbo.sysjobs
    WHERE job_id IN (SELECT job_id FROM #temp_jobs_to_delete)
    SELECT @err = @@ERROR
 
    IF @err <> 0
    BEGIN
    ROLLBACK TRANSACTION
    RETURN @err
    END

    
    --Delete the schedule(s) if requested to and it isn't being used by other jobs
    IF(@delete_unused_schedule = 1)
    BEGIN
      --Now OK to delete the schedule
      DELETE FROM msdb.dbo.sysschedules
      WHERE schedule_id IN 
        (SELECT schedule_id
         FROM @temp_schedules_to_delete as sdel
         WHERE NOT EXISTS(SELECT * 
                          FROM msdb.dbo.sysjobschedules AS js
                          WHERE (js.schedule_id = sdel.schedule_id)))
    END


    -- Delete the job history if requested    
    IF (@delete_history = 1)
    BEGIN
      DELETE FROM msdb.dbo.sysjobhistory
      WHERE job_id IN (SELECT job_id FROM #temp_jobs_to_delete)
    END
    -- All done
    COMMIT TRANSACTION

    -- Now notify agent to delete the job.
    IF(EXISTS(SELECT * FROM #temp_jobs_to_delete WHERE job_is_cached > 0))
    BEGIN
      DECLARE @nt_user_name   NVARCHAR(100)
      SELECT @nt_user_name = ISNULL(NT_CLIENT(), ISNULL(SUSER_SNAME(), FORMATMESSAGE(14205)))
      --Call the xp directly. sp_sqlagent_notify checks sysjobs_view and the record has already been deleted
      EXEC master.dbo.xp_sqlagent_notify N'J', @job_id, 0, 0, N'D', @nt_user_name, 1, @@trancount, NULL, NULL
    END

  END
  ELSE
  -- Do the delete (for all jobs originating from the specific server)
  IF (@originating_server IS NOT NULL)
  BEGIN
    EXECUTE msdb.dbo.sp_delete_all_msx_jobs @msx_server = @originating_server

    -- NOTE: In this case there is no need to propagate the delete via sp_post_msx_operation
    --       since this type of delete is only ever performed on a TSX.
  END

  IF (OBJECT_ID(N'tempdb.dbo.#temp_jobs_to_delete', 'U') IS NOT NULL)    
    DROP TABLE #temp_jobs_to_delete

  RETURN(0) -- 0 means success
END

dbo,sp_delete_job_references,CREATE PROCEDURE sp_delete_job_references
  @notify_sqlagent BIT = 1
AS
BEGIN
  DECLARE @deleted_job_id  UNIQUEIDENTIFIER
  DECLARE @task_id_as_char VARCHAR(10)
  DECLARE @job_is_cached   INT
  DECLARE @alert_name      sysname
  DECLARE @maintplan_plan_id  UNIQUEIDENTIFIER
  DECLARE @maintplan_subplan_id  UNIQUEIDENTIFIER

  -- Keep SQLServerAgent's cache in-sync and cleanup any 'webtask' cross-references to the deleted job(s)
  -- NOTE: The caller must have created a table called #temp_jobs_to_delete of the format
  --       (job_id UNIQUEIDENTIFIER NOT NULL, job_is_cached INT NOT NULL).

  DECLARE sqlagent_notify CURSOR LOCAL
  FOR
  SELECT job_id, job_is_cached
  FROM #temp_jobs_to_delete

  OPEN sqlagent_notify
  FETCH NEXT FROM sqlagent_notify INTO @deleted_job_id, @job_is_cached

  WHILE (@@fetch_status = 0)
  BEGIN
    -- NOTE: We only notify SQLServerAgent if we know the job has been cached
    IF(@job_is_cached = 1 AND @notify_sqlagent = 1)
      EXECUTE msdb.dbo.sp_sqlagent_notify @op_type     = N'J',
                                          @job_id      = @deleted_job_id,
                                          @action_type = N'D'

    IF (EXISTS (SELECT *
                FROM master.dbo.sysobjects
                WHERE (name = N'sp_cleanupwebtask')
                  AND (type = 'P')))
    BEGIN
      SELECT @task_id_as_char = CONVERT(VARCHAR(10), task_id)
      FROM msdb.dbo.systaskids
      WHERE (job_id = @deleted_job_id)
      IF (@task_id_as_char IS NOT NULL)
        EXECUTE ('master.dbo.sp_cleanupwebtask @taskid = ' + @task_id_as_char)
    END

    -- Maintenance plan cleanup for SQL 2005.
    -- If this job came from another server and it runs a subplan of a
    -- maintenance plan, then delete the subplan record. If that was
    -- the last subplan still referencing that plan, delete the plan.
    -- This removes a distributed maintenance plan from a target server
    -- once all of jobs from the master server that used that maintenance
    -- plan are deleted.
    SELECT @maintplan_plan_id = plans.plan_id, @maintplan_subplan_id = plans.subplan_id
    FROM sysmaintplan_subplans plans, sysjobs_view sjv
    WHERE plans.job_id = @deleted_job_id
      AND plans.job_id = sjv.job_id
      AND sjv.master_server = 1 -- This means the job came from the master

    IF (@maintplan_subplan_id is not NULL)
    BEGIN
      EXECUTE sp_maintplan_delete_subplan @subplan_id = @maintplan_subplan_id, @delete_jobs = 0
      IF (NOT EXISTS (SELECT *
                      FROM sysmaintplan_subplans
                      where plan_id = @maintplan_plan_id))
      BEGIN
        DECLARE @plan_name sysname

        SELECT @plan_name = name
          FROM sysmaintplan_plans
          WHERE id = @maintplan_plan_id

        EXECUTE sp_ssis_deletepackage @name = @plan_name, @folderid = '08aa12d5-8f98-4dab-a4fc-980b150a5dc8' -- this is the guid for 'Maintenance Plans'
      END
    END

    FETCH NEXT FROM sqlagent_notify INTO @deleted_job_id, @job_is_cached
  END
  DEALLOCATE sqlagent_notify

  -- Remove systaskid references (must do this AFTER sp_cleanupwebtask stuff)
  DELETE FROM msdb.dbo.systaskids
  WHERE job_id IN (SELECT job_id FROM #temp_jobs_to_delete)

  -- Remove sysdbmaintplan_jobs references (legacy maintenance plans prior to SQL 2005)
  DELETE FROM msdb.dbo.sysdbmaintplan_jobs
  WHERE job_id IN (SELECT job_id FROM #temp_jobs_to_delete)

  -- Finally, clean up any dangling references in sysalerts to the deleted job(s)
  DECLARE sysalerts_cleanup CURSOR LOCAL
  FOR
  SELECT name
  FROM msdb.dbo.sysalerts
  WHERE (job_id IN (SELECT job_id FROM #temp_jobs_to_delete))

  OPEN sysalerts_cleanup
  FETCH NEXT FROM sysalerts_cleanup INTO @alert_name
  WHILE (@@fetch_status = 0)
  BEGIN
    EXECUTE msdb.dbo.sp_update_alert @name   = @alert_name,
                                     @job_id = 0x00
    FETCH NEXT FROM sysalerts_cleanup INTO @alert_name
  END
  DEALLOCATE sysalerts_cleanup
END

dbo,sp_delete_jobschedule,CREATE PROCEDURE sp_delete_jobschedule           -- This SP is deprecated. Use sp_detach_schedule and sp_delete_schedule.
  @job_id           UNIQUEIDENTIFIER = NULL,
  @job_name         sysname          = NULL,
  @name             sysname,
  @keep_schedule    int              = 0,
  @automatic_post       BIT          = 1         -- If 1 will post notifications to all tsx servers to that run this schedule
AS
BEGIN
  DECLARE @retval           INT
  DECLARE @sched_count      INT
  DECLARE @schedule_id      INT
  DECLARE @job_owner_sid    VARBINARY(85)

  SET NOCOUNT ON

  -- Remove any leading/trailing spaces from parameters
  SELECT @name = LTRIM(RTRIM(@name))

  -- Check authority (only SQLServerAgent can delete a schedule of a non-local job)
  EXECUTE @retval = sp_verify_jobproc_caller @job_id = @job_id, @program_name = N'SQLAgent%'
  IF (@retval <> 0)
    RETURN(@retval)

  -- Check that we can uniquely identify the job
  EXECUTE @retval = sp_verify_job_identifiers '@job_name',
                                              '@job_id',
                                               @job_name OUTPUT,
                                               @job_id   OUTPUT,
                                               @owner_sid = @job_owner_sid OUTPUT
  IF (@retval <> 0)
    RETURN(1) -- Failure

  IF ((ISNULL(IS_SRVROLEMEMBER(N'sysadmin'), 0) <> 1) AND
      (SUSER_SID() <> @job_owner_sid))
  BEGIN
   RAISERROR(14525, -1, -1)
   RETURN(1) -- Failure
  END


  IF (UPPER(@name collate SQL_Latin1_General_CP1_CS_AS) = N'ALL')
  BEGIN
    SELECT @schedule_id = -1  -- We use this in the call to sp_sqlagent_notify
    
    --Delete the schedule(s) if it isn't being used by other jobs
    DECLARE @temp_schedules_to_delete TABLE (schedule_id INT NOT NULL)


    --If user requests that the schedules be removed (the legacy behavoir)
    --make sure it isnt being used by other jobs
    IF (@keep_schedule = 0)
    BEGIN
        --Get the list of schedules to delete
        INSERT INTO @temp_schedules_to_delete
        SELECT DISTINCT schedule_id 
        FROM   msdb.dbo.sysschedules
        WHERE (schedule_id IN 
                (SELECT schedule_id
                FROM msdb.dbo.sysjobschedules
                WHERE (job_id = @job_id)))
            
        --make sure no other jobs use these schedules
        IF( EXISTS(SELECT *
                    FROM msdb.dbo.sysjobschedules 
                    WHERE (job_id <> @job_id)
                    AND (schedule_id in ( SELECT schedule_id 
                                            FROM @temp_schedules_to_delete ))))
        BEGIN
        RAISERROR(14367, -1, -1)   
        RETURN(1) -- Failure
        END
    END

    --OK to delete the jobschedule
    DELETE FROM msdb.dbo.sysjobschedules
    WHERE (job_id = @job_id)
    
    --OK to delete the schedule - temp_schedules_to_delete is empty if @keep_schedule <> 0
    DELETE FROM msdb.dbo.sysschedules
    WHERE schedule_id IN 
    (SELECT schedule_id from @temp_schedules_to_delete)
  END
  ELSE
  BEGIN

    -- Make sure the schedule_id can be uniquely identified and that it exists
    -- Note: It's safe use the values returned by the MIN() function because the SP errors out if more than 1 record exists
    SELECT @sched_count = COUNT(*),
           @schedule_id = MIN(sched.schedule_id)
    FROM msdb.dbo.sysjobschedules as jsched
      JOIN msdb.dbo.sysschedules_localserver_view as sched
        ON jsched.schedule_id = sched.schedule_id
    WHERE (jsched.job_id = @job_id)
      AND (sched.name = @name)
  
    -- Need to use sp_detach_schedule to remove this ambiguous schedule name
    IF(@sched_count > 1)
    BEGIN
      RAISERROR(14376, -1, -1, @name, @job_name)
      RETURN(1) -- Failure
    END

    IF (@schedule_id IS NULL)
    BEGIN    
     --raise an explicit message if the schedule does exist but isn't attached to this job
     IF EXISTS(SELECT * 
             FROM sysschedules_localserver_view
                WHERE (name = @name))
     BEGIN
      RAISERROR(14374, -1, -1, @name, @job_name)
     END
     ELSE
      BEGIN
        --If the schedule is from an MSX and a sysadmin is calling report a specific 'MSX' message
        IF(PROGRAM_NAME() NOT LIKE N'SQLAgent%' AND
           ISNULL(IS_SRVROLEMEMBER(N'sysadmin'), 0) = 1 AND
           EXISTS(SELECT * 
                  FROM msdb.dbo.sysschedules as sched
                    JOIN msdb.dbo.sysoriginatingservers_view as svr
                      ON sched.originating_server_id = svr.originating_server_id
                    JOIN msdb.dbo.sysjobschedules as js 
                      ON sched.schedule_id = js.schedule_id
                  WHERE (svr.master_server = 1) AND
                        (sched.name = @name) AND
                        (js.job_id = @job_id)))
       BEGIN
         RAISERROR(14274, -1, -1)
       END
        ELSE
        BEGIN
          --Generic message that the schedule doesn't exist
          RAISERROR(14262, -1, -1, '@name', @name)
        END
     END

      RETURN(1) -- Failure
    END

    --If user requests that the schedule be removed (the legacy behavoir)
    --make sure it isnt being used by another job
    IF (@keep_schedule = 0)
    BEGIN
      IF( EXISTS(SELECT * 
                 FROM msdb.dbo.sysjobschedules
                 WHERE (schedule_id = @schedule_id)
                   AND (job_id <> @job_id) ))
      BEGIN
        RAISERROR(14368, -1, -1, @name)
        RETURN(1) -- Failure
      END
    END

    --Delete the job schedule link first
    DELETE FROM msdb.dbo.sysjobschedules
    WHERE (job_id = @job_id)
    AND (schedule_id = @schedule_id)
    --Delete schedule if required
    IF (@keep_schedule = 0)
    BEGIN
      --Now delete the schedule if required
      DELETE FROM msdb.dbo.sysschedules
      WHERE (schedule_id = @schedule_id)   
    END

  END


  -- Update the job's version/last-modified information
  UPDATE msdb.dbo.sysjobs
  SET version_number = version_number + 1,
      date_modified = GETDATE()
  WHERE (job_id = @job_id)

  -- Notify SQLServerAgent of the change, but only if we know the job has been cached
  IF (EXISTS (SELECT *
              FROM msdb.dbo.sysjobservers
              WHERE (job_id = @job_id)
                AND (server_id = 0)))
  BEGIN
    EXECUTE msdb.dbo.sp_sqlagent_notify @op_type     = N'S',
                                        @job_id      = @job_id,
                                        @schedule_id = @schedule_id,
                                        @action_type = N'D'
  END

  -- For a multi-server job, remind the user that they need to call sp_post_msx_operation
  IF (EXISTS (SELECT *
              FROM msdb.dbo.sysjobservers
              WHERE (job_id = @job_id)
                AND (server_id <> 0)))
    -- Instruct the tsx servers to pick up the altered schedule
    IF (@automatic_post = 1)
    BEGIN
      DECLARE @schedule_uid UNIQUEIDENTIFIER
      SELECT @schedule_uid = schedule_uid 
      FROM sysschedules 
      WHERE schedule_id = @schedule_id

      IF(NOT @schedule_uid IS NULL)
      BEGIN
        -- sp_post_msx_operation will do nothing if the schedule isn't assigned to any tsx machines 
        EXECUTE sp_post_msx_operation @operation = 'INSERT', @object_type = 'SCHEDULE', @schedule_uid = @schedule_uid
      END
    END
    ELSE
      RAISERROR(14547, 0, 1, N'INSERT', N'sp_post_msx_operation')

  RETURN(@retval) -- 0 means success
END

dbo,sp_delete_jobserver,CREATE PROCEDURE sp_delete_jobserver
  @job_id      UNIQUEIDENTIFIER = NULL, -- Must provide either this or job_name
  @job_name    sysname          = NULL, -- Must provide either this or job_id
  @server_name sysname
AS
BEGIN
  DECLARE @retval             INT
  DECLARE @server_id          INT
  DECLARE @local_machine_name sysname

  SET NOCOUNT ON

  /* check input parameters */
  IF @server_name IS NULL
  BEGIN
  RAISERROR(14043, -1, -1, '@server_name')
  RETURN(1) -- Failure
  END

  -- Remove any leading/trailing spaces from parameters
  -- and convert it to upper for future comparisons
  SELECT @server_name = UPPER(LTRIM(RTRIM(@server_name)))

  IF (@server_name collate SQL_Latin1_General_CP1_CS_AS = '(LOCAL)')
  BEGIN
    SELECT @server_name = UPPER(CONVERT(sysname, SERVERPROPERTY('MachineName')))
  END

  EXECUTE @retval = sp_verify_job_identifiers '@job_name',
                                              '@job_id',
                                               @job_name OUTPUT,
                                               @job_id   OUTPUT
  IF (@retval <> 0)
  BEGIN
    RETURN(1) -- Failure
  END

  -- If a msx jobserver is being removed, 
  -- get server_id is 0 
  -- else server_id record matching the server_name from systargetservers
  IF (@server_name <> UPPER(CONVERT(sysname, SERVERPROPERTY('ServerName'))))
  BEGIN
    SELECT @server_id = server_id
    FROM msdb.dbo.systargetservers
    WHERE (UPPER(server_name) = @server_name)
    IF (@server_id IS NULL)
    BEGIN
      RAISERROR(14262, -1, -1, '@server_name', @server_name)
      RETURN(1) -- Failure
    END
  END
  ELSE
  BEGIN
    SELECT @server_id = 0
  END

  -- Check that the job is actually targeted at the server
  IF (NOT EXISTS (SELECT *
                  FROM msdb.dbo.sysjobservers
                  WHERE (job_id = @job_id)
                    AND (server_id = @server_id)))
  BEGIN
    RAISERROR(14270, -1, -1, @job_name, @server_name)
    RETURN(1) -- Failure
  END

  -- Instruct the deleted server to purge the job
  -- NOTE: We must do this BEFORE we delete the sysjobservers row
  EXECUTE @retval = sp_post_msx_operation 'DELETE', 'JOB', @job_id, @server_name

  -- Delete the sysjobservers row
  DELETE FROM msdb.dbo.sysjobservers
  WHERE (job_id = @job_id)
    AND (server_id = @server_id)

  -- If the job is local, make sure that SQLServerAgent removes it from cache
  IF (@server_id = 0)
  BEGIN
    EXECUTE msdb.dbo.sp_sqlagent_notify @op_type     = N'J',
                                        @job_id      = @job_id,
                                        @action_type = N'D'
  END

  RETURN(@retval) -- 0 means success
END

dbo,sp_delete_jobstep,CREATE PROCEDURE sp_delete_jobstep
  @job_id   UNIQUEIDENTIFIER = NULL, -- Must provide either this or job_name
  @job_name sysname          = NULL, -- Must provide either this or job_id
  @step_id  INT
AS
BEGIN
  DECLARE @retval      INT
  DECLARE @max_step_id INT
  DECLARE @valid_range VARCHAR(50)
  DECLARE @job_owner_sid VARBINARY(85)

  SET NOCOUNT ON

  EXECUTE @retval = sp_verify_job_identifiers '@job_name',
                                              '@job_id',
                                               @job_name OUTPUT,
                                               @job_id   OUTPUT,
                                               @owner_sid = @job_owner_sid OUTPUT
  IF (@retval <> 0)
    RETURN(1) -- Failure

  -- Check authority (only SQLServerAgent can delete a step of a non-local job)
  EXECUTE @retval = sp_verify_jobproc_caller @job_id = @job_id, @program_name = 'SQLAgent%'
  IF (@retval <> 0)
    RETURN(@retval)
    
  -- SQLAgentReader and SQLAgentOperator roles that can see all jobs
  -- cannot modify jobs they do not own
  IF (@job_owner_sid <> SUSER_SID()                   -- does not own the job
     AND (ISNULL(IS_SRVROLEMEMBER(N'sysadmin'), 0) <> 1))   -- is not sysadmin
  BEGIN
   RAISERROR(14525, -1, -1);
   RETURN(1) -- Failure
  END

  -- Get current maximum step id
  SELECT @max_step_id = ISNULL(MAX(step_id), 0)
  FROM msdb.dbo.sysjobsteps
  WHERE (job_id = @job_id)

  -- Check step id
  IF (@step_id < 0) OR (@step_id > @max_step_id)
  BEGIN
    SELECT @valid_range = FORMATMESSAGE(14201) + CONVERT(VARCHAR, @max_step_id)
    RAISERROR(14266, -1, -1, '@step_id', @valid_range)
    RETURN(1) -- Failure
  END

  BEGIN TRANSACTION

    -- Delete either the specified step or ALL the steps (if step id is 0)
    IF (@step_id = 0)
    BEGIN
      DELETE FROM msdb.dbo.sysjobsteps
      WHERE (job_id = @job_id)
     END
      ELSE
     BEGIN
      DELETE FROM msdb.dbo.sysjobsteps
      WHERE (job_id = @job_id)
        AND (step_id = @step_id)
    END

    IF (@step_id <> 0)
    BEGIN
      -- Adjust step id's
      UPDATE msdb.dbo.sysjobsteps
      SET step_id = step_id - 1
      WHERE (step_id > @step_id)
        AND (job_id = @job_id)

      -- Clean up OnSuccess/OnFail references
      UPDATE msdb.dbo.sysjobsteps
      SET on_success_step_id = on_success_step_id - 1
      WHERE (on_success_step_id > @step_id)
        AND (job_id = @job_id)

      UPDATE msdb.dbo.sysjobsteps
      SET on_fail_step_id = on_fail_step_id - 1
      WHERE (on_fail_step_id > @step_id)
        AND (job_id = @job_id)

      UPDATE msdb.dbo.sysjobsteps
      SET on_success_step_id = 0,
          on_success_action = 1   -- Quit With Success
      WHERE (on_success_step_id = @step_id)
        AND (job_id = @job_id)

      UPDATE msdb.dbo.sysjobsteps
      SET on_fail_step_id = 0,
          on_fail_action = 2   -- Quit With Failure
      WHERE (on_fail_step_id = @step_id)
        AND (job_id = @job_id)
        
    END

    
    -- Update the job's version/last-modified information
    UPDATE msdb.dbo.sysjobs
    SET version_number = version_number + 1,
        date_modified = GETDATE()
    WHERE (job_id = @job_id)

  COMMIT TRANSACTION

  -- Make sure that SQLServerAgent refreshes the job if the 'Has Steps' property has changed
  IF ((SELECT COUNT(*)
       FROM msdb.dbo.sysjobsteps
       WHERE (job_id = @job_id)) = 0)
  BEGIN
    -- NOTE: We only notify SQLServerAgent if we know the job has been cached
    IF (EXISTS (SELECT *
                FROM msdb.dbo.sysjobservers
                WHERE (job_id = @job_id)
                  AND (server_id = 0)))
      EXECUTE msdb.dbo.sp_sqlagent_notify @op_type       = N'J',
                                            @job_id      = @job_id,
                                            @action_type = N'U'
  END

  -- For a multi-server job, push changes to the target servers
  IF (EXISTS (SELECT *
              FROM msdb.dbo.sysjobservers
              WHERE (job_id = @job_id)
                AND (server_id <> 0)))
  BEGIN
    EXECUTE msdb.dbo.sp_post_msx_operation 'INSERT', 'JOB', @job_id
  END

  RETURN(0) -- Success
END

dbo,sp_delete_jobsteplog,CREATE PROCEDURE sp_delete_jobsteplog
  @job_id      UNIQUEIDENTIFIER = NULL, -- Must provide either this or job_name
  @job_name    sysname          = NULL, -- Must provide either this or job_id
  @step_id     INT              = NULL,
  @step_name   sysname          = NULL,
  @older_than  datetime         = NULL,
  @larger_than int      = NULL   -- (in megabytes)
AS
BEGIN
  DECLARE @retval      INT
  DECLARE @max_step_id INT
  DECLARE @valid_range VARCHAR(50)

  EXECUTE @retval = sp_verify_job_identifiers '@job_name',
                                              '@job_id',
                                               @job_name OUTPUT,
                                               @job_id   OUTPUT,
                                              'NO_TEST'
  IF (@retval <> 0)
    RETURN(1) -- Failure

  -- Check step id (if supplied)
  IF (@step_id IS NOT NULL)
  BEGIN
    -- Get current maximum step id
    SELECT @max_step_id = ISNULL(MAX(step_id), 0)
    FROM msdb.dbo.sysjobsteps
    WHERE job_id = @job_id
   IF @max_step_id = 0
   BEGIN
      RAISERROR(14528, -1, -1, @job_name)
      RETURN(1) -- Failure 
   END
    ELSE IF (@step_id < 1) OR (@step_id > @max_step_id)
    BEGIN
      SELECT @valid_range = '1..' + CONVERT(VARCHAR, @max_step_id)
      RAISERROR(14266, -1, -1, '@step_id', @valid_range)
      RETURN(1) -- Failure
    END
  END

  -- Check step name (if supplied)
  -- NOTE: A supplied step id overrides a supplied step name
  IF ((@step_id IS NULL) AND (@step_name IS NOT NULL))
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


   -- Delete either the specified step or ALL the steps (if step id is NULL)
   
   DELETE FROM msdb.dbo.sysjobstepslogs
   WHERE (step_uid IN (SELECT DISTINCT step_uid 
                        FROM   msdb.dbo.sysjobsteps js, msdb.dbo.sysjobs_view jv
                        WHERE (  @job_id = jv.job_id )
                          AND (js.job_id = jv.job_id )
                          AND ((@step_id IS NULL) OR (@step_id = step_id)))) 
    AND ((@older_than IS NULL) OR (date_modified < @older_than))
    AND ((@larger_than IS NULL) OR (log_size > @larger_than))

  RETURN(@retval) -- 0 means success

END

dbo,sp_delete_log_shipping_monitor_info,CREATE PROCEDURE sp_delete_log_shipping_monitor_info
  @primary_server_name                 sysname,
  @primary_database_name               sysname,
  @secondary_server_name               sysname,
  @secondary_database_name             sysname
AS BEGIN
  -- check that the primary exists
  IF (NOT EXISTS (SELECT * FROM msdb.dbo.log_shipping_primaries WHERE primary_server_name = @primary_server_name AND primary_database_name = @primary_database_name))
  BEGIN
    DECLARE @pp sysname
    SELECT @pp = @primary_server_name + N'.' + @primary_database_name
    RAISERROR (14262, 16, 1, N'primary_server_name.primary_database_name', @pp)
    RETURN (1) -- error
  END

  -- check that the secondary exists
  IF (NOT EXISTS (SELECT * FROM msdb.dbo.log_shipping_secondaries WHERE secondary_server_name = @secondary_server_name AND secondary_database_name = @secondary_database_name))
  BEGIN
    DECLARE @sp sysname
    SELECT @sp = @secondary_server_name + N'.' + @secondary_database_name
    RAISERROR (14262, 16, 1, N'secondary_server_name.secondary_database_name', @sp)
    RETURN (1) -- error
  END

  BEGIN TRANSACTION

  -- delete the secondary
  DELETE FROM msdb.dbo.log_shipping_secondaries WHERE secondary_server_name = @secondary_server_name AND secondary_database_name = @secondary_database_name
  IF (@@error <> 0)
    goto rollback_quit

  -- if there are no more secondaries for this primary then delete it
  IF (NOT EXISTS (SELECT * FROM msdb.dbo.log_shipping_primaries p, msdb.dbo.log_shipping_secondaries s WHERE p.primary_id = s.primary_id AND primary_server_name = @primary_server_name AND primary_database_name = @primary_database_name))
  BEGIN
    DELETE FROM msdb.dbo.log_shipping_primaries WHERE primary_server_name = @primary_server_name AND primary_database_name = @primary_database_name
    IF (@@error <> 0)
      goto rollback_quit
  END
 COMMIT TRANSACTION
 RETURN (0)

rollback_quit:
  ROLLBACK TRANSACTION
  RETURN(1) -- Failure
END

dbo,sp_delete_log_shipping_monitor_jobs,CREATE PROCEDURE sp_delete_log_shipping_monitor_jobs AS
BEGIN
  DECLARE @backup_job_name sysname
  SET NOCOUNT ON
  SET @backup_job_name = N'Log Shipping Alert Job - Backup'
  IF (EXISTS (SELECT * FROM msdb.dbo.sysjobs WHERE name = @backup_job_name))
    EXECUTE msdb.dbo.sp_delete_job @job_name = N'Log Shipping Alert Job - Backup'

  DECLARE @restore_job_name sysname
  SET @restore_job_name = 'Log Shipping Alert Job - Restore'
  IF (EXISTS (SELECT * FROM msdb.dbo.sysjobs WHERE name = @restore_job_name))
    EXECUTE msdb.dbo.sp_delete_job @job_name = N'Log Shipping Alert Job - Restore'
END

dbo,sp_delete_log_shipping_primary,CREATE PROCEDURE sp_delete_log_shipping_primary 
  @primary_server_name sysname,
  @primary_database_name sysname,
  @delete_secondaries BIT = 0
AS BEGIN
  DECLARE @primary_id INT

  SET NOCOUNT ON

  SELECT @primary_id = primary_id 
    FROM msdb.dbo.log_shipping_primaries 
    WHERE primary_server_name = @primary_server_name AND primary_database_name = @primary_database_name
  IF (@primary_id IS NULL)
    RETURN (0)

  BEGIN TRANSACTION
  IF (EXISTS (SELECT * FROM msdb.dbo.log_shipping_secondaries WHERE primary_id = @primary_id))
  BEGIN
    IF (@delete_secondaries = 0)
    BEGIN
      RAISERROR (14429,-1,-1)
      goto rollback_quit
    END
    DELETE FROM msdb.dbo.log_shipping_secondaries WHERE primary_id = @primary_id
    IF (@@ERROR <> 0)
      GOTO rollback_quit
  END
  DELETE FROM msdb.dbo.log_shipping_primaries WHERE primary_id = @primary_id
  IF (@@ERROR <> 0)
    GOTO rollback_quit

  COMMIT TRANSACTION
  DECLARE @i INT
  SELECT @i = COUNT(*) FROM msdb.dbo.log_shipping_primaries
  IF (@i=0)
    EXECUTE msdb.dbo.sp_delete_log_shipping_monitor_jobs
  RETURN (0)

rollback_quit:
  ROLLBACK TRANSACTION
  RETURN(1) -- error
END

dbo,sp_delete_log_shipping_secondary,CREATE PROCEDURE sp_delete_log_shipping_secondary 
  @secondary_server_name   sysname,
  @secondary_database_name sysname
AS BEGIN
  SET NOCOUNT ON
  DELETE FROM msdb.dbo.log_shipping_secondaries WHERE 
    secondary_server_name   = @secondary_server_name AND
    secondary_database_name = @secondary_database_name
END

dbo,sp_delete_maintenance_plan,CREATE PROCEDURE sp_delete_maintenance_plan
  @plan_id UNIQUEIDENTIFIER
AS
BEGIN
  /*check if the plan_id is valid*/
  IF (NOT EXISTS(SELECT *
                 FROM sysdbmaintplans
                 WHERE plan_id=@plan_id))
  BEGIN
    DECLARE @syserr VARCHAR(100)
    SELECT @syserr=CONVERT(VARCHAR(100),@plan_id)
    RAISERROR(14262,-1,-1,'@plan_id',@syserr)
    RETURN(1)
  END
  /* clean the related records in sysdbmaintplan_database */
  DELETE FROM msdb.dbo.sysdbmaintplan_databases
  WHERE plan_id=@plan_id
  /* clean the related records in sysdbmaintplan_jobs*/
  DELETE FROM msdb.dbo.sysdbmaintplan_jobs
  WHERE plan_id=@plan_id
  /* clean sysdbmaintplans */
  DELETE FROM msdb.dbo.sysdbmaintplans
  WHERE  plan_id= @plan_id
END

dbo,sp_delete_maintenance_plan_db,CREATE PROCEDURE sp_delete_maintenance_plan_db
  @plan_id uniqueidentifier,
  @db_name sysname
AS
BEGIN
  /*check if the (plan_id, db_name) exists in the table*/
  IF (NOT EXISTS(SELECT *
                 FROM msdb.dbo.sysdbmaintplan_databases
                 WHERE @plan_id=plan_id AND @db_name=database_name))
  BEGIN
    DECLARE @syserr VARCHAR(300)
    SELECT @syserr=CONVERT(VARCHAR(100),@plan_id)+' + '+@db_name
    RAISERROR(14262,-1,-1,'@plan_id+@db_name',@syserr)
    RETURN(1)
  END
  /*delete the pair*/
  DELETE FROM msdb.dbo.sysdbmaintplan_databases
  WHERE plan_id=@plan_id AND database_name=@db_name
END

dbo,sp_delete_maintenance_plan_job,CREATE PROCEDURE sp_delete_maintenance_plan_job
  @plan_id uniqueidentifier,
  @job_id  uniqueidentifier
AS
BEGIN
  /*check if the (plan_id, job_id) exists*/
  IF (NOT EXISTS(SELECT *
                 FROM sysdbmaintplan_jobs
                 WHERE @plan_id=plan_id AND @job_id=job_id))
  BEGIN
    DECLARE @syserr VARCHAR(300)
    SELECT @syserr=CONVERT(VARCHAR(100),@plan_id)+' + '+CONVERT(VARCHAR(100),@job_id)
    RAISERROR(14262,-1,-1,'@plan_id+@job_id',@syserr)
    RETURN(1)
  END
  DELETE FROM msdb.dbo.sysdbmaintplan_jobs
  WHERE plan_id=@plan_id AND job_id=@job_id
END

dbo,sp_delete_notification,CREATE PROCEDURE sp_delete_notification
  @alert_name    sysname,
  @operator_name sysname
AS
BEGIN
  DECLARE @alert_id             INT
  DECLARE @operator_id          INT
  DECLARE @ignored              TINYINT
  DECLARE @notification         NVARCHAR(512)
  DECLARE @retval               INT
  DECLARE @old_has_notification INT
  DECLARE @new_has_notification INT
  DECLARE @res_notification     NVARCHAR(100)

  SET NOCOUNT ON

  SELECT @res_notification = FORMATMESSAGE(14210)

  -- Remove any leading/trailing spaces from parameters
  SELECT @alert_name    = LTRIM(RTRIM(@alert_name))
  SELECT @operator_name = LTRIM(RTRIM(@operator_name))

  -- Only a sysadmin can do this
  IF ((ISNULL(IS_SRVROLEMEMBER(N'sysadmin'), 0) <> 1))
  BEGIN
    RAISERROR(15003, 16, 1, N'sysadmin')
    RETURN(1) -- Failure
  END

  -- Get the alert and operator ID's
  EXECUTE sp_verify_notification @alert_name,
                                 @operator_name,
                                 7,           -- A dummy (but valid) value
                                 @alert_id    OUTPUT,
                                 @operator_id OUTPUT

  -- Check if this notification exists
  IF (NOT EXISTS (SELECT *
                  FROM msdb.dbo.sysnotifications
                  WHERE (alert_id = @alert_id)
                    AND (operator_id = @operator_id)))
  BEGIN
    SELECT @notification = @alert_name + N' / ' + @operator_name
    RAISERROR(14262, 16, 1, @res_notification, @notification)
    RETURN(1) -- Failure
  END

  SELECT @old_has_notification = has_notification
  FROM msdb.dbo.sysalerts
  WHERE (id = @alert_id)

  -- Do the Delete
  DELETE FROM msdb.dbo.sysnotifications
  WHERE (alert_id = @alert_id)
    AND (operator_id = @operator_id)

  SELECT @retval = @@error

  SELECT @new_has_notification = has_notification
  FROM msdb.dbo.sysalerts
  WHERE (id = @alert_id)

  -- Notify SQLServerAgent of the change - if any - to has_notifications
  IF (@old_has_notification <> @new_has_notification)
    EXECUTE msdb.dbo.sp_sqlagent_notify @op_type       = N'A',
                                          @alert_id    = @alert_id,
                                          @action_type = N'U'

  RETURN(@retval) -- 0 means success
END

dbo,sp_delete_operator,CREATE PROCEDURE sp_delete_operator
  @name                 sysname,
  @reassign_to_operator sysname = NULL
AS
BEGIN
  DECLARE @id                         INT
  DECLARE @alert_fail_safe_operator   sysname
  DECLARE @job_id                     UNIQUEIDENTIFIER
  DECLARE @job_id_as_char             VARCHAR(36)
  DECLARE @notify_email_operator_id   INT
  DECLARE @notify_netsend_operator_id INT
  DECLARE @notify_page_operator_id    INT
  DECLARE @reassign_to_id             INT
  DECLARE @cmd                        NVARCHAR(1000)
  DECLARE @current_msx_server         sysname
  DECLARE @reassign_to_escaped        NVARCHAR(256)

  SET NOCOUNT ON

  -- Remove any leading/trailing spaces from parameters
  SELECT @name                 = LTRIM(RTRIM(@name))
  SELECT @reassign_to_operator = LTRIM(RTRIM(@reassign_to_operator))

  -- Turn [nullable] empty string parameters into NULLs
  IF (@reassign_to_operator = N'') SELECT @reassign_to_operator = NULL

  -- Only a sysadmin can do this
  IF ((ISNULL(IS_SRVROLEMEMBER(N'sysadmin'), 0) <> 1))
  BEGIN
    RAISERROR(15003, 16, 1, N'sysadmin')
    RETURN(1) -- Failure
  END

  -- Check if this Operator exists
  IF (NOT EXISTS (SELECT *
                  FROM msdb.dbo.sysoperators
                  WHERE (name = @name)))
  BEGIN
    RAISERROR(14262, 16, 1, '@name', @name)
    RETURN(1) -- Failure
  END

  -- Check if this operator the FailSafe Operator
  EXECUTE master.dbo.xp_instance_regread N'HKEY_LOCAL_MACHINE',
                                         N'SOFTWARE\Microsoft\MSSQLServer\SQLServerAgent',
                                         N'AlertFailSafeOperator',
                                         @alert_fail_safe_operator OUTPUT,
                                         N'no_output'

  -- If it is, we disallow the delete operation
  IF (LTRIM(RTRIM(@alert_fail_safe_operator)) = @name)
  BEGIN
    RAISERROR(14504, 16, 1, @name, @name)
    RETURN(1) -- Failure
  END

  -- Check if this operator is 'MSXOperator'
  IF (@name = N'MSXOperator')
  BEGIN
    DECLARE @server_type VARCHAR(3)

    -- Disallow the delete operation if we're an MSX or a TSX
    EXECUTE master.dbo.xp_instance_regread N'HKEY_LOCAL_MACHINE',
                                           N'SOFTWARE\Microsoft\MSSQLServer\SQLServerAgent',
                                           N'MSXServerName',
                                           @current_msx_server OUTPUT,
                                           N'no_output'
    IF (@current_msx_server IS NOT NULL)
      SELECT @server_type = 'TSX'

    IF ((SELECT COUNT(*)
         FROM msdb.dbo.systargetservers) > 0)
      SELECT @server_type = 'MSX'

    IF (@server_type IS NOT NULL)
    BEGIN
      RAISERROR(14223, 16, 1, 'MSXOperator', @server_type)
      RETURN(1) -- Failure
    END
  END

  -- Convert the Name to it's ID
  SELECT @id = id
  FROM msdb.dbo.sysoperators
  WHERE (name = @name)

  IF (@reassign_to_operator IS NOT NULL)
  BEGIN
    -- On a TSX or standalone server, disallow re-assigning to the MSXOperator
    IF (@reassign_to_operator = N'MSXOperator') AND
       (NOT EXISTS (SELECT *
                    FROM msdb.dbo.systargetservers))
    BEGIN
      RAISERROR(14251, -1, -1, @reassign_to_operator)
      RETURN(1) -- Failure
    END

    SELECT @reassign_to_id = id
    FROM msdb.dbo.sysoperators
    WHERE (name = @reassign_to_operator)

    IF (@reassign_to_id IS NULL)
    BEGIN
      RAISERROR(14262, -1, -1, '@reassign_to_operator', @reassign_to_operator)
      RETURN(1) -- Failure
    END
  END

  -- Double up any single quotes in @reassign_to_operator
  IF (@reassign_to_operator IS NOT NULL)
    SET @reassign_to_escaped  = REPLACE(@reassign_to_operator, N'''', N'''''')

  BEGIN TRANSACTION

    -- Reassign (or delete) any sysnotifications rows that reference this operator
    IF (@reassign_to_operator IS NOT NULL)
    BEGIN
      UPDATE msdb.dbo.sysnotifications
      SET operator_id = @reassign_to_id
      WHERE (operator_id = @id)
        AND (NOT EXISTS (SELECT *
                         FROM msdb.dbo.sysnotifications sn2
                         WHERE (sn2.alert_id = msdb.dbo.sysnotifications.alert_id)
                           AND (sn2.operator_id = @reassign_to_id)))
    END

    DELETE FROM msdb.dbo.sysnotifications
    WHERE (operator_id = @id)

    -- Update any jobs that reference this operator
    DECLARE jobs_referencing_this_operator CURSOR LOCAL
    FOR
    SELECT job_id,
           notify_email_operator_id,
           notify_netsend_operator_id,
           notify_page_operator_id
    FROM msdb.dbo.sysjobs
    WHERE (notify_email_operator_id = @id)
       OR (notify_netsend_operator_id = @id)
       OR (notify_page_operator_id = @id)

    OPEN jobs_referencing_this_operator
    FETCH NEXT FROM jobs_referencing_this_operator INTO @job_id,
                                                        @notify_email_operator_id,
                                                        @notify_netsend_operator_id,
                                                        @notify_page_operator_id
    WHILE (@@fetch_status = 0)
    BEGIN
      SELECT @job_id_as_char = CONVERT(VARCHAR(36), @job_id)
      SELECT @cmd = N'msdb.dbo.sp_update_job @job_id = ''' + @job_id_as_char + N''', '

      IF (@notify_email_operator_id = @id)
        IF (@reassign_to_operator IS NOT NULL)
          SELECT @cmd = @cmd + N'@notify_email_operator_name = N''' + @reassign_to_escaped  + N''', '
        ELSE
          SELECT @cmd = @cmd + N'@notify_email_operator_name = N'''', @notify_level_email = 0, '

      IF (@notify_netsend_operator_id = @id)
        IF (@reassign_to_operator IS NOT NULL)
          SELECT @cmd = @cmd + N'@notify_netsend_operator_name = N''' + @reassign_to_escaped  + N''', '
        ELSE
          SELECT @cmd = @cmd + N'@notify_netsend_operator_name = N'''', @notify_level_netsend = 0, '

      IF (@notify_page_operator_id = @id)
        IF (@reassign_to_operator IS NOT NULL)
          SELECT @cmd = @cmd + N'@notify_page_operator_name = N''' + @reassign_to_escaped  + N''', '
        ELSE
          SELECT @cmd = @cmd + N'@notify_page_operator_name = N'''', @notify_level_page = 0, '

      SELECT @cmd = SUBSTRING(@cmd, 1, (DATALENGTH(@cmd) / 2) - 2)
      EXECUTE (N'EXECUTE ' + @cmd)

      FETCH NEXT FROM jobs_referencing_this_operator INTO @job_id,
                                                          @notify_email_operator_id,
                                                          @notify_netsend_operator_id,
                                                          @notify_page_operator_id
    END
    DEALLOCATE jobs_referencing_this_operator

    -- Finally, do the actual DELETE
    DELETE FROM msdb.dbo.sysoperators
    WHERE (id = @id)

  COMMIT TRANSACTION

  RETURN(@@error) -- 0 means success
END
```

