# dbo.seasonal_index

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| seasonal_profile_group_id | decimal | 9 | 0 | YES |  |  |
| calendar_week_id | decimal | 9 | 0 | YES |  |  |
| calendar_year_id | smallint | 2 | 0 | YES |  |  |
| location_id | smallint | 2 | 0 | YES |  |  |
| weekly_sales | int | 4 | 1 |  |  |  |
| index_value | decimal | 5 | 0 |  |  |  |
| suggested_index_value | decimal | 5 | 1 |  |  |  |
| entity_loc_group_id | int | 4 | 0 | YES |  |  |
| last_generated_date_time | datetime | 8 | 1 |  |  |  |

