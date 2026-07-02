# internal.environment_variables

**Database:** SSISDB  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| variable_id | bigint | 8 | 0 | YES |  |  |
| environment_id | bigint | 8 | 0 |  | YES |  |
| name | sysname | 256 | 0 |  |  |  |
| description | nvarchar | 2048 | 1 |  |  |  |
| type | nvarchar | 256 | 0 |  |  |  |
| sensitive | bit | 1 | 0 |  |  |  |
| value | sql_variant | 8016 | 1 |  |  |  |
| sensitive_value | varbinary | -1 | 1 |  |  |  |
| base_data_type | nvarchar | 256 | 0 |  |  |  |

## Referenced By Stored Procedures

- [SSISDB: catalog.create_environment_variable](../../StoredProcedures/SSISDB/catalog.create_environment_variable.md)
- [SSISDB: catalog.create_execution](../../StoredProcedures/SSISDB/catalog.create_execution.md)
- [SSISDB: catalog.delete_environment_variable](../../StoredProcedures/SSISDB/catalog.delete_environment_variable.md)
- [SSISDB: catalog.set_environment_variable_property](../../StoredProcedures/SSISDB/catalog.set_environment_variable_property.md)
- [SSISDB: catalog.set_environment_variable_protection](../../StoredProcedures/SSISDB/catalog.set_environment_variable_protection.md)
- [SSISDB: catalog.set_environment_variable_value](../../StoredProcedures/SSISDB/catalog.set_environment_variable_value.md)
- [SSISDB: catalog.set_object_parameter_value](../../StoredProcedures/SSISDB/catalog.set_object_parameter_value.md)
- [SSISDB: internal.get_decrypted_parameter_values](../../StoredProcedures/SSISDB/internal.get_decrypted_parameter_values.md)

