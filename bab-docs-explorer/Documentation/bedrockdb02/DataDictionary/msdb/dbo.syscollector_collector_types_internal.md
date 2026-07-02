# dbo.syscollector_collector_types_internal

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| collector_type_uid | uniqueidentifier | 16 | 0 | YES |  |  |
| name | sysname | 256 | 0 |  |  |  |
| parameter_schema | xml | -1 | 1 |  |  |  |
| parameter_formatter | xml | -1 | 1 |  |  |  |
| schema_collection | sysname | 256 | 1 |  |  |  |
| collection_package_name | sysname | 256 | 0 |  | YES |  |
| collection_package_folderid | uniqueidentifier | 16 | 0 |  | YES |  |
| upload_package_name | sysname | 256 | 0 |  | YES |  |
| upload_package_folderid | uniqueidentifier | 16 | 0 |  | YES |  |
| is_system | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_syscollector_create_collector_type](../../StoredProcedures/msdb/dbo.sp_syscollector_create_collector_type.md)
- [msdb: dbo.sp_syscollector_delete_collector_type](../../StoredProcedures/msdb/dbo.sp_syscollector_delete_collector_type.md)
- [msdb: dbo.sp_syscollector_update_collector_type](../../StoredProcedures/msdb/dbo.sp_syscollector_update_collector_type.md)
- [msdb: dbo.sp_syscollector_validate_xml](../../StoredProcedures/msdb/dbo.sp_syscollector_validate_xml.md)

