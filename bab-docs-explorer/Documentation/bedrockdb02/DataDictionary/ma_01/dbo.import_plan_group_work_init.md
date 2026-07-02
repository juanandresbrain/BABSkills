# dbo.import_plan_group_work_init

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| plan_version_code | nvarchar | 40 | 0 |  |  |  |
| hierarchy_group_code | nvarchar | 40 | 0 |  |  |  |
| location_code | nvarchar | 40 | 1 |  |  |  |
| wk_pd_indicator | nchar | 2 | 0 |  |  |  |
| time_period | int | 4 | 0 |  |  |  |
| plan_element_number | nvarchar | 40 | 0 |  |  |  |
| plan_value | decimal | 9 | 0 |  |  |  |
| loc_chn_indicator | nchar | 2 | 0 |  |  |  |
| merch_level_indicator | nchar | 2 | 0 |  |  |  |
| timetag | tinyint | 1 | 0 |  |  |  |

