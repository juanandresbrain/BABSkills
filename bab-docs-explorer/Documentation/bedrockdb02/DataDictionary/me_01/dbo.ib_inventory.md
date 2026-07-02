# dbo.ib_inventory

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ib_inventory_id | decimal | 9 | 0 | YES |  |  |
| sku_id | decimal | 9 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
| price_status_id | smallint | 2 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| transaction_type_code | smallint | 2 | 0 |  |  |  |
| inventory_status_id | smallint | 2 | 0 |  |  |  |
| other_location_id | smallint | 2 | 1 |  |  |  |
| transaction_reason_id | smallint | 2 | 1 |  |  |  |
| document_number | nvarchar | 40 | 1 |  |  |  |
| transaction_units | int | 4 | 0 |  |  |  |
| transaction_cost | decimal | 9 | 0 |  |  |  |
| transaction_valuation_retail | decimal | 9 | 0 |  |  |  |
| transaction_selling_retail | decimal | 9 | 0 |  |  |  |
| price_change_type | smallint | 2 | 1 |  |  |  |
| units_affected | int | 4 | 1 |  |  |  |
| transaction_cost_local | decimal | 9 | 1 |  |  |  |
| updated_flag | bit | 1 | 1 |  |  |  |
| transaction_no | int | 4 | 1 |  |  |  |
| batch_no | int | 4 | 1 |  |  |  |
| register_no | smallint | 2 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.adjust_future_reserve_$sp](../../StoredProcedures/me_01/dbo.adjust_future_reserve_$sp.md)
- [me_01: dbo.adjust_reserve_remnant_cost_$sp](../../StoredProcedures/me_01/dbo.adjust_reserve_remnant_cost_$sp.md)
- [me_01: dbo.eom_complete_$sp](../../StoredProcedures/me_01/dbo.eom_complete_$sp.md)
- [me_01: dbo.eom_reserve_$sp](../../StoredProcedures/me_01/dbo.eom_reserve_$sp.md)
- [me_01: dbo.es_reserve_$sp](../../StoredProcedures/me_01/dbo.es_reserve_$sp.md)
- [me_01: dbo.get_avg_cost_sku_chain_$sp](../../StoredProcedures/me_01/dbo.get_avg_cost_sku_chain_$sp.md)
- [me_01: dbo.get_avg_cost_sku_jurisdiction_$sp](../../StoredProcedures/me_01/dbo.get_avg_cost_sku_jurisdiction_$sp.md)
- [me_01: dbo.get_avg_cost_sku_location_$sp](../../StoredProcedures/me_01/dbo.get_avg_cost_sku_location_$sp.md)
- [me_01: dbo.get_avg_cost_style_chain_$sp](../../StoredProcedures/me_01/dbo.get_avg_cost_style_chain_$sp.md)
- [me_01: dbo.get_avg_cost_style_jurisdiction_$sp](../../StoredProcedures/me_01/dbo.get_avg_cost_style_jurisdiction_$sp.md)
- [me_01: dbo.get_avg_cost_style_location_$sp](../../StoredProcedures/me_01/dbo.get_avg_cost_style_location_$sp.md)
- [me_01: dbo.ib_populate_notax_retails_$sp](../../StoredProcedures/me_01/dbo.ib_populate_notax_retails_$sp.md)
- [me_01: dbo.ib_populate_notax_retails_$sp_bak](../../StoredProcedures/me_01/dbo.ib_populate_notax_retails_$sp_bak.md)
- [me_01: dbo.ib_populate_notax_retails_$sp_modified_fast](../../StoredProcedures/me_01/dbo.ib_populate_notax_retails_$sp_modified_fast.md)
- [me_01: dbo.import_asn_third_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_third_step_$sp.md)
- [me_01: dbo.ins_ib_inventory_perm_pc_effective_$sp](../../StoredProcedures/me_01/dbo.ins_ib_inventory_perm_pc_effective_$sp.md)
- [me_01: dbo.insert_pseudo_$sp](../../StoredProcedures/me_01/dbo.insert_pseudo_$sp.md)
- [me_01: dbo.insert_pseudo_ols_$sp](../../StoredProcedures/me_01/dbo.insert_pseudo_ols_$sp.md)
- [me_01: dbo.insert_skus_$sp](../../StoredProcedures/me_01/dbo.insert_skus_$sp.md)
- [me_01: dbo.insert_skus_ols_$sp](../../StoredProcedures/me_01/dbo.insert_skus_ols_$sp.md)
- [me_01: dbo.inventory_update_$sp](../../StoredProcedures/me_01/dbo.inventory_update_$sp.md)
- [me_01: dbo.inventory_update2_$sp](../../StoredProcedures/me_01/dbo.inventory_update2_$sp.md)
- [me_01: dbo.iv_filter_forecasting_styles_$sp](../../StoredProcedures/me_01/dbo.iv_filter_forecasting_styles_$sp.md)
- [me_01: dbo.pi_remove_future_oh_loc_$sp](../../StoredProcedures/me_01/dbo.pi_remove_future_oh_loc_$sp.md)
- [me_01: dbo.pop_25Nov25_temp_ib_inv_$sp](../../StoredProcedures/me_01/dbo.pop_25Nov25_temp_ib_inv_$sp.md)
- [me_01: dbo.populate_ib_cost_retail_$sp](../../StoredProcedures/me_01/dbo.populate_ib_cost_retail_$sp.md)
- [me_01: dbo.populate_temp_ib_inventory_$sp](../../StoredProcedures/me_01/dbo.populate_temp_ib_inventory_$sp.md)
- [me_01: dbo.post_25Nov25_cust_order_sale_$sp](../../StoredProcedures/me_01/dbo.post_25Nov25_cust_order_sale_$sp.md)
- [me_01: dbo.post_cust_order_sale_$sp](../../StoredProcedures/me_01/dbo.post_cust_order_sale_$sp.md)
- [me_01: dbo.post_inventory_loc_$sp](../../StoredProcedures/me_01/dbo.post_inventory_loc_$sp.md)
- [me_01: dbo.post_pending_loc_$sp](../../StoredProcedures/me_01/dbo.post_pending_loc_$sp.md)
- [me_01: dbo.post_sales_batch_$sp](../../StoredProcedures/me_01/dbo.post_sales_batch_$sp.md)
- [me_01: dbo.process_modified_transactions_$sp](../../StoredProcedures/me_01/dbo.process_modified_transactions_$sp.md)
- [me_01: dbo.reclass_hist_$sp](../../StoredProcedures/me_01/dbo.reclass_hist_$sp.md)
- [me_01: dbo.reclass_hist_oh_$sp](../../StoredProcedures/me_01/dbo.reclass_hist_oh_$sp.md)
- [me_01: dbo.sales_balancing_c$sp](../../StoredProcedures/me_01/dbo.sales_balancing_c$sp.md)
- [me_01: dbo.sales_balancing_l$sp](../../StoredProcedures/me_01/dbo.sales_balancing_l$sp.md)
- [me_01: dbo.spAvgCostLoop](../../StoredProcedures/me_01/dbo.spAvgCostLoop.md)
- [me_01: dbo.spHearMeSalesConversion](../../StoredProcedures/me_01/dbo.spHearMeSalesConversion.md)
- [me_01: dbo.spHearMeSalesConversion_03082016](../../StoredProcedures/me_01/dbo.spHearMeSalesConversion_03082016.md)
- [me_01: dbo.spHearMeSalesConversion_bak_01282020LT](../../StoredProcedures/me_01/dbo.spHearMeSalesConversion_bak_01282020LT.md)
- [me_01: dbo.spHearMeSalesConversion_BJB20190326](../../StoredProcedures/me_01/dbo.spHearMeSalesConversion_BJB20190326.md)
- [me_01: dbo.spHearMeSalesConversionBACKUP20150818](../../StoredProcedures/me_01/dbo.spHearMeSalesConversionBACKUP20150818.md)
- [me_01: dbo.spHearMeSalesConversionBACKUP20150818_TC_TEST](../../StoredProcedures/me_01/dbo.spHearMeSalesConversionBACKUP20150818_TC_TEST.md)
- [me_01: dbo.SPMerchandisingArchiveAverageCost](../../StoredProcedures/me_01/dbo.SPMerchandisingArchiveAverageCost.md)
- [me_01: dbo.SPMerchandisingArchiveAverageCost_BACKUP_20150803](../../StoredProcedures/me_01/dbo.SPMerchandisingArchiveAverageCost_BACKUP_20150803.md)
- [me_01: dbo.spMerchandisingEmailInactiveStyleTransactions](../../StoredProcedures/me_01/dbo.spMerchandisingEmailInactiveStyleTransactions.md)
- [me_01: dbo.spMerchandisingEmailNonUnivSoundStores](../../StoredProcedures/me_01/dbo.spMerchandisingEmailNonUnivSoundStores.md)
- [me_01: dbo.spMerchandisingInsertIbInventoryID](../../StoredProcedures/me_01/dbo.spMerchandisingInsertIbInventoryID.md)
- [me_01: dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerification](../../StoredProcedures/me_01/dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerification.md)
- [me_01: dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJC2](../../StoredProcedures/me_01/dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJC2.md)
- [me_01: dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJC2V2](../../StoredProcedures/me_01/dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJC2V2.md)
- [me_01: dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJCtest](../../StoredProcedures/me_01/dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJCtest.md)
- [me_01: dbo.spMerchVsMACompare](../../StoredProcedures/me_01/dbo.spMerchVsMACompare.md)
- [me_01: dbo.startup_discrepancy_ib_inv_$sp](../../StoredProcedures/me_01/dbo.startup_discrepancy_ib_inv_$sp.md)
- [me_01: dbo.startup_ib_inventory_$sp](../../StoredProcedures/me_01/dbo.startup_ib_inventory_$sp.md)
- [me_01: dbo.startup_ib_inventory_total_$sp](../../StoredProcedures/me_01/dbo.startup_ib_inventory_total_$sp.md)
- [me_01: dbo.z_ib_notax_cleanup_$sp](../../StoredProcedures/me_01/dbo.z_ib_notax_cleanup_$sp.md)
- [master: dbo.c_stp_print_tickets_$sp](../../StoredProcedures/master/dbo.c_stp_print_tickets_$sp.md)

