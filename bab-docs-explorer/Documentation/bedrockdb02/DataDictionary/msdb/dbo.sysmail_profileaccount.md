# dbo.sysmail_profileaccount

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| profile_id | int | 4 | 0 | YES |  |  |
| account_id | int | 4 | 0 | YES | YES |  |
| sequence_number | int | 4 | 1 |  |  |  |
| last_mod_datetime | datetime | 8 | 0 |  |  |  |
| last_mod_user | sysname | 256 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_MailItemResultSets](../../StoredProcedures/msdb/dbo.sp_MailItemResultSets.md)
- [msdb: dbo.sysmail_add_profileaccount_sp](../../StoredProcedures/msdb/dbo.sysmail_add_profileaccount_sp.md)
- [msdb: dbo.sysmail_delete_profileaccount_sp](../../StoredProcedures/msdb/dbo.sysmail_delete_profileaccount_sp.md)
- [msdb: dbo.sysmail_help_profileaccount_sp](../../StoredProcedures/msdb/dbo.sysmail_help_profileaccount_sp.md)
- [msdb: dbo.sysmail_update_profileaccount_sp](../../StoredProcedures/msdb/dbo.sysmail_update_profileaccount_sp.md)

