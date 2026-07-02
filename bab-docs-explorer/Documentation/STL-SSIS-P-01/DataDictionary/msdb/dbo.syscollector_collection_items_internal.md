# dbo.syscollector_collection_items_internal

**Database:** msdb  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| collection_set_id | int | 4 | 0 | YES | YES |  |
| collection_item_id | int | 4 | 0 | YES |  |  |
| collector_type_uid | uniqueidentifier | 16 | 0 |  | YES |  |
| name | sysname | 256 | 0 |  |  |  |
| name_id | int | 4 | 1 |  |  |  |
| frequency | int | 4 | 0 |  |  |  |
| parameters | xml | -1 | 1 |  |  |  |

