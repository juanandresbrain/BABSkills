# dbo.sp_syscollector_snapshot_dm_exec_requests_internal

**Database:** msdb  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_syscollector_snapshot_dm_exec_requests_internal"]
    SP --> NoRefs(["No table dependencies detected"])
```

## Table Dependencies

_No table references detected automatically._

## Stored Procedure Code

```sql
CREATE PROC [dbo].[sp_syscollector_snapshot_dm_exec_requests_internal]
  @include_system_databases bit = 1
AS
BEGIN
    SET NOCOUNT ON

    -- Get the collection time as UTC time
    DECLARE @collection_time datetime
    SET @collection_time = GETDATE()

    SELECT
    CONVERT(INT, ROW_NUMBER() OVER (ORDER BY sess.session_id, ISNULL (req.request_id, -1), ISNULL (tasks.exec_context_id, -1)) ) AS row_id,
    -- IDs and Blocking IDs
    sess.session_id, 
    ISNULL (req.request_id, -1) AS request_id, 
    ISNULL (tasks.exec_context_id, -1) AS exec_context_id, 
    ISNULL (req.blocking_session_id, 0) AS blocking_session_id,
    CONVERT (BIT, CASE 
                    WHEN EXISTS (SELECT TOP 1 session_id FROM sys.dm_exec_requests bl WHERE bl.blocking_session_id = req.session_id) THEN 1
                    ELSE 0
                  END) AS is_blocking,
    ISNULL (waits.blocking_exec_context_id, 0) AS blocking_exec_context_id, 
    tasks.scheduler_id, 
    DB_NAME(req.database_id) as database_name, 
    req.[user_id], 

    -- State information
    LEFT (tasks.task_state, 10) AS task_state, 
    LEFT (req.status, 15) AS request_status, 
    LEFT (sess.status, 15) AS session_status,
    req.executing_managed_code, 

    -- Session information
    sess.login_time, 
    sess.is_user_process, 
    LEFT (ISNULL (sess.[host_name], ''), 20) AS [host_name], 
    LEFT (ISNULL (sess.[program_name], ''), 50) AS [program_name], 
    LEFT (ISNULL (sess.login_name, ''), 30) AS login_name, 

    -- Waits information
    LEFT (ISNULL (req.wait_type, ''), 45) AS wait_type, 
    LEFT (ISNULL (req.last_wait_type, ''), 45) AS last_wait_type, 
    ISNULL (waits.wait_duration_ms, 0) AS wait_duration_ms, 
    LEFT (ISNULL (req.wait_resource, ''), 50) AS wait_resource, 
    LEFT (ISNULL (waits.resource_description, ''), 140) AS resource_description,

    -- Transaction information
    req.transaction_id, 
    ISNULL(req.open_transaction_count, 0) AS open_transaction_count,
    COALESCE(req.transaction_isolation_level, sess.transaction_isolation_level) AS transaction_isolation_level,

    -- Request stats
    req.cpu_time AS request_cpu_time, 
    req.logical_reads AS request_logical_reads, 
    req.reads AS request_reads, 
    req.writes AS request_writes, 
    req.total_elapsed_time AS request_total_elapsed_time, 
    req.start_time AS request_start_time, 

    -- Session stats
    sess.memory_usage, 
    sess.cpu_time AS session_cpu_time, 
    sess.reads AS session_reads, 
    sess.writes AS session_writes, 
    sess.logical_reads AS session_logical_reads, 
    sess.total_scheduled_time AS session_total_scheduled_time, 
    sess.total_elapsed_time AS session_total_elapsed_time, 
    sess.last_request_start_time, 
    sess.last_request_end_time, 
    req.open_resultset_count AS open_resultsets, 
    sess.row_count AS session_row_count, 
    sess.prev_error, 
    tasks.pending_io_count, 

    -- Text/Plan handles
    ISNULL (req.command, 'AWAITING COMMAND') AS command,  
    req.plan_handle, 
    req.sql_handle, 
    req.statement_start_offset, 
    req.statement_end_offset,
    @collection_time AS collection_time
    FROM sys.dm_exec_sessions sess 
    LEFT OUTER MERGE JOIN sys.dm_exec_requests req  ON sess.session_id = req.session_id
    LEFT OUTER MERGE JOIN sys.dm_os_tasks tasks ON tasks.session_id = sess.session_id AND tasks.request_id = req.request_id AND tasks.task_address = req.task_address
    LEFT OUTER MERGE JOIN sys.dm_os_waiting_tasks waits ON waits.session_id = sess.session_id AND waits.waiting_task_address = req.task_address
    WHERE 
        sess.session_id <> @@SPID
        AND
        (
            (req.session_id IS NOT NULL AND (sess.is_user_process = 1 OR req.status COLLATE Latin1_General_BIN NOT IN ('background', 'sleeping')))    -- active request
                OR 
            (sess.session_id IN (SELECT DISTINCT blocking_session_id FROM sys.dm_exec_requests WHERE blocking_session_id != 0))                    -- not active, but head blocker
        )
        AND (@include_system_databases = 1 OR (req.database_id > 4 AND req.database_id < 32767))
    OPTION (FORCE ORDER)
END

dbo,sp_syscollector_sql_text_lookup,CREATE PROCEDURE [dbo].[sp_syscollector_sql_text_lookup]
    @sql_handle varbinary(64)
AS
BEGIN
    SET NOCOUNT ON
    SELECT    
        @sql_handle as sql_handle,
        dm.[dbid] AS database_id,
        dm.[objectid] AS object_id,
        OBJECT_NAME(objectid, dbid) AS object_name,
        CASE dm.[encrypted]
            WHEN 1 THEN N'Query SQL Text Encrypted'
            ELSE dm.[text]
        END AS sql_text
        FROM    
            [sys].[dm_exec_sql_text](@sql_handle) dm
END

dbo,sp_syscollector_start_collection_set,CREATE PROCEDURE [dbo].[sp_syscollector_start_collection_set]
    @collection_set_id        int = NULL,
    @name                     sysname = NULL
WITH EXECUTE AS OWNER -- 'MS_DataCollectorInternalUser'
AS
BEGIN
    SET NOCOUNT ON

    DECLARE @TranCounter INT
    SET @TranCounter = @@TRANCOUNT
    IF (@TranCounter > 0)
        SAVE TRANSACTION tran_start_collection_set
    ELSE
        BEGIN TRANSACTION

    BEGIN TRY

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
        RAISERROR(14688, -1, -1)
        RETURN (1)
    END

    -- check if MDW is setup
    DECLARE @instance_name sysname
    SELECT @instance_name = CONVERT(sysname,parameter_value)
    FROM [msdb].[dbo].[syscollector_config_store_internal]
    WHERE parameter_name = N'MDWInstance'
    IF (@instance_name IS NULL)
    BEGIN
        RAISERROR(14689, -1, -1)
        RETURN (1)
    END    
    DECLARE @database_name sysname
    SELECT @database_name = CONVERT(sysname,parameter_value)
    FROM [msdb].[dbo].[syscollector_config_store_internal]
    WHERE parameter_name = N'MDWDatabase'
    IF (@database_name IS NULL)
    BEGIN
        RAISERROR(14689, -1, -1)
        RETURN (1)
    END

    -- Verify the input parameters
    DECLARE @retVal int
    EXEC @retVal = dbo.sp_syscollector_verify_collection_set @collection_set_id OUTPUT, @name OUTPUT
    IF (@retVal <> 0)
        RETURN (1)

    -- Check if the collection set does not have any collection items
    IF NOT EXISTS(
        SELECT i.collection_item_id 
        FROM [dbo].[syscollector_collection_sets] AS s
        INNER JOIN [dbo].[syscollector_collection_items] AS i
            ON(s.collection_set_id = i.collection_set_id)
        WHERE s.collection_set_id = @collection_set_id
    )
    BEGIN
        RAISERROR(14685, 10, -1, @name) -- Raise a warning message
        IF (@TranCounter = 0)
            COMMIT TRANSACTION
        RETURN (0)
    END

    DECLARE @proxy_id int;
    DECLARE @collection_job_id uniqueidentifier
    DECLARE @upload_job_id uniqueidentifier
    DECLARE @schedule_uid uniqueidentifier;

    SELECT 
        @collection_job_id = collection_job_id, 
        @upload_job_id = upload_job_id, 
        @proxy_id = proxy_id,
        @schedule_uid = schedule_uid
    FROM [dbo].[syscollector_collection_sets_internal]
    WHERE collection_set_id = @collection_set_id;

    -- Check if the set does not have a proxy
    IF (@proxy_id IS NULL)
    BEGIN
        -- to start a collection set without a proxy, the caller has to be a sysadmin
        EXECUTE AS CALLER;
            IF (NOT (ISNULL(IS_SRVROLEMEMBER(N'sysadmin'), 0) = 1))
            BEGIN
                REVERT;
                RAISERROR(14692, -1, -1, @name)
                RETURN (1)
            END
        REVERT;
    END

    -- Starting a collection set requires a schedule
    IF @schedule_uid IS NULL
    BEGIN
        RAISERROR(14693, -1, -1)
        RETURN (1)
    END

    -- Check if we have jobs created, and if not, create them
    IF (@collection_job_id IS NULL AND @upload_job_id IS NULL)
    BEGIN
        -- Jobs not created yet, go and crete them
        -- We need to get some data from collection_sets table 
        -- before we do that.
        DECLARE @collection_set_uid uniqueidentifier;
        DECLARE @schedule_id int;
        DECLARE @collection_mode int;

        SELECT 
            @collection_set_uid = collection_set_uid,
            @collection_mode = collection_mode
        FROM
            [dbo].[syscollector_collection_sets_internal]
        WHERE
            collection_set_id = @collection_set_id;
        
        -- Sanity check
        -- Make sure the proxy and schedule are still there, someone could have
        -- remove them between when the collection set was created and now.
        IF (@proxy_id IS NOT NULL)
        BEGIN
            DECLARE @proxy_name sysname
            
            -- this will throw if the id does not exist
            EXEC @retVal = sp_verify_proxy_identifiers '@proxy_name', '@proxy_id', @proxy_name OUTPUT, @proxy_id OUTPUT
            IF (@retVal <> 0)
                RETURN (1)
        END

        SELECT @schedule_id = schedule_id FROM sysschedules_localserver_view WHERE @schedule_uid = schedule_uid
        EXEC @retVal = sp_verify_schedule_identifiers  @name_of_name_parameter = '@schedule_name',
                                                       @name_of_id_parameter   = '@schedule_id',
                                                       @schedule_name          = NULL,
                                                       @schedule_id            = @schedule_id,
                                                       @owner_sid              = NULL,
                                                       @orig_server_id         = NULL 
        IF (@retVal <> 0)
            RETURN (1)

        -- Go add the jobs
        EXEC [dbo].[sp_syscollector_create_jobs]
            @collection_set_id    = @collection_set_id,
            @collection_set_uid = @collection_set_uid,
            @collection_set_name = @name,
            @proxy_id            = @proxy_id,
            @schedule_id        = @schedule_id,
            @collection_mode    = @collection_mode,
            @collection_job_id    = @collection_job_id OUTPUT,
            @upload_job_id        = @upload_job_id OUTPUT

        -- Finally, update the collection_sets table
        UPDATE [dbo].[syscollector_collection_sets_internal]
        SET
            upload_job_id        = @upload_job_id,
            collection_job_id    = @collection_job_id
        WHERE @collection_set_id = collection_set_id
    END

    -- Update the is_running column for this collection set
    -- There is a trigger defined for that table that turns on
    -- the collection and upload jobs in response to that bit
    -- changing.
    UPDATE [dbo].[syscollector_collection_sets_internal]
    SET is_running = 1
    WHERE collection_set_id = @collection_set_id

    IF (@TranCounter = 0)
        COMMIT TRANSACTION
    RETURN (0)

    END TRY
    BEGIN CATCH
        IF (@TranCounter = 0 OR XACT_STATE() = -1)
            ROLLBACK TRANSACTION
        ELSE IF (XACT_STATE() = 1)
            ROLLBACK TRANSACTION tran_start_collection_set

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
```

