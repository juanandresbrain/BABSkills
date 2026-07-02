# dbo.forecast_sale

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| forecast_id | T_ID | 16 | 0 | YES |  |  |
| forecast_detail_id | T_ID | 16 | 0 | YES |  |  |
| calendar_week_id | decimal | 9 | 0 | YES |  |  |
| forecast_error | float | 8 | 0 |  |  |  |
| safety_stock | float | 8 | 0 |  |  |  |
| forecast_value | float | 8 | 0 |  |  |  |
| forecast_trace | nvarchar | 4000 | 1 |  |  |  |
| adjustment_factor | decimal | 5 | 0 |  |  |  |

