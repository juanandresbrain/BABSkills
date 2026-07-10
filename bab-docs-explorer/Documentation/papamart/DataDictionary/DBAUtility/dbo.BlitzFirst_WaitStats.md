# dbo.BlitzFirst_WaitStats

**Database:** DBAUtility  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ID | int | 4 | 0 | YES |  |  |
| ServerName | nvarchar | 256 | 1 |  |  |  |
| CheckDate | datetimeoffset | 10 | 1 |  |  |  |
| wait_type | nvarchar | 120 | 1 |  |  |  |
| wait_time_ms | bigint | 8 | 1 |  |  |  |
| signal_wait_time_ms | bigint | 8 | 1 |  |  |  |
| waiting_tasks_count | bigint | 8 | 1 |  |  |  |
