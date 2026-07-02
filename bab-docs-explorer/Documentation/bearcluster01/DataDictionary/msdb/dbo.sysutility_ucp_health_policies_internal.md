# dbo.sysutility_ucp_health_policies_internal

**Database:** msdb  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| health_policy_id | int | 4 | 0 | YES |  |  |
| policy_name | sysname | 256 | 0 |  |  |  |
| rollup_object_urn | nvarchar | 8000 | 0 |  |  |  |
| rollup_object_type | int | 4 | 0 |  |  |  |
| target_type | int | 4 | 0 |  |  |  |
| resource_type | int | 4 | 0 |  |  |  |
| utilization_type | int | 4 | 0 |  |  |  |
| utilization_threshold | float | 8 | 0 |  |  |  |
| is_global_policy | bit | 1 | 1 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_sysutility_ucp_remove](../../StoredProcedures/msdb/dbo.sp_sysutility_ucp_remove.md)

