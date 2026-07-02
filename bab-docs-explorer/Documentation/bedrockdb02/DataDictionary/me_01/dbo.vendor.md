# dbo.vendor

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| vendor_id | decimal | 9 | 0 | YES |  |  |
| vendor_code | nvarchar | 40 | 0 |  |  |  |
| vendor_name | nvarchar | 100 | 0 |  |  |  |
| alternate_vendor_code | nvarchar | 40 | 1 |  |  |  |
| country_id | decimal | 9 | 0 |  |  |  |
| currency_id | decimal | 9 | 0 |  |  |  |
| terms_id | smallint | 2 | 0 |  |  |  |
| gl_distribution_set_id | int | 4 | 1 |  |  |  |
| vendor_parameter_set_id | int | 4 | 1 |  |  |  |
| reference_set_id | int | 4 | 1 |  |  |  |
| remit_to_vendor_id | int | 4 | 1 |  |  |  |
| imat_able_flag | bit | 1 | 0 |  |  |  |
| import_flag | bit | 1 | 0 |  |  |  |
| requires_vendor_upc_flag | bit | 1 | 0 |  |  |  |
| rtv_option | smallint | 2 | 0 |  |  |  |
| rtv_acknowledgement_req_flag | bit | 1 | 0 |  |  |  |
| asn_auto_receive_flag | bit | 1 | 0 |  |  |  |
| fob_description | nvarchar | 40 | 1 |  |  |  |
| ship_via_id | smallint | 2 | 1 |  |  |  |
| carrier_id | smallint | 2 | 1 |  |  |  |
| active_flag | bit | 1 | 0 |  |  |  |
| vendor_interchange_id_qual | nvarchar | 4 | 1 |  |  |  |
| vendor_interchange_id_code | nvarchar | 30 | 1 |  |  |  |
| retailer_interchange_id_qual | nvarchar | 4 | 1 |  |  |  |
| retailer_interchange_id_code | nvarchar | 20 | 1 |  |  |  |
| send_location_id_qual | nvarchar | 4 | 1 |  |  |  |
| send_location_id_code | nvarchar | 20 | 1 |  |  |  |
| receive_location_id_qual | nvarchar | 4 | 1 |  |  |  |
| edi_able_flag | bit | 1 | 0 |  |  |  |
| edi_850_dtm_cancel_after_flag | bit | 1 | 0 |  |  |  |
| edi_850_dtm_delivery_req_flag | bit | 1 | 0 |  |  |  |
| edi_850_dtm_effective_flag | bit | 1 | 0 |  |  |  |
| edi_850_ctp_msr_flag | bit | 1 | 0 |  |  |  |
| edi_850_ctp_resale_flag | bit | 1 | 0 |  |  |  |
| interchange_control_number | decimal | 5 | 0 |  |  |  |
| group_control_number | decimal | 5 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |
| jurisdiction_id | smallint | 2 | 1 |  |  |  |
| allow_customer_shipment_flag | bit | 1 | 0 |  |  |  |
| min_on_order_cost_bulk_xdock | decimal | 9 | 1 |  |  |  |
| min_on_order_cost_dropship | decimal | 9 | 1 |  |  |  |
| supports_store_pack | bit | 1 | 0 |  |  |  |
| interface_to_wholesale | bit | 1 | 0 |  |  |  |
| asn_auto_generate_po_rcpt_status | smallint | 2 | 0 |  |  |  |
| track_in_transit_flag | bit | 1 | 0 |  |  |  |
| allow_customer_back_order_flag | bit | 1 | 0 |  |  |  |
| allow_direct_shipments_to_customer_flag | bit | 1 | 0 |  |  |  |
| allow_customer_back_order | smallint | 2 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.c_location_eligibilty_rep_$sp](../../StoredProcedures/me_01/dbo.c_location_eligibilty_rep_$sp.md)
- [me_01: dbo.cascade_allow_customer_back_order_to_skus_$sp](../../StoredProcedures/me_01/dbo.cascade_allow_customer_back_order_to_skus_$sp.md)
- [me_01: dbo.dl_generate_upc_state_$sp](../../StoredProcedures/me_01/dbo.dl_generate_upc_state_$sp.md)
- [me_01: dbo.dl_style_task_validate_$sp](../../StoredProcedures/me_01/dbo.dl_style_task_validate_$sp.md)
- [me_01: dbo.dl_validate_import_upc_$sp](../../StoredProcedures/me_01/dbo.dl_validate_import_upc_$sp.md)
- [me_01: dbo.get_price_change_details_$sp](../../StoredProcedures/me_01/dbo.get_price_change_details_$sp.md)
- [me_01: dbo.get_price_change_details_pricing_level_$sp](../../StoredProcedures/me_01/dbo.get_price_change_details_pricing_level_$sp.md)
- [me_01: dbo.imw_asn_$sp](../../StoredProcedures/me_01/dbo.imw_asn_$sp.md)
- [me_01: dbo.imw_asncomplete_$sp](../../StoredProcedures/me_01/dbo.imw_asncomplete_$sp.md)
- [me_01: dbo.imw_price_change_v1_$sp](../../StoredProcedures/me_01/dbo.imw_price_change_v1_$sp.md)
- [me_01: dbo.pocost_valid_styles_$sp](../../StoredProcedures/me_01/dbo.pocost_valid_styles_$sp.md)
- [me_01: dbo.populate_ib_cost_retail_$sp](../../StoredProcedures/me_01/dbo.populate_ib_cost_retail_$sp.md)
- [me_01: dbo.populate_im_sale_from_file_$sp](../../StoredProcedures/me_01/dbo.populate_im_sale_from_file_$sp.md)
- [me_01: dbo.populate_temp_asn_$sp](../../StoredProcedures/me_01/dbo.populate_temp_asn_$sp.md)
- [me_01: dbo.populate_temp_po_receipt_$sp](../../StoredProcedures/me_01/dbo.populate_temp_po_receipt_$sp.md)
- [me_01: dbo.retrieve_dist_$sp](../../StoredProcedures/me_01/dbo.retrieve_dist_$sp.md)
- [me_01: dbo.rpt_get_address_for_po_$sp](../../StoredProcedures/me_01/dbo.rpt_get_address_for_po_$sp.md)
- [me_01: dbo.rpt_get_pending_send_edi_pos_$sp](../../StoredProcedures/me_01/dbo.rpt_get_pending_send_edi_pos_$sp.md)
- [me_01: dbo.rpt_get_po_receipt_$sp](../../StoredProcedures/me_01/dbo.rpt_get_po_receipt_$sp.md)
- [me_01: dbo.rpt_get_pos_$sp](../../StoredProcedures/me_01/dbo.rpt_get_pos_$sp.md)
- [me_01: dbo.rpt_get_store_shipment_$sp](../../StoredProcedures/me_01/dbo.rpt_get_store_shipment_$sp.md)
- [me_01: dbo.rpt_get_unsolicited_receipt_$sp](../../StoredProcedures/me_01/dbo.rpt_get_unsolicited_receipt_$sp.md)
- [me_01: dbo.sp_po_cancel](../../StoredProcedures/me_01/dbo.sp_po_cancel.md)
- [me_01: dbo.sp_po_deleted_lines](../../StoredProcedures/me_01/dbo.sp_po_deleted_lines.md)
- [me_01: dbo.sp_po_line_quantity_zero](../../StoredProcedures/me_01/dbo.sp_po_line_quantity_zero.md)
- [me_01: dbo.sp_po_new](../../StoredProcedures/me_01/dbo.sp_po_new.md)
- [me_01: dbo.sp_po_updates](../../StoredProcedures/me_01/dbo.sp_po_updates.md)
- [me_01: dbo.spMerchandisingDBSchenkerPOExport_3_SelectPoData](../../StoredProcedures/me_01/dbo.spMerchandisingDBSchenkerPOExport_3_SelectPoData.md)
- [me_01: dbo.spMerchandisingDBSchenkerPOExport_3_SelectPoDatabackup20180702](../../StoredProcedures/me_01/dbo.spMerchandisingDBSchenkerPOExport_3_SelectPoDatabackup20180702.md)
- [me_01: dbo.spMerchandisingDBSchenkerPOExport_6_InsertLineSwapAndCanceledLines](../../StoredProcedures/me_01/dbo.spMerchandisingDBSchenkerPOExport_6_InsertLineSwapAndCanceledLines.md)
- [me_01: dbo.spMerchandisingDBSchenkerPOExport_6_InsertLineSwapAndCanceledLinesBACKUP20180702](../../StoredProcedures/me_01/dbo.spMerchandisingDBSchenkerPOExport_6_InsertLineSwapAndCanceledLinesBACKUP20180702.md)
- [me_01: dbo.spMerchandisingEmailMissingUPCs](../../StoredProcedures/me_01/dbo.spMerchandisingEmailMissingUPCs.md)
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
- [me_01: dbo.validate_import_asn_tables_$sp](../../StoredProcedures/me_01/dbo.validate_import_asn_tables_$sp.md)
- [DBAUtility: dbo.spPLM_GetMerchandingData](../../StoredProcedures/DBAUtility/dbo.spPLM_GetMerchandingData.md)
- [DBAUtility: dbo.spPLM_GetMerchandingData_dev](../../StoredProcedures/DBAUtility/dbo.spPLM_GetMerchandingData_dev.md)
- [ma_01: dbo.rpt_style_color_sell_thru_$sp](../../StoredProcedures/ma_01/dbo.rpt_style_color_sell_thru_$sp.md)

