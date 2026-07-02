# internal.projects

**Database:** SSISDB  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| project_id | bigint | 8 | 0 | YES |  |  |
| folder_id | bigint | 8 | 0 |  | YES |  |
| name | sysname | 256 | 0 |  |  |  |
| description | nvarchar | 2048 | 1 |  |  |  |
| project_format_version | int | 4 | 1 |  |  |  |
| deployed_by_sid | varbinary | 85 | 0 |  |  |  |
| deployed_by_name | nvarchar | 256 | 0 |  |  |  |
| last_deployed_time | datetimeoffset | 10 | 0 |  |  |  |
| created_time | datetimeoffset | 10 | 0 |  |  |  |
| object_version_lsn | bigint | 8 | 0 |  |  |  |
| validation_status | char | 1 | 0 |  |  |  |
| last_validation_time | datetimeoffset | 10 | 1 |  |  |  |

## Referenced By Stored Procedures

- [SSISDB: catalog.create_execution](../../StoredProcedures/SSISDB/catalog.create_execution.md)
- [SSISDB: catalog.delete_project](../../StoredProcedures/SSISDB/catalog.delete_project.md)
- [SSISDB: catalog.move_project](../../StoredProcedures/SSISDB/catalog.move_project.md)
- [SSISDB: catalog.restore_project](../../StoredProcedures/SSISDB/catalog.restore_project.md)
- [SSISDB: catalog.startup](../../StoredProcedures/SSISDB/catalog.startup.md)
- [SSISDB: internal.cleanup_server_execution_keys](../../StoredProcedures/SSISDB/internal.cleanup_server_execution_keys.md)
- [SSISDB: internal.configure_execution_encryption_algorithm](../../StoredProcedures/SSISDB/internal.configure_execution_encryption_algorithm.md)
- [SSISDB: internal.get_decrypted_parameter_values](../../StoredProcedures/SSISDB/internal.get_decrypted_parameter_values.md)
- [SSISDB: internal.prepare_packages_deploy](../../StoredProcedures/SSISDB/internal.prepare_packages_deploy.md)
- [SSISDB: internal.update_package_deployment_status](../../StoredProcedures/SSISDB/internal.update_package_deployment_status.md)

