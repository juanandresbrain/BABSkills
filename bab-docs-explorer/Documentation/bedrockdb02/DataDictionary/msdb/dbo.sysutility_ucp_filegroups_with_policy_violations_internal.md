# dbo.sysutility_ucp_filegroups_with_policy_violations_internal

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| server_instance_name | sysname | 256 | 0 | YES |  |  |
| database_name | sysname | 256 | 0 | YES |  |  |
| filegroup_name | sysname | 256 | 0 | YES |  |  |
| policy_id | int | 4 | 0 | YES |  |  |
| set_number | int | 4 | 0 | YES |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_sysutility_ucp_calculate_dac_file_space_health](../../StoredProcedures/msdb/dbo.sp_sysutility_ucp_calculate_dac_file_space_health.md)
- [msdb: dbo.sp_sysutility_ucp_calculate_filegroups_with_policy_violations](../../StoredProcedures/msdb/dbo.sp_sysutility_ucp_calculate_filegroups_with_policy_violations.md)
- [msdb: dbo.sp_sysutility_ucp_calculate_health](../../StoredProcedures/msdb/dbo.sp_sysutility_ucp_calculate_health.md)
- [msdb: dbo.sp_sysutility_ucp_calculate_mi_file_space_health](../../StoredProcedures/msdb/dbo.sp_sysutility_ucp_calculate_mi_file_space_health.md)
- [msdb: dbo.sp_sysutility_ucp_remove](../../StoredProcedures/msdb/dbo.sp_sysutility_ucp_remove.md)

