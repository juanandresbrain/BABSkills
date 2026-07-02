# dbo.plan_group_loc_wk_currency_rate

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| location_id | smallint | 2 | 0 | YES |  |  |
| cost_exchange_rate | float | 8 | 0 |  |  |  |
| retail_exchange_rate | float | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.startup_plan_group_loc_wk_$sp](../../StoredProcedures/ma_01/dbo.startup_plan_group_loc_wk_$sp.md)

