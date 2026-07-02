# internal.object_versions

**Database:** SSISDB  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| object_version_lsn | bigint | 8 | 0 | YES |  |  |
| object_id | bigint | 8 | 0 |  |  |  |
| object_type | smallint | 2 | 0 |  |  |  |
| description | nvarchar | 2048 | 1 |  |  |  |
| created_by | nvarchar | 256 | 0 |  |  |  |
| created_time | datetimeoffset | 10 | 0 |  |  |  |
| restored_by | nvarchar | 256 | 1 |  |  |  |
| last_restored_time | datetimeoffset | 10 | 1 |  |  |  |
| object_data | varbinary | -1 | 0 |  |  |  |
| object_status | char | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [SSISDB: catalog.delete_project](../../StoredProcedures/SSISDB/catalog.delete_project.md)
- [SSISDB: catalog.restore_project](../../StoredProcedures/SSISDB/catalog.restore_project.md)
- [SSISDB: catalog.startup](../../StoredProcedures/SSISDB/catalog.startup.md)
- [SSISDB: internal.cleanup_server_project_version](../../StoredProcedures/SSISDB/internal.cleanup_server_project_version.md)
- [SSISDB: internal.get_project_internal](../../StoredProcedures/SSISDB/internal.get_project_internal.md)
- [SSISDB: internal.prepare_packages_deploy](../../StoredProcedures/SSISDB/internal.prepare_packages_deploy.md)
- [SSISDB: internal.update_object_versions](../../StoredProcedures/SSISDB/internal.update_object_versions.md)
- [SSISDB: internal.update_package_deployment_status](../../StoredProcedures/SSISDB/internal.update_package_deployment_status.md)

