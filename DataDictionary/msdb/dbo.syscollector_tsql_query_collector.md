# dbo.syscollector_tsql_query_collector

**Database:** msdb  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| collection_set_uid | uniqueidentifier | 16 | 0 |  |  |  |
| collection_set_id | int | 4 | 0 |  | YES |  |
| collection_item_id | int | 4 | 0 |  | YES |  |
| collection_package_id | uniqueidentifier | 16 | 0 |  |  |  |
| upload_package_id | uniqueidentifier | 16 | 0 |  |  |  |

