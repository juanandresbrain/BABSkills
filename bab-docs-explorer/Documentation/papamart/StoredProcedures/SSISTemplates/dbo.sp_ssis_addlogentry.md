# dbo.sp_ssis_addlogentry

**Database:** SSISTemplates  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_ssis_addlogentry"]
    sysssislog(["sysssislog"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| sysssislog |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[sp_ssis_addlogentry]  @event sysname,  @computer nvarchar(128),  @operator nvarchar(128),  @source nvarchar(1024),  @sourceid uniqueidentifier,  @executionid uniqueidentifier,  @starttime datetime,  @endtime datetime,  @datacode int,  @databytes image,  @message nvarchar(2048)AS  INSERT INTO sysssislog (      event,      computer,      operator,      source,      sourceid,      executionid,      starttime,      endtime,      datacode,      databytes,      message )  VALUES (      @event,      @computer,      @operator,      @source,      @sourceid,      @executionid,      @starttime,      @endtime,      @datacode,      @databytes,      @message )  RETURN 0
audit,up_CheckPreviousExecution,-- =============================================
-- Author:		Burge, Shawn
-- Create date: 04/13/2012
-- Description:	Check the status of the last time the SSIS Package has executed.
-- =============================================
CREATE PROCEDURE [audit].[up_CheckPreviousExecution]
	@PackageGuid	uniqueidentifier
AS
BEGIN
	SET NOCOUNT ON;
	DECLARE @CurrentStatus INT;
	SET @CurrentStatus = (SELECT TOP 1 [Status] FROM audit.ExecutionLog
		WHERE PackageGuid = @PackageGuid
		ORDER BY LogID DESC)
	IF @CurrentStatus IS NULL
	BEGIN
		SET @CurrentStatus = 1;
	END;
	SELECT @CurrentStatus AS [Status];
END

audit,up_SetStatusToRepaired,-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [audit].[up_SetStatusToRepaired]
	@LogId int
AS
BEGIN
	UPDATE audit.ExecutionLog SET [Status] = 3 WHERE LogID = @LogId
END
```

