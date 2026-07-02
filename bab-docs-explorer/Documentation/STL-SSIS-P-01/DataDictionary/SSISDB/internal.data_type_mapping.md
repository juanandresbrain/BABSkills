# internal.data_type_mapping

**Database:** SSISDB  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| mapping_id | bigint | 8 | 0 | YES |  |  |
| ssis_data_type | nvarchar | 256 | 0 |  |  |  |
| sql_data_type | nvarchar | 256 | 0 |  |  |  |

## Referenced By Stored Procedures

- [SSISDB: catalog.create_environment_variable](../../StoredProcedures/SSISDB/catalog.create_environment_variable.md)
- [SSISDB: catalog.set_environment_variable_property](../../StoredProcedures/SSISDB/catalog.set_environment_variable_property.md)
- [SSISDB: catalog.set_execution_parameter_value](../../StoredProcedures/SSISDB/catalog.set_execution_parameter_value.md)
- [SSISDB: internal.check_data_type_value](../../StoredProcedures/SSISDB/internal.check_data_type_value.md)

