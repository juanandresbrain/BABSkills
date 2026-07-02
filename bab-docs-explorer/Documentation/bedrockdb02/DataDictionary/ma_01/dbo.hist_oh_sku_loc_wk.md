# dbo.hist_oh_sku_loc_wk

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_id | decimal | 9 | 0 | YES |  |  |
| color_id | smallint | 2 | 0 | YES |  |  |
| size_master_id | int | 4 | 0 | YES |  |  |
| merch_year_wk | int | 4 | 0 | YES |  |  |
| location_id | smallint | 2 | 0 | YES |  |  |
| inventory_status_id | smallint | 2 | 0 | YES |  |  |
| price_status_id | smallint | 2 | 0 | YES |  |  |
| on_hand_units | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.dl_hist_oh_sku_vld_$sp](../../StoredProcedures/ma_01/dbo.dl_hist_oh_sku_vld_$sp.md)
- [ma_01: dbo.es_calc_sell_thru_$sp](../../StoredProcedures/ma_01/dbo.es_calc_sell_thru_$sp.md)
- [ma_01: dbo.hk_sku_modify_hist_oh_$sp](../../StoredProcedures/ma_01/dbo.hk_sku_modify_hist_oh_$sp.md)
- [ma_01: dbo.hk_style_delete_hist_oh_$sp](../../StoredProcedures/ma_01/dbo.hk_style_delete_hist_oh_$sp.md)
- [ma_01: dbo.post_binv_sku_$sp](../../StoredProcedures/ma_01/dbo.post_binv_sku_$sp.md)
- [ma_01: dbo.post_binv_sku_adj_hist_$sp](../../StoredProcedures/ma_01/dbo.post_binv_sku_adj_hist_$sp.md)
- [ma_01: dbo.post_hist_oh_sku_$sp](../../StoredProcedures/ma_01/dbo.post_hist_oh_sku_$sp.md)
- [ma_01: dbo.post_oh_sku_$sp](../../StoredProcedures/ma_01/dbo.post_oh_sku_$sp.md)
- [ma_01: dbo.roll_oh_sku_loc_wk_$sp](../../StoredProcedures/ma_01/dbo.roll_oh_sku_loc_wk_$sp.md)
- [ma_01: dbo.roll_oh_sku_wk_$sp](../../StoredProcedures/ma_01/dbo.roll_oh_sku_wk_$sp.md)

