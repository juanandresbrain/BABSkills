# dbo.import_loc_attrib_set

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| import_loc_attrib_set_id | decimal | 9 | 0 | YES |  |  |
| entity_type | nvarchar | 4 | 0 |  |  |  |
| action_type | nchar | 2 | 0 |  |  |  |
| location_code | nvarchar | 40 | 0 |  |  |  |
| attribute_code | nvarchar | 12 | 0 |  |  |  |
| attribute_set_code | nvarchar | 12 | 0 |  |  |  |
| import_replication_queue_id | decimal | 9 | 1 |  |  |  |

