# dbo.tblDBA_ErrorLogHistoryRepository

**Database:** DBAUtilityMaster  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| InstanceName | varchar | 128 | 1 |  |  |  |
| LogType | varchar | 100 | 1 |  |  |  |
| LogDate | datetime | 8 | 1 |  |  |  |
| ProcessInfo | varchar | 50 | 1 |  |  |  |
| MessageText | nvarchar | -1 | 1 |  |  |  |
| InsertDate | datetime | 8 | 0 |  |  |  |
| ID | int | 4 | 0 | YES |  |  |
