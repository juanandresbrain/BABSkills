# dbo.forecast_parameter

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| forecast_parameter_id | T_ID | 16 | 0 | YES |  |  |
| style_id | decimal | 9 | 1 |  |  |  |
| hierarchy_group_id | int | 4 | 1 |  |  |  |
| vendor_id | decimal | 9 | 1 |  |  |  |
| location_id | smallint | 2 | 1 |  |  |  |
| eligibility | bit | 1 | 1 |  |  |  |
| forecast_period_type | tinyint | 1 | 1 |  |  |  |
| week_model_group_id | T_ID | 16 | 1 |  |  |  |
| period_model_group_id | T_ID | 16 | 1 |  |  |  |
| no_future_weeks | smallint | 2 | 1 |  |  |  |
| no_future_periods | smallint | 2 | 1 |  |  |  |
| service_level | tinyint | 1 | 1 |  |  |  |
| no_past_observations | smallint | 2 | 1 |  |  |  |
| no_past_iterations | smallint | 2 | 1 |  |  |  |
| seasonal_basic | bit | 1 | 1 |  |  |  |
| season_start_week_code | tinyint | 1 | 1 |  |  |  |
| season_end_week_code | tinyint | 1 | 1 |  |  |  |
| start_calendar_week_id | decimal | 9 | 1 |  |  |  |
| end_calendar_week_id | decimal | 9 | 1 |  |  |  |
| adjustment_factor | decimal | 5 | 1 |  |  |  |
| adj_start_calendar_week_id | decimal | 9 | 1 |  |  |  |
| adj_end_calendar_week_id | decimal | 9 | 1 |  |  |  |
| updatestamp_eligibility | int | 4 | 1 |  |  |  |
| updatestamp_seasonal_basic | int | 4 | 1 |  |  |  |
| updatestamp_forecast_level | int | 4 | 1 |  |  |  |
| updatestamp_forecast_adjust | int | 4 | 1 |  |  |  |
| updatestamp_date_exception | int | 4 | 1 |  |  |  |
| updatestamp_service_level | int | 4 | 1 |  |  |  |
| updatestamp_forecast_error | int | 4 | 1 |  |  |  |

