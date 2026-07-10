# dbo.tblDBA_BackupHistory

**Database:** DBAUtility_new  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| BackupHistoryID | int | 4 | 0 | YES |  |  |
| InstanceName | varchar | 200 | 0 |  |  |  |
| DatabaseName | varchar | 200 | 0 |  |  |  |
| BackupName | varchar | 200 | 1 |  |  |  |
| BackupStarted | datetime | 8 | 0 |  |  |  |
| BackupFinished | datetime | 8 | 1 |  |  |  |
| BackupType | varchar | 4 | 0 |  |  |  |
| BackupFileLocation | varchar | 1000 | 1 |  |  |  |
| BackupFileSize | int | 4 | 1 |  |  |  |
| StatusID | int | 4 | 0 |  |  |  |
