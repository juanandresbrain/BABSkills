# dbo.tblDBA_DriveHistoryRepository

**Database:** DBAUtilityMaster  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| InstanceName | nvarchar | 256 | 1 |  |  |  |
| Drive | char | 1 | 1 |  |  |  |
| FreeSpace | int | 4 | 1 |  |  |  |
| TotalSize | int | 4 | 1 |  |  |  |
| PercentFree | int | 4 | 1 |  |  |  |
| ExecutionTime | datetime | 8 | 1 |  |  |  |
| EmailSent | bit | 1 | 1 |  |  |  |
