# dbo.sysmail_server

**Database:** msdb  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| account_id | int | 4 | 0 | YES | YES |  |
| servertype | sysname | 256 | 0 | YES | YES |  |
| servername | sysname | 256 | 0 |  |  |  |
| port | int | 4 | 0 |  |  |  |
| username | nvarchar | 256 | 1 |  |  |  |
| credential_id | int | 4 | 1 |  |  |  |
| use_default_credentials | bit | 1 | 0 |  |  |  |
| enable_ssl | bit | 1 | 0 |  |  |  |
| flags | int | 4 | 0 |  |  |  |
| timeout | int | 4 | 1 |  |  |  |
| last_mod_datetime | datetime | 8 | 0 |  |  |  |
| last_mod_user | sysname | 256 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sysmail_add_account_sp](../../StoredProcedures/msdb/dbo.sysmail_add_account_sp.md)
- [msdb: dbo.sysmail_delete_account_sp](../../StoredProcedures/msdb/dbo.sysmail_delete_account_sp.md)
- [msdb: dbo.sysmail_help_account_sp](../../StoredProcedures/msdb/dbo.sysmail_help_account_sp.md)
- [msdb: dbo.sysmail_help_admin_account_sp](../../StoredProcedures/msdb/dbo.sysmail_help_admin_account_sp.md)
- [msdb: dbo.sysmail_update_account_sp](../../StoredProcedures/msdb/dbo.sysmail_update_account_sp.md)

