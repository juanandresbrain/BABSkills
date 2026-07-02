# dbo.sysproxylogin

**Database:** msdb  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| proxy_id | int | 4 | 0 |  |  |  |
| sid | varbinary | 85 | 1 |  |  |  |
| flags | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_delete_proxy](../../StoredProcedures/msdb/dbo.sp_delete_proxy.md)
- [msdb: dbo.sp_enum_login_for_proxy](../../StoredProcedures/msdb/dbo.sp_enum_login_for_proxy.md)
- [msdb: dbo.sp_revoke_login_from_proxy](../../StoredProcedures/msdb/dbo.sp_revoke_login_from_proxy.md)

