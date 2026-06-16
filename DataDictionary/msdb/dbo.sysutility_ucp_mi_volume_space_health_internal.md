# dbo.sysutility_ucp_mi_volume_space_health_internal

**Database:** msdb  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| physical_server_name | sysname | 256 | 0 |  |  |  |
| server_instance_name | sysname | 256 | 0 | YES |  |  |
| volume_device_id | sysname | 256 | 0 | YES |  |  |
| health_state | int | 4 | 0 |  |  |  |
| set_number | int | 4 | 0 | YES |  |  |
| processing_time | datetimeoffset | 10 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_sysutility_ucp_calculate_computer_health](../../StoredProcedures/msdb/dbo.sp_sysutility_ucp_calculate_computer_health.md)
- [msdb: dbo.sp_sysutility_ucp_calculate_dac_health](../../StoredProcedures/msdb/dbo.sp_sysutility_ucp_calculate_dac_health.md)
- [msdb: dbo.sp_sysutility_ucp_calculate_health](../../StoredProcedures/msdb/dbo.sp_sysutility_ucp_calculate_health.md)
- [msdb: dbo.sp_sysutility_ucp_calculate_mi_health](../../StoredProcedures/msdb/dbo.sp_sysutility_ucp_calculate_mi_health.md)
- [msdb: dbo.sp_sysutility_ucp_remove](../../StoredProcedures/msdb/dbo.sp_sysutility_ucp_remove.md)

