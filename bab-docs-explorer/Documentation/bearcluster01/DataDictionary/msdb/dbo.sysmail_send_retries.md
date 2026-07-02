# dbo.sysmail_send_retries

**Database:** msdb  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| conversation_handle | uniqueidentifier | 16 | 0 | YES |  |  |
| mailitem_id | int | 4 | 0 |  | YES |  |
| send_attempts | int | 4 | 0 |  |  |  |
| last_send_attempt_date | datetime | 8 | 0 |  |  |  |

