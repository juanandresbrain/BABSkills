# internal.executable_statistics

**Database:** SSISDB  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| statistics_id | bigint | 8 | 0 | YES |  |  |
| execution_id | bigint | 8 | 0 |  | YES |  |
| executable_id | bigint | 8 | 0 |  | YES |  |
| execution_path | nvarchar | -1 | 1 |  |  |  |
| start_time | datetimeoffset | 10 | 1 |  |  |  |
| end_time | datetimeoffset | 10 | 1 |  |  |  |
| execution_hierarchy | hierarchyid | 892 | 1 |  |  |  |
| execution_duration | int | 4 | 1 |  |  |  |
| execution_result | smallint | 2 | 1 |  |  |  |
| execution_value | sql_variant | 8016 | 1 |  |  |  |

## Referenced By Stored Procedures

- [SSISDB: internal.append_executable_statistics](../../StoredProcedures/SSISDB/internal.append_executable_statistics.md)

