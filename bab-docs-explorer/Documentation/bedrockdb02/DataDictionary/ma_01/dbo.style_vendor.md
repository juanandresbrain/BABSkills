# dbo.style_vendor

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_vendor_id | decimal | 9 | 0 | YES |  |  |
| style_id | decimal | 9 | 0 |  |  |  |
| vendor_id | decimal | 9 | 0 |  |  |  |
| vendor_style | nvarchar | 80 | 1 |  |  |  |
| primary_vendor_flag | bit | 1 | 0 |  |  |  |
| current_cost | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.c_location_eligibilty_rep_$sp](../../StoredProcedures/me_01/dbo.c_location_eligibilty_rep_$sp.md)
- [me_01: dbo.dl_generate_upc_state_$sp](../../StoredProcedures/me_01/dbo.dl_generate_upc_state_$sp.md)
- [me_01: dbo.dl_style_task_validate_$sp](../../StoredProcedures/me_01/dbo.dl_style_task_validate_$sp.md)
- [me_01: dbo.dl_validate_import_upc_$sp](../../StoredProcedures/me_01/dbo.dl_validate_import_upc_$sp.md)
- [me_01: dbo.ecom_get_style_list_$sp](../../StoredProcedures/me_01/dbo.ecom_get_style_list_$sp.md)
- [me_01: dbo.get_price_change_details_$sp](../../StoredProcedures/me_01/dbo.get_price_change_details_$sp.md)
- [me_01: dbo.get_price_change_details_pricing_level_$sp](../../StoredProcedures/me_01/dbo.get_price_change_details_pricing_level_$sp.md)
- [me_01: dbo.import_pc_batch_tickets_$sp](../../StoredProcedures/me_01/dbo.import_pc_batch_tickets_$sp.md)
- [me_01: dbo.imw_asn_$sp](../../StoredProcedures/me_01/dbo.imw_asn_$sp.md)
- [me_01: dbo.imw_asncomplete_$sp](../../StoredProcedures/me_01/dbo.imw_asncomplete_$sp.md)
- [me_01: dbo.imw_price_change_v1_$sp](../../StoredProcedures/me_01/dbo.imw_price_change_v1_$sp.md)
- [me_01: dbo.insert_packs_bi_$sp](../../StoredProcedures/me_01/dbo.insert_packs_bi_$sp.md)
- [me_01: dbo.insert_skus_$sp](../../StoredProcedures/me_01/dbo.insert_skus_$sp.md)
- [me_01: dbo.insert_skus_bi_$sp](../../StoredProcedures/me_01/dbo.insert_skus_bi_$sp.md)
- [me_01: dbo.insert_skus_bi_ols_$sp](../../StoredProcedures/me_01/dbo.insert_skus_bi_ols_$sp.md)
- [me_01: dbo.insert_skus_ols_$sp](../../StoredProcedures/me_01/dbo.insert_skus_ols_$sp.md)
- [me_01: dbo.pcm_get_tickets_$sp](../../StoredProcedures/me_01/dbo.pcm_get_tickets_$sp.md)
- [me_01: dbo.pi_update_inventory_tables_$sp](../../StoredProcedures/me_01/dbo.pi_update_inventory_tables_$sp.md)
- [me_01: dbo.pocost_valid_styles_$sp](../../StoredProcedures/me_01/dbo.pocost_valid_styles_$sp.md)
- [me_01: dbo.populate_im_sale_from_file_$sp](../../StoredProcedures/me_01/dbo.populate_im_sale_from_file_$sp.md)
- [me_01: dbo.rpt_get_po_receipt_$sp](../../StoredProcedures/me_01/dbo.rpt_get_po_receipt_$sp.md)
- [me_01: dbo.rpt_get_pos_$sp](../../StoredProcedures/me_01/dbo.rpt_get_pos_$sp.md)
- [me_01: dbo.rpt_get_store_shipment_$sp](../../StoredProcedures/me_01/dbo.rpt_get_store_shipment_$sp.md)
- [me_01: dbo.rpt_get_unsolicited_receipt_$sp](../../StoredProcedures/me_01/dbo.rpt_get_unsolicited_receipt_$sp.md)
- [me_01: dbo.set_current_cost_$sp](../../StoredProcedures/me_01/dbo.set_current_cost_$sp.md)
- [me_01: dbo.sp_po_cancel](../../StoredProcedures/me_01/dbo.sp_po_cancel.md)
- [me_01: dbo.sp_po_line_quantity_zero](../../StoredProcedures/me_01/dbo.sp_po_line_quantity_zero.md)
- [me_01: dbo.sp_po_new](../../StoredProcedures/me_01/dbo.sp_po_new.md)
- [me_01: dbo.sp_po_updates](../../StoredProcedures/me_01/dbo.sp_po_updates.md)
- [me_01: dbo.spMerchandising_Report_NewStyleUDA](../../StoredProcedures/me_01/dbo.spMerchandising_Report_NewStyleUDA.md)
- [me_01: dbo.spMerchandisingEmailMissingUPCs](../../StoredProcedures/me_01/dbo.spMerchandisingEmailMissingUPCs.md)
- [me_01: dbo.spMerchandisingExportStoreDistributionsCN](../../StoredProcedures/me_01/dbo.spMerchandisingExportStoreDistributionsCN.md)
- [me_01: dbo.spMerchandisingExportStoreDistributionsCN_bak_20180608](../../StoredProcedures/me_01/dbo.spMerchandisingExportStoreDistributionsCN_bak_20180608.md)
- [me_01: dbo.spMerchandisingExportStoreDistributionsCN_BAK20180712](../../StoredProcedures/me_01/dbo.spMerchandisingExportStoreDistributionsCN_BAK20180712.md)
- [me_01: dbo.spMerchandisingExportStoreDistributionsUK](../../StoredProcedures/me_01/dbo.spMerchandisingExportStoreDistributionsUK.md)
- [me_01: dbo.spMerchandisingExportStoreDistributionsUK_BACKUP20180712](../../StoredProcedures/me_01/dbo.spMerchandisingExportStoreDistributionsUK_BACKUP20180712.md)
- [me_01: dbo.spMerchandisingExportStoreDistributionsWC](../../StoredProcedures/me_01/dbo.spMerchandisingExportStoreDistributionsWC.md)
- [me_01: dbo.spMerchandisingExportStoreDistributionsWC_BACKUP20180712](../../StoredProcedures/me_01/dbo.spMerchandisingExportStoreDistributionsWC_BACKUP20180712.md)
- [me_01: dbo.spMerchandisingExportStoreDistributionsWC_NEW](../../StoredProcedures/me_01/dbo.spMerchandisingExportStoreDistributionsWC_NEW.md)
- [me_01: dbo.spMerchandisingOutputCNStyleVendor](../../StoredProcedures/me_01/dbo.spMerchandisingOutputCNStyleVendor.md)
- [me_01: dbo.spMerchandisingOutputCNStyleVendor_BAK_20180305](../../StoredProcedures/me_01/dbo.spMerchandisingOutputCNStyleVendor_BAK_20180305.md)
- [me_01: dbo.spMerchandisingOutputCNStyleVendor_BAK_20180710](../../StoredProcedures/me_01/dbo.spMerchandisingOutputCNStyleVendor_BAK_20180710.md)
- [me_01: dbo.spMerchandisingOutputPOData](../../StoredProcedures/me_01/dbo.spMerchandisingOutputPOData.md)
- [me_01: dbo.spMerchandisingOutputStylesMissingUPC](../../StoredProcedures/me_01/dbo.spMerchandisingOutputStylesMissingUPC.md)
- [me_01: dbo.spMerchandisingOutputUpdateCNYStyleVendor](../../StoredProcedures/me_01/dbo.spMerchandisingOutputUpdateCNYStyleVendor.md)
- [me_01: dbo.spMerchandisingReportRoyaltyUpdates](../../StoredProcedures/me_01/dbo.spMerchandisingReportRoyaltyUpdates.md)
- [me_01: dbo.spMerchandisingReportStyleList](../../StoredProcedures/me_01/dbo.spMerchandisingReportStyleList.md)
- [me_01: dbo.spMerchandisingReportStyleList_BU20200513](../../StoredProcedures/me_01/dbo.spMerchandisingReportStyleList_BU20200513.md)
- [me_01: dbo.spMerchandisingReportSupplies](../../StoredProcedures/me_01/dbo.spMerchandisingReportSupplies.md)
- [me_01: dbo.spMerchandisingSelectRpacPO](../../StoredProcedures/me_01/dbo.spMerchandisingSelectRpacPO.md)
- [me_01: dbo.spMerchandisingSelectRpacPO_BAK_02282018](../../StoredProcedures/me_01/dbo.spMerchandisingSelectRpacPO_BAK_02282018.md)
- [me_01: dbo.spMerchandisingStageDistrosToStoreShipments](../../StoredProcedures/me_01/dbo.spMerchandisingStageDistrosToStoreShipments.md)
- [me_01: dbo.spMerchandisingStageDistrosToStoreShipmentsBAK20220731](../../StoredProcedures/me_01/dbo.spMerchandisingStageDistrosToStoreShipmentsBAK20220731.md)
- [me_01: dbo.spUKAvailSupplies](../../StoredProcedures/me_01/dbo.spUKAvailSupplies.md)
- [me_01: dbo.upd_pc_generate_tickets_$sp](../../StoredProcedures/me_01/dbo.upd_pc_generate_tickets_$sp.md)
- [me_01: dbo.validate_import_asn_tables_$sp](../../StoredProcedures/me_01/dbo.validate_import_asn_tables_$sp.md)
- [me_01: dbo.validate_pc_generate_tickets_details_$sp](../../StoredProcedures/me_01/dbo.validate_pc_generate_tickets_details_$sp.md)
- [me_01: dbo.validate_pc_generate_tickets_header_$sp](../../StoredProcedures/me_01/dbo.validate_pc_generate_tickets_header_$sp.md)
- [DBAUtility: dbo.spPLM_GetMerchandingData](../../StoredProcedures/DBAUtility/dbo.spPLM_GetMerchandingData.md)
- [DBAUtility: dbo.spPLM_GetMerchandingData_dev](../../StoredProcedures/DBAUtility/dbo.spPLM_GetMerchandingData_dev.md)
- [ma_01: dbo.rpt_style_color_sell_thru_$sp](../../StoredProcedures/ma_01/dbo.rpt_style_color_sell_thru_$sp.md)

