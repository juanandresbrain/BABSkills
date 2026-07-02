# dbo.sp_verify_subsystems

**Database:** msdb  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_verify_subsystems"]
    dbo_syssubsystems(["dbo.syssubsystems"]) --> SP
    dbo_xp_instance_regread(["dbo.xp_instance_regread"]) --> SP
    dbo_xp_msver(["dbo.xp_msver"]) --> SP
    dbo_xp_regread(["dbo.xp_regread"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.syssubsystems |
| dbo.xp_instance_regread |
| dbo.xp_msver |
| dbo.xp_regread |

## Stored Procedure Code

```sql
CREATE PROCEDURE dbo.sp_verify_subsystems
   @syssubsytems_refresh_needed BIT = 0
AS
BEGIN
  SET NOCOUNT ON
   
  DECLARE @retval         INT
  DECLARE @InstRootPath nvarchar(512)
  DECLARE @VersionRootPath nvarchar(512)
  DECLARE @ComRootPath nvarchar(512)
  DECLARE @DtsRootPath nvarchar(512)
  DECLARE @SQLPSPath nvarchar(512)
  DECLARE @DTExec nvarchar(512)
  DECLARE @DTExecExists INT
  DECLARE @ToolsPath nvarchar(512)


  IF ( (@syssubsytems_refresh_needed=1) OR (NOT EXISTS(select * from syssubsystems)) )
  BEGIN
     EXEC master.dbo.xp_instance_regread N'HKEY_LOCAL_MACHINE', N'SOFTWARE\Microsoft\MSSQLServer\Setup', N'SQLBinRoot', @InstRootPath OUTPUT
     IF @InstRootPath IS NULL
     BEGIN
       RAISERROR(14658, -1, -1) WITH LOG
       RETURN (1)
     END
     IF RIGHT(@InstRootPath, 1) <> N'\'
       SELECT @InstRootPath = @InstRootPath + N'\'

     EXEC master.dbo.xp_regread N'HKEY_LOCAL_MACHINE', N'SOFTWARE\Microsoft\Microsoft Sql Server\110', N'VerSpecificRootDir', @VersionRootPath OUTPUT
     IF @VersionRootPath IS NULL
     BEGIN
       RAISERROR(14659, -1, -1) WITH LOG
       RETURN(1)
     END

     EXEC master.dbo.xp_regread N'HKEY_LOCAL_MACHINE', N'SOFTWARE\Microsoft\Microsoft SQL Server\110\SSIS\Setup\DTSPath', N'', @DtsRootPath OUTPUT, N'no_output'
     IF (@DtsRootPath IS NOT NULL)
     BEGIN
       SELECT @DtsRootPath  = @DtsRootPath  + N'Binn\'
       SELECT @DTExec = @DtsRootPath + N'DTExec.exe'
       CREATE TABLE #t (file_exists int, is_directory int, parent_directory_exists int)
       INSERT #t EXEC xp_fileexist @DTExec
       SELECT TOP 1 @DTExecExists=file_exists from #t
       DROP TABLE #t
       IF ((@DTExecExists IS NULL) OR (@DTExecExists = 0))
         SET @DtsRootPath = NULL
     END

     SELECT @ComRootPath  = @VersionRootPath  + N'COM\'

     CREATE TABLE #Platform(ID int,  Name  sysname, Internal_Value int NULL, Value nvarchar(512))
     INSERT #Platform exec master.dbo.xp_msver 'Platform'

     IF EXISTS(SELECT * FROM #Platform WHERE Value LIKE '%64%')
	 BEGIN
		EXEC master.dbo.xp_regread N'HKEY_LOCAL_MACHINE', N'SOFTWARE\Wow6432Node\Microsoft\Microsoft Sql Server\110\Tools\ClientSetup', N'SQLPath', @ToolsPath OUTPUT
	 END
	 ELSE
	 BEGIN
		EXEC master.dbo.xp_regread N'HKEY_LOCAL_MACHINE', N'SOFTWARE\Microsoft\Microsoft Sql Server\110\Tools\ClientSetup', N'SQLPath', @ToolsPath OUTPUT
	 END

     DROP TABLE #Platform

     SELECT @SQLPSPath  = @ToolsPath  + N'\Binn\SQLPS.exe'
     
     -- Procedure must start its own transaction if we don't have one already.
     DECLARE @TranCounter INT;
     SET @TranCounter = @@TRANCOUNT;
     IF @TranCounter = 0
     BEGIN
        BEGIN TRANSACTION;
     END

	-- backup subsystem's max worker thread setting
	 DECLARE @subsystemsettings TABLE
	 (
	 	subsystem          NVARCHAR(40) COLLATE database_default NOT NULL,
	 	max_worker_threads INT           NULL
	 )

     INSERT INTO @subsystemsettings
     SELECT 
     subsystem, max_worker_threads 
     FROM  syssubsystems

     -- Fix for #525111 - when MSDB is restored from any other sqlserver, it is possible that physical path to agent_exe, subsystem_dll may not be valid on current server
     --  It is better to delete all records in this table and reinsert them again
     -- perform delete and re-insert operations within a transaction
     TRUNCATE TABLE syssubsystems

     -- Obtain processor count to determine maximum number of threads per subsystem
     DECLARE @xp_results TABLE
     (
     id              INT           NOT NULL,
     name            NVARCHAR(30)  COLLATE database_default NOT NULL,
     internal_value  INT           NULL,
     character_value NVARCHAR(212) COLLATE database_default NULL
     )
     INSERT INTO @xp_results
     EXECUTE master.dbo.xp_msver

     DECLARE @processor_count INT
     SELECT @processor_count = internal_value from @xp_results where id=16 -- ProcessorCount

     -- Modify database.
     BEGIN TRY

       --create subsystems
       --TSQL subsystem
       INSERT syssubsystems
       VALUES
       (
          1, N'TSQL',14556, FORMATMESSAGE(14557), FORMATMESSAGE(14557), FORMATMESSAGE(14557), FORMATMESSAGE(14557), FORMATMESSAGE(14557), 20 * @processor_count
       )
       --ActiveScripting subsystem
       INSERT syssubsystems
       VALUES
       (
          2, N'ActiveScripting',  14555, @InstRootPath + N'SQLATXSS.DLL',NULL,N'ActiveScriptStart',N'ActiveScriptEvent',N'ActiveScriptStop', 10 * @processor_count
       )

       --CmdExec subsystem
       INSERT syssubsystems
       VALUES
       (
          3, N'CmdExec', 14550, @InstRootPath + N'SQLCMDSS.DLL',NULL,N'CmdExecStart',N'CmdEvent',N'CmdExecStop', 10 * @processor_count
       )

       --Snapshot subsystem
       INSERT syssubsystems
       VALUES
       (
          4, N'Snapshot',   14551, @InstRootPath + N'SQLREPSS.DLL', @ComRootPath + N'SNAPSHOT.EXE', N'ReplStart',N'ReplEvent',N'ReplStop',100 * @processor_count
       )

       --LogReader subsystem
       INSERT syssubsystems
       VALUES
       (
          5, N'LogReader',  14552, @InstRootPath + N'SQLREPSS.DLL', @ComRootPath + N'logread.exe',N'ReplStart',N'ReplEvent',N'ReplStop',25 * @processor_count
       )

       --Distribution subsystem
       INSERT syssubsystems
       VALUES
       (
          6, N'Distribution',  14553, @InstRootPath + N'SQLREPSS.DLL', @ComRootPath + N'DISTRIB.EXE',N'ReplStart',N'ReplEvent',N'ReplStop',100 * @processor_count
       )

       --Merge subsystem
       INSERT syssubsystems
       VALUES
       (
          7, N'Merge',   14554, @InstRootPath + N'SQLREPSS.DLL',@ComRootPath + N'REPLMERG.EXE',N'ReplStart',N'ReplEvent',N'ReplStop',100 * @processor_count
       )

       --QueueReader subsystem
       INSERT syssubsystems
       VALUES
       (
          8, N'QueueReader',   14581, @InstRootPath + N'SQLREPSS.dll',@ComRootPath + N'qrdrsvc.exe',N'ReplStart',N'ReplEvent',N'ReplStop',100 * @processor_count
       )

       --ANALYSISQUERY subsystem
       INSERT syssubsystems
       VALUES
       (
          9, N'ANALYSISQUERY', 14513, @InstRootPath + N'SQLOLAPSS.DLL',NULL,N'OlapStart',N'OlapQueryEvent',N'OlapStop',100 * @processor_count
       )

       --ANALYSISCOMMAND subsystem
       INSERT syssubsystems
       VALUES
       (
          10, N'ANALYSISCOMMAND', 14514, @InstRootPath + N'SQLOLAPSS.DLL',NULL,N'OlapStart',N'OlapCommandEvent',N'OlapStop',100 * @processor_count
       )

       IF(@DtsRootPath IS NOT NULL)
       BEGIN
		--DTS subsystem
		INSERT syssubsystems
		VALUES
		(
			11, N'SSIS', 14538, @InstRootPath + N'SQLDTSSS.DLL',@DtsRootPath + N'DTExec.exe',N'DtsStart',N'DtsEvent',N'DtsStop',100 * @processor_count
		)
       END
       
       --PowerShell subsystem     
       INSERT syssubsystems
       VALUES
       (
              12, N'PowerShell', 14698, @InstRootPath + N'SQLPOWERSHELLSS.DLL', @SQLPSPath, N'PowerShellStart',N'PowerShellEvent',N'PowerShellStop',2
       )

        -- restore back subsystem's max_worker thread setting(s)
        UPDATE syssubsystems
        SET max_worker_threads = se.max_worker_threads
        FROM syssubsystems sub, @subsystemsettings se
        WHERE sub.subsystem = se.subsystem	

   END TRY
   BEGIN CATCH

       DECLARE @ErrorMessage NVARCHAR(400)
       DECLARE @ErrorSeverity INT
       DECLARE @ErrorState INT

       SELECT @ErrorMessage = ERROR_MESSAGE()
       SELECT @ErrorSeverity = ERROR_SEVERITY()
       SELECT @ErrorState = ERROR_STATE()

       -- Roll back the transaction that we started if we are not nested
       IF @TranCounter = 0
       BEGIN
         ROLLBACK TRANSACTION;
       END
       -- if we are nested inside another transaction just raise the 
       -- error and let the outer transaction do the rollback
       RAISERROR (@ErrorMessage, -- Message text.
                   @ErrorSeverity, -- Severity.
                   @ErrorState -- State.
                   )
       RETURN (1)                  
     END CATCH
  END --(NOT EXISTS(select * from syssubsystems))
  
  -- commit the transaction we started
  IF @TranCounter = 0
  BEGIN
    COMMIT TRANSACTION;
  END
  
  RETURN(0) -- Success
END
```

