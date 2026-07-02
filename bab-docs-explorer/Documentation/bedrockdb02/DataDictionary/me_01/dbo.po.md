# dbo.po

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| po_id | decimal | 9 | 0 |  |  |  |
| vendor_id | decimal | 9 | 0 |  | YES |  |
| print_flag | bit | 1 | 0 |  |  |  |
| edi_flag | bit | 1 | 0 |  |  |  |
| import_order_flag | bit | 1 | 0 |  |  |  |
| special_order_flag | bit | 1 | 0 |  |  |  |
| multiple_shipments_flag | bit | 1 | 0 |  |  |  |
| cancellation_exemption_flag | bit | 1 | 0 |  |  |  |
| allocation_completed_flag | bit | 1 | 0 |  |  |  |
| new_store_flag | bit | 1 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| ticket_source | smallint | 2 | 0 |  |  |  |
| ticket_status | smallint | 2 | 0 |  |  |  |
| gen_tkts_frm_warehouse | bit | 1 | 0 |  |  |  |
| last_modified | smalldatetime | 4 | 1 |  |  |  |
| position_id | decimal | 9 | 0 |  | YES |  |
| ship_via_id | smallint | 2 | 1 |  | YES |  |
| fob_description | nvarchar | 40 | 1 |  |  |  |
| country_id | decimal | 9 | 0 |  | YES |  |
| currency_id | decimal | 9 | 0 |  | YES |  |
| terms_id | smallint | 2 | 0 |  | YES |  |
| po_no | nvarchar | 40 | 0 |  |  |  |
| po_description | nvarchar | 120 | 1 |  |  |  |
| po_type | smallint | 2 | 0 |  |  |  |
| predistribution_type | smallint | 2 | 0 |  |  |  |
| create_date | smalldatetime | 4 | 0 |  |  |  |
| system_cancel_date | smalldatetime | 4 | 1 |  |  |  |
| order_date | smalldatetime | 4 | 1 |  |  |  |
| terms_as_of | smalldatetime | 4 | 1 |  |  |  |
| po_discount_last_modified | smalldatetime | 4 | 1 |  |  |  |
| exchange_rate | float | 8 | 0 |  |  |  |
| po_status | smallint | 2 | 0 |  |  |  |
| approval_status | smallint | 2 | 0 |  |  |  |
| blanket_po_number | nvarchar | 40 | 1 |  |  |  |
| release_number | smallint | 2 | 1 |  |  |  |
| approval_category | smallint | 2 | 0 |  |  |  |
| carrier_id | smallint | 2 | 1 |  | YES |  |
| number_of_releases | smallint | 2 | 1 |  |  |  |
| printed_status | smallint | 2 | 0 |  |  |  |
| edi_status | smallint | 2 | 0 |  |  |  |
| cancellation_reason | smallint | 2 | 0 |  |  |  |
| source | smallint | 2 | 0 |  |  |  |
| external_system_name | nvarchar | 40 | 1 |  |  |  |
| external_document_no | nvarchar | 40 | 1 |  |  |  |
| reference_po_no | nvarchar | 40 | 1 |  |  |  |
| po_cancellation_reason_id | decimal | 5 | 1 |  | YES |  |
| agent | nvarchar | 120 | 1 |  |  |  |
| consolidator | nvarchar | 120 | 1 |  |  |  |
| actual_cancel_date | smalldatetime | 4 | 1 |  |  |  |
| reinstated_flag | bit | 1 | 1 |  |  |  |
| from_delivery_date | smalldatetime | 4 | 1 |  |  |  |
| to_delivery_date | smalldatetime | 4 | 1 |  |  |  |
| validate_order_multiple | bit | 1 | 1 |  |  |  |
| release_to_dc_flag | bit | 1 | 0 |  |  |  |
| split_release_po_flag | bit | 1 | 0 |  |  |  |
| total_net_final_imu_percent | decimal | 9 | 1 |  |  |  |
| storepack_defns_ready_flag | bit | 1 | 0 |  |  |  |
| generated_by_wholesale_distro | bit | 1 | 0 |  |  |  |
| line_shipment_cost_factors_flag | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.balance_cost_factors_$sp](../../StoredProcedures/me_01/dbo.balance_cost_factors_$sp.md)
- [me_01: dbo.delete_asn_documents_$sp](../../StoredProcedures/me_01/dbo.delete_asn_documents_$sp.md)
- [me_01: dbo.delete_po_receipt_documents_$sp](../../StoredProcedures/me_01/dbo.delete_po_receipt_documents_$sp.md)
- [me_01: dbo.es_init_worktables_$sp](../../StoredProcedures/me_01/dbo.es_init_worktables_$sp.md)
- [me_01: dbo.import_asn_batch_$sp](../../StoredProcedures/me_01/dbo.import_asn_batch_$sp.md)
- [me_01: dbo.import_asn_eighth_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_eighth_step_$sp.md)
- [me_01: dbo.import_asn_first_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_first_step_$sp.md)
- [me_01: dbo.import_asn_forth_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_forth_step_$sp.md)
- [me_01: dbo.import_asn_seventh_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_seventh_step_$sp.md)
- [me_01: dbo.import_asn_sixth_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_sixth_step_$sp.md)
- [me_01: dbo.imw_asn_$sp](../../StoredProcedures/me_01/dbo.imw_asn_$sp.md)
- [me_01: dbo.imw_asncomplete_$sp](../../StoredProcedures/me_01/dbo.imw_asncomplete_$sp.md)
- [me_01: dbo.on_order_reduction_$sp](../../StoredProcedures/me_01/dbo.on_order_reduction_$sp.md)
- [me_01: dbo.on_order_reduction_pack_$sp](../../StoredProcedures/me_01/dbo.on_order_reduction_pack_$sp.md)
- [me_01: dbo.on_order_reduction_pseudo_$sp](../../StoredProcedures/me_01/dbo.on_order_reduction_pseudo_$sp.md)
- [me_01: dbo.pocost_get_po_lines_$sp](../../StoredProcedures/me_01/dbo.pocost_get_po_lines_$sp.md)
- [me_01: dbo.pom_check_released_units_$sp](../../StoredProcedures/me_01/dbo.pom_check_released_units_$sp.md)
- [me_01: dbo.pom_retrieve_released_units_$sp](../../StoredProcedures/me_01/dbo.pom_retrieve_released_units_$sp.md)
- [me_01: dbo.populate_ib_cfd_$sp](../../StoredProcedures/me_01/dbo.populate_ib_cfd_$sp.md)
- [me_01: dbo.populate_ib_cost_retail_$sp](../../StoredProcedures/me_01/dbo.populate_ib_cost_retail_$sp.md)
- [me_01: dbo.populate_temp_asn_$sp](../../StoredProcedures/me_01/dbo.populate_temp_asn_$sp.md)
- [me_01: dbo.populate_temp_po_receipt_$sp](../../StoredProcedures/me_01/dbo.populate_temp_po_receipt_$sp.md)
- [me_01: dbo.retrieve_dist_$sp](../../StoredProcedures/me_01/dbo.retrieve_dist_$sp.md)
- [me_01: dbo.rpt_get_fob_BABW_$sp](../../StoredProcedures/me_01/dbo.rpt_get_fob_BABW_$sp.md)
- [me_01: dbo.rpt_get_pending_send_edi_pos_$sp](../../StoredProcedures/me_01/dbo.rpt_get_pending_send_edi_pos_$sp.md)
- [me_01: dbo.rpt_get_po_receipt_$sp](../../StoredProcedures/me_01/dbo.rpt_get_po_receipt_$sp.md)
- [me_01: dbo.rpt_get_pos_$sp](../../StoredProcedures/me_01/dbo.rpt_get_pos_$sp.md)
- [me_01: dbo.rpt_get_pos_BABW_$sp](../../StoredProcedures/me_01/dbo.rpt_get_pos_BABW_$sp.md)
- [me_01: dbo.rpt_get_pos_BABW_$sp_01042018](../../StoredProcedures/me_01/dbo.rpt_get_pos_BABW_$sp_01042018.md)
- [me_01: dbo.rpt_get_pos_BABW_$sp_BAK_02272018](../../StoredProcedures/me_01/dbo.rpt_get_pos_BABW_$sp_BAK_02272018.md)
- [me_01: dbo.set_delivery_dates_$sp](../../StoredProcedures/me_01/dbo.set_delivery_dates_$sp.md)
- [me_01: dbo.sp_keith_ib_audit_trail](../../StoredProcedures/me_01/dbo.sp_keith_ib_audit_trail.md)
- [me_01: dbo.sp_keith_ib_audit_trailBACKU20150511](../../StoredProcedures/me_01/dbo.sp_keith_ib_audit_trailBACKU20150511.md)
- [me_01: dbo.sp_keith_ib_audit_trailBAK20220801](../../StoredProcedures/me_01/dbo.sp_keith_ib_audit_trailBAK20220801.md)
- [me_01: dbo.sp_po_cancel](../../StoredProcedures/me_01/dbo.sp_po_cancel.md)
- [me_01: dbo.sp_po_deleted_lines](../../StoredProcedures/me_01/dbo.sp_po_deleted_lines.md)
- [me_01: dbo.sp_po_line_quantity_zero](../../StoredProcedures/me_01/dbo.sp_po_line_quantity_zero.md)
- [me_01: dbo.sp_po_new](../../StoredProcedures/me_01/dbo.sp_po_new.md)
- [me_01: dbo.sp_po_updates](../../StoredProcedures/me_01/dbo.sp_po_updates.md)
- [me_01: dbo.spMerchandisingDBSchenkerPOExport_3_SelectPoData](../../StoredProcedures/me_01/dbo.spMerchandisingDBSchenkerPOExport_3_SelectPoData.md)
- [me_01: dbo.spMerchandisingDBSchenkerPOExport_3_SelectPoDatabackup20180702](../../StoredProcedures/me_01/dbo.spMerchandisingDBSchenkerPOExport_3_SelectPoDatabackup20180702.md)
- [me_01: dbo.spMerchandisingDBSchenkerPOExport_4_PreviouslyCanceled](../../StoredProcedures/me_01/dbo.spMerchandisingDBSchenkerPOExport_4_PreviouslyCanceled.md)
- [me_01: dbo.spMerchandisingDBSchenkerPOExport_5_SelectCanceledPO](../../StoredProcedures/me_01/dbo.spMerchandisingDBSchenkerPOExport_5_SelectCanceledPO.md)
- [me_01: dbo.spMerchandisingDBSchenkerPOExport_6_InsertLineSwapAndCanceledLines](../../StoredProcedures/me_01/dbo.spMerchandisingDBSchenkerPOExport_6_InsertLineSwapAndCanceledLines.md)
- [me_01: dbo.spMerchandisingDBSchenkerPOExport_6_InsertLineSwapAndCanceledLinesBACKUP20180702](../../StoredProcedures/me_01/dbo.spMerchandisingDBSchenkerPOExport_6_InsertLineSwapAndCanceledLinesBACKUP20180702.md)
- [me_01: dbo.spMerchandisingOutputPOData](../../StoredProcedures/me_01/dbo.spMerchandisingOutputPOData.md)
- [me_01: dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJCtest](../../StoredProcedures/me_01/dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJCtest.md)
- [me_01: dbo.spMerchandisingSelectCanceledPO](../../StoredProcedures/me_01/dbo.spMerchandisingSelectCanceledPO.md)
- [me_01: dbo.spMerchandisingSelectPOReceiptSummary](../../StoredProcedures/me_01/dbo.spMerchandisingSelectPOReceiptSummary.md)
- [me_01: dbo.spMerchandisingSelectRpacPO](../../StoredProcedures/me_01/dbo.spMerchandisingSelectRpacPO.md)
- [me_01: dbo.spMerchandisingSelectRpacPO_BAK_02282018](../../StoredProcedures/me_01/dbo.spMerchandisingSelectRpacPO_BAK_02282018.md)
- [me_01: dbo.spWMCostcoShipmentNotification](../../StoredProcedures/me_01/dbo.spWMCostcoShipmentNotification.md)
- [me_01: dbo.validate_import_asn_tables_$sp](../../StoredProcedures/me_01/dbo.validate_import_asn_tables_$sp.md)

