# dbo.import_merch_attrib_set

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| import_merch_attrib_set_id | smallint | 2 | 0 | YES |  |  |
| entity_type | nvarchar | 4 | 0 |  |  |  |
| action_type | nchar | 2 | 0 |  |  |  |
| alternate_flag | nchar | 2 | 1 |  |  |  |
| hierarchy_name | nvarchar | 60 | 1 |  |  |  |
| hierarchy_group_code | nvarchar | 40 | 0 |  |  |  |
| attribute_code | nvarchar | 12 | 0 |  |  |  |
| attribute_set_code | nvarchar | 12 | 0 |  |  |  |

