# internal.executables

**Database:** SSISDB  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| executable_id | bigint | 8 | 0 | YES |  |  |
| project_id | bigint | 8 | 0 |  | YES |  |
| project_version_lsn | bigint | 8 | 0 |  |  |  |
| package_name | nvarchar | 520 | 0 |  |  |  |
| package_location_type | nvarchar | 256 | 1 |  |  |  |
| package_path_full | nvarchar | 8000 | 1 |  |  |  |
| executable_name | nvarchar | 8000 | 1 |  |  |  |
| executable_guid | nvarchar | 76 | 1 |  |  |  |
| package_path | nvarchar | -1 | 1 |  |  |  |

## Referenced By Stored Procedures

- [SSISDB: internal.append_executable_statistics](../../StoredProcedures/SSISDB/internal.append_executable_statistics.md)

