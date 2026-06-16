# internal.executions

**Database:** SSISDB  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| execution_id | bigint | 8 | 0 | YES | YES |  |
| folder_name | sysname | 256 | 0 |  |  |  |
| project_name | sysname | 256 | 0 |  |  |  |
| package_name | nvarchar | 520 | 0 |  |  |  |
| reference_id | bigint | 8 | 1 |  |  |  |
| reference_type | char | 1 | 1 |  |  |  |
| environment_folder_name | nvarchar | 256 | 1 |  |  |  |
| environment_name | nvarchar | 256 | 1 |  |  |  |
| project_lsn | bigint | 8 | 1 |  |  |  |
| executed_as_sid | varbinary | 85 | 0 |  |  |  |
| executed_as_name | nvarchar | 256 | 0 |  |  |  |
| use32bitruntime | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [SSISDB: catalog.create_execution](../../StoredProcedures/SSISDB/catalog.create_execution.md)
- [SSISDB: internal.configure_execution_encryption_algorithm](../../StoredProcedures/SSISDB/internal.configure_execution_encryption_algorithm.md)

