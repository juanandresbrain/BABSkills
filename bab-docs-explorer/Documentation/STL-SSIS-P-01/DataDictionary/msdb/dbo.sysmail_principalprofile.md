# dbo.sysmail_principalprofile

**Database:** msdb  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| profile_id | int | 4 | 0 | YES | YES |  |
| principal_sid | varbinary | 85 | 0 | YES |  |  |
| is_default | bit | 1 | 0 |  |  |  |
| last_mod_datetime | datetime | 8 | 0 |  |  |  |
| last_mod_user | sysname | 256 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sysmail_add_principalprofile_sp](../../StoredProcedures/msdb/dbo.sysmail_add_principalprofile_sp.md)
- [msdb: dbo.sysmail_delete_principalprofile_sp](../../StoredProcedures/msdb/dbo.sysmail_delete_principalprofile_sp.md)
- [msdb: dbo.sysmail_help_principalprofile_sp](../../StoredProcedures/msdb/dbo.sysmail_help_principalprofile_sp.md)
- [msdb: dbo.sysmail_update_principalprofile_sp](../../StoredProcedures/msdb/dbo.sysmail_update_principalprofile_sp.md)

