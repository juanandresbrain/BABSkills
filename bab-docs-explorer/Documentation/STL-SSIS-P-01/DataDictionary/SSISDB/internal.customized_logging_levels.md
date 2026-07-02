# internal.customized_logging_levels

**Database:** SSISDB  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| level_id | bigint | 8 | 0 | YES |  |  |
| name | sysname | 256 | 0 |  |  |  |
| description | nvarchar | 2048 | 1 |  |  |  |
| profile_value | bigint | 8 | 0 |  |  |  |
| events_value | bigint | 8 | 0 |  |  |  |
| created_by_sid | varbinary | 85 | 0 |  |  |  |
| created_by_name | nvarchar | 256 | 0 |  |  |  |
| created_time | datetimeoffset | 10 | 0 |  |  |  |

## Referenced By Stored Procedures

- [SSISDB: catalog.configure_catalog](../../StoredProcedures/SSISDB/catalog.configure_catalog.md)
- [SSISDB: catalog.create_customized_logging_level](../../StoredProcedures/SSISDB/catalog.create_customized_logging_level.md)
- [SSISDB: catalog.delete_customized_logging_level](../../StoredProcedures/SSISDB/catalog.delete_customized_logging_level.md)
- [SSISDB: catalog.rename_customized_logging_level](../../StoredProcedures/SSISDB/catalog.rename_customized_logging_level.md)
- [SSISDB: catalog.set_customized_logging_level_description](../../StoredProcedures/SSISDB/catalog.set_customized_logging_level_description.md)
- [SSISDB: catalog.set_customized_logging_level_value](../../StoredProcedures/SSISDB/catalog.set_customized_logging_level_value.md)
- [SSISDB: internal.check_parameter_value_by_name](../../StoredProcedures/SSISDB/internal.check_parameter_value_by_name.md)

