# dbo.wrk_ib_on_order

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| hierarchy_group_id | int | 4 | 0 |  |  |  |
| style_id | decimal | 9 | 0 |  |  |  |
| color_id | smallint | 2 | 0 |  |  |  |
| size_master_id | int | 4 | 0 |  |  |  |
| ib_on_order_id | decimal | 9 | 0 | YES |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| receipt_date | smalldatetime | 4 | 0 |  |  |  |
| on_order_units | int | 4 | 0 |  |  |  |
| on_order_cost | decimal | 9 | 0 |  |  |  |
| on_order_retail | decimal | 9 | 0 |  |  |  |
| on_order_retail_te | decimal | 9 | 0 |  |  |  |
| on_order_retail_local | decimal | 9 | 1 |  |  |  |
| on_order_retail_te_local | decimal | 9 | 1 |  |  |  |
| on_order_cost_local | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.cleanup_wrk_ib_on_order_$sp](../../StoredProcedures/ma_01/dbo.cleanup_wrk_ib_on_order_$sp.md)
- [ma_01: dbo.get_max_wrk_ib_on_order_id_$sp](../../StoredProcedures/ma_01/dbo.get_max_wrk_ib_on_order_id_$sp.md)
- [ma_01: dbo.post_wrk_ib_on_order_$sp](../../StoredProcedures/ma_01/dbo.post_wrk_ib_on_order_$sp.md)
- [ma_01: dbo.wpost_oo_group_$sp](../../StoredProcedures/ma_01/dbo.wpost_oo_group_$sp.md)
- [ma_01: dbo.wpost_oo_sku_$sp](../../StoredProcedures/ma_01/dbo.wpost_oo_sku_$sp.md)
- [ma_01: dbo.wpost_oo_style_$sp](../../StoredProcedures/ma_01/dbo.wpost_oo_style_$sp.md)
- [ma_01: dbo.wpost_oo_style_color_$sp](../../StoredProcedures/ma_01/dbo.wpost_oo_style_color_$sp.md)
- [ma_01: dbo.wprep_oo_group_$sp](../../StoredProcedures/ma_01/dbo.wprep_oo_group_$sp.md)
- [ma_01: dbo.wprep_oo_sku_$sp](../../StoredProcedures/ma_01/dbo.wprep_oo_sku_$sp.md)
- [ma_01: dbo.wprep_oo_style_$sp](../../StoredProcedures/ma_01/dbo.wprep_oo_style_$sp.md)
- [ma_01: dbo.wprep_oo_style_color_$sp](../../StoredProcedures/ma_01/dbo.wprep_oo_style_color_$sp.md)

