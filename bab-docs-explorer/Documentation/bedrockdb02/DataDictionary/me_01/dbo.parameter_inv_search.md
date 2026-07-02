# dbo.parameter_inv_search

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| parameter_inv_search_id | smallint | 2 | 0 | YES |  |  |
| parameter_ml_id | tinyint | 1 | 0 |  |  |  |
| bookmark | nvarchar | 20 | 0 |  |  |  |
| leading_key | nvarchar | 20 | 1 |  |  |  |
| search_type | tinyint | 1 | 0 |  |  |  |
| location_id | smallint | 2 | 1 |  |  |  |
| hierarchy_id | smallint | 2 | 1 |  |  |  |
| hierarchy_level_id | int | 4 | 1 |  |  |  |
| attribute_id | decimal | 9 | 1 |  |  |  |

