# internal.environment_references

**Database:** SSISDB  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| reference_id | bigint | 8 | 0 | YES |  |  |
| project_id | bigint | 8 | 0 |  | YES |  |
| reference_type | char | 1 | 0 |  |  |  |
| environment_folder_name | nvarchar | 256 | 1 |  |  |  |
| environment_name | sysname | 256 | 0 |  |  |  |
| validation_status | char | 1 | 0 |  |  |  |
| last_validation_time | datetimeoffset | 10 | 1 |  |  |  |

## Referenced By Stored Procedures

- [SSISDB: catalog.create_environment_reference](../../StoredProcedures/SSISDB/catalog.create_environment_reference.md)
- [SSISDB: catalog.delete_environment_reference](../../StoredProcedures/SSISDB/catalog.delete_environment_reference.md)
- [SSISDB: catalog.set_object_parameter_value](../../StoredProcedures/SSISDB/catalog.set_object_parameter_value.md)

