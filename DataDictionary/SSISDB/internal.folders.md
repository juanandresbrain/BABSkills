# internal.folders

**Database:** SSISDB  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| folder_id | bigint | 8 | 0 | YES |  |  |
| name | sysname | 256 | 0 |  |  |  |
| description | nvarchar | 2048 | 1 |  |  |  |
| created_by_sid | varbinary | 85 | 0 |  |  |  |
| created_by_name | nvarchar | 256 | 0 |  |  |  |
| created_time | datetimeoffset | 10 | 0 |  |  |  |

## Referenced By Stored Procedures

- [SSISDB: catalog.create_environment](../../StoredProcedures/SSISDB/catalog.create_environment.md)
- [SSISDB: catalog.create_execution](../../StoredProcedures/SSISDB/catalog.create_execution.md)
- [SSISDB: catalog.create_folder](../../StoredProcedures/SSISDB/catalog.create_folder.md)
- [SSISDB: catalog.delete_folder](../../StoredProcedures/SSISDB/catalog.delete_folder.md)
- [SSISDB: catalog.rename_environment](../../StoredProcedures/SSISDB/catalog.rename_environment.md)
- [SSISDB: catalog.rename_folder](../../StoredProcedures/SSISDB/catalog.rename_folder.md)
- [SSISDB: catalog.set_folder_description](../../StoredProcedures/SSISDB/catalog.set_folder_description.md)
- [SSISDB: catalog.set_object_parameter_value](../../StoredProcedures/SSISDB/catalog.set_object_parameter_value.md)
- [SSISDB: internal.get_decrypted_parameter_values](../../StoredProcedures/SSISDB/internal.get_decrypted_parameter_values.md)

