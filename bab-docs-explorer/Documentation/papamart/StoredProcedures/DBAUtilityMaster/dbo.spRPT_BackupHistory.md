# dbo.spRPT_BackupHistory

**Database:** DBAUtilityMaster  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spRPT_BackupHistory"]
    dbo_tblDBA_BackupHistoryRepository(["dbo.tblDBA_BackupHistoryRepository"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tblDBA_BackupHistoryRepository |

## Stored Procedure Code

```sql
CREATE PROCEDURE spRPT_BackupHistory
AS
SELECT InstanceName, DatabaseName, BackupName, BackupStarted, BackupFinished, BackupType, BackupFileLocation, BackupFileSize, StatusID
FROM DBAUtilityMaster.dbo.tblDBA_BackupHistoryRepository
```

