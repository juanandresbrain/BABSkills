# dbo.jobList

**Database:** TXTStaging  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ServerName | varchar | 23 | 0 |  |  |  |
| job_id | uniqueidentifier | 16 | 0 |  |  |  |
| originating_server_id | int | 4 | 0 |  |  |  |
| name | sysname | 256 | 0 |  |  |  |
| enabled | tinyint | 1 | 0 |  |  |  |
| description | nvarchar | 1024 | 1 |  |  |  |
| start_step_id | int | 4 | 0 |  |  |  |
| category_id | int | 4 | 0 |  |  |  |
| owner_sid | varbinary | 85 | 0 |  |  |  |
| notify_level_eventlog | int | 4 | 0 |  |  |  |
| notify_level_email | int | 4 | 0 |  |  |  |
| notify_level_netsend | int | 4 | 0 |  |  |  |
| notify_level_page | int | 4 | 0 |  |  |  |
| notify_email_operator_id | int | 4 | 0 |  |  |  |
| notify_netsend_operator_id | int | 4 | 0 |  |  |  |
| notify_page_operator_id | int | 4 | 0 |  |  |  |
| delete_level | int | 4 | 0 |  |  |  |
| date_created | datetime | 8 | 0 |  |  |  |
| date_modified | datetime | 8 | 0 |  |  |  |
| version_number | int | 4 | 0 |  |  |  |

