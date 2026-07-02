# internal.execution_component_phases

**Database:** SSISDB  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| phase_stats_id | bigint | 8 | 0 | YES |  |  |
| execution_id | bigint | 8 | 0 |  | YES |  |
| package_name | nvarchar | 520 | 0 |  |  |  |
| package_location_type | nvarchar | 256 | 1 |  |  |  |
| package_path_full | nvarchar | 8000 | 1 |  |  |  |
| task_name | nvarchar | 8000 | 0 |  |  |  |
| subcomponent_name | nvarchar | 8000 | 1 |  |  |  |
| phase | sysname | 256 | 0 |  |  |  |
| is_start | bit | 1 | 1 |  |  |  |
| phase_time | datetimeoffset | 10 | 1 |  |  |  |
| execution_path | nvarchar | -1 | 1 |  |  |  |
| sequence_id | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [SSISDB: internal.append_execution_component_phases](../../StoredProcedures/SSISDB/internal.append_execution_component_phases.md)

