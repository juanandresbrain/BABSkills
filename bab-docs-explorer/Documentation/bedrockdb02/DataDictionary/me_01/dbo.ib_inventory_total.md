# dbo.ib_inventory_total

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| sku_id | decimal | 9 | 0 | YES |  |  |
| location_id | smallint | 2 | 0 | YES |  |  |
| inventory_status_id | smallint | 2 | 0 | YES |  |  |
| price_status_id | smallint | 2 | 0 |  |  |  |
| total_on_hand_units | int | 4 | 0 |  |  |  |
| total_on_hand_cost | decimal | 9 | 0 |  |  |  |
| total_on_hand_valuation_retail | decimal | 9 | 0 |  |  |  |
| total_on_hand_selling_retail | decimal | 9 | 0 |  |  |  |
| update_guid | uniqueidentifier | 16 | 0 |  |  |  |
| total_on_hand_cost_local | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.adjust_future_reserve_$sp](../../StoredProcedures/me_01/dbo.adjust_future_reserve_$sp.md)
- [me_01: dbo.adjust_reserve_remnant_cost_$sp](../../StoredProcedures/me_01/dbo.adjust_reserve_remnant_cost_$sp.md)
- [me_01: dbo.copy_location_prices_validation_$sp](../../StoredProcedures/me_01/dbo.copy_location_prices_validation_$sp.md)
- [me_01: dbo.eom_complete_$sp](../../StoredProcedures/me_01/dbo.eom_complete_$sp.md)
- [me_01: dbo.eom_reserve_$sp](../../StoredProcedures/me_01/dbo.eom_reserve_$sp.md)
- [me_01: dbo.es_reserve_$sp](../../StoredProcedures/me_01/dbo.es_reserve_$sp.md)
- [me_01: dbo.get_avg_cost_sku_chain_$sp](../../StoredProcedures/me_01/dbo.get_avg_cost_sku_chain_$sp.md)
- [me_01: dbo.get_avg_cost_sku_jurisdiction_$sp](../../StoredProcedures/me_01/dbo.get_avg_cost_sku_jurisdiction_$sp.md)
- [me_01: dbo.get_avg_cost_sku_location_$sp](../../StoredProcedures/me_01/dbo.get_avg_cost_sku_location_$sp.md)
- [me_01: dbo.get_avg_cost_style_chain_$sp](../../StoredProcedures/me_01/dbo.get_avg_cost_style_chain_$sp.md)
- [me_01: dbo.get_avg_cost_style_jurisdiction_$sp](../../StoredProcedures/me_01/dbo.get_avg_cost_style_jurisdiction_$sp.md)
- [me_01: dbo.get_avg_cost_style_location_$sp](../../StoredProcedures/me_01/dbo.get_avg_cost_style_location_$sp.md)
- [me_01: dbo.get_imrd_oh_orig_retail_$sp](../../StoredProcedures/me_01/dbo.get_imrd_oh_orig_retail_$sp.md)
- [me_01: dbo.get_pc_instruction_values_$sp](../../StoredProcedures/me_01/dbo.get_pc_instruction_values_$sp.md)
- [me_01: dbo.get_price_change_details_$sp](../../StoredProcedures/me_01/dbo.get_price_change_details_$sp.md)
- [me_01: dbo.import_asn_third_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_third_step_$sp.md)
- [me_01: dbo.import_pc_populate_temp_pc_from_ib_$sp](../../StoredProcedures/me_01/dbo.import_pc_populate_temp_pc_from_ib_$sp.md)
- [me_01: dbo.imw_price_change_v1_$sp](../../StoredProcedures/me_01/dbo.imw_price_change_v1_$sp.md)
- [me_01: dbo.ins_ib_inventory_perm_pc_effective_$sp](../../StoredProcedures/me_01/dbo.ins_ib_inventory_perm_pc_effective_$sp.md)
- [me_01: dbo.ins_missing_skus_depart_$sp](../../StoredProcedures/me_01/dbo.ins_missing_skus_depart_$sp.md)
- [me_01: dbo.ins_missing_skus_enterpr_$sp](../../StoredProcedures/me_01/dbo.ins_missing_skus_enterpr_$sp.md)
- [me_01: dbo.ins_missing_skus_style_$sp](../../StoredProcedures/me_01/dbo.ins_missing_skus_style_$sp.md)
- [me_01: dbo.insert_pseudo_$sp](../../StoredProcedures/me_01/dbo.insert_pseudo_$sp.md)
- [me_01: dbo.insert_pseudo_ols_$sp](../../StoredProcedures/me_01/dbo.insert_pseudo_ols_$sp.md)
- [me_01: dbo.insert_skus_$sp](../../StoredProcedures/me_01/dbo.insert_skus_$sp.md)
- [me_01: dbo.insert_skus_ols_$sp](../../StoredProcedures/me_01/dbo.insert_skus_ols_$sp.md)
- [me_01: dbo.inventory_update_$sp](../../StoredProcedures/me_01/dbo.inventory_update_$sp.md)
- [me_01: dbo.inventory_update2_$sp](../../StoredProcedures/me_01/dbo.inventory_update2_$sp.md)
- [me_01: dbo.iv_filter_forecasting_styles_$sp](../../StoredProcedures/me_01/dbo.iv_filter_forecasting_styles_$sp.md)
- [me_01: dbo.pc_calc_total_au_jur_$sp](../../StoredProcedures/me_01/dbo.pc_calc_total_au_jur_$sp.md)
- [me_01: dbo.pc_calc_total_au_loc_list_$sp](../../StoredProcedures/me_01/dbo.pc_calc_total_au_loc_list_$sp.md)
- [me_01: dbo.pc_calc_total_au_pg_list_$sp](../../StoredProcedures/me_01/dbo.pc_calc_total_au_pg_list_$sp.md)
- [me_01: dbo.pi_freeze_on_hand_loc_$sp](../../StoredProcedures/me_01/dbo.pi_freeze_on_hand_loc_$sp.md)
- [me_01: dbo.pop_fixed_avg_cost_by_jurisdiction_$sp](../../StoredProcedures/me_01/dbo.pop_fixed_avg_cost_by_jurisdiction_$sp.md)
- [me_01: dbo.pop_fixed_avg_cost_for_pseudo_style_$sp](../../StoredProcedures/me_01/dbo.pop_fixed_avg_cost_for_pseudo_style_$sp.md)
- [me_01: dbo.populate_dynamic_average_cost_$sp](../../StoredProcedures/me_01/dbo.populate_dynamic_average_cost_$sp.md)
- [me_01: dbo.populate_fixed_average_cost_by_location_$sp](../../StoredProcedures/me_01/dbo.populate_fixed_average_cost_by_location_$sp.md)
- [me_01: dbo.post_inventory_loc_$sp](../../StoredProcedures/me_01/dbo.post_inventory_loc_$sp.md)
- [me_01: dbo.post_pending_loc_$sp](../../StoredProcedures/me_01/dbo.post_pending_loc_$sp.md)
- [me_01: dbo.post_sales_batch_$sp](../../StoredProcedures/me_01/dbo.post_sales_batch_$sp.md)
- [me_01: dbo.process_modified_transactions_$sp](../../StoredProcedures/me_01/dbo.process_modified_transactions_$sp.md)
- [me_01: dbo.reclass_hist_oh_$sp](../../StoredProcedures/me_01/dbo.reclass_hist_oh_$sp.md)
- [me_01: dbo.sp_smartlook_WH_AVAILABLE_OH_RPT](../../StoredProcedures/me_01/dbo.sp_smartlook_WH_AVAILABLE_OH_RPT.md)
- [me_01: dbo.sp_smartlook_WH_AVAILABLE_OH_RPT_S](../../StoredProcedures/me_01/dbo.sp_smartlook_WH_AVAILABLE_OH_RPT_S.md)
- [me_01: dbo.sp_smartlook_WH_AVAILABLE_OH_RPT_W](../../StoredProcedures/me_01/dbo.sp_smartlook_WH_AVAILABLE_OH_RPT_W.md)
- [me_01: dbo.sp_smartlook_WH_AVAILABLE_OH_RPT_W2](../../StoredProcedures/me_01/dbo.sp_smartlook_WH_AVAILABLE_OH_RPT_W2.md)
- [me_01: dbo.spBABW_getGooglePriceQuantityData](../../StoredProcedures/me_01/dbo.spBABW_getGooglePriceQuantityData.md)
- [me_01: dbo.spBABW_getGoogleProductFeedData](../../StoredProcedures/me_01/dbo.spBABW_getGoogleProductFeedData.md)
- [me_01: dbo.spHearMeSalesConversion](../../StoredProcedures/me_01/dbo.spHearMeSalesConversion.md)
- [me_01: dbo.spHearMeSalesConversion_bak_01282020LT](../../StoredProcedures/me_01/dbo.spHearMeSalesConversion_bak_01282020LT.md)
- [me_01: dbo.spHearMeSalesConversion_BJB20190326](../../StoredProcedures/me_01/dbo.spHearMeSalesConversion_BJB20190326.md)
- [me_01: dbo.spMerchandising_980NightlySync_OnDemand](../../StoredProcedures/me_01/dbo.spMerchandising_980NightlySync_OnDemand.md)
- [me_01: dbo.spMerchandising_WEB_NightlySync_OnDemand](../../StoredProcedures/me_01/dbo.spMerchandising_WEB_NightlySync_OnDemand.md)
- [me_01: dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerification](../../StoredProcedures/me_01/dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerification.md)
- [me_01: dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJC2](../../StoredProcedures/me_01/dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJC2.md)
- [me_01: dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJC2V2](../../StoredProcedures/me_01/dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJC2V2.md)
- [me_01: dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJCtest](../../StoredProcedures/me_01/dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJCtest.md)
- [me_01: dbo.spMerchandisingReportWMLockedVsMerchLocation1000](../../StoredProcedures/me_01/dbo.spMerchandisingReportWMLockedVsMerchLocation1000.md)
- [me_01: dbo.spMerchandisingReportWMLockedVsMerchLocation1000_Backup_03_01_2017](../../StoredProcedures/me_01/dbo.spMerchandisingReportWMLockedVsMerchLocation1000_Backup_03_01_2017.md)
- [me_01: dbo.spMerchandisingReportWMLockedVsMerchLocation1000_Backup_08_14_2017](../../StoredProcedures/me_01/dbo.spMerchandisingReportWMLockedVsMerchLocation1000_Backup_08_14_2017.md)
- [me_01: dbo.spMerchandisingSelectMismatchedStdPackQty](../../StoredProcedures/me_01/dbo.spMerchandisingSelectMismatchedStdPackQty.md)
- [me_01: dbo.spMerchandisingSelectNonWhseInventoryShrink](../../StoredProcedures/me_01/dbo.spMerchandisingSelectNonWhseInventoryShrink.md)
- [me_01: dbo.spMerchandisingSelectNonWhseInventoryShrink_BAK20230829](../../StoredProcedures/me_01/dbo.spMerchandisingSelectNonWhseInventoryShrink_BAK20230829.md)
- [me_01: dbo.spMerchandisingSelectWhseInventoryShrink](../../StoredProcedures/me_01/dbo.spMerchandisingSelectWhseInventoryShrink.md)
- [me_01: dbo.spMerchandisingSelectWhseInventoryShrink_Bak20210614](../../StoredProcedures/me_01/dbo.spMerchandisingSelectWhseInventoryShrink_Bak20210614.md)
- [me_01: dbo.spMerchandisingSelectWhseInventoryShrink_BAK20230829](../../StoredProcedures/me_01/dbo.spMerchandisingSelectWhseInventoryShrink_BAK20230829.md)
- [me_01: dbo.spMerchandisingSelectWhseInventoryShrink_Bak20231219](../../StoredProcedures/me_01/dbo.spMerchandisingSelectWhseInventoryShrink_Bak20231219.md)
- [me_01: dbo.spMerchandisingSelectWhseInventoryShrink_manual](../../StoredProcedures/me_01/dbo.spMerchandisingSelectWhseInventoryShrink_manual.md)
- [me_01: dbo.spMerchandisingSelectWhseInventoryShrinkBAK20220801](../../StoredProcedures/me_01/dbo.spMerchandisingSelectWhseInventoryShrinkBAK20220801.md)
- [me_01: dbo.spPartyManager_ActiveDistro](../../StoredProcedures/me_01/dbo.spPartyManager_ActiveDistro.md)
- [me_01: dbo.spUKAvailSupplies](../../StoredProcedures/me_01/dbo.spUKAvailSupplies.md)
- [me_01: dbo.startup_discrepancy_ib_inv_$sp](../../StoredProcedures/me_01/dbo.startup_discrepancy_ib_inv_$sp.md)
- [me_01: dbo.startup_ib_inventory_$sp](../../StoredProcedures/me_01/dbo.startup_ib_inventory_$sp.md)
- [me_01: dbo.startup_ib_inventory_total_$sp](../../StoredProcedures/me_01/dbo.startup_ib_inventory_total_$sp.md)
- [master: dbo.c_stp_print_tickets_$sp](../../StoredProcedures/master/dbo.c_stp_print_tickets_$sp.md)

