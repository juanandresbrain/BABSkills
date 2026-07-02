# dbo.hierarchy_level

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| hierarchy_level_id | int | 4 | 0 | YES |  |  |
| hierarchy_level_label | nvarchar | 60 | 0 |  |  |  |
| hierarchy_id | decimal | 9 | 0 |  |  |  |
| parent_level_id | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.c_location_eligibilty_rep_$sp](../../StoredProcedures/me_01/dbo.c_location_eligibilty_rep_$sp.md)
- [me_01: dbo.cum_val_hist_$sp](../../StoredProcedures/me_01/dbo.cum_val_hist_$sp.md)
- [me_01: dbo.dl_style_task_validate_$sp](../../StoredProcedures/me_01/dbo.dl_style_task_validate_$sp.md)
- [me_01: dbo.get_stock_ledger_cim_$sp](../../StoredProcedures/me_01/dbo.get_stock_ledger_cim_$sp.md)
- [me_01: dbo.get_stock_ledger_cim_lg_$sp](../../StoredProcedures/me_01/dbo.get_stock_ledger_cim_lg_$sp.md)
- [me_01: dbo.get_stock_ledger_rim_$sp](../../StoredProcedures/me_01/dbo.get_stock_ledger_rim_$sp.md)
- [me_01: dbo.pi_update_inventory_tables_$sp](../../StoredProcedures/me_01/dbo.pi_update_inventory_tables_$sp.md)
- [me_01: dbo.plu_hg_regen_queue_$sp](../../StoredProcedures/me_01/dbo.plu_hg_regen_queue_$sp.md)
- [me_01: dbo.plu_regen_queue_$sp](../../StoredProcedures/me_01/dbo.plu_regen_queue_$sp.md)
- [me_01: dbo.retrieve_dist_$sp](../../StoredProcedures/me_01/dbo.retrieve_dist_$sp.md)
- [me_01: dbo.rpt_get_merch_group_code_mask_$sp](../../StoredProcedures/me_01/dbo.rpt_get_merch_group_code_mask_$sp.md)
- [me_01: dbo.spMerchandisingInsertMinMaxProfileArchive](../../StoredProcedures/me_01/dbo.spMerchandisingInsertMinMaxProfileArchive.md)
- [ma_01: dbo.dl_hist_group_vld_$sp](../../StoredProcedures/ma_01/dbo.dl_hist_group_vld_$sp.md)
- [ma_01: dbo.dl_hist_oh_group_vld_$sp](../../StoredProcedures/ma_01/dbo.dl_hist_oh_group_vld_$sp.md)
- [ma_01: dbo.nsb_core_chain_$sp](../../StoredProcedures/ma_01/dbo.nsb_core_chain_$sp.md)
- [ma_01: dbo.nsb_core_location_$sp](../../StoredProcedures/ma_01/dbo.nsb_core_location_$sp.md)
- [ma_01: dbo.nsb_mar_chain_md_$sp](../../StoredProcedures/ma_01/dbo.nsb_mar_chain_md_$sp.md)
- [ma_01: dbo.nsb_mar_location_md_$sp](../../StoredProcedures/ma_01/dbo.nsb_mar_location_md_$sp.md)
- [ma_01: dbo.nsb_otb_chain_$sp](../../StoredProcedures/ma_01/dbo.nsb_otb_chain_$sp.md)
- [ma_01: dbo.nsb_otb_location_$sp](../../StoredProcedures/ma_01/dbo.nsb_otb_location_$sp.md)
- [ma_01: dbo.nsb_par_chain_$sp](../../StoredProcedures/ma_01/dbo.nsb_par_chain_$sp.md)
- [ma_01: dbo.nsb_par_chain_rim_$sp](../../StoredProcedures/ma_01/dbo.nsb_par_chain_rim_$sp.md)
- [ma_01: dbo.nsb_par_location_$sp](../../StoredProcedures/ma_01/dbo.nsb_par_location_$sp.md)
- [ma_01: dbo.nsb_style_analysis_$sp](../../StoredProcedures/ma_01/dbo.nsb_style_analysis_$sp.md)
- [ma_01: dbo.nsb_vendor_analysis_$sp](../../StoredProcedures/ma_01/dbo.nsb_vendor_analysis_$sp.md)
- [ma_01: dbo.rpt_otb_chain_$sp](../../StoredProcedures/ma_01/dbo.rpt_otb_chain_$sp.md)
- [ma_01: dbo.rpt_otb_location_$sp](../../StoredProcedures/ma_01/dbo.rpt_otb_location_$sp.md)
- [ma_01: dbo.rpt_vendor_analysis_$sp](../../StoredProcedures/ma_01/dbo.rpt_vendor_analysis_$sp.md)

