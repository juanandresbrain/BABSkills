# dbo.Sr_History

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| execution_id | int | 4 | 0 |  |  |  |
| job_id | int | 4 | 0 |  |  |  |
| server_id | int | 4 | 0 |  |  |  |
| thread_index | int | 4 | 0 |  |  |  |
| topic_id | int | 4 | 0 |  |  |  |
| db_group_id | int | 4 | 0 |  |  |  |
| object_id | int | 4 | 0 |  |  |  |
| include_in_average | bit | 1 | 0 |  |  |  |
| start_datetime | datetime | 8 | 0 |  |  |  |
| end_datetime | datetime | 8 | 1 |  |  |  |
| duration | int | 4 | 1 |  |  |  |
| sucessful | bit | 1 | 0 |  |  |  |
| exit_code | int | 4 | 1 |  |  |  |
| parent_job_id | int | 4 | 0 |  |  |  |
| machine_id | int | 4 | 0 |  |  |  |
| trace | smallint | 2 | 1 |  |  |  |
