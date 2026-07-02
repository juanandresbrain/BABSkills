# dbo.jurisdiction

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| jurisdiction_id | smallint | 2 | 0 | YES |  |  |
| jurisdiction_code | nvarchar | 40 | 0 |  |  |  |
| jurisdiction_description | nvarchar | 100 | 0 |  |  |  |
| jurisdiction_type | tinyint | 1 | 0 |  |  |  |
| tax_registration_number1 | nvarchar | 40 | 1 |  |  |  |
| tax_registration_number2 | nvarchar | 40 | 1 |  |  |  |
| country_id | decimal | 9 | 0 |  |  |  |
| pricing_rule_id | decimal | 9 | 1 |  |  |  |
| jurisdiction_equivalency_rate | decimal | 5 | 1 |  |  |  |
| rate_last_modified | smalldatetime | 4 | 1 |  |  |  |
| home_jurisdiction_flag | bit | 1 | 0 |  |  |  |
| default_src_jurisdiction_flag | bit | 1 | 0 |  |  |  |
| availability_status | smallint | 2 | 0 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.balance_cost_factors_$sp](../../StoredProcedures/me_01/dbo.balance_cost_factors_$sp.md)
- [me_01: dbo.cum_val_hist_$sp](../../StoredProcedures/me_01/dbo.cum_val_hist_$sp.md)
- [me_01: dbo.dl_style_task_validate_$sp](../../StoredProcedures/me_01/dbo.dl_style_task_validate_$sp.md)
- [me_01: dbo.get_cost_rate_$sp](../../StoredProcedures/me_01/dbo.get_cost_rate_$sp.md)
- [me_01: dbo.get_pc_instruction_price_history_$sp](../../StoredProcedures/me_01/dbo.get_pc_instruction_price_history_$sp.md)
- [me_01: dbo.get_pc_instruction_values_$sp](../../StoredProcedures/me_01/dbo.get_pc_instruction_values_$sp.md)
- [me_01: dbo.get_pc_totals_$sp](../../StoredProcedures/me_01/dbo.get_pc_totals_$sp.md)
- [me_01: dbo.get_price_change_details_$sp](../../StoredProcedures/me_01/dbo.get_price_change_details_$sp.md)
- [me_01: dbo.get_price_change_details_pricing_level_$sp](../../StoredProcedures/me_01/dbo.get_price_change_details_pricing_level_$sp.md)
- [me_01: dbo.get_retails_MA_$sp](../../StoredProcedures/me_01/dbo.get_retails_MA_$sp.md)
- [me_01: dbo.import_asn_eighth_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_eighth_step_$sp.md)
- [me_01: dbo.import_asn_forth_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_forth_step_$sp.md)
- [me_01: dbo.import_pc_batch_tickets_$sp](../../StoredProcedures/me_01/dbo.import_pc_batch_tickets_$sp.md)
- [me_01: dbo.import_pc_populate_temp_pc_$sp](../../StoredProcedures/me_01/dbo.import_pc_populate_temp_pc_$sp.md)
- [me_01: dbo.import_pc_populate_temp_pc_from_ib_$sp](../../StoredProcedures/me_01/dbo.import_pc_populate_temp_pc_from_ib_$sp.md)
- [me_01: dbo.import_pc_validate_$sp](../../StoredProcedures/me_01/dbo.import_pc_validate_$sp.md)
- [me_01: dbo.imw_price_change_v1_$sp](../../StoredProcedures/me_01/dbo.imw_price_change_v1_$sp.md)
- [me_01: dbo.insert_packs_bi_$sp](../../StoredProcedures/me_01/dbo.insert_packs_bi_$sp.md)
- [me_01: dbo.insert_pseudo_$sp](../../StoredProcedures/me_01/dbo.insert_pseudo_$sp.md)
- [me_01: dbo.insert_pseudo_bi_$sp](../../StoredProcedures/me_01/dbo.insert_pseudo_bi_$sp.md)
- [me_01: dbo.insert_pseudo_bi_ols_$sp](../../StoredProcedures/me_01/dbo.insert_pseudo_bi_ols_$sp.md)
- [me_01: dbo.insert_pseudo_ols_$sp](../../StoredProcedures/me_01/dbo.insert_pseudo_ols_$sp.md)
- [me_01: dbo.insert_skus_$sp](../../StoredProcedures/me_01/dbo.insert_skus_$sp.md)
- [me_01: dbo.insert_skus_bi_$sp](../../StoredProcedures/me_01/dbo.insert_skus_bi_$sp.md)
- [me_01: dbo.insert_skus_bi_ols_$sp](../../StoredProcedures/me_01/dbo.insert_skus_bi_ols_$sp.md)
- [me_01: dbo.insert_skus_ols_$sp](../../StoredProcedures/me_01/dbo.insert_skus_ols_$sp.md)
- [me_01: dbo.no_wms_create_ss_$sp](../../StoredProcedures/me_01/dbo.no_wms_create_ss_$sp.md)
- [me_01: dbo.pcm_get_tickets_$sp](../../StoredProcedures/me_01/dbo.pcm_get_tickets_$sp.md)
- [me_01: dbo.pi_move_store_count_$sp](../../StoredProcedures/me_01/dbo.pi_move_store_count_$sp.md)
- [me_01: dbo.pi_update_inventory_tables_$sp](../../StoredProcedures/me_01/dbo.pi_update_inventory_tables_$sp.md)
- [me_01: dbo.pop_25nov25_temp_sale_master_$sp](../../StoredProcedures/me_01/dbo.pop_25nov25_temp_sale_master_$sp.md)
- [me_01: dbo.populate_dynamic_average_cost_$sp](../../StoredProcedures/me_01/dbo.populate_dynamic_average_cost_$sp.md)
- [me_01: dbo.populate_ib_cfd_$sp](../../StoredProcedures/me_01/dbo.populate_ib_cfd_$sp.md)
- [me_01: dbo.populate_ib_cost_retail_$sp](../../StoredProcedures/me_01/dbo.populate_ib_cost_retail_$sp.md)
- [me_01: dbo.populate_multi_currency_location_$sp](../../StoredProcedures/me_01/dbo.populate_multi_currency_location_$sp.md)
- [me_01: dbo.populate_temp_sale_master_$sp](../../StoredProcedures/me_01/dbo.populate_temp_sale_master_$sp.md)
- [me_01: dbo.prep_fixed_avg_cost_calculation_$sp](../../StoredProcedures/me_01/dbo.prep_fixed_avg_cost_calculation_$sp.md)
- [me_01: dbo.process_modified_transactions_$sp](../../StoredProcedures/me_01/dbo.process_modified_transactions_$sp.md)
- [me_01: dbo.rpt_get_lookup_home_currency_$sp](../../StoredProcedures/me_01/dbo.rpt_get_lookup_home_currency_$sp.md)
- [me_01: dbo.rpt_get_lookup_jurisdiction_currency_$sp](../../StoredProcedures/me_01/dbo.rpt_get_lookup_jurisdiction_currency_$sp.md)
- [me_01: dbo.rpt_get_po_receipt_$sp](../../StoredProcedures/me_01/dbo.rpt_get_po_receipt_$sp.md)
- [me_01: dbo.rpt_get_pos_BABW_$sp](../../StoredProcedures/me_01/dbo.rpt_get_pos_BABW_$sp.md)
- [me_01: dbo.rpt_get_pos_BABW_$sp_01042018](../../StoredProcedures/me_01/dbo.rpt_get_pos_BABW_$sp_01042018.md)
- [me_01: dbo.rpt_get_pos_BABW_$sp_BAK_02272018](../../StoredProcedures/me_01/dbo.rpt_get_pos_BABW_$sp_BAK_02272018.md)
- [me_01: dbo.sales_balancing_c$sp](../../StoredProcedures/me_01/dbo.sales_balancing_c$sp.md)
- [me_01: dbo.sales_balancing_l$sp](../../StoredProcedures/me_01/dbo.sales_balancing_l$sp.md)
- [me_01: dbo.spDW_CurrentRetail](../../StoredProcedures/me_01/dbo.spDW_CurrentRetail.md)
- [me_01: dbo.spDW_DoorCount](../../StoredProcedures/me_01/dbo.spDW_DoorCount.md)
- [me_01: dbo.spHearMeSalesConversion](../../StoredProcedures/me_01/dbo.spHearMeSalesConversion.md)
- [me_01: dbo.spHearMeSalesConversion_bak_01282020LT](../../StoredProcedures/me_01/dbo.spHearMeSalesConversion_bak_01282020LT.md)
- [me_01: dbo.spHearMeSalesConversion_BJB20190326](../../StoredProcedures/me_01/dbo.spHearMeSalesConversion_BJB20190326.md)
- [me_01: dbo.spMerchandisingRoyaltyReports](../../StoredProcedures/me_01/dbo.spMerchandisingRoyaltyReports.md)
- [me_01: dbo.spMerchandisingSelectStoreDistribution_UK_CN](../../StoredProcedures/me_01/dbo.spMerchandisingSelectStoreDistribution_UK_CN.md)
- [me_01: dbo.spMerchandisingSelectStoreDistribution_UK_CNBAK20220406](../../StoredProcedures/me_01/dbo.spMerchandisingSelectStoreDistribution_UK_CNBAK20220406.md)
- [me_01: dbo.spMerchandisingSelectStoreDistribution_UK_CNWIP20220406](../../StoredProcedures/me_01/dbo.spMerchandisingSelectStoreDistribution_UK_CNWIP20220406.md)
- [me_01: dbo.spMerchandisingSelectStoreDistributions](../../StoredProcedures/me_01/dbo.spMerchandisingSelectStoreDistributions.md)
- [me_01: dbo.spMerchandisingSelectStoreDistributionsBAK20220406](../../StoredProcedures/me_01/dbo.spMerchandisingSelectStoreDistributionsBAK20220406.md)
- [me_01: dbo.spMerchandisingSelectStoreDistributionsWIP20220406](../../StoredProcedures/me_01/dbo.spMerchandisingSelectStoreDistributionsWIP20220406.md)
- [me_01: dbo.spMerchandisingSplitReport_ALL_WHSE](../../StoredProcedures/me_01/dbo.spMerchandisingSplitReport_ALL_WHSE.md)
- [me_01: dbo.spMerchandisingSplitReport_BHSE](../../StoredProcedures/me_01/dbo.spMerchandisingSplitReport_BHSE.md)
- [me_01: dbo.spMerchandisingSplitReport_UK](../../StoredProcedures/me_01/dbo.spMerchandisingSplitReport_UK.md)
- [me_01: dbo.spMerchandisingSplitReport_WC](../../StoredProcedures/me_01/dbo.spMerchandisingSplitReport_WC.md)
- [me_01: dbo.spPOSPricebookStage](../../StoredProcedures/me_01/dbo.spPOSPricebookStage.md)
- [me_01: dbo.spPOSPricebookStage_BAK20231101](../../StoredProcedures/me_01/dbo.spPOSPricebookStage_BAK20231101.md)
- [me_01: dbo.spPOSPricebookStageUpdatedWIP](../../StoredProcedures/me_01/dbo.spPOSPricebookStageUpdatedWIP.md)
- [me_01: dbo.spWEBPricebookStage](../../StoredProcedures/me_01/dbo.spWEBPricebookStage.md)
- [me_01: dbo.spWEBPricebookStage_Bak20220705](../../StoredProcedures/me_01/dbo.spWEBPricebookStage_Bak20220705.md)
- [me_01: dbo.spWEBPricebookStage_TCOnDemand](../../StoredProcedures/me_01/dbo.spWEBPricebookStage_TCOnDemand.md)
- [me_01: dbo.startup_sl_history_$sp](../../StoredProcedures/me_01/dbo.startup_sl_history_$sp.md)
- [me_01: dbo.upd_pc_generate_tickets_$sp](../../StoredProcedures/me_01/dbo.upd_pc_generate_tickets_$sp.md)
- [me_01: dbo.upd_style_retails_pc_$sp](../../StoredProcedures/me_01/dbo.upd_style_retails_pc_$sp.md)
- [me_01: dbo.validate_pc_generate_tickets_details_$sp](../../StoredProcedures/me_01/dbo.validate_pc_generate_tickets_details_$sp.md)
- [master: dbo.c_stp_print_tickets_$sp](../../StoredProcedures/master/dbo.c_stp_print_tickets_$sp.md)
- [DBAUtility: dbo.spDM_MaintainProducts](../../StoredProcedures/DBAUtility/dbo.spDM_MaintainProducts.md)
- [DBAUtility: dbo.spPLM_GetMerchandingData](../../StoredProcedures/DBAUtility/dbo.spPLM_GetMerchandingData.md)
- [DBAUtility: dbo.spPLM_GetMerchandingData_dev](../../StoredProcedures/DBAUtility/dbo.spPLM_GetMerchandingData_dev.md)
- [ma_01: dbo.post_oo_unc_$sp](../../StoredProcedures/ma_01/dbo.post_oo_unc_$sp.md)
- [ma_01: dbo.spDW_Inventory](../../StoredProcedures/ma_01/dbo.spDW_Inventory.md)
- [ma_01: dbo.spDW_TopStyleTy](../../StoredProcedures/ma_01/dbo.spDW_TopStyleTy.md)
- [ma_01: dbo.spDW_TopStyleTyBACKUP20180108](../../StoredProcedures/ma_01/dbo.spDW_TopStyleTyBACKUP20180108.md)
- [ma_01: dbo.spTimCTopStyleTesting](../../StoredProcedures/ma_01/dbo.spTimCTopStyleTesting.md)
- [ma_01: dbo.startup_flsh_group_loc_da_$sp](../../StoredProcedures/ma_01/dbo.startup_flsh_group_loc_da_$sp.md)
- [ma_01: dbo.startup_flsh_loc_da_$sp](../../StoredProcedures/ma_01/dbo.startup_flsh_loc_da_$sp.md)
- [ma_01: dbo.startup_flsh_style_loc_da_$sp](../../StoredProcedures/ma_01/dbo.startup_flsh_style_loc_da_$sp.md)

