# dbo.gl_distribution_set

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| gl_distribution_set_id | int | 4 | 0 | YES |  |  |
| gl_distribution_set_code | nvarchar | 40 | 0 |  |  |  |
| distribution_set_description | nvarchar | 60 | 0 |  |  |  |
| discount_recognition | smallint | 2 | 0 |  |  |  |
| inter_cost | bit | 1 | 0 |  |  |  |
| match | bit | 1 | 0 |  |  |  |
| active_flag | bit | 1 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |

