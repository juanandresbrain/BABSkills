# dbo.wrk_oo_all_styleclr_loc_wk

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| id | decimal | 9 | 0 |  |  |  |
| style_id | decimal | 9 | 0 |  |  |  |
| color_id | smallint | 2 | 0 |  |  |  |
| merch_year_wk | int | 4 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| on_order_units | int | 4 | 0 |  |  |  |
| on_order_retail | decimal | 9 | 0 |  |  |  |
| allocation_units | int | 4 | 0 |  |  |  |
| on_order_retail_te | decimal | 9 | 0 |  |  |  |
| on_order_retail_local | decimal | 9 | 1 |  |  |  |
| on_order_retail_te_local | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.cleanup_wrk_oo_all_$sp](../../StoredProcedures/ma_01/dbo.cleanup_wrk_oo_all_$sp.md)
- [ma_01: dbo.post_oo_style_color_$sp](../../StoredProcedures/ma_01/dbo.post_oo_style_color_$sp.md)
- [ma_01: dbo.prep_oo_style_color_$sp](../../StoredProcedures/ma_01/dbo.prep_oo_style_color_$sp.md)
- [ma_01: dbo.prep_wrk_oo_all_$sp](../../StoredProcedures/ma_01/dbo.prep_wrk_oo_all_$sp.md)
- [ma_01: dbo.validate_oo_all_$sp](../../StoredProcedures/ma_01/dbo.validate_oo_all_$sp.md)
- [ma_01: dbo.wpost_all_style_color_$sp](../../StoredProcedures/ma_01/dbo.wpost_all_style_color_$sp.md)
- [ma_01: dbo.wpost_oo_style_color_$sp](../../StoredProcedures/ma_01/dbo.wpost_oo_style_color_$sp.md)

