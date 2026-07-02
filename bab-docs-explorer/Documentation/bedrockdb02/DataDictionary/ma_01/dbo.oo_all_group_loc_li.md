# dbo.oo_all_group_loc_li

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| hierarchy_group_id | int | 4 | 0 | YES |  |  |
| location_id | smallint | 2 | 0 | YES |  |  |
| on_order_units | int | 4 | 0 |  |  |  |
| on_order_retail | decimal | 9 | 0 |  |  |  |
| on_order_cost | decimal | 9 | 0 |  |  |  |
| allocation_units | int | 4 | 0 |  |  |  |
| on_order_retail_te | decimal | 9 | 0 |  |  |  |
| on_order_retail_local | decimal | 9 | 1 |  |  |  |
| on_order_retail_te_local | decimal | 9 | 1 |  |  |  |
| on_order_cost_local | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.post_oo_all_group_$sp](../../StoredProcedures/ma_01/dbo.post_oo_all_group_$sp.md)
- [ma_01: dbo.post_oo_group_$sp](../../StoredProcedures/ma_01/dbo.post_oo_group_$sp.md)
- [ma_01: dbo.reclass_oo_all_$sp](../../StoredProcedures/ma_01/dbo.reclass_oo_all_$sp.md)
- [ma_01: dbo.startup_oo_all_group_$sp](../../StoredProcedures/ma_01/dbo.startup_oo_all_group_$sp.md)

