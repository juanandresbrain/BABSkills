# dbo.post_oo_all_group_sum

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| hierarchy_group_id | int | 4 | 0 |  |  |  |
| merch_year_wk | int | 4 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| on_order_units | int | 4 | 0 |  |  |  |
| on_order_retail | decimal | 9 | 0 |  |  |  |
| on_order_cost | decimal | 9 | 0 |  |  |  |
| allocation_units | int | 4 | 0 |  |  |  |
| on_order_retail_te | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.hk_style_reclass_oo_all_$sp](../../StoredProcedures/ma_01/dbo.hk_style_reclass_oo_all_$sp.md)
- [ma_01: dbo.post_oo_all_group_$sp](../../StoredProcedures/ma_01/dbo.post_oo_all_group_$sp.md)

