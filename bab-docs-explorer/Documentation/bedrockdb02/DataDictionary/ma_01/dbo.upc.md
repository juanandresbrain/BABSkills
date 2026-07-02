# dbo.upc

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| upc_id | decimal | 9 | 0 | YES |  |  |
| sku_id | decimal | 9 | 1 |  |  |  |
| pack_id | decimal | 9 | 1 |  |  |  |
| upc_type | tinyint | 1 | 0 |  |  |  |
| upc_number | nvarchar | 28 | 0 |  |  |  |
| activation_date | smalldatetime | 4 | 1 |  |  |  |
| last_activity_date | smalldatetime | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.dl_style_task_validate_$sp](../../StoredProcedures/me_01/dbo.dl_style_task_validate_$sp.md)
- [me_01: dbo.dl_validate_import_upc_$sp](../../StoredProcedures/me_01/dbo.dl_validate_import_upc_$sp.md)
- [me_01: dbo.ecom_get_style_list_$sp](../../StoredProcedures/me_01/dbo.ecom_get_style_list_$sp.md)
- [me_01: dbo.get_pricing_history_$sp](../../StoredProcedures/me_01/dbo.get_pricing_history_$sp.md)
- [me_01: dbo.imw_asn_$sp](../../StoredProcedures/me_01/dbo.imw_asn_$sp.md)
- [me_01: dbo.imw_asncomplete_$sp](../../StoredProcedures/me_01/dbo.imw_asncomplete_$sp.md)
- [me_01: dbo.insert_packs_$sp](../../StoredProcedures/me_01/dbo.insert_packs_$sp.md)
- [me_01: dbo.insert_packs_bi_$sp](../../StoredProcedures/me_01/dbo.insert_packs_bi_$sp.md)
- [me_01: dbo.insert_pseudo_$sp](../../StoredProcedures/me_01/dbo.insert_pseudo_$sp.md)
- [me_01: dbo.insert_pseudo_bi_$sp](../../StoredProcedures/me_01/dbo.insert_pseudo_bi_$sp.md)
- [me_01: dbo.insert_skus_$sp](../../StoredProcedures/me_01/dbo.insert_skus_$sp.md)
- [me_01: dbo.insert_skus_bi_$sp](../../StoredProcedures/me_01/dbo.insert_skus_bi_$sp.md)
- [me_01: dbo.pi_load_retail_data_loc_$sp](../../StoredProcedures/me_01/dbo.pi_load_retail_data_loc_$sp.md)
- [me_01: dbo.pi_process_loc_$sp](../../StoredProcedures/me_01/dbo.pi_process_loc_$sp.md)
- [me_01: dbo.pi_update_inventory_tables_$sp](../../StoredProcedures/me_01/dbo.pi_update_inventory_tables_$sp.md)
- [me_01: dbo.plu_common_item_$sp](../../StoredProcedures/me_01/dbo.plu_common_item_$sp.md)
- [me_01: dbo.plu_item_queue_$sp](../../StoredProcedures/me_01/dbo.plu_item_queue_$sp.md)
- [me_01: dbo.plu_update_item_$sp](../../StoredProcedures/me_01/dbo.plu_update_item_$sp.md)
- [me_01: dbo.populate_im_sale_from_file_$sp](../../StoredProcedures/me_01/dbo.populate_im_sale_from_file_$sp.md)
- [me_01: dbo.post_sales_batch_$sp](../../StoredProcedures/me_01/dbo.post_sales_batch_$sp.md)
- [me_01: dbo.process_modified_transactions_$sp](../../StoredProcedures/me_01/dbo.process_modified_transactions_$sp.md)
- [me_01: dbo.retrieve_dist_$sp](../../StoredProcedures/me_01/dbo.retrieve_dist_$sp.md)
- [me_01: dbo.rpt_get_pack_upc_$sp](../../StoredProcedures/me_01/dbo.rpt_get_pack_upc_$sp.md)
- [me_01: dbo.rpt_get_pending_send_edi_pos_$sp](../../StoredProcedures/me_01/dbo.rpt_get_pending_send_edi_pos_$sp.md)
- [me_01: dbo.rpt_get_pos_$sp](../../StoredProcedures/me_01/dbo.rpt_get_pos_$sp.md)
- [me_01: dbo.rpt_get_upc_$sp](../../StoredProcedures/me_01/dbo.rpt_get_upc_$sp.md)
- [me_01: dbo.sp_po_cancel](../../StoredProcedures/me_01/dbo.sp_po_cancel.md)
- [me_01: dbo.sp_po_line_quantity_zero](../../StoredProcedures/me_01/dbo.sp_po_line_quantity_zero.md)
- [me_01: dbo.sp_po_new](../../StoredProcedures/me_01/dbo.sp_po_new.md)
- [me_01: dbo.sp_po_updates](../../StoredProcedures/me_01/dbo.sp_po_updates.md)
- [me_01: dbo.spMerchandising_980NightlySync_OnDemand](../../StoredProcedures/me_01/dbo.spMerchandising_980NightlySync_OnDemand.md)
- [me_01: dbo.spMerchandising_Report_NewStyleUDA](../../StoredProcedures/me_01/dbo.spMerchandising_Report_NewStyleUDA.md)
- [me_01: dbo.spMerchandising_WEB_NightlySync_OnDemand](../../StoredProcedures/me_01/dbo.spMerchandising_WEB_NightlySync_OnDemand.md)
- [me_01: dbo.spMerchandisingEmailMissingUPCs](../../StoredProcedures/me_01/dbo.spMerchandisingEmailMissingUPCs.md)
- [me_01: dbo.spMerchandisingExportStoreDistributionsWC](../../StoredProcedures/me_01/dbo.spMerchandisingExportStoreDistributionsWC.md)
- [me_01: dbo.spMerchandisingExportStoreDistributionsWC_BACKUP20180712](../../StoredProcedures/me_01/dbo.spMerchandisingExportStoreDistributionsWC_BACKUP20180712.md)
- [me_01: dbo.spMerchandisingExportStoreDistributionsWC_NEW](../../StoredProcedures/me_01/dbo.spMerchandisingExportStoreDistributionsWC_NEW.md)
- [me_01: dbo.spMerchandisingNightlySyncPostSummary](../../StoredProcedures/me_01/dbo.spMerchandisingNightlySyncPostSummary.md)
- [me_01: dbo.spMerchandisingOutputPOData](../../StoredProcedures/me_01/dbo.spMerchandisingOutputPOData.md)
- [me_01: dbo.spMerchandisingOutputStylesMissingUPC](../../StoredProcedures/me_01/dbo.spMerchandisingOutputStylesMissingUPC.md)
- [me_01: dbo.spMerchandisingSelectPOReceiptSummary](../../StoredProcedures/me_01/dbo.spMerchandisingSelectPOReceiptSummary.md)
- [me_01: dbo.spMerchandisingSelectRpacPO](../../StoredProcedures/me_01/dbo.spMerchandisingSelectRpacPO.md)
- [me_01: dbo.spMerchandisingSelectRpacPO_BAK_02282018](../../StoredProcedures/me_01/dbo.spMerchandisingSelectRpacPO_BAK_02282018.md)
- [me_01: dbo.spMerchandisingSelectShipmentSummary](../../StoredProcedures/me_01/dbo.spMerchandisingSelectShipmentSummary.md)
- [me_01: dbo.spMerchandisingSelectShrinkAdjustmentSummary](../../StoredProcedures/me_01/dbo.spMerchandisingSelectShrinkAdjustmentSummary.md)
- [me_01: dbo.spMerchandisingSelectShrinkErrors](../../StoredProcedures/me_01/dbo.spMerchandisingSelectShrinkErrors.md)
- [me_01: dbo.spMerchandisingSelectWhseInventoryShrink](../../StoredProcedures/me_01/dbo.spMerchandisingSelectWhseInventoryShrink.md)
- [me_01: dbo.spMerchandisingSelectWhseInventoryShrink_Bak20210614](../../StoredProcedures/me_01/dbo.spMerchandisingSelectWhseInventoryShrink_Bak20210614.md)
- [me_01: dbo.spMerchandisingSelectWhseInventoryShrink_BAK20230829](../../StoredProcedures/me_01/dbo.spMerchandisingSelectWhseInventoryShrink_BAK20230829.md)
- [me_01: dbo.spMerchandisingSelectWhseInventoryShrink_Bak20231219](../../StoredProcedures/me_01/dbo.spMerchandisingSelectWhseInventoryShrink_Bak20231219.md)
- [me_01: dbo.spMerchandisingSelectWhseInventoryShrink_manual](../../StoredProcedures/me_01/dbo.spMerchandisingSelectWhseInventoryShrink_manual.md)
- [me_01: dbo.spMerchandisingSelectWhseInventoryShrinkBAK20220801](../../StoredProcedures/me_01/dbo.spMerchandisingSelectWhseInventoryShrinkBAK20220801.md)
- [me_01: dbo.spPartyManager_ActiveDistro](../../StoredProcedures/me_01/dbo.spPartyManager_ActiveDistro.md)
- [me_01: dbo.update_phys_inv_table_$sp](../../StoredProcedures/me_01/dbo.update_phys_inv_table_$sp.md)
- [me_01: dbo.update_phys_inv_table_$sp_091609](../../StoredProcedures/me_01/dbo.update_phys_inv_table_$sp_091609.md)
- [me_01: dbo.validate_import_asn_tables_$sp](../../StoredProcedures/me_01/dbo.validate_import_asn_tables_$sp.md)
- [DBAUtility: dbo.spDM_MaintainProducts](../../StoredProcedures/DBAUtility/dbo.spDM_MaintainProducts.md)
- [DBAUtility: dbo.spDV_ActiveProducts](../../StoredProcedures/DBAUtility/dbo.spDV_ActiveProducts.md)
- [DBAUtility: dbo.spMerchStyleValidation_GetStyleBySku](../../StoredProcedures/DBAUtility/dbo.spMerchStyleValidation_GetStyleBySku.md)
- [DBAUtility: dbo.spPLM_GetMerchandingData](../../StoredProcedures/DBAUtility/dbo.spPLM_GetMerchandingData.md)
- [DBAUtility: dbo.spPLM_GetMerchandingData_dev](../../StoredProcedures/DBAUtility/dbo.spPLM_GetMerchandingData_dev.md)
- [DBAUtility: dbo.spZebraBarcode_GetStylesWithUPC](../../StoredProcedures/DBAUtility/dbo.spZebraBarcode_GetStylesWithUPC.md)
- [ma_01: dbo.dl_hist_oh_sku_vld_$sp](../../StoredProcedures/ma_01/dbo.dl_hist_oh_sku_vld_$sp.md)
- [ma_01: dbo.dl_hist_sku_vld_$sp](../../StoredProcedures/ma_01/dbo.dl_hist_sku_vld_$sp.md)
- [ma_01: dbo.import_hist_cmp_sku_$sp](../../StoredProcedures/ma_01/dbo.import_hist_cmp_sku_$sp.md)

