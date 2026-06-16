# dbo.sysmail_profile

**Database:** msdb  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| profile_id | int | 4 | 0 | YES |  |  |
| name | sysname | 256 | 0 |  |  |  |
| description | nvarchar | 512 | 1 |  |  |  |
| last_mod_datetime | datetime | 8 | 0 |  |  |  |
| last_mod_user | sysname | 256 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sysmail_add_profile_sp](../../StoredProcedures/msdb/dbo.sysmail_add_profile_sp.md)
- [msdb: dbo.sysmail_delete_profile_sp](../../StoredProcedures/msdb/dbo.sysmail_delete_profile_sp.md)
- [msdb: dbo.sysmail_help_principalprofile_sp](../../StoredProcedures/msdb/dbo.sysmail_help_principalprofile_sp.md)
- [msdb: dbo.sysmail_help_profile_sp](../../StoredProcedures/msdb/dbo.sysmail_help_profile_sp.md)
- [msdb: dbo.sysmail_help_profileaccount_sp](../../StoredProcedures/msdb/dbo.sysmail_help_profileaccount_sp.md)
- [msdb: dbo.sysmail_update_profile_sp](../../StoredProcedures/msdb/dbo.sysmail_update_profile_sp.md)
- [msdb: dbo.sysmail_verify_profile_sp](../../StoredProcedures/msdb/dbo.sysmail_verify_profile_sp.md)

