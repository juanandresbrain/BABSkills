# dbo.sa_partition_log

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| entry_date | datetime | 8 | 0 |  |  |  |
| table_name | nvarchar | 60 | 0 |  |  |  |
| log_message | nvarchar | 2000 | 1 |  |  |  |
| partition_name | nvarchar | 100 | 1 |  |  |  |
