# dbo.multi_currency_location_cost_pd

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| location_id | smallint | 2 | 0 | YES |  |  |
| effective_from_year_pd | int | 4 | 0 | YES |  |  |
| effective_to_year_pd | int | 4 | 1 |  |  |  |
| cost_exchange_rate | float | 8 | 0 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.populate_multi_currency_by_loc_pd_$sp](../../StoredProcedures/ma_01/dbo.populate_multi_currency_by_loc_pd_$sp.md)
- [ma_01: dbo.startup_plan_group_loc_pd_$sp](../../StoredProcedures/ma_01/dbo.startup_plan_group_loc_pd_$sp.md)

