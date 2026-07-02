# dbo.import_merch_plu_profile

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| import_merch_plu_profile_id | decimal | 9 | 0 | YES |  |  |
| entity_type | nvarchar | 4 | 0 |  |  |  |
| action_type | nchar | 2 | 0 |  |  |  |
| hierarchy_group_code | nvarchar | 40 | 0 |  |  |  |
| attribute_code | nvarchar | 12 | 0 |  |  |  |
| plu_collection_code | nvarchar | 8 | 0 |  |  |  |
| attribute_set_code | nvarchar | 12 | 0 |  |  |  |
| plu_profile_code | nvarchar | 12 | 0 |  |  |  |
| import_replication_queue_id | decimal | 9 | 1 |  |  |  |

