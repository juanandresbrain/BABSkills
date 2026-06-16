# internal.object_parameters

**Database:** SSISDB  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| parameter_id | bigint | 8 | 0 | YES |  |  |
| project_id | bigint | 8 | 0 |  | YES |  |
| project_version_lsn | bigint | 8 | 0 |  | YES |  |
| object_type | smallint | 2 | 0 |  |  |  |
| object_name | nvarchar | 520 | 0 |  |  |  |
| parameter_name | sysname | 256 | 0 |  |  |  |
| parameter_data_type | nvarchar | 256 | 0 |  |  |  |
| required | bit | 1 | 0 |  |  |  |
| sensitive | bit | 1 | 0 |  |  |  |
| description | nvarchar | 2048 | 1 |  |  |  |
| design_default_value | sql_variant | 8016 | 1 |  |  |  |
| default_value | sql_variant | 8016 | 1 |  |  |  |
| sensitive_default_value | varbinary | -1 | 1 |  |  |  |
| base_data_type | nvarchar | 256 | 1 |  |  |  |
| value_type | char | 1 | 0 |  |  |  |
| value_set | bit | 1 | 0 |  |  |  |
| referenced_variable_name | nvarchar | 256 | 1 |  |  |  |
| validation_status | char | 1 | 0 |  |  |  |
| last_validation_time | datetimeoffset | 10 | 1 |  |  |  |

## Referenced By Stored Procedures

- [SSISDB: catalog.clear_object_parameter_value](../../StoredProcedures/SSISDB/catalog.clear_object_parameter_value.md)
- [SSISDB: catalog.create_execution](../../StoredProcedures/SSISDB/catalog.create_execution.md)
- [SSISDB: catalog.restore_project](../../StoredProcedures/SSISDB/catalog.restore_project.md)
- [SSISDB: catalog.set_object_parameter_value](../../StoredProcedures/SSISDB/catalog.set_object_parameter_value.md)
- [SSISDB: internal.get_decrypted_parameter_values](../../StoredProcedures/SSISDB/internal.get_decrypted_parameter_values.md)

