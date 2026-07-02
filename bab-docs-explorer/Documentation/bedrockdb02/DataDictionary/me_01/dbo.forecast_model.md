# dbo.forecast_model

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| forecast_model_id | T_ID | 16 | 0 | YES |  |  |
| forecast_model_name | nvarchar | 80 | 0 |  |  |  |
| forecast_algorithm | tinyint | 1 | 0 |  |  |  |
| number_of_observations | smallint | 2 | 1 |  |  |  |
| smoothing_weight | decimal | 5 | 1 |  |  |  |
| smoothed_sum_of_errors_weight | decimal | 5 | 1 |  |  |  |
| base_factor | decimal | 5 | 1 |  |  |  |
| apply_seasonality | bit | 1 | 0 |  |  |  |
| elim_out_of_stock_influences | bit | 1 | 0 |  |  |  |
| eliminate_promo_influences | bit | 1 | 0 |  |  |  |
| eliminate_outlier_influences | bit | 1 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |

