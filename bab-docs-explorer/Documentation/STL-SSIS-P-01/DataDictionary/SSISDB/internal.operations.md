# internal.operations

**Database:** SSISDB  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| operation_id | bigint | 8 | 0 | YES |  |  |
| operation_type | smallint | 2 | 0 |  |  |  |
| created_time | datetimeoffset | 10 | 1 |  |  |  |
| object_type | smallint | 2 | 1 |  |  |  |
| object_id | bigint | 8 | 1 |  |  |  |
| object_name | nvarchar | 520 | 1 |  |  |  |
| status | int | 4 | 0 |  |  |  |
| start_time | datetimeoffset | 10 | 1 |  |  |  |
| end_time | datetimeoffset | 10 | 1 |  |  |  |
| caller_sid | varbinary | 85 | 0 |  |  |  |
| caller_name | sysname | 256 | 0 |  |  |  |
| process_id | int | 4 | 1 |  |  |  |
| stopped_by_sid | varbinary | 85 | 1 |  |  |  |
| stopped_by_name | nvarchar | 256 | 1 |  |  |  |
| operation_guid | uniqueidentifier | 16 | 1 |  |  |  |
| server_name | nvarchar | 256 | 1 |  |  |  |
| machine_name | nvarchar | 256 | 1 |  |  |  |

## Referenced By Stored Procedures

- [SSISDB: catalog.configure_catalog](../../StoredProcedures/SSISDB/catalog.configure_catalog.md)
- [SSISDB: catalog.create_execution](../../StoredProcedures/SSISDB/catalog.create_execution.md)
- [SSISDB: catalog.deploy_packages](../../StoredProcedures/SSISDB/catalog.deploy_packages.md)
- [SSISDB: catalog.restore_project](../../StoredProcedures/SSISDB/catalog.restore_project.md)
- [SSISDB: catalog.startup](../../StoredProcedures/SSISDB/catalog.startup.md)
- [SSISDB: catalog.stop_operation](../../StoredProcedures/SSISDB/catalog.stop_operation.md)
- [SSISDB: internal.cleanup_server_execution_keys](../../StoredProcedures/SSISDB/internal.cleanup_server_execution_keys.md)
- [SSISDB: internal.cleanup_server_log](../../StoredProcedures/SSISDB/internal.cleanup_server_log.md)
- [SSISDB: internal.cleanup_server_project_version](../../StoredProcedures/SSISDB/internal.cleanup_server_project_version.md)
- [SSISDB: internal.cleanup_server_retention_window](../../StoredProcedures/SSISDB/internal.cleanup_server_retention_window.md)
- [SSISDB: internal.configure_execution_encryption_algorithm](../../StoredProcedures/SSISDB/internal.configure_execution_encryption_algorithm.md)
- [SSISDB: internal.get_decrypted_parameter_values](../../StoredProcedures/SSISDB/internal.get_decrypted_parameter_values.md)
- [SSISDB: internal.get_execution_property_override_values](../../StoredProcedures/SSISDB/internal.get_execution_property_override_values.md)
- [SSISDB: internal.get_execution_values](../../StoredProcedures/SSISDB/internal.get_execution_values.md)
- [SSISDB: internal.insert_operation](../../StoredProcedures/SSISDB/internal.insert_operation.md)
- [SSISDB: internal.prepare_packages_deploy](../../StoredProcedures/SSISDB/internal.prepare_packages_deploy.md)
- [SSISDB: internal.prepare_validate_package](../../StoredProcedures/SSISDB/internal.prepare_validate_package.md)
- [SSISDB: internal.prepare_validate_project](../../StoredProcedures/SSISDB/internal.prepare_validate_project.md)
- [SSISDB: internal.sync_operation_status](../../StoredProcedures/SSISDB/internal.sync_operation_status.md)
- [SSISDB: internal.sync_validation_status](../../StoredProcedures/SSISDB/internal.sync_validation_status.md)
- [SSISDB: internal.update_operation_status](../../StoredProcedures/SSISDB/internal.update_operation_status.md)
- [SSISDB: internal.update_package_deployment_status](../../StoredProcedures/SSISDB/internal.update_package_deployment_status.md)

