# dbo.hist_oh_style_loc_wk

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_id | decimal | 9 | 0 | YES |  |  |
| merch_year_wk | int | 4 | 0 | YES |  |  |
| location_id | smallint | 2 | 0 | YES |  |  |
| inventory_status_id | smallint | 2 | 0 | YES |  |  |
| price_status_id | smallint | 2 | 0 | YES |  |  |
| on_hand_units | int | 4 | 0 |  |  |  |
| on_hand_retail | decimal | 9 | 0 |  |  |  |
| on_hand_cost | decimal | 9 | 0 |  |  |  |
| on_hand_retail_te | decimal | 9 | 0 |  |  |  |
| on_hand_retail_local | decimal | 9 | 1 |  |  |  |
| on_hand_retail_te_local | decimal | 9 | 1 |  |  |  |
| on_hand_cost_local | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingReportStoreSkinReview](../../StoredProcedures/me_01/dbo.spMerchandisingReportStoreSkinReview.md)
- [ma_01: dbo.dl_hist_oh_style_vld_$sp](../../StoredProcedures/ma_01/dbo.dl_hist_oh_style_vld_$sp.md)
- [ma_01: dbo.hk_style_delete_hist_oh_$sp](../../StoredProcedures/ma_01/dbo.hk_style_delete_hist_oh_$sp.md)
- [ma_01: dbo.hk_style_reclass_hist_oh_$sp](../../StoredProcedures/ma_01/dbo.hk_style_reclass_hist_oh_$sp.md)
- [ma_01: dbo.nsb_style_analysis_$sp](../../StoredProcedures/ma_01/dbo.nsb_style_analysis_$sp.md)
- [ma_01: dbo.post_binv_style_$sp](../../StoredProcedures/ma_01/dbo.post_binv_style_$sp.md)
- [ma_01: dbo.post_binv_style_adj_hist_$sp](../../StoredProcedures/ma_01/dbo.post_binv_style_adj_hist_$sp.md)
- [ma_01: dbo.post_hist_oh_style_$sp](../../StoredProcedures/ma_01/dbo.post_hist_oh_style_$sp.md)
- [ma_01: dbo.post_oh_style_$sp](../../StoredProcedures/ma_01/dbo.post_oh_style_$sp.md)
- [ma_01: dbo.reclass_hist_oh_$sp](../../StoredProcedures/ma_01/dbo.reclass_hist_oh_$sp.md)
- [ma_01: dbo.roll_oh_style_loc_wk_$sp](../../StoredProcedures/ma_01/dbo.roll_oh_style_loc_wk_$sp.md)
- [ma_01: dbo.roll_oh_style_wk_$sp](../../StoredProcedures/ma_01/dbo.roll_oh_style_wk_$sp.md)
- [ma_01: dbo.rpt_style_analysis_$sp](../../StoredProcedures/ma_01/dbo.rpt_style_analysis_$sp.md)
- [ma_01: dbo.rpt_style_listing_class_vendor_$sp](../../StoredProcedures/ma_01/dbo.rpt_style_listing_class_vendor_$sp.md)
- [ma_01: dbo.spDW_Inventory](../../StoredProcedures/ma_01/dbo.spDW_Inventory.md)
- [ma_01: dbo.spDW_TopStyleTy](../../StoredProcedures/ma_01/dbo.spDW_TopStyleTy.md)
- [ma_01: dbo.spDW_TopStyleTyBACKUP20180108](../../StoredProcedures/ma_01/dbo.spDW_TopStyleTyBACKUP20180108.md)
- [ma_01: dbo.startup_oh_style_loc_pd_$sp](../../StoredProcedures/ma_01/dbo.startup_oh_style_loc_pd_$sp.md)
- [ma_01: dbo.startup_oh_style_loc_wk_$sp](../../StoredProcedures/ma_01/dbo.startup_oh_style_loc_wk_$sp.md)

