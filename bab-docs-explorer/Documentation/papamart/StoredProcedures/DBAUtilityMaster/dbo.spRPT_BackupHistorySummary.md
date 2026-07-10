# dbo.spRPT_BackupHistorySummary

**Database:** DBAUtilityMaster  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spRPT_BackupHistorySummary"]
    dbo_tblDBA_BackupHistoryRepository(["dbo.tblDBA_BackupHistoryRepository"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tblDBA_BackupHistoryRepository |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[spRPT_BackupHistorySummary]
AS
SELECT InstanceName, DatabaseName, BackupName, MIN(BackupStarted) BackupStarted, 
MAX(BackupFinished) BackupFinished, BackupType, COUNT(BackupFileLocation) NumberOfFiles, 
SUM(BackupFileSize) BackupFileSize, MIN(StatusID) StatusID
FROM DBAUtilityMaster.dbo.tblDBA_BackupHistoryRepository
GROUP BY InstanceName, DatabaseName, BackupName, BackupType
```

