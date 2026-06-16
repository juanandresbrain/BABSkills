# dbo.sysmail_account

**Database:** msdb  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| account_id | int | 4 | 0 | YES |  |  |
| name | sysname | 256 | 0 |  |  |  |
| description | nvarchar | 512 | 1 |  |  |  |
| email_address | nvarchar | 256 | 0 |  |  |  |
| display_name | nvarchar | 256 | 1 |  |  |  |
| replyto_address | nvarchar | 256 | 1 |  |  |  |
| last_mod_datetime | datetime | 8 | 0 |  |  |  |
| last_mod_user | sysname | 256 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sysmail_add_account_sp](../../StoredProcedures/msdb/dbo.sysmail_add_account_sp.md)
- [msdb: dbo.sysmail_delete_account_sp](../../StoredProcedures/msdb/dbo.sysmail_delete_account_sp.md)
- [msdb: dbo.sysmail_help_account_sp](../../StoredProcedures/msdb/dbo.sysmail_help_account_sp.md)
- [msdb: dbo.sysmail_help_admin_account_sp](../../StoredProcedures/msdb/dbo.sysmail_help_admin_account_sp.md)
- [msdb: dbo.sysmail_help_profileaccount_sp](../../StoredProcedures/msdb/dbo.sysmail_help_profileaccount_sp.md)
- [msdb: dbo.sysmail_update_account_sp](../../StoredProcedures/msdb/dbo.sysmail_update_account_sp.md)
- [msdb: dbo.sysmail_verify_account_sp](../../StoredProcedures/msdb/dbo.sysmail_verify_account_sp.md)

