# dbo.sysutility_mi_dac_execution_statistics_internal

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| dac_instance_name | sysname | 256 | 0 | YES |  |  |
| database_name | sysname | 256 | 0 |  |  |  |
| database_id | int | 4 | 0 |  |  |  |
| date_created | datetime | 8 | 1 |  |  |  |
| description | nvarchar | 8000 | 1 |  |  |  |
| first_collection_time | datetimeoffset | 10 | 1 |  |  |  |
| last_collection_time | datetimeoffset | 10 | 1 |  |  |  |
| last_upload_time | datetimeoffset | 10 | 1 |  |  |  |
| lifetime_cpu_time_ms | bigint | 8 | 1 |  |  |  |
| cpu_time_ms_at_last_upload | bigint | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_sysutility_mi_collect_dac_execution_statistics_internal](../../StoredProcedures/msdb/dbo.sp_sysutility_mi_collect_dac_execution_statistics_internal.md)
- [msdb: dbo.sp_sysutility_mi_get_dac_execution_statistics_internal](../../StoredProcedures/msdb/dbo.sp_sysutility_mi_get_dac_execution_statistics_internal.md)

