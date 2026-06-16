# dbo.syscollector_collector_types_internal

**Database:** msdb  

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

