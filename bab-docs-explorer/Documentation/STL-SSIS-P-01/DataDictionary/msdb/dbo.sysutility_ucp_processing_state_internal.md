# dbo.sysutility_ucp_processing_state_internal

**Database:** msdb  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| latest_processing_time | datetimeoffset | 10 | 1 |  |  |  |
| latest_health_state_id | int | 4 | 1 |  |  |  |
| next_health_state_id | int | 4 | 1 |  |  |  |
| id | int | 4 | 0 | YES |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_sysutility_ucp_calculate_health](../../StoredProcedures/msdb/dbo.sp_sysutility_ucp_calculate_health.md)
- [msdb: dbo.sp_sysutility_ucp_delete_policy_history](../../StoredProcedures/msdb/dbo.sp_sysutility_ucp_delete_policy_history.md)
- [msdb: dbo.sp_sysutility_ucp_remove](../../StoredProcedures/msdb/dbo.sp_sysutility_ucp_remove.md)
- [msdb: dbo.sp_sysutility_ucp_remove_mi](../../StoredProcedures/msdb/dbo.sp_sysutility_ucp_remove_mi.md)

