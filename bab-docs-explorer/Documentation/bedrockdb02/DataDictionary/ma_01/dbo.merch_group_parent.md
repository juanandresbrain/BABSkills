# dbo.merch_group_parent

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| hierarchy_level_id | int | 4 | 0 | YES |  |  |
| hierarchy_group_id | int | 4 | 0 | YES |  |  |
| parent_hierarchy_group_id | int | 4 | 0 | YES |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.c_location_eligibilty_rep_$sp](../../StoredProcedures/me_01/dbo.c_location_eligibilty_rep_$sp.md)
- [me_01: dbo.cum_val_hist_$sp](../../StoredProcedures/me_01/dbo.cum_val_hist_$sp.md)
- [me_01: dbo.cum_val_hist_lowest_loc_$sp](../../StoredProcedures/me_01/dbo.cum_val_hist_lowest_loc_$sp.md)
- [me_01: dbo.es_init_worktables_$sp](../../StoredProcedures/me_01/dbo.es_init_worktables_$sp.md)
- [me_01: dbo.es_reserve_$sp](../../StoredProcedures/me_01/dbo.es_reserve_$sp.md)
- [me_01: dbo.get_stock_ledger_cim_$sp](../../StoredProcedures/me_01/dbo.get_stock_ledger_cim_$sp.md)
- [me_01: dbo.get_stock_ledger_cim_lg_$sp](../../StoredProcedures/me_01/dbo.get_stock_ledger_cim_lg_$sp.md)
- [me_01: dbo.get_stock_ledger_rim_$sp](../../StoredProcedures/me_01/dbo.get_stock_ledger_rim_$sp.md)
- [me_01: dbo.ib_populate_notax_retails_$sp](../../StoredProcedures/me_01/dbo.ib_populate_notax_retails_$sp.md)
- [me_01: dbo.ib_populate_notax_retails_$sp_bak](../../StoredProcedures/me_01/dbo.ib_populate_notax_retails_$sp_bak.md)
- [me_01: dbo.ib_populate_notax_retails_$sp_modified_fast](../../StoredProcedures/me_01/dbo.ib_populate_notax_retails_$sp_modified_fast.md)
- [me_01: dbo.init_val_onhand_$sp](../../StoredProcedures/me_01/dbo.init_val_onhand_$sp.md)
- [me_01: dbo.init_val_onhand_deltemp_$sp](../../StoredProcedures/me_01/dbo.init_val_onhand_deltemp_$sp.md)
- [me_01: dbo.init_val_onhand_deltemp_ll_$sp](../../StoredProcedures/me_01/dbo.init_val_onhand_deltemp_ll_$sp.md)
- [me_01: dbo.init_val_onhand_lowestloc_$sp](../../StoredProcedures/me_01/dbo.init_val_onhand_lowestloc_$sp.md)
- [me_01: dbo.initvalccpergrpgrp_$sp](../../StoredProcedures/me_01/dbo.initvalccpergrpgrp_$sp.md)
- [me_01: dbo.initvalccpergrpgrpdel_$sp](../../StoredProcedures/me_01/dbo.initvalccpergrpgrpdel_$sp.md)
- [me_01: dbo.initvalccpergrploc_$sp](../../StoredProcedures/me_01/dbo.initvalccpergrploc_$sp.md)
- [me_01: dbo.initvalccpergrplocdel_$sp](../../StoredProcedures/me_01/dbo.initvalccpergrplocdel_$sp.md)
- [me_01: dbo.initvalccperlocgrp_$sp](../../StoredProcedures/me_01/dbo.initvalccperlocgrp_$sp.md)
- [me_01: dbo.initvalccperlocgrpdel_$sp](../../StoredProcedures/me_01/dbo.initvalccperlocgrpdel_$sp.md)
- [me_01: dbo.initvalccperlocloc_$sp](../../StoredProcedures/me_01/dbo.initvalccperlocloc_$sp.md)
- [me_01: dbo.initvalccperloclocdel_$sp](../../StoredProcedures/me_01/dbo.initvalccperloclocdel_$sp.md)
- [me_01: dbo.ins_missing_skus_depart_$sp](../../StoredProcedures/me_01/dbo.ins_missing_skus_depart_$sp.md)
- [me_01: dbo.ins_missing_skus_enterpr_$sp](../../StoredProcedures/me_01/dbo.ins_missing_skus_enterpr_$sp.md)
- [me_01: dbo.insert_packs_$sp](../../StoredProcedures/me_01/dbo.insert_packs_$sp.md)
- [me_01: dbo.insert_packs_bi_$sp](../../StoredProcedures/me_01/dbo.insert_packs_bi_$sp.md)
- [me_01: dbo.insert_pseudo_$sp](../../StoredProcedures/me_01/dbo.insert_pseudo_$sp.md)
- [me_01: dbo.insert_pseudo_bi_$sp](../../StoredProcedures/me_01/dbo.insert_pseudo_bi_$sp.md)
- [me_01: dbo.insert_pseudo_bi_ols_$sp](../../StoredProcedures/me_01/dbo.insert_pseudo_bi_ols_$sp.md)
- [me_01: dbo.insert_pseudo_ols_$sp](../../StoredProcedures/me_01/dbo.insert_pseudo_ols_$sp.md)
- [me_01: dbo.insert_skus_$sp](../../StoredProcedures/me_01/dbo.insert_skus_$sp.md)
- [me_01: dbo.insert_skus_bi_$sp](../../StoredProcedures/me_01/dbo.insert_skus_bi_$sp.md)
- [me_01: dbo.insert_skus_bi_ols_$sp](../../StoredProcedures/me_01/dbo.insert_skus_bi_ols_$sp.md)
- [me_01: dbo.insert_skus_ols_$sp](../../StoredProcedures/me_01/dbo.insert_skus_ols_$sp.md)
- [me_01: dbo.oo_populate_notax_retails_$sp](../../StoredProcedures/me_01/dbo.oo_populate_notax_retails_$sp.md)
- [me_01: dbo.pi_update_inventory_tables_$sp](../../StoredProcedures/me_01/dbo.pi_update_inventory_tables_$sp.md)
- [me_01: dbo.plu_common_style_$sp](../../StoredProcedures/me_01/dbo.plu_common_style_$sp.md)
- [me_01: dbo.plu_regen_style_$sp](../../StoredProcedures/me_01/dbo.plu_regen_style_$sp.md)
- [me_01: dbo.plu_update_item_style_$sp](../../StoredProcedures/me_01/dbo.plu_update_item_style_$sp.md)
- [me_01: dbo.pop_fixed_avg_cost_by_jurisdiction_$sp](../../StoredProcedures/me_01/dbo.pop_fixed_avg_cost_by_jurisdiction_$sp.md)
- [me_01: dbo.pop_fixed_avg_cost_for_pseudo_style_$sp](../../StoredProcedures/me_01/dbo.pop_fixed_avg_cost_for_pseudo_style_$sp.md)
- [me_01: dbo.populate_dynamic_average_cost_$sp](../../StoredProcedures/me_01/dbo.populate_dynamic_average_cost_$sp.md)
- [me_01: dbo.populate_fixed_average_cost_by_location_$sp](../../StoredProcedures/me_01/dbo.populate_fixed_average_cost_by_location_$sp.md)
- [me_01: dbo.rpt_get_pos_$sp](../../StoredProcedures/me_01/dbo.rpt_get_pos_$sp.md)
- [DBAUtility: dbo.spDM_MaintainProducts](../../StoredProcedures/DBAUtility/dbo.spDM_MaintainProducts.md)
- [ma_01: dbo.nsb_core_chain_$sp](../../StoredProcedures/ma_01/dbo.nsb_core_chain_$sp.md)
- [ma_01: dbo.nsb_core_location_$sp](../../StoredProcedures/ma_01/dbo.nsb_core_location_$sp.md)
- [ma_01: dbo.nsb_mar_chain_md_$sp](../../StoredProcedures/ma_01/dbo.nsb_mar_chain_md_$sp.md)
- [ma_01: dbo.nsb_mar_location_md_$sp](../../StoredProcedures/ma_01/dbo.nsb_mar_location_md_$sp.md)
- [ma_01: dbo.nsb_otb_chain_$sp](../../StoredProcedures/ma_01/dbo.nsb_otb_chain_$sp.md)
- [ma_01: dbo.nsb_otb_location_$sp](../../StoredProcedures/ma_01/dbo.nsb_otb_location_$sp.md)
- [ma_01: dbo.nsb_par_chain_$sp](../../StoredProcedures/ma_01/dbo.nsb_par_chain_$sp.md)
- [ma_01: dbo.nsb_par_chain_rim_$sp](../../StoredProcedures/ma_01/dbo.nsb_par_chain_rim_$sp.md)
- [ma_01: dbo.nsb_par_location_$sp](../../StoredProcedures/ma_01/dbo.nsb_par_location_$sp.md)
- [ma_01: dbo.rpt_otb_cost_retail_$sp](../../StoredProcedures/ma_01/dbo.rpt_otb_cost_retail_$sp.md)

