# dbo.oo_unc_group_loc_wk

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| hierarchy_group_id | int | 4 | 0 | YES |  |  |
| merch_year_wk | int | 4 | 0 | YES |  |  |
| location_id | smallint | 2 | 0 | YES |  |  |
| on_order_units | int | 4 | 0 |  |  |  |
| on_order_retail | decimal | 9 | 0 |  |  |  |
| on_order_cost | decimal | 9 | 0 |  |  |  |
| on_order_retail_local | decimal | 9 | 1 |  |  |  |
| on_order_cost_local | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.post_oo_unc_$sp](../../StoredProcedures/ma_01/dbo.post_oo_unc_$sp.md)

