# dbo.sysutility_mi_configuration_internal

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| configuration_id | int | 4 | 0 | YES |  |  |
| ucp_instance_name | sysname | 256 | 1 |  |  |  |
| mdw_database_name | sysname | 256 | 1 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_sysutility_mi_add_ucp_registration](../../StoredProcedures/msdb/dbo.sp_sysutility_mi_add_ucp_registration.md)
- [msdb: dbo.sp_sysutility_mi_remove_ucp_registration](../../StoredProcedures/msdb/dbo.sp_sysutility_mi_remove_ucp_registration.md)

