# internal.catalog_encryption_keys

**Database:** SSISDB  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| key_id | bigint | 8 | 0 | YES |  |  |
| key_name | nvarchar | 510 | 0 |  |  |  |
| KEY | varbinary | 8000 | 0 |  |  |  |
| IV | varbinary | 8000 | 0 |  |  |  |

## Referenced By Stored Procedures

- [SSISDB: catalog.delete_project](../../StoredProcedures/SSISDB/catalog.delete_project.md)
- [SSISDB: catalog.startup](../../StoredProcedures/SSISDB/catalog.startup.md)
- [SSISDB: internal.get_project_internal](../../StoredProcedures/SSISDB/internal.get_project_internal.md)
- [SSISDB: internal.get_updatedpackages](../../StoredProcedures/SSISDB/internal.get_updatedpackages.md)
- [SSISDB: internal.prepare_packages_deploy](../../StoredProcedures/SSISDB/internal.prepare_packages_deploy.md)
- [SSISDB: internal.update_project_object](../../StoredProcedures/SSISDB/internal.update_project_object.md)

