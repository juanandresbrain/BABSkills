# dbo.style_retail

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_retail_id | decimal | 9 | 0 | YES |  |  |
| style_id | decimal | 9 | 0 |  |  |  |
| jurisdiction_id | smallint | 2 | 0 |  |  |  |
| compare_at_retail | decimal | 9 | 1 |  |  |  |
| original_valuation_retail | decimal | 9 | 1 |  |  |  |
| original_selling_retail | decimal | 9 | 1 |  |  |  |
| original_price_status_id | smallint | 2 | 1 |  |  |  |
| current_valuation_retail | decimal | 9 | 1 |  |  |  |
| current_selling_retail | decimal | 9 | 1 |  |  |  |
| current_price_status_id | smallint | 2 | 1 |  |  |  |
| mix_match_rule_id1 | decimal | 9 | 1 |  |  |  |
| mix_match_rule_id2 | decimal | 9 | 1 |  |  |  |
| mix_match_rule_id3 | decimal | 9 | 1 |  |  |  |
| mix_match_rule_id4 | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.ecom_get_style_list_$sp](../../StoredProcedures/me_01/dbo.ecom_get_style_list_$sp.md)
- [me_01: dbo.get_imrd_oh_orig_retail_$sp](../../StoredProcedures/me_01/dbo.get_imrd_oh_orig_retail_$sp.md)
- [me_01: dbo.get_pc_instruction_values_$sp](../../StoredProcedures/me_01/dbo.get_pc_instruction_values_$sp.md)
- [me_01: dbo.get_pricing_$sp](../../StoredProcedures/me_01/dbo.get_pricing_$sp.md)
- [me_01: dbo.get_pricing_pg_$sp](../../StoredProcedures/me_01/dbo.get_pricing_pg_$sp.md)
- [me_01: dbo.import_pc_populate_temp_pc_from_ib_$sp](../../StoredProcedures/me_01/dbo.import_pc_populate_temp_pc_from_ib_$sp.md)
- [me_01: dbo.move_pg_exceptions_to_locations_$sp](../../StoredProcedures/me_01/dbo.move_pg_exceptions_to_locations_$sp.md)
- [me_01: dbo.pi_get_retails_$sp](../../StoredProcedures/me_01/dbo.pi_get_retails_$sp.md)
- [me_01: dbo.plu_common_price_$sp](../../StoredProcedures/me_01/dbo.plu_common_price_$sp.md)
- [me_01: dbo.plu_style_queue_$sp](../../StoredProcedures/me_01/dbo.plu_style_queue_$sp.md)
- [me_01: dbo.pop_fixed_avg_cost_by_jurisdiction_$sp](../../StoredProcedures/me_01/dbo.pop_fixed_avg_cost_by_jurisdiction_$sp.md)
- [me_01: dbo.populate_fixed_average_cost_by_location_$sp](../../StoredProcedures/me_01/dbo.populate_fixed_average_cost_by_location_$sp.md)
- [me_01: dbo.rpt_get_po_receipt_$sp](../../StoredProcedures/me_01/dbo.rpt_get_po_receipt_$sp.md)
- [me_01: dbo.sp_po_cancel](../../StoredProcedures/me_01/dbo.sp_po_cancel.md)
- [me_01: dbo.sp_po_line_quantity_zero](../../StoredProcedures/me_01/dbo.sp_po_line_quantity_zero.md)
- [me_01: dbo.sp_po_new](../../StoredProcedures/me_01/dbo.sp_po_new.md)
- [me_01: dbo.sp_po_updates](../../StoredProcedures/me_01/dbo.sp_po_updates.md)
- [me_01: dbo.spBABW_getGooglePriceQuantityData](../../StoredProcedures/me_01/dbo.spBABW_getGooglePriceQuantityData.md)
- [me_01: dbo.spDW_CurrentRetail](../../StoredProcedures/me_01/dbo.spDW_CurrentRetail.md)
- [me_01: dbo.spMerchandising_Report_NewStyleUDA](../../StoredProcedures/me_01/dbo.spMerchandising_Report_NewStyleUDA.md)
- [me_01: dbo.spMerchandisingDBSchenkerPOExport_3_SelectPoData](../../StoredProcedures/me_01/dbo.spMerchandisingDBSchenkerPOExport_3_SelectPoData.md)
- [me_01: dbo.spMerchandisingDBSchenkerPOExport_3_SelectPoDatabackup20180702](../../StoredProcedures/me_01/dbo.spMerchandisingDBSchenkerPOExport_3_SelectPoDatabackup20180702.md)
- [me_01: dbo.spMerchandisingDBSchenkerPOExport_6_InsertLineSwapAndCanceledLines](../../StoredProcedures/me_01/dbo.spMerchandisingDBSchenkerPOExport_6_InsertLineSwapAndCanceledLines.md)
- [me_01: dbo.spMerchandisingDBSchenkerPOExport_6_InsertLineSwapAndCanceledLinesBACKUP20180702](../../StoredProcedures/me_01/dbo.spMerchandisingDBSchenkerPOExport_6_InsertLineSwapAndCanceledLinesBACKUP20180702.md)
- [me_01: dbo.spMerchandisingOutputPOData](../../StoredProcedures/me_01/dbo.spMerchandisingOutputPOData.md)
- [me_01: dbo.spMerchandisingReportRoyaltyUpdates](../../StoredProcedures/me_01/dbo.spMerchandisingReportRoyaltyUpdates.md)
- [me_01: dbo.spMerchandisingReportStyleList](../../StoredProcedures/me_01/dbo.spMerchandisingReportStyleList.md)
- [me_01: dbo.spMerchandisingReportStyleList_BU20200513](../../StoredProcedures/me_01/dbo.spMerchandisingReportStyleList_BU20200513.md)
- [me_01: dbo.spMerchandisingSelectRpacPO](../../StoredProcedures/me_01/dbo.spMerchandisingSelectRpacPO.md)
- [me_01: dbo.spMerchandisingSelectRpacPO_BAK_02282018](../../StoredProcedures/me_01/dbo.spMerchandisingSelectRpacPO_BAK_02282018.md)
- [me_01: dbo.spPOSPricebookStage](../../StoredProcedures/me_01/dbo.spPOSPricebookStage.md)
- [me_01: dbo.spPOSPricebookStage_BAK20231101](../../StoredProcedures/me_01/dbo.spPOSPricebookStage_BAK20231101.md)
- [me_01: dbo.spPOSPricebookStageUpdatedWIP](../../StoredProcedures/me_01/dbo.spPOSPricebookStageUpdatedWIP.md)
- [me_01: dbo.spWEBPricebookStage](../../StoredProcedures/me_01/dbo.spWEBPricebookStage.md)
- [me_01: dbo.spWEBPricebookStage_Bak20220705](../../StoredProcedures/me_01/dbo.spWEBPricebookStage_Bak20220705.md)
- [me_01: dbo.spWEBPricebookStage_TCOnDemand](../../StoredProcedures/me_01/dbo.spWEBPricebookStage_TCOnDemand.md)
- [me_01: dbo.upd_style_retails_pc_$sp](../../StoredProcedures/me_01/dbo.upd_style_retails_pc_$sp.md)
- [master: dbo.c_stp_print_tickets_$sp](../../StoredProcedures/master/dbo.c_stp_print_tickets_$sp.md)
- [DBAUtility: dbo.spDM_MaintainProducts](../../StoredProcedures/DBAUtility/dbo.spDM_MaintainProducts.md)
- [DBAUtility: dbo.spMerchStyleValidation_GetProductByStyle](../../StoredProcedures/DBAUtility/dbo.spMerchStyleValidation_GetProductByStyle.md)
- [DBAUtility: dbo.spPLM_GetMerchandingData](../../StoredProcedures/DBAUtility/dbo.spPLM_GetMerchandingData.md)
- [DBAUtility: dbo.spPLM_GetMerchandingData_dev](../../StoredProcedures/DBAUtility/dbo.spPLM_GetMerchandingData_dev.md)
- [DBAUtility: dbo.spZebraBarcode_GetStyles](../../StoredProcedures/DBAUtility/dbo.spZebraBarcode_GetStyles.md)
- [DBAUtility: dbo.spZebraBarcode_GetStylesWithUPC](../../StoredProcedures/DBAUtility/dbo.spZebraBarcode_GetStylesWithUPC.md)

