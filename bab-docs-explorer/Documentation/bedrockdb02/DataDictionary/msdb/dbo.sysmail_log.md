# dbo.sysmail_log

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| log_id | int | 4 | 0 | YES |  |  |
| event_type | int | 4 | 0 |  |  |  |
| log_date | datetime | 8 | 0 |  |  |  |
| description | nvarchar | -1 | 1 |  |  |  |
| process_id | int | 4 | 1 |  |  |  |
| mailitem_id | int | 4 | 1 |  |  |  |
| account_id | int | 4 | 1 |  |  |  |
| last_mod_date | datetime | 8 | 0 |  |  |  |
| last_mod_user | sysname | 256 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sysmail_delete_log_sp](../../StoredProcedures/msdb/dbo.sysmail_delete_log_sp.md)
- [msdb: dbo.sysmail_logmailevent_sp](../../StoredProcedures/msdb/dbo.sysmail_logmailevent_sp.md)

