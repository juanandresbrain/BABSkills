# dbo.forecast_detail

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| forecast_id | T_ID | 16 | 0 | YES |  |  |
| forecast_detail_id | T_ID | 16 | 0 | YES |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| sku_id | decimal | 9 | 1 |  |  |  |
| style_id | decimal | 9 | 1 |  |  |  |
| style_color_id | decimal | 9 | 1 |  |  |  |
| alternate_history_used | bit | 1 | 0 |  |  |  |
| seasonal_profile_group_id | decimal | 9 | 1 |  | YES |  |
| forecast_model_id | T_ID | 16 | 0 |  |  |  |
| service_level | tinyint | 1 | 0 |  |  |  |
| forecast_error_trace | nvarchar | -1 | 1 |  |  |  |
| service_level_trace | nvarchar | -1 | 1 |  |  |  |
| comp_set_id | bigint | 8 | 1 |  |  |  |
| comp_set_used | bit | 1 | 0 |  |  |  |
| sales_history_trace | nvarchar | -1 | 1 |  |  |  |
| entity_loc_group_id | int | 4 | 1 |  |  |  |

