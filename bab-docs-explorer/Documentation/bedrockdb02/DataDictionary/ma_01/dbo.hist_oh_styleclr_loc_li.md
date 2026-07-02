# dbo.hist_oh_styleclr_loc_li

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_id | decimal | 9 | 0 | YES |  |  |
| color_id | smallint | 2 | 0 | YES |  |  |
| location_id | smallint | 2 | 0 | YES |  |  |
| inventory_status_id | smallint | 2 | 0 | YES |  |  |
| price_status_id | smallint | 2 | 0 | YES |  |  |
| on_hand_units | int | 4 | 0 |  |  |  |
| on_hand_retail | decimal | 9 | 0 |  |  |  |
| on_hand_retail_te | decimal | 9 | 0 |  |  |  |
| on_hand_retail_local | decimal | 9 | 1 |  |  |  |
| on_hand_retail_te_local | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.hk_style_delete_hist_oh_$sp](../../StoredProcedures/ma_01/dbo.hk_style_delete_hist_oh_$sp.md)
- [ma_01: dbo.post_binv_styleclr_$sp](../../StoredProcedures/ma_01/dbo.post_binv_styleclr_$sp.md)
- [ma_01: dbo.post_hist_oh_styleclr_$sp](../../StoredProcedures/ma_01/dbo.post_hist_oh_styleclr_$sp.md)
- [ma_01: dbo.post_oh_style_color_$sp](../../StoredProcedures/ma_01/dbo.post_oh_style_color_$sp.md)
- [ma_01: dbo.startup_oh_styleclr_loc_li_$sp](../../StoredProcedures/ma_01/dbo.startup_oh_styleclr_loc_li_$sp.md)

