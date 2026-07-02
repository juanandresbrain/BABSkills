# dbo.spDBA_Transfer_BackupHistoryRepository

**Database:** DBAUtility  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spDBA_Transfer_BackupHistoryRepository"]
    dbo_tblDBA_BackupHistory(["dbo.tblDBA_BackupHistory"]) --> SP
    dbo_tblDBA_BackupHistoryRepository(["dbo.tblDBA_BackupHistoryRepository"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tblDBA_BackupHistory |
| dbo.tblDBA_BackupHistoryRepository |

## Stored Procedure Code

```sql
CREATE PROC [dbo].[spDBA_Transfer_BackupHistoryRepository]

@Action VARCHAR(100) = 'Process'
AS

-- =============================================================================================================
-- Name: spDBA_Transfer_ProcVersionRepository
--
-- Description:	Inserts backup history into central repository table.
-- Output: None

-- Available actions: None
--	
-- Dependencies: 
--	DBAUtility.dbo.tblDBA_BackupHistory
--	COREDB01_MAINT.DBAUtilityMaster.dbo.tblDBA_BackupHistoryRepository
--
-- Revision History
--		Name:			Date:			Comments:
--		Mike Pelikan	09/18/2012		Initial Release

DECLARE @Revision DATETIME
SET @Revision = '09/18/2012'
-----------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------------------
--// Set options                                                                                //--
----------------------------------------------------------------------------------------------------
SET NOCOUNT ON

----------------------------------------------------------------------------------------------------
--// Declare variables                                                                          //--
----------------------------------------------------------------------------------------------------
DECLARE @EndMessage varchar(2000)
DECLARE @ReturnCode int

----------------------------------------------------------------------------------------------------
--// Revision                                                                                  //--
----------------------------------------------------------------------------------------------------
IF @Action = 'ReturnVersion'
BEGIN
	SELECT @Revision
END
ELSE
BEGIN

	--Update existing
	--UPDATE COREDB01_MAINT.DBAUtilityMaster.dbo.tblDBA_ObjectVersionRepository
	--SET VersionDate = pvl.VersionDate, usesRevision = pvl.usesRevision 
	--FROM  COREDB01_MAINT.DBAUtilityMaster.dbo.tblDBA_ObjectVersionRepository pvr 
	--INNER JOIN DBAUtility.dbo.tblDBA_ObjectVersionLog pvl ON pvr.InstanceName = pvl.InstanceName COLLATE SQL_Latin1_General_CP1_CI_AS 
	--AND pvr.ObjectName = pvl.ObjectName COLLATE SQL_Latin1_General_CP1_CI_AS
	--AND pvr.ObjectType = pvl.ObjectType COLLATE SQL_Latin1_General_CP1_CI_AS
	--WHERE pvr.VersionDate <> pvl.VersionDate OR pvr.usesRevision <> pvl.usesRevision 
	--Insert New

	INSERT INTO COREDB01_MAINT.DBAUtilityMaster.dbo.tblDBA_BackupHistoryRepository (InstanceName, DatabaseName, BackupName, BackupStarted, BackupFinished, BackupType, BackupFileLocation, BackupFileSize, StatusID)
	SELECT pvl.InstanceName, pvl.DatabaseName, pvl.BackupName, pvl.BackupStarted, pvl.BackupFinished, pvl.BackupType, pvl.BackupFileLocation, pvl.BackupFileSize, pvl.StatusID
	FROM DBAUtility.dbo.tblDBA_BackupHistory pvl 
	LEFT JOIN COREDB01_MAINT.DBAUtilityMaster.dbo.tblDBA_BackupHistoryRepository pvr ON pvl.InstanceName = pvr.InstanceName COLLATE SQL_Latin1_General_CP1_CI_AS 
	AND pvl.DatabaseName = pvr.DatabaseName COLLATE SQL_Latin1_General_CP1_CI_AS
	AND pvr.BackupStarted = pvl.BackupStarted 
	WHERE pvr.BackupHistoryID IS NULL AND pvl.BackupStarted < DATEADD(dd, - 1, GETDATE()) 

	--Delete old
	DELETE FROM DBAUtility.dbo.tblDBA_BackupHistory
	WHERE BackupStarted < DATEADD(dd, - 1, GETDATE())
	
END

EndHere:
IF @Action = 'ReturnVersion'
BEGIN
	SELECT @Revision 
END
ELSE
BEGIN
	SET @EndMessage = 'DateTime: ' + CONVERT(nvarchar,GETDATE(),120)
	SET @EndMessage = REPLACE(@EndMessage,'%','%%')
	RAISERROR(@EndMessage,10,1) WITH NOWAIT

	IF @ReturnCode <> 0
	BEGIN
		RETURN @ReturnCode
	--SELECT @ReturnCode
	END
END
```

