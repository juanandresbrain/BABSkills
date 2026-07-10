# dbo.spRPT_BackupHistory_Errors

**Database:** DBAUtilityMaster  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spRPT_BackupHistory_Errors"]
    dbo_tblDBA_BackupHistoryRepository(["dbo.tblDBA_BackupHistoryRepository"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tblDBA_BackupHistoryRepository |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[spRPT_BackupHistory_Errors]
AS
SET NOCOUNT ON 
SELECT InstanceName, DatabaseName, BackupName, MIN(BackupStarted) BackupStarted, 
MAX(BackupFinished) BackupFinished, BackupType, COUNT(BackupFileLocation) NumberOfFiles, 
SUM(BackupFileSize) BackupFileSize, StatusID
FROM DBAUtilityMaster.dbo.tblDBA_BackupHistoryRepository
WHERE StatusID <> 1
GROUP BY InstanceName, DatabaseName, BackupName, BackupType, StatusID
```

