# dbo.process_status_log

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_no | smallint | 2 | 0 |  |  |  |
| process_start_time | datetime | 8 | 0 |  |  |  |
| expected_workload | int | 4 | 0 |  |  |  |
| completed_workload | int | 4 | 0 |  |  |  |
| completed_flag | tinyint | 1 | 0 |  |  |  |
| abort_requested | tinyint | 1 | 0 |  |  |  |
| transaction_qty | int | 4 | 1 |  |  |  |
