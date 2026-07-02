# dbo.entity_loc_group_item

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| entity_loc_group_id | int | 4 | 0 | YES |  |  |
| entity_loc_group_item_id | int | 4 | 0 | YES |  |  |
| entity_loc_group_item_type | tinyint | 1 | 0 |  |  |  |
| location_id | smallint | 2 | 1 |  |  |  |
| hierarchy_level_id | int | 4 | 1 |  |  |  |
| hierarchy_group_id | int | 4 | 1 |  |  |  |
| attribute_id | decimal | 9 | 1 |  |  |  |
| attribute_set_id | decimal | 9 | 1 |  |  |  |
| root_hierarchy_level_id | int | 4 | 1 |  |  |  |
| root_hierarchy_group_id | int | 4 | 1 |  |  |  |
| is_excluded | bit | 1 | 0 |  |  |  |

