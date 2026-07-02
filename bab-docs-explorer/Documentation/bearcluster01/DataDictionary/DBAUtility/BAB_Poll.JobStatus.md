# BAB\Poll.JobStatus

**Database:** DBAUtility  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| job_id | uniqueidentifier | 16 | 1 |  |  |  |
| originating_server | nvarchar | 60 | 1 |  |  |  |
| name | sysname | 256 | 1 |  |  |  |
| enabled | tinyint | 1 | 1 |  |  |  |
| description | nvarchar | 1024 | 1 |  |  |  |
| start_step_id | int | 4 | 1 |  |  |  |
| category | sysname | 256 | 1 |  |  |  |
| owner | sysname | 256 | 1 |  |  |  |
| notify_level_eventlog | int | 4 | 1 |  |  |  |
| notify_level_email | int | 4 | 1 |  |  |  |
| notify_level_netsend | int | 4 | 1 |  |  |  |
| notify_level_page | int | 4 | 1 |  |  |  |
| notify_email_operator | sysname | 256 | 1 |  |  |  |
| notify_netsend_operator | sysname | 256 | 1 |  |  |  |
| notify_page_operator | sysname | 256 | 1 |  |  |  |
| delete_level | int | 4 | 1 |  |  |  |
| date_created | datetime | 8 | 1 |  |  |  |
| date_modified | datetime | 8 | 1 |  |  |  |
| version_number | int | 4 | 1 |  |  |  |
| last_run_date | int | 4 | 1 |  |  |  |
| last_run_time | int | 4 | 1 |  |  |  |
| last_run_outcome | int | 4 | 1 |  |  |  |
| next_run_date | int | 4 | 1 |  |  |  |
| next_run_time | int | 4 | 1 |  |  |  |
| next_run_schedule_id | int | 4 | 1 |  |  |  |
| current_execution_status | int | 4 | 1 |  |  |  |
| current_execution_step | sysname | 256 | 1 |  |  |  |
| current_retry_attempt | int | 4 | 1 |  |  |  |
| has_step | int | 4 | 1 |  |  |  |
| has_schedule | int | 4 | 1 |  |  |  |
| has_target | int | 4 | 1 |  |  |  |
| type | int | 4 | 1 |  |  |  |

