# internal.execution_data_statistics

**Database:** SSISDB  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| data_stats_id | bigint | 8 | 0 | YES |  |  |
| execution_id | bigint | 8 | 0 |  | YES |  |
| package_name | nvarchar | 520 | 0 |  |  |  |
| package_location_type | nvarchar | 256 | 1 |  |  |  |
| package_path_full | nvarchar | 8000 | 1 |  |  |  |
| task_name | nvarchar | 8000 | 1 |  |  |  |
| dataflow_path_id_string | nvarchar | 8000 | 1 |  |  |  |
| dataflow_path_name | nvarchar | 8000 | 1 |  |  |  |
| source_component_name | nvarchar | 8000 | 1 |  |  |  |
| destination_component_name | nvarchar | 8000 | 1 |  |  |  |
| rows_sent | bigint | 8 | 1 |  |  |  |
| created_time | datetimeoffset | 10 | 1 |  |  |  |
| execution_path | nvarchar | -1 | 1 |  |  |  |

## Referenced By Stored Procedures

- [SSISDB: internal.append_execution_data_statistics](../../StoredProcedures/SSISDB/internal.append_execution_data_statistics.md)

