# dbo.sysproxysubsystem

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| subsystem_id | int | 4 | 0 |  |  |  |
| proxy_id | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_delete_proxy](../../StoredProcedures/msdb/dbo.sp_delete_proxy.md)
- [msdb: dbo.sp_enum_proxy_for_subsystem](../../StoredProcedures/msdb/dbo.sp_enum_proxy_for_subsystem.md)
- [msdb: dbo.sp_grant_proxy_to_subsystem](../../StoredProcedures/msdb/dbo.sp_grant_proxy_to_subsystem.md)
- [msdb: dbo.sp_reassign_proxy](../../StoredProcedures/msdb/dbo.sp_reassign_proxy.md)
- [msdb: dbo.sp_revoke_proxy_from_subsystem](../../StoredProcedures/msdb/dbo.sp_revoke_proxy_from_subsystem.md)
- [msdb: dbo.sp_verify_proxy_permissions](../../StoredProcedures/msdb/dbo.sp_verify_proxy_permissions.md)

