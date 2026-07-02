# dbo.sysutility_ucp_dac_file_space_health_internal

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| dac_name | sysname | 256 | 0 | YES |  |  |
| dac_server_instance_name | sysname | 256 | 0 | YES |  |  |
| fg_name | sysname | 256 | 0 | YES |  |  |
| over_utilized_count | int | 4 | 0 |  |  |  |
| under_utilized_count | int | 4 | 0 |  |  |  |
| file_type | int | 4 | 0 |  |  |  |
| set_number | int | 4 | 0 | YES |  |  |
| processing_time | datetimeoffset | 10 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_sysutility_ucp_calculate_dac_file_space_health](../../StoredProcedures/msdb/dbo.sp_sysutility_ucp_calculate_dac_file_space_health.md)
- [msdb: dbo.sp_sysutility_ucp_calculate_dac_health](../../StoredProcedures/msdb/dbo.sp_sysutility_ucp_calculate_dac_health.md)
- [msdb: dbo.sp_sysutility_ucp_calculate_health](../../StoredProcedures/msdb/dbo.sp_sysutility_ucp_calculate_health.md)
- [msdb: dbo.sp_sysutility_ucp_remove](../../StoredProcedures/msdb/dbo.sp_sysutility_ucp_remove.md)

