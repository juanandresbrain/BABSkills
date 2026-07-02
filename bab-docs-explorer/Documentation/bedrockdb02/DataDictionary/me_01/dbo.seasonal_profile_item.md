# dbo.seasonal_profile_item

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| seasonal_profile_group_id | decimal | 9 | 0 | YES |  |  |
| seasonal_profile_item_id | decimal | 9 | 0 | YES |  |  |
| style_id | decimal | 9 | 1 |  |  |  |
| sku_id | decimal | 9 | 1 |  |  |  |
| style_color_id | decimal | 9 | 1 |  |  |  |
| hierarchy_group_id | int | 4 | 1 |  |  |  |
| start_calc_calendar_year_id | smallint | 2 | 1 |  |  |  |
| end_calc_calendar_year_id | smallint | 2 | 1 |  |  |  |

