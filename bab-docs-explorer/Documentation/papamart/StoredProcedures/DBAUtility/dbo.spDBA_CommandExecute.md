# dbo.spDBA_CommandExecute

**Database:** DBAUtility  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spDBA_CommandExecute"]
    dbo_tblDBA_CommandLog(["dbo.tblDBA_CommandLog"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tblDBA_CommandLog |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[spDBA_CommandExecute]
	@Command varchar(2000),
	@CommandType varchar(2000),
	@Mode int,
	@Comment varchar(2000) = NULL,
	@DatabaseName varchar(2000) = NULL,
	@SchemaName varchar(2000) = NULL,
	@ObjectName varchar(2000) = NULL,
	@ObjectType varchar(2000) = NULL,
	@IndexName varchar(2000) = NULL,
	@IndexType int = NULL,
	@StatisticsName varchar(2000) = NULL,
	@PartitionNumber int = NULL,
	@ExtendedInfo varchar(2000) = NULL,
	@LogToTable varchar(3) = 'Y',
	@Execute varchar(2000)
AS

BEGIN
-- =============================================================================================================
-- Name: spCommandExecute
--
-- Description:	Executes and logs commands
--  Works on the Standard, Enterprise, Workgroup, Express, 
--  and Developer Editions of SQL Server 2000 or greater. 
--  The solution is supported on the same OSs that SQL Server supports.
-- 
-- WARNING:::::: only comment the mode 2 code in SQL 2000 environments.
--			The mode 2 section can only beused for SQL 2005 or greater
-- 
-- Output: error logging.
-- 
-- Available actions:
--

-- Dependencies: 
--	sp_DBACommandExecute
--	fnDBA_DatabaseSelect
--	DBAUtility.dbo.tblDBA_CommandLog
--	DBAUtility.dbo.tblDBA_BackupHistory
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
--		Mike Pelikan	06/13/2012		Changed Repository to local log file
--		Mike Pelikan	06/20/2012		Changed revision date to match SQL 2000 version of the procedure -- this was done on 8/27/2012
--		Mike Pelikan	01/06/2014		Converted nvarchar(max) to varchar(2000) so that one procedure can be used
--											on all servers. Also commented out Try Catch block.
--		Mike Pelikan	03/24/2014		Commented out the Mode logic
--	
DECLARE @Revision DATETIME
SET @Revision = '03/24/2014'
									
/*

*/
-- =============================================================================================================

  ----------------------------------------------------------------------------------------------------
  --// Source: http://ola.hallengren.com                                                          //--
  ----------------------------------------------------------------------------------------------------
  SET NOCOUNT ON

  SET LOCK_TIMEOUT 3600000

  DECLARE @StartMessage varchar(2000)
  DECLARE @EndMessage varchar(2000)
  DECLARE @ErrorMessage varchar(2000)
  DECLARE @ErrorMessageOriginal varchar(2000)

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
		INSERT INTO DBAUtility.dbo.tblDBA_CommandLog(InstanceName, DatabaseName, SchemaName, ObjectName, ObjectType, IndexName, IndexType, StatisticsName, PartitionNumber, ExtendedInfo, CommandType, Command, StartTime)
		VALUES (@@ServerName, @DatabaseName, @SchemaName, @ObjectName, @ObjectType, @IndexName, @IndexType, @StatisticsName, @PartitionNumber, @ExtendedInfo, @CommandType, @Command, @StartTime)
  END

  SET @ID = SCOPE_IDENTITY()

  ----------------------------------------------------------------------------------------------------
  --// Execute command                                                                            //--
  ----------------------------------------------------------------------------------------------------

  --IF @Mode = 1 AND @Execute = 'Y'
  IF @Execute = 'Y'
  BEGIN
    EXECUTE(@Command)
    SET @Error = @@ERROR
    SET @ReturnCode = @Error
  END
  --IF @Mode = 2 AND @Execute = 'Y'
  --BEGIN
  --  BEGIN TRY
  --    EXECUTE(@Command)
  --  END TRY
  --  BEGIN CATCH
  --    SET @Error = ERROR_NUMBER()
  --    SET @ReturnCode = @Error
  --    SET @ErrorMessageOriginal = ERROR_MESSAGE()
  --    SET @ErrorMessage = 'Msg ' + CAST(@Error AS nvarchar) + ', ' + ISNULL(@ErrorMessageOriginal,'')
  --    RAISERROR(@ErrorMessage,16,1) WITH NOWAIT
  --  END CATCH
  --END

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
	UPDATE DBAUtility.dbo.tblDBA_CommandLog
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

