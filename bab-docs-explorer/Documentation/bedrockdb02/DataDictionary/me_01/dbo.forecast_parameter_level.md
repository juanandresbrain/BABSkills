# dbo.forecast_parameter_level

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| forecast_parameter_id | T_ID | 16 | 0 | YES |  |  |
| forecast_parameter_level_id | int | 4 | 0 | YES |  |  |
| forecast_level | tinyint | 1 | 0 |  |  |  |
| hierarchy_level_id | int | 4 | 1 |  | YES |  |

