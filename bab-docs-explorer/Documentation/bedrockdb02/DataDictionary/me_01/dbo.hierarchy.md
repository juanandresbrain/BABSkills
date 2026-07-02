# dbo.hierarchy

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| hierarchy_id | smallint | 2 | 0 | YES |  |  |
| hierarchy_label | nvarchar | 60 | 0 |  |  |  |
| hierarchy_type | tinyint | 1 | 0 |  |  |  |
| alternate_flag | bit | 1 | 0 |  |  |  |
| active_flag | bit | 1 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.c_location_eligibilty_rep_$sp](../../StoredProcedures/me_01/dbo.c_location_eligibilty_rep_$sp.md)
- [me_01: dbo.cum_val_hist_$sp](../../StoredProcedures/me_01/dbo.cum_val_hist_$sp.md)
- [me_01: dbo.dl_style_task_validate_$sp](../../StoredProcedures/me_01/dbo.dl_style_task_validate_$sp.md)
- [me_01: dbo.get_price_change_details_$sp](../../StoredProcedures/me_01/dbo.get_price_change_details_$sp.md)
- [me_01: dbo.get_price_change_details_pricing_level_$sp](../../StoredProcedures/me_01/dbo.get_price_change_details_pricing_level_$sp.md)
- [me_01: dbo.plu_common_dept_$sp](../../StoredProcedures/me_01/dbo.plu_common_dept_$sp.md)
- [me_01: dbo.plu_hg_regen_dept_$sp](../../StoredProcedures/me_01/dbo.plu_hg_regen_dept_$sp.md)
- [me_01: dbo.plu_hg_regen_queue_$sp](../../StoredProcedures/me_01/dbo.plu_hg_regen_queue_$sp.md)
- [me_01: dbo.plu_regen_dept_$sp](../../StoredProcedures/me_01/dbo.plu_regen_dept_$sp.md)
- [me_01: dbo.plu_regen_queue_$sp](../../StoredProcedures/me_01/dbo.plu_regen_queue_$sp.md)
- [me_01: dbo.plu_update_dept_$sp](../../StoredProcedures/me_01/dbo.plu_update_dept_$sp.md)
- [me_01: dbo.plu_update_item_dept_$sp](../../StoredProcedures/me_01/dbo.plu_update_item_dept_$sp.md)
- [me_01: dbo.reclass_hist_$sp](../../StoredProcedures/me_01/dbo.reclass_hist_$sp.md)
- [me_01: dbo.reclass_hist_oh_$sp](../../StoredProcedures/me_01/dbo.reclass_hist_oh_$sp.md)
- [me_01: dbo.retrieve_dist_$sp](../../StoredProcedures/me_01/dbo.retrieve_dist_$sp.md)
- [me_01: dbo.rpt_get_merch_group_code_mask_$sp](../../StoredProcedures/me_01/dbo.rpt_get_merch_group_code_mask_$sp.md)
- [me_01: dbo.rpt_get_pos_$sp](../../StoredProcedures/me_01/dbo.rpt_get_pos_$sp.md)
- [ma_01: dbo.dl_hist_group_vld_$sp](../../StoredProcedures/ma_01/dbo.dl_hist_group_vld_$sp.md)
- [ma_01: dbo.dl_hist_oh_group_vld_$sp](../../StoredProcedures/ma_01/dbo.dl_hist_oh_group_vld_$sp.md)
- [ma_01: dbo.nsb_style_analysis_$sp](../../StoredProcedures/ma_01/dbo.nsb_style_analysis_$sp.md)

