# dbo.syscollector_tsql_query_collector

**Database:** msdb  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| collection_set_uid | uniqueidentifier | 16 | 0 |  |  |  |
| collection_set_id | int | 4 | 0 |  | YES |  |
| collection_item_id | int | 4 | 0 |  | YES |  |
| collection_package_id | uniqueidentifier | 16 | 0 |  |  |  |
| upload_package_id | uniqueidentifier | 16 | 0 |  |  |  |

## Referenced By Stored Procedures

- [msdb: dbo.sp_syscollector_create_tsql_query_collector](../../StoredProcedures/msdb/dbo.sp_syscollector_create_tsql_query_collector.md)
- [msdb: dbo.sp_syscollector_get_tsql_query_collector_package_ids](../../StoredProcedures/msdb/dbo.sp_syscollector_get_tsql_query_collector_package_ids.md)

