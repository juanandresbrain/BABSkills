# dbo.process_trace_log

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_start_time | datetime | 8 | 0 |  |  |  |
| process_no | smallint | 2 | 0 |  |  |  |
| process_end_time | datetime | 8 | 0 |  |  |  |
| subprocess1_start_time | datetime | 8 | 1 |  |  |  |
| subprocess2_start_time | datetime | 8 | 1 |  |  |  |
| subprocess3_start_time | datetime | 8 | 1 |  |  |  |
| transaction_count | int | 4 | 0 |  |  |  |
| process_status_flag | tinyint | 1 | 0 |  |  |  |
| batch_process_id | tinyint | 1 | 0 |  |  |  |
| process_comment | nvarchar | 200 | 1 |  |  |  |
| process_info | nvarchar | 6000 | 1 |  |  |  |
