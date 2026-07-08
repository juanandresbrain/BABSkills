# dbo.process_log

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_start_time | datetime | 8 | 0 |  |  |  |
| process_no | smallint | 2 | 0 |  |  |  |
| process_timestamp | float | 8 | 0 |  |  |  |
| process_end_time | datetime | 8 | 0 |  |  |  |
| transaction_count | int | 4 | 0 |  |  |  |
| process_status_flag | tinyint | 1 | 0 |  |  |  |
| file_name | nvarchar | 510 | 1 |  |  |  |
| file_size | int | 4 | 1 |  |  |  |
| batch_process_id | tinyint | 1 | 0 |  |  |  |
