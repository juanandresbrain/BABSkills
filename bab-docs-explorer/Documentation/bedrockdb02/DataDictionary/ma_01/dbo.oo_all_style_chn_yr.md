# dbo.oo_all_style_chn_yr

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_id | decimal | 9 | 0 | YES |  |  |
| merch_year | smallint | 2 | 0 | YES |  |  |
| on_order_units | int | 4 | 0 |  |  |  |
| on_order_retail | decimal | 9 | 0 |  |  |  |
| on_order_cost | decimal | 9 | 0 |  |  |  |
| allocation_units | int | 4 | 0 |  |  |  |
| on_order_retail_te | decimal | 9 | 0 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.hk_style_delete_oo_all_$sp](../../StoredProcedures/ma_01/dbo.hk_style_delete_oo_all_$sp.md)
- [ma_01: dbo.post_oo_all_style_$sp](../../StoredProcedures/ma_01/dbo.post_oo_all_style_$sp.md)
- [ma_01: dbo.post_oo_style_$sp](../../StoredProcedures/ma_01/dbo.post_oo_style_$sp.md)

