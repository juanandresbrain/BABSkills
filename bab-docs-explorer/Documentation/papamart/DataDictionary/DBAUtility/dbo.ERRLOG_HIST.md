# dbo.ERRLOG_HIST

**Database:** DBAUtility  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SERVER_NM | nvarchar | 256 | 1 |  |  |  |
| LOG_TYPE | nvarchar | 200 | 1 |  |  |  |
| LOG_DT | datetime | 8 | 1 |  |  |  |
| PROCESS_INFO | nvarchar | 100 | 1 |  |  |  |
| MESSAGE_TXT | nvarchar | -1 | 1 |  |  |  |
| INSERT_DT | datetime | 8 | 0 |  |  |  |
