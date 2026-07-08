# dbo.process_step_log

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_no | smallint | 2 | 0 |  |  |  |
| stream_no | numeric | 9 | 0 |  |  |  |
| process_step_no | int | 4 | 0 |  |  |  |
| process_step_start_time | datetime | 8 | 0 |  |  |  |
| expected_workload | int | 4 | 0 |  |  |  |
| completed_workload | int | 4 | 0 |  |  |  |
