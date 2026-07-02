# dbo.import_plan_group_work

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| plan_version_code | nvarchar | 40 | 0 |  |  |  |
| hierarchy_group_code | nvarchar | 40 | 1 |  |  |  |
| location_code | nvarchar | 40 | 1 |  |  |  |
| wk_pd_indicator | nchar | 2 | 0 |  |  |  |
| time_period | int | 4 | 0 |  |  |  |
| plan_element_number | nvarchar | 40 | 0 |  |  |  |
| plan_value | decimal | 9 | 0 |  |  |  |
| loc_chn_indicator | nchar | 2 | 0 |  |  |  |
| hierarchy_group_code_temp | nvarchar | 40 | 0 |  |  |  |
| location_hierarchy_code | nvarchar | 40 | 1 |  |  |  |
| exchange_rate | float | 8 | 1 |  |  |  |
| planning_jurisdiction_id | smallint | 2 | 1 |  |  |  |

