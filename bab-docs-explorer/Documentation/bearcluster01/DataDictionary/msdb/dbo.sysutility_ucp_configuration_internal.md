# dbo.sysutility_ucp_configuration_internal

**Database:** msdb  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| name | sysname | 256 | 0 | YES |  |  |
| current_value | sql_variant | 8016 | 1 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_sysutility_ucp_delete_policy_history](../../StoredProcedures/msdb/dbo.sp_sysutility_ucp_delete_policy_history.md)
- [msdb: dbo.sp_sysutility_ucp_initialize](../../StoredProcedures/msdb/dbo.sp_sysutility_ucp_initialize.md)
- [msdb: dbo.sp_sysutility_ucp_remove](../../StoredProcedures/msdb/dbo.sp_sysutility_ucp_remove.md)

