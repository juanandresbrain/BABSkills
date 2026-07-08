# dbo.Sr_Job

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| job_id | int | 4 | 0 |  |  |  |
| server_id | int | 4 | 0 |  |  |  |
| sequence_number | int | 4 | 0 |  |  |  |
| topic_id | int | 4 | 0 |  |  |  |
| object_id | int | 4 | 0 |  |  |  |
| object_type | smallint | 2 | 0 |  |  |  |
| db_group_id | int | 4 | 0 |  |  |  |
| interval_count | int | 4 | 1 |  |  |  |
| interval_type | smallint | 2 | 1 |  |  |  |
| start_date_time | datetime | 8 | 1 |  |  |  |
| end_date_time | datetime | 8 | 1 |  |  |  |
| schedule_details | varchar | 255 | 1 |  |  |  |
| last_date_time | datetime | 8 | 1 |  |  |  |
| next_date_time | datetime | 8 | 1 |  |  |  |
| locked | int | 4 | 0 |  |  |  |
| scheduled_executions | int | 4 | 0 |  |  |  |
| done_executions | int | 4 | 0 |  |  |  |
| auto_execute | bit | 1 | 0 |  |  |  |
| execution_id | int | 4 | 0 |  |  |  |
| active | bit | 1 | 0 |  |  |  |
| avg_duration | int | 4 | 1 |  |  |  |
| label | nvarchar | 160 | 1 |  |  |  |
| cmd_line | varchar | 255 | 1 |  |  |  |
| cmd_line_parameters | varchar | 255 | 1 |  |  |  |
| data | text | 16 | 1 |  |  |  |
| previous_status | tinyint | 1 | 1 |  |  |  |
| next_job_id | int | 4 | 0 |  |  |  |
| debug_level | smallint | 2 | 0 |  |  |  |
| created_date_time | datetime | 8 | 1 |  |  |  |
| scheduling_mode | int | 4 | 1 |  |  |  |
| max_threads | int | 4 | 0 |  |  |  |
| job_flags | int | 4 | 1 |  |  |  |
| machine_id | int | 4 | 0 |  |  |  |
| pid | int | 4 | 0 |  |  |  |
| data_ext | varchar | 255 | 1 |  |  |  |
| compatibility_version | int | 4 | 1 |  |  |  |
| wizard_id | int | 4 | 1 |  |  |  |
| kill_job | int | 4 | 1 |  |  |  |
| exit_code | varchar | 255 | 1 |  |  |  |
| need_rerun | bit | 1 | 0 |  |  |  |
| auto_recovery | bit | 1 | 0 |  |  |  |
| complete_percentage | smallint | 2 | 1 |  |  |  |
| stop_job | bit | 1 | 1 |  |  |  |
| created_by | int | 4 | 1 |  |  |  |
| last_modified_by | int | 4 | 1 |  |  |  |
| last_modified_date_time | datetime | 8 | 1 |  |  |  |
