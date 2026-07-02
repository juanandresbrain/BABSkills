# dbo.hist_oh_group_loc_wk

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| hierarchy_group_id | int | 4 | 0 | YES |  |  |
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

- [ma_01: dbo.dl_hist_oh_group_vld_$sp](../../StoredProcedures/ma_01/dbo.dl_hist_oh_group_vld_$sp.md)
- [ma_01: dbo.nsb_core_location_$sp](../../StoredProcedures/ma_01/dbo.nsb_core_location_$sp.md)
- [ma_01: dbo.nsb_mar_location_md_$sp](../../StoredProcedures/ma_01/dbo.nsb_mar_location_md_$sp.md)
- [ma_01: dbo.post_binv_group_$sp](../../StoredProcedures/ma_01/dbo.post_binv_group_$sp.md)
- [ma_01: dbo.post_binv_group_adj_hist_$sp](../../StoredProcedures/ma_01/dbo.post_binv_group_adj_hist_$sp.md)
- [ma_01: dbo.post_hist_oh_group_$sp](../../StoredProcedures/ma_01/dbo.post_hist_oh_group_$sp.md)
- [ma_01: dbo.post_oh_group_$sp](../../StoredProcedures/ma_01/dbo.post_oh_group_$sp.md)
- [ma_01: dbo.reclass_hist_oh_$sp](../../StoredProcedures/ma_01/dbo.reclass_hist_oh_$sp.md)
- [ma_01: dbo.roll_oh_group_loc_wk_$sp](../../StoredProcedures/ma_01/dbo.roll_oh_group_loc_wk_$sp.md)
- [ma_01: dbo.roll_oh_group_wk_$sp](../../StoredProcedures/ma_01/dbo.roll_oh_group_wk_$sp.md)
- [ma_01: dbo.rpt_core_location_home_$sp](../../StoredProcedures/ma_01/dbo.rpt_core_location_home_$sp.md)
- [ma_01: dbo.rpt_core_location_local_$sp](../../StoredProcedures/ma_01/dbo.rpt_core_location_local_$sp.md)
- [ma_01: dbo.rpt_mar_location_md_home_$sp](../../StoredProcedures/ma_01/dbo.rpt_mar_location_md_home_$sp.md)
- [ma_01: dbo.rpt_mar_location_md_local_$sp](../../StoredProcedures/ma_01/dbo.rpt_mar_location_md_local_$sp.md)
- [ma_01: dbo.startup_oh_group_loc_pd_$sp](../../StoredProcedures/ma_01/dbo.startup_oh_group_loc_pd_$sp.md)
- [ma_01: dbo.startup_oh_group_loc_wk_$sp](../../StoredProcedures/ma_01/dbo.startup_oh_group_loc_wk_$sp.md)

