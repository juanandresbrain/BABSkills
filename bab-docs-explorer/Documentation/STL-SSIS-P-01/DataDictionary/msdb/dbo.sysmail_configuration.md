# dbo.sysmail_configuration

**Database:** msdb  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| paramname | nvarchar | 512 | 0 | YES |  |  |
| paramvalue | nvarchar | 512 | 1 |  |  |  |
| description | nvarchar | 512 | 1 |  |  |  |
| last_mod_datetime | datetime | 8 | 0 |  |  |  |
| last_mod_user | sysname | 256 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sysmail_configure_sp](../../StoredProcedures/msdb/dbo.sysmail_configure_sp.md)
- [msdb: dbo.sysmail_help_configure_sp](../../StoredProcedures/msdb/dbo.sysmail_help_configure_sp.md)
- [msdb: dbo.sysmail_help_configure_value_sp](../../StoredProcedures/msdb/dbo.sysmail_help_configure_value_sp.md)

