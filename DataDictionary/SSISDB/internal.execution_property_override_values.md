# internal.execution_property_override_values

**Database:** SSISDB  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| property_id | bigint | 8 | 0 | YES |  |  |
| execution_id | bigint | 8 | 0 |  | YES |  |
| property_path | nvarchar | 8000 | 0 |  |  |  |
| property_value | nvarchar | -1 | 1 |  |  |  |
| sensitive_property_value | varbinary | -1 | 1 |  |  |  |
| sensitive | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [SSISDB: catalog.set_execution_property_override_value](../../StoredProcedures/SSISDB/catalog.set_execution_property_override_value.md)
- [SSISDB: internal.configure_execution_encryption_algorithm](../../StoredProcedures/SSISDB/internal.configure_execution_encryption_algorithm.md)
- [SSISDB: internal.get_execution_property_override_values](../../StoredProcedures/SSISDB/internal.get_execution_property_override_values.md)

