# dbo.oo_all_sku_loc_pd

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_id | decimal | 9 | 0 | YES |  |  |
| color_id | smallint | 2 | 0 | YES |  |  |
| size_master_id | int | 4 | 0 | YES |  |  |
| merch_year_pd | int | 4 | 0 | YES |  |  |
| location_id | smallint | 2 | 0 | YES |  |  |
| on_order_units | int | 4 | 0 |  |  |  |
| allocation_units | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.hk_sku_modify_oo_all_$sp](../../StoredProcedures/ma_01/dbo.hk_sku_modify_oo_all_$sp.md)
- [ma_01: dbo.hk_style_delete_oo_all_$sp](../../StoredProcedures/ma_01/dbo.hk_style_delete_oo_all_$sp.md)
- [ma_01: dbo.post_oo_all_sku_$sp](../../StoredProcedures/ma_01/dbo.post_oo_all_sku_$sp.md)
- [ma_01: dbo.post_oo_sku_$sp](../../StoredProcedures/ma_01/dbo.post_oo_sku_$sp.md)

