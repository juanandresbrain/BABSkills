# dbo.Ex_ServerMain

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| thread_index | int | 4 | 0 |  |  |  |
| sequence_number | int | 4 | 0 |  |  |  |
| job_id | int | 4 | 0 |  |  |  |
| topic_id | int | 4 | 0 |  |  |  |
| object_id | int | 4 | 0 |  |  |  |
| db_group_id | int | 4 | 0 |  |  |  |
| locked | int | 4 | 0 |  |  |  |
| scheduled_executions | int | 4 | 0 |  |  |  |
| done_executions | int | 4 | 0 |  |  |  |
| executing | bit | 1 | 0 |  |  |  |
| active | bit | 1 | 0 |  |  |  |
| in_sync | bit | 1 | 0 |  |  |  |
| auto_execute | bit | 1 | 0 |  |  |  |
| avg_duration | int | 4 | 1 |  |  |  |
| description | varchar | 255 | 1 |  |  |  |
| data | text | 16 | 1 |  |  |  |
| previous_status | tinyint | 1 | 1 |  |  |  |
