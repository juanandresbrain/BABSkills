# dbo.sysproxies

**Database:** msdb  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| proxy_id | int | 4 | 0 |  |  |  |
| name | sysname | 256 | 0 |  |  |  |
| credential_id | int | 4 | 0 |  |  |  |
| enabled | tinyint | 1 | 0 |  |  |  |
| description | nvarchar | 1024 | 1 |  |  |  |
| user_sid | varbinary | 85 | 0 |  |  |  |
| credential_date_created | datetime | 8 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_add_proxy](../../StoredProcedures/msdb/dbo.sp_add_proxy.md)
- [msdb: dbo.sp_delete_proxy](../../StoredProcedures/msdb/dbo.sp_delete_proxy.md)
- [msdb: dbo.sp_enum_login_for_proxy](../../StoredProcedures/msdb/dbo.sp_enum_login_for_proxy.md)
- [msdb: dbo.sp_enum_proxy_for_subsystem](../../StoredProcedures/msdb/dbo.sp_enum_proxy_for_subsystem.md)
- [msdb: dbo.sp_help_proxy](../../StoredProcedures/msdb/dbo.sp_help_proxy.md)
- [msdb: dbo.sp_sysutility_mi_configure_proxy_account](../../StoredProcedures/msdb/dbo.sp_sysutility_mi_configure_proxy_account.md)
- [msdb: dbo.sp_sysutility_mi_validate_proxy_account](../../StoredProcedures/msdb/dbo.sp_sysutility_mi_validate_proxy_account.md)
- [msdb: dbo.sp_update_proxy](../../StoredProcedures/msdb/dbo.sp_update_proxy.md)
- [msdb: dbo.sp_verify_proxy](../../StoredProcedures/msdb/dbo.sp_verify_proxy.md)
- [msdb: dbo.sp_verify_proxy_identifiers](../../StoredProcedures/msdb/dbo.sp_verify_proxy_identifiers.md)

