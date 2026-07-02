# dbo.price_change_user_prefs

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| price_change_user_prefs_id | decimal | 9 | 0 | YES |  |  |
| calculation_method | smallint | 2 | 0 |  |  |  |
| base_calculation_on | smallint | 2 | 1 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |
| user_id | numeric | 9 | 0 |  |  |  |

