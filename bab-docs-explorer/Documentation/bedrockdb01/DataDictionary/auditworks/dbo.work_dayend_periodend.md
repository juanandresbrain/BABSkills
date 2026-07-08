# dbo.work_dayend_periodend

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_id | binary | 16 | 0 |  |  |  |
| instance_id | smallint | 2 | 0 |  |  |  |
| process_no | smallint | 2 | 0 |  |  |  |
| process_start_time | datetime | 8 | 0 |  |  |  |
| process_step_no | int | 4 | 0 |  |  |  |
| process_step_start_time | datetime | 8 | 0 |  |  |  |
| transaction_qty | int | 4 | 0 |  |  |  |
| process_completed_workload | int | 4 | 0 |  |  |  |
| process_expected_workload | int | 4 | 0 |  |  |  |
| step_completed_workload | int | 4 | 0 |  |  |  |
| step_expected_workload | int | 4 | 0 |  |  |  |
| stream_no | int | 4 | 0 |  |  |  |
| abortable_process | tinyint | 1 | 0 |  |  |  |
| aborted_requested | tinyint | 1 | 0 |  |  |  |
| immediate_dayend_requested | tinyint | 1 | 0 |  |  |  |
| completed_flag | tinyint | 1 | 0 |  |  |  |
| dayend_status | smallint | 2 | 0 |  |  |  |
| work_tb_entry_date_time | datetime | 8 | 1 |  |  |  |
