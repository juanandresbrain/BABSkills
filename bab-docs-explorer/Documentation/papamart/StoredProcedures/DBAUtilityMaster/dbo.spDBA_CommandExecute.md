# dbo.spDBA_CommandExecute

**Database:** DBAUtilityMaster  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spDBA_CommandExecute"]
    dbo_tblCommandLogRepository(["dbo.tblCommandLogRepository"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tblCommandLogRepository |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[spDBA_CommandExecute]
	@Command nvarchar(max),
	@CommandType nvarchar(max),
	@Mode int,
	@Comment nvarchar(max) = NULL,
	@DatabaseName nvarchar(max) = NULL,
	@SchemaName nvarchar(max) = NULL,
	@ObjectName nvarchar(max) = NULL,
	@ObjectType nvarchar(max) = NULL,
	@IndexName nvarchar(max) = NULL,
	@IndexType int = NULL,
	@StatisticsName nvarchar(max) = NULL,
	@PartitionNumber int = NULL,
	@ExtendedInfo varchar(max) = NULL,
	@LogToTable nvarchar(3) = 'Y',
	@Execute nvarchar(max)
AS

BEGIN
-- =============================================================================================================
-- Name: spCommandExecute
--
-- Description:	Executes and logs commands
--  Works on the Standard, Enterprise, Workgroup, Express, 
--  and Developer Editions of SQL Server 2008 and SQL Server 2005 SP2 running 
--  on X86, X64, or IA64 platforms. The solution is supported on the same OSs 
--  that SQL Server supports.
-- 
-- WARNING:::::: only comment the mode 2 code in SQL 2000 environments.
--			The mode 2 section is needed for SQL 2005
-- 
-- Output: error logging.
-- 
-- Available actions:
--

-- Dependencies: 
--	sp_DBACommandExecute
--	fnDBA_DatabaseSelect
--	CoreDB01_Maint.DBAMasterUtility.dbo.tblCommandLogRepository 
--	CoreDB01_Maint.DBAMasterUtility.dbo.tblDBA_BackupHistoryRepository
--
----------------------------------------------------------------------------------------------------
--// Original Source: http://ola.hallengren.com                                                          //--
----------------------------------------------------------------------------------------------------
--
-- Revision History
--		Name:			Date:			Comments:
--		Mike Pelikan	02/10/2012		Created based on SQL Server Maintance Scripts from  http://ola.hallengren.com 
--		Mike Pelikan	02/14/2012		Converted  @ExtendedInfo into varchar(max) as xml data type is not supported in distributed queries
--		Mike Pelikan	04/30/2012		Added Default to @LogToTable
--		Mike Pelikan	06/07/2012		Added Revision return logic
--	
DECLARE @Revision DATETIME
SET @Revision = '06/07/2012'
									
/*

*/
-- =============================================================================================================

  ----------------------------------------------------------------------------------------------------
  --// Source: http://ola.hallengren.com                                                          //--
  ----------------------------------------------------------------------------------------------------
  SET NOCOUNT ON

  SET LOCK_TIMEOUT 3600000

  DECLARE @StartMessage nvarchar(max)
  DECLARE @EndMessage nvarchar(max)
  DECLARE @ErrorMessage nvarchar(max)
  DECLARE @ErrorMessageOriginal nvarchar(max)

  DECLARE @StartTime datetime
  DECLARE @EndTime datetime

  DECLARE @StartTimeSec datetime
  DECLARE @EndTimeSec datetime

  DECLARE @ID int

  DECLARE @Error int
  DECLARE @ReturnCode int

  SET @Error = 0
  SET @ReturnCode = 0

----------------------------------------------------------------------------------------------------
--// Revision Return		                                                                    //--
----------------------------------------------------------------------------------------------------
IF @Command = 'ReturnVersion' GOTO ReturnCode
	

  ----------------------------------------------------------------------------------------------------
  --// Check core requirements                                                                    //--
  ----------------------------------------------------------------------------------------------------

  IF SERVERPROPERTY('EngineEdition') = 5
  BEGIN
    SET @ErrorMessage = 'SQL Azure is not supported.' + CHAR(13) + CHAR(10) + ' '
    RAISERROR(@ErrorMessage,16,1) WITH NOWAIT
    SET @Error = @@ERROR
  END

  IF @Error <> 0
  BEGIN
    SET @ReturnCode = @Error
    GOTO ReturnCode
  END

  IF @Error <> 0
  BEGIN
    SET @ReturnCode = @Error
    GOTO ReturnCode
  END

  ----------------------------------------------------------------------------------------------------
  --// Check input parameters                                                                     //--
  ----------------------------------------------------------------------------------------------------

  IF @Command IS NULL OR @Command = ''
  BEGIN
    SET @ErrorMessage = 'The value for parameter @Command is not supported.' + CHAR(13) + CHAR(10) + ' '
    RAISERROR(@ErrorMessage,16,1) WITH NOWAIT
    SET @Error = @@ERROR
  END

  IF @CommandType IS NULL OR @CommandType = '' OR LEN(@CommandType) > 60
  BEGIN
    SET @ErrorMessage = 'The value for parameter @CommandType is not supported.' + CHAR(13) + CHAR(10) + ' '
    RAISERROR(@ErrorMessage,16,1) WITH NOWAIT
    SET @Error = @@ERROR
  END

  IF @Mode NOT IN(1,2) OR @Mode IS NULL
  BEGIN
    SET @ErrorMessage = 'The value for parameter @Mode is not supported.' + CHAR(13) + CHAR(10) + ' '
    RAISERROR(@ErrorMessage,16,1) WITH NOWAIT
    SET @Error = @@ERROR
  END

  IF @LogToTable NOT IN('Y','N') OR @LogToTable IS NULL
  BEGIN
    SET @ErrorMessage = 'The value for parameter @LogToTable is not supported.' + CHAR(13) + CHAR(10) + ' '
    RAISERROR(@ErrorMessage,16,1) WITH NOWAIT
    SET @Error = @@ERROR
  END

  IF @Execute NOT IN('Y','N') OR @Execute IS NULL
  BEGIN
    SET @ErrorMessage = 'The value for parameter @Execute is not supported.' + CHAR(13) + CHAR(10) + ' '
    RAISERROR(@ErrorMessage,16,1) WITH NOWAIT
    SET @Error = @@ERROR
  END

  IF @Error <> 0
  BEGIN
    SET @ReturnCode = @Error
    GOTO ReturnCode
  END

  ----------------------------------------------------------------------------------------------------
  --// Log initial information                                                                    //--
  ----------------------------------------------------------------------------------------------------

  SET @StartTime = GETDATE()
  SET @StartTimeSec = CONVERT(datetime,CONVERT(nvarchar,@StartTime,120),120)

  SET @StartMessage = 'DateTime: ' + CONVERT(nvarchar,@StartTimeSec,120) + CHAR(13) + CHAR(10)
  SET @StartMessage = @StartMessage + 'Command: ' + @Command
  IF @Comment IS NOT NULL SET @StartMessage = @StartMessage + CHAR(13) + CHAR(10) + 'Comment: ' + @Comment
  SET @StartMessage = REPLACE(@StartMessage,'%','%%')
  RAISERROR(@StartMessage,10,1) WITH NOWAIT

  IF @LogToTable = 'Y'
  BEGIN
	IF @@SERVERNAME = 'COREDB01'
		INSERT INTO DBAUtilityMaster.dbo.tblCommandLogRepository(InstanceName, DatabaseName, SchemaName, ObjectName, ObjectType, IndexName, IndexType, StatisticsName, PartitionNumber, ExtendedInfo, CommandType, Command, StartTime)
		VALUES (@@ServerName, @DatabaseName, @SchemaName, @ObjectName, @ObjectType, @IndexName, @IndexType, @StatisticsName, @PartitionNumber, @ExtendedInfo, @CommandType, @Command, @StartTime)
	ELSE
		INSERT INTO COREDB01_MAINT.DBAUtilityMaster.dbo.tblCommandLogRepository(InstanceName, DatabaseName, SchemaName, ObjectName, ObjectType, IndexName, IndexType, StatisticsName, PartitionNumber, ExtendedInfo, CommandType, Command, StartTime)
		VALUES (@@ServerName, @DatabaseName, @SchemaName, @ObjectName, @ObjectType, @IndexName, @IndexType, @StatisticsName, @PartitionNumber, @ExtendedInfo, @CommandType, @Command, @StartTime)
  END

  SET @ID = SCOPE_IDENTITY()

  ----------------------------------------------------------------------------------------------------
  --// Execute command                                                                            //--
  ----------------------------------------------------------------------------------------------------

  IF @Mode = 1 AND @Execute = 'Y'
  BEGIN
    EXECUTE(@Command)
    SET @Error = @@ERROR
    SET @ReturnCode = @Error
  END
  IF @Mode = 2 AND @Execute = 'Y'
  BEGIN
    BEGIN TRY
      EXECUTE(@Command)
    END TRY
    BEGIN CATCH
      SET @Error = ERROR_NUMBER()
      SET @ReturnCode = @Error
      SET @ErrorMessageOriginal = ERROR_MESSAGE()
      SET @ErrorMessage = 'Msg ' + CAST(@Error AS nvarchar) + ', ' + ISNULL(@ErrorMessageOriginal,'')
      RAISERROR(@ErrorMessage,16,1) WITH NOWAIT
    END CATCH
  END

  ----------------------------------------------------------------------------------------------------
  --// Log completing information                                                                 //--
  ----------------------------------------------------------------------------------------------------

  SET @EndTime = GETDATE()
  SET @EndTimeSec = CONVERT(datetime,CONVERT(varchar,@EndTime,120),120)

  SET @EndMessage = 'Outcome: ' + CASE WHEN @Execute = 'N' THEN 'Not Executed' WHEN @Error = 0 THEN 'Succeeded' ELSE 'Failed' END + CHAR(13) + CHAR(10)
  SET @EndMessage = @EndMessage + 'Duration: ' + CASE WHEN DATEDIFF(ss,@StartTimeSec, @EndTimeSec)/(24*3600) > 0 THEN CAST(DATEDIFF(ss,@StartTimeSec, @EndTimeSec)/(24*3600) AS nvarchar) + '.' ELSE '' END + CONVERT(nvarchar,@EndTimeSec - @StartTimeSec,108) + CHAR(13) + CHAR(10)
  SET @EndMessage = @EndMessage + 'DateTime: ' + CONVERT(nvarchar,@EndTimeSec,120) + CHAR(13) + CHAR(10) + ' '
  SET @EndMessage = REPLACE(@EndMessage,'%','%%')
  RAISERROR(@EndMessage,10,1) WITH NOWAIT

  IF @LogToTable = 'Y'
  BEGIN
  	IF @@SERVERNAME = 'COREDB01'
		UPDATE DBAUtilityMaster.dbo.tblCommandLogRepository
		SET EndTime = @EndTime,
			ErrorNumber = CASE WHEN @Execute = 'N' THEN NULL ELSE @Error END,
			ErrorMessage = @ErrorMessageOriginal
		WHERE ID = @ID
	ELSE
		UPDATE COREDB01_MAINT.DBAUtilityMaster.dbo.tblCommandLogRepository
		SET EndTime = @EndTime,
			ErrorNumber = CASE WHEN @Execute = 'N' THEN NULL ELSE @Error END,
			ErrorMessage = @ErrorMessageOriginal
		WHERE ID = @ID

  END

ReturnCode:
IF @Command = 'ReturnVersion'
BEGIN
	SELECT @Revision 
END
ELSE
BEGIN
    RETURN ISNULL(@ReturnCode,0)
END

  ----------------------------------------------------------------------------------------------------

END
```

