# dbo.sa_partition_log

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| entry_date | datetime | 8 | 0 |  |  |  |
| table_name | nvarchar | 100 | 0 |  |  |  |
| log_message | nvarchar | 240 | 0 |  |  |  |
| partition_name | nvarchar | 60 | 1 |  |  |  |
