# dbo.color

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| color_id | smallint | 2 | 0 | YES |  |  |
| color_code | nvarchar | 6 | 0 |  |  |  |
| color_long_description | nvarchar | 40 | 0 |  |  |  |
| color_short_description | nvarchar | 16 | 0 |  |  |  |
| active_flag | bit | 1 | 0 |  |  |  |
| no_color_flag | bit | 1 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.c_location_eligibilty_rep_$sp](../../StoredProcedures/me_01/dbo.c_location_eligibilty_rep_$sp.md)
- [me_01: dbo.dl_generate_upc_state_$sp](../../StoredProcedures/me_01/dbo.dl_generate_upc_state_$sp.md)
- [me_01: dbo.dl_style_task_validate_$sp](../../StoredProcedures/me_01/dbo.dl_style_task_validate_$sp.md)
- [me_01: dbo.dl_validate_import_upc_$sp](../../StoredProcedures/me_01/dbo.dl_validate_import_upc_$sp.md)
- [me_01: dbo.get_pc_instruction_price_history_$sp](../../StoredProcedures/me_01/dbo.get_pc_instruction_price_history_$sp.md)
- [me_01: dbo.get_pc_instruction_values_$sp](../../StoredProcedures/me_01/dbo.get_pc_instruction_values_$sp.md)
- [me_01: dbo.get_price_change_details_$sp](../../StoredProcedures/me_01/dbo.get_price_change_details_$sp.md)
- [me_01: dbo.get_price_change_details_pricing_level_$sp](../../StoredProcedures/me_01/dbo.get_price_change_details_pricing_level_$sp.md)
- [me_01: dbo.import_pc_populate_actual_pc_$sp](../../StoredProcedures/me_01/dbo.import_pc_populate_actual_pc_$sp.md)
- [me_01: dbo.import_pc_populate_temp_pc_$sp](../../StoredProcedures/me_01/dbo.import_pc_populate_temp_pc_$sp.md)
- [me_01: dbo.import_pc_validate_$sp](../../StoredProcedures/me_01/dbo.import_pc_validate_$sp.md)
- [me_01: dbo.imw_asn_$sp](../../StoredProcedures/me_01/dbo.imw_asn_$sp.md)
- [me_01: dbo.imw_asncomplete_$sp](../../StoredProcedures/me_01/dbo.imw_asncomplete_$sp.md)
- [me_01: dbo.imw_price_change_v1_$sp](../../StoredProcedures/me_01/dbo.imw_price_change_v1_$sp.md)
- [me_01: dbo.populate_im_sale_from_file_$sp](../../StoredProcedures/me_01/dbo.populate_im_sale_from_file_$sp.md)
- [me_01: dbo.retrieve_dist_$sp](../../StoredProcedures/me_01/dbo.retrieve_dist_$sp.md)
- [me_01: dbo.rpt_get_po_line_by_size_$sp](../../StoredProcedures/me_01/dbo.rpt_get_po_line_by_size_$sp.md)
- [me_01: dbo.rpt_get_po_line_shp_by_sz_$sp](../../StoredProcedures/me_01/dbo.rpt_get_po_line_shp_by_sz_$sp.md)
- [me_01: dbo.rpt_get_po_receipt_$sp](../../StoredProcedures/me_01/dbo.rpt_get_po_receipt_$sp.md)
- [me_01: dbo.rpt_get_pos_$sp](../../StoredProcedures/me_01/dbo.rpt_get_pos_$sp.md)
- [me_01: dbo.rpt_get_store_shipment_$sp](../../StoredProcedures/me_01/dbo.rpt_get_store_shipment_$sp.md)
- [me_01: dbo.rpt_get_unsolicited_receipt_$sp](../../StoredProcedures/me_01/dbo.rpt_get_unsolicited_receipt_$sp.md)
- [me_01: dbo.sp_po_cancel](../../StoredProcedures/me_01/dbo.sp_po_cancel.md)
- [me_01: dbo.sp_po_line_quantity_zero](../../StoredProcedures/me_01/dbo.sp_po_line_quantity_zero.md)
- [me_01: dbo.sp_po_new](../../StoredProcedures/me_01/dbo.sp_po_new.md)
- [me_01: dbo.sp_po_updates](../../StoredProcedures/me_01/dbo.sp_po_updates.md)
- [me_01: dbo.spMerchandisingDBSchenkerPOExport_3_SelectPoData](../../StoredProcedures/me_01/dbo.spMerchandisingDBSchenkerPOExport_3_SelectPoData.md)
- [me_01: dbo.spMerchandisingDBSchenkerPOExport_3_SelectPoDatabackup20180702](../../StoredProcedures/me_01/dbo.spMerchandisingDBSchenkerPOExport_3_SelectPoDatabackup20180702.md)
- [me_01: dbo.spMerchandisingDBSchenkerPOExport_6_InsertLineSwapAndCanceledLines](../../StoredProcedures/me_01/dbo.spMerchandisingDBSchenkerPOExport_6_InsertLineSwapAndCanceledLines.md)
- [me_01: dbo.spMerchandisingDBSchenkerPOExport_6_InsertLineSwapAndCanceledLinesBACKUP20180702](../../StoredProcedures/me_01/dbo.spMerchandisingDBSchenkerPOExport_6_InsertLineSwapAndCanceledLinesBACKUP20180702.md)
- [me_01: dbo.spMerchandisingDistroImportValidation](../../StoredProcedures/me_01/dbo.spMerchandisingDistroImportValidation.md)
- [me_01: dbo.spMerchandisingDistroTransfersValidation](../../StoredProcedures/me_01/dbo.spMerchandisingDistroTransfersValidation.md)
- [me_01: dbo.spMerchandisingEmailMissingUPCs](../../StoredProcedures/me_01/dbo.spMerchandisingEmailMissingUPCs.md)
- [me_01: dbo.spMerchandisingExportStoreDistributionsWC](../../StoredProcedures/me_01/dbo.spMerchandisingExportStoreDistributionsWC.md)
- [me_01: dbo.spMerchandisingExportStoreDistributionsWC_BACKUP20180712](../../StoredProcedures/me_01/dbo.spMerchandisingExportStoreDistributionsWC_BACKUP20180712.md)
- [me_01: dbo.spMerchandisingExportStoreDistributionsWC_NEW](../../StoredProcedures/me_01/dbo.spMerchandisingExportStoreDistributionsWC_NEW.md)
- [me_01: dbo.spMerchandisingOutputPOData](../../StoredProcedures/me_01/dbo.spMerchandisingOutputPOData.md)
- [me_01: dbo.spMerchandisingOutputStylesMissingUPC](../../StoredProcedures/me_01/dbo.spMerchandisingOutputStylesMissingUPC.md)
- [me_01: dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerification](../../StoredProcedures/me_01/dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerification.md)
- [me_01: dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJC2](../../StoredProcedures/me_01/dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJC2.md)
- [me_01: dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJC2V2](../../StoredProcedures/me_01/dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJC2V2.md)
- [me_01: dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJCtest](../../StoredProcedures/me_01/dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJCtest.md)
- [me_01: dbo.spMerchandisingReportRecType](../../StoredProcedures/me_01/dbo.spMerchandisingReportRecType.md)
- [me_01: dbo.spMerchandisingReportRoyaltyUpdates](../../StoredProcedures/me_01/dbo.spMerchandisingReportRoyaltyUpdates.md)
- [me_01: dbo.spMerchandisingReportStyleList](../../StoredProcedures/me_01/dbo.spMerchandisingReportStyleList.md)
- [me_01: dbo.spMerchandisingReportStyleList_BU20200513](../../StoredProcedures/me_01/dbo.spMerchandisingReportStyleList_BU20200513.md)
- [me_01: dbo.spMerchandisingSelectDistroComplete](../../StoredProcedures/me_01/dbo.spMerchandisingSelectDistroComplete.md)
- [me_01: dbo.spMerchandisingSplitReport_BHSE](../../StoredProcedures/me_01/dbo.spMerchandisingSplitReport_BHSE.md)
- [me_01: dbo.spMerchandisingSplitReport_UK](../../StoredProcedures/me_01/dbo.spMerchandisingSplitReport_UK.md)
- [me_01: dbo.spMerchandisingSplitReport_WC](../../StoredProcedures/me_01/dbo.spMerchandisingSplitReport_WC.md)
- [me_01: dbo.spMerchandisingToCNDistroExportNotification](../../StoredProcedures/me_01/dbo.spMerchandisingToCNDistroExportNotification.md)
- [me_01: dbo.spMerchandisingToUKDistroExportNotification](../../StoredProcedures/me_01/dbo.spMerchandisingToUKDistroExportNotification.md)
- [me_01: dbo.spMerchandisingToWCDistroExportNotification](../../StoredProcedures/me_01/dbo.spMerchandisingToWCDistroExportNotification.md)
- [me_01: dbo.spMerchandisingToWmDistroExportNotification](../../StoredProcedures/me_01/dbo.spMerchandisingToWmDistroExportNotification.md)
- [me_01: dbo.upd_style_retails_pc_$sp](../../StoredProcedures/me_01/dbo.upd_style_retails_pc_$sp.md)
- [me_01: dbo.update_phys_inv_table_$sp](../../StoredProcedures/me_01/dbo.update_phys_inv_table_$sp.md)
- [me_01: dbo.update_phys_inv_table_$sp_091609](../../StoredProcedures/me_01/dbo.update_phys_inv_table_$sp_091609.md)
- [me_01: dbo.validate_import_asn_tables_$sp](../../StoredProcedures/me_01/dbo.validate_import_asn_tables_$sp.md)
- [DBAUtility: dbo.spDV_ActiveProducts](../../StoredProcedures/DBAUtility/dbo.spDV_ActiveProducts.md)
- [DBAUtility: dbo.spPLM_GetMerchandingData](../../StoredProcedures/DBAUtility/dbo.spPLM_GetMerchandingData.md)
- [DBAUtility: dbo.spPLM_GetMerchandingData_dev](../../StoredProcedures/DBAUtility/dbo.spPLM_GetMerchandingData_dev.md)
- [ma_01: dbo.dl_hist_oh_styleclr_vld_$sp](../../StoredProcedures/ma_01/dbo.dl_hist_oh_styleclr_vld_$sp.md)
- [ma_01: dbo.dl_hist_styleclr_vld_$sp](../../StoredProcedures/ma_01/dbo.dl_hist_styleclr_vld_$sp.md)
- [ma_01: dbo.import_hist_cmp_styleclr_$sp](../../StoredProcedures/ma_01/dbo.import_hist_cmp_styleclr_$sp.md)
- [ma_01: dbo.rpt_style_color_sell_thru_$sp](../../StoredProcedures/ma_01/dbo.rpt_style_color_sell_thru_$sp.md)
- [USICOAL: dbo.DC_CHK_ITM_REF_INTGR](../../StoredProcedures/USICOAL/dbo.DC_CHK_ITM_REF_INTGR.md)
- [USICOAL: dbo.DC_INS_ITEM](../../StoredProcedures/USICOAL/dbo.DC_INS_ITEM.md)
- [USICOAL: dbo.DC_RPL_ITEM](../../StoredProcedures/USICOAL/dbo.DC_RPL_ITEM.md)
- [USICOAL: dbo.DC_RPL_PLU](../../StoredProcedures/USICOAL/dbo.DC_RPL_PLU.md)
- [USICOAL: dbo.DC_UPD_ITEM](../../StoredProcedures/USICOAL/dbo.DC_UPD_ITEM.md)
- [USICOAL: dbo.RPT_MRCH_RESTOCKING1](../../StoredProcedures/USICOAL/dbo.RPT_MRCH_RESTOCKING1.md)
- [USICOAL: dbo.RPT_TOP_SELL_BY_QTY1](../../StoredProcedures/USICOAL/dbo.RPT_TOP_SELL_BY_QTY1.md)

