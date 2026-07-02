# dbo.sysutility_ucp_aggregated_mi_health_internal

**Database:** msdb  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| mi_count | int | 4 | 0 |  |  |  |
| mi_healthy_count | int | 4 | 0 |  |  |  |
| mi_unhealthy_count | int | 4 | 0 |  |  |  |
| mi_over_utilize_count | int | 4 | 0 |  |  |  |
| mi_under_utilize_count | int | 4 | 0 |  |  |  |
| mi_on_over_utilized_computer_count | int | 4 | 0 |  |  |  |
| mi_on_under_utilized_computer_count | int | 4 | 0 |  |  |  |
| mi_with_files_on_over_utilized_volume_count | int | 4 | 0 |  |  |  |
| mi_with_files_on_under_utilized_volume_count | int | 4 | 0 |  |  |  |
| mi_with_over_utilized_file_count | int | 4 | 0 |  |  |  |
| mi_with_under_utilized_file_count | int | 4 | 0 |  |  |  |
| mi_with_over_utilized_processor_count | int | 4 | 0 |  |  |  |
| mi_with_under_utilized_processor_count | int | 4 | 0 |  |  |  |
| set_number | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_sysutility_ucp_calculate_aggregated_mi_health](../../StoredProcedures/msdb/dbo.sp_sysutility_ucp_calculate_aggregated_mi_health.md)
- [msdb: dbo.sp_sysutility_ucp_calculate_health](../../StoredProcedures/msdb/dbo.sp_sysutility_ucp_calculate_health.md)
- [msdb: dbo.sp_sysutility_ucp_remove](../../StoredProcedures/msdb/dbo.sp_sysutility_ucp_remove.md)
- [msdb: dbo.sp_sysutility_ucp_remove_mi](../../StoredProcedures/msdb/dbo.sp_sysutility_ucp_remove_mi.md)

