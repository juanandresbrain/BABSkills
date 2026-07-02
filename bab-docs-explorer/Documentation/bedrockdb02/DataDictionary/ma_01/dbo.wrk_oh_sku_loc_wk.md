# dbo.wrk_oh_sku_loc_wk

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| id | decimal | 9 | 0 |  |  |  |
| style_id | decimal | 9 | 0 |  |  |  |
| color_id | smallint | 2 | 0 |  |  |  |
| size_master_id | int | 4 | 0 |  |  |  |
| merch_year_wk | int | 4 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| inventory_status_id | smallint | 2 | 0 |  |  |  |
| price_status_id | smallint | 2 | 0 |  |  |  |
| on_hand_units | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.cleanup_wrk_oh_$sp](../../StoredProcedures/ma_01/dbo.cleanup_wrk_oh_$sp.md)
- [ma_01: dbo.post_oh_sku_$sp](../../StoredProcedures/ma_01/dbo.post_oh_sku_$sp.md)
- [ma_01: dbo.prep_oh_sku_$sp](../../StoredProcedures/ma_01/dbo.prep_oh_sku_$sp.md)
- [ma_01: dbo.prep_wrk_oh_$sp](../../StoredProcedures/ma_01/dbo.prep_wrk_oh_$sp.md)
- [ma_01: dbo.validate_oh_$sp](../../StoredProcedures/ma_01/dbo.validate_oh_$sp.md)
- [ma_01: dbo.wpost_oh_sku_$sp](../../StoredProcedures/ma_01/dbo.wpost_oh_sku_$sp.md)

