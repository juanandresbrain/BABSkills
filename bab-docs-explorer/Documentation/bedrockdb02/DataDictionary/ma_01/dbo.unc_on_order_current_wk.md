# dbo.unc_on_order_current_wk

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| merchandise_code | nvarchar | 40 | 0 |  |  |  |
| loc_hierarchy_group_code | nvarchar | 40 | 1 |  |  |  |
| merch_year_wk | int | 4 | 0 |  |  |  |
| on_order_units | int | 4 | 0 |  |  |  |
| on_order_retail | decimal | 9 | 0 |  |  |  |
| on_order_cost | decimal | 9 | 0 |  |  |  |
| on_order_retail_local | decimal | 9 | 1 |  |  |  |
| on_order_cost_local | decimal | 9 | 1 |  |  |  |

