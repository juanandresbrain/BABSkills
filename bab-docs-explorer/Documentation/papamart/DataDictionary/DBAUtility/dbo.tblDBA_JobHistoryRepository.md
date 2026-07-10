# dbo.tblDBA_JobHistoryRepository

**Database:** DBAUtility  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| InstanceName | nvarchar | 256 | 1 |  |  |  |
| JobName | nvarchar | 256 | 1 |  |  |  |
| StepName | nvarchar | 256 | 1 |  |  |  |
| StepID | int | 4 | 1 |  |  |  |
| StepNameHistory | nvarchar | 256 | 1 |  |  |  |
| RunDate | int | 4 | 1 |  |  |  |
| RunTime | int | 4 | 1 |  |  |  |
| SQLServity | int | 4 | 1 |  |  |  |
| MessageText | varchar | 7000 | 1 |  |  |  |
| InsertDate | datetime | 8 | 0 |  |  |  |
