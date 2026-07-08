# dbo.notification_history

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| log_id | int | 4 | 0 | YES |  |  |
| stored_proc_name | varchar | 100 | 1 |  |  |  |
| record_logged_datetime | datetime | 8 | 1 |  |  |  |
| issues_found | varchar | 5 | 1 |  |  |  |
| action_required | varchar | 5 | 1 |  |  |  |
| notification_sent | varchar | 5 | 1 |  |  |  |
| email_type | varchar | 20 | 1 |  |  |  |
| email_to | varchar | 300 | 1 |  |  |  |
| email_cc | varchar | 300 | 1 |  |  |  |
| email_subject | varchar | 150 | 1 |  |  |  |
| comment | varchar | 8000 | 1 |  |  |  |
