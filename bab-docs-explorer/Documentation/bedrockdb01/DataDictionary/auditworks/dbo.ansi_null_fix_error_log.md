# dbo.ansi_null_fix_error_log

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| log_id | int | 4 | 0 | YES |  |  |
| schema_name | nvarchar | 256 | 1 |  |  |  |
| object_name | nvarchar | 256 | 1 |  |  |  |
| error_severity | int | 4 | 1 |  |  |  |
| error_state | int | 4 | 1 |  |  |  |
| error_number | int | 4 | 1 |  |  |  |
| error_message | nvarchar | 8000 | 1 |  |  |  |
| drop_statement | nvarchar | 1000 | 1 |  |  |  |
| definition | nvarchar | -1 | 1 |  |  |  |
| log_date | datetime | 8 | 1 |  |  |  |
