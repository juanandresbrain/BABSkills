# internal.execution_parameter_values

**Database:** SSISDB  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| execution_parameter_id | bigint | 8 | 0 | YES |  |  |
| execution_id | bigint | 8 | 0 |  | YES |  |
| object_type | smallint | 2 | 0 |  |  |  |
| parameter_data_type | nvarchar | 256 | 0 |  |  |  |
| parameter_name | sysname | 256 | 0 |  |  |  |
| parameter_value | sql_variant | 8016 | 1 |  |  |  |
| sensitive_parameter_value | varbinary | -1 | 1 |  |  |  |
| base_data_type | nvarchar | 256 | 1 |  |  |  |
| sensitive | bit | 1 | 0 |  |  |  |
| required | bit | 1 | 0 |  |  |  |
| value_set | bit | 1 | 0 |  |  |  |
| runtime_override | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [SSISDB: catalog.create_execution](../../StoredProcedures/SSISDB/catalog.create_execution.md)
- [SSISDB: catalog.set_execution_parameter_value](../../StoredProcedures/SSISDB/catalog.set_execution_parameter_value.md)
- [SSISDB: internal.configure_execution_encryption_algorithm](../../StoredProcedures/SSISDB/internal.configure_execution_encryption_algorithm.md)
- [SSISDB: internal.get_execution_values](../../StoredProcedures/SSISDB/internal.get_execution_values.md)

