# dbo.sysutility_ucp_dac_health_internal

**Database:** msdb  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| dac_name | sysname | 256 | 0 | YES |  |  |
| dac_server_instance_name | sysname | 256 | 0 | YES |  |  |
| is_volume_space_over_utilized | int | 4 | 0 |  |  |  |
| is_volume_space_under_utilized | int | 4 | 0 |  |  |  |
| is_computer_processor_over_utilized | int | 4 | 0 |  |  |  |
| is_computer_processor_under_utilized | int | 4 | 0 |  |  |  |
| is_file_space_over_utilized | int | 4 | 0 |  |  |  |
| is_file_space_under_utilized | int | 4 | 0 |  |  |  |
| is_dac_processor_over_utilized | int | 4 | 0 |  |  |  |
| is_dac_processor_under_utilized | int | 4 | 0 |  |  |  |
| is_policy_overridden | bit | 1 | 0 |  |  |  |
| set_number | int | 4 | 0 | YES |  |  |
| processing_time | datetimeoffset | 10 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_sysutility_ucp_calculate_aggregated_dac_health](../../StoredProcedures/msdb/dbo.sp_sysutility_ucp_calculate_aggregated_dac_health.md)
- [msdb: dbo.sp_sysutility_ucp_calculate_dac_health](../../StoredProcedures/msdb/dbo.sp_sysutility_ucp_calculate_dac_health.md)
- [msdb: dbo.sp_sysutility_ucp_calculate_health](../../StoredProcedures/msdb/dbo.sp_sysutility_ucp_calculate_health.md)
- [msdb: dbo.sp_sysutility_ucp_remove](../../StoredProcedures/msdb/dbo.sp_sysutility_ucp_remove.md)
- [msdb: dbo.sp_sysutility_ucp_remove_mi](../../StoredProcedures/msdb/dbo.sp_sysutility_ucp_remove_mi.md)

