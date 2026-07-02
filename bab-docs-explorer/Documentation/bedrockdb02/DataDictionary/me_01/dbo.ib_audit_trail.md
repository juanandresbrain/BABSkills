# dbo.ib_audit_trail

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ib_audit_trail_id | decimal | 9 | 0 | YES |  |  |
| entry_date | smalldatetime | 4 | 0 |  |  |  |
| application | nvarchar | 20 | 0 |  |  |  |
| activity | nvarchar | 40 | 1 |  |  |  |
| application_type_id | nvarchar | 30 | 1 |  |  |  |
| application_type | nvarchar | 80 | 0 |  |  |  |
| application_identifier | nvarchar | 40 | 1 |  |  |  |
| application_level | nvarchar | 80 | 1 |  |  |  |
| application_key | nvarchar | 510 | 1 |  |  |  |
| action | nvarchar | 40 | 1 |  |  |  |
| field_affected | nvarchar | 80 | 1 |  |  |  |
| old_value | nvarchar | 510 | 1 |  |  |  |
| new_value | nvarchar | 510 | 1 |  |  |  |
| status | nvarchar | 40 | 1 |  |  |  |
| employee_last_name | nvarchar | 60 | 0 |  |  |  |
| employee_first_name | nvarchar | 60 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.build_pg_time_table_$sp](../../StoredProcedures/me_01/dbo.build_pg_time_table_$sp.md)
- [me_01: dbo.cascade_allow_customer_back_order_to_skus_$sp](../../StoredProcedures/me_01/dbo.cascade_allow_customer_back_order_to_skus_$sp.md)
- [me_01: dbo.copy_location_perm_prices_$sp](../../StoredProcedures/me_01/dbo.copy_location_perm_prices_$sp.md)
- [me_01: dbo.copy_location_to_deals_$sp](../../StoredProcedures/me_01/dbo.copy_location_to_deals_$sp.md)
- [me_01: dbo.copy_location_to_price_changes_$sp](../../StoredProcedures/me_01/dbo.copy_location_to_price_changes_$sp.md)
- [me_01: dbo.delete_asn_documents_$sp](../../StoredProcedures/me_01/dbo.delete_asn_documents_$sp.md)
- [me_01: dbo.delete_avg_cost_adj_documents_$sp](../../StoredProcedures/me_01/dbo.delete_avg_cost_adj_documents_$sp.md)
- [me_01: dbo.delete_imrd_documents_$sp](../../StoredProcedures/me_01/dbo.delete_imrd_documents_$sp.md)
- [me_01: dbo.delete_inv_control_documents_$sp](../../StoredProcedures/me_01/dbo.delete_inv_control_documents_$sp.md)
- [me_01: dbo.delete_pc_documents_$sp](../../StoredProcedures/me_01/dbo.delete_pc_documents_$sp.md)
- [me_01: dbo.delete_po_receipt_documents_$sp](../../StoredProcedures/me_01/dbo.delete_po_receipt_documents_$sp.md)
- [me_01: dbo.delete_rtv_documents_$sp](../../StoredProcedures/me_01/dbo.delete_rtv_documents_$sp.md)
- [me_01: dbo.delete_shrink_adj_documents_$sp](../../StoredProcedures/me_01/dbo.delete_shrink_adj_documents_$sp.md)
- [me_01: dbo.delete_ss_adj_documents_$sp](../../StoredProcedures/me_01/dbo.delete_ss_adj_documents_$sp.md)
- [me_01: dbo.delete_store_shipment_documents_$sp](../../StoredProcedures/me_01/dbo.delete_store_shipment_documents_$sp.md)
- [me_01: dbo.delete_transfer_documents_$sp](../../StoredProcedures/me_01/dbo.delete_transfer_documents_$sp.md)
- [me_01: dbo.delete_udt_documents_$sp](../../StoredProcedures/me_01/dbo.delete_udt_documents_$sp.md)
- [me_01: dbo.delete_uns_receipt_documents_$sp](../../StoredProcedures/me_01/dbo.delete_uns_receipt_documents_$sp.md)
- [me_01: dbo.import_asn_first_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_first_step_$sp.md)
- [me_01: dbo.import_asn_second_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_second_step_$sp.md)
- [me_01: dbo.import_pc_populate_actual_pc_$sp](../../StoredProcedures/me_01/dbo.import_pc_populate_actual_pc_$sp.md)
- [me_01: dbo.no_wms_create_ss_$sp](../../StoredProcedures/me_01/dbo.no_wms_create_ss_$sp.md)
- [me_01: dbo.pcm_issue_pc_$sp](../../StoredProcedures/me_01/dbo.pcm_issue_pc_$sp.md)
- [me_01: dbo.set_current_cost_$sp](../../StoredProcedures/me_01/dbo.set_current_cost_$sp.md)
- [me_01: dbo.sp_keith_ib_audit_trail](../../StoredProcedures/me_01/dbo.sp_keith_ib_audit_trail.md)
- [me_01: dbo.sp_keith_ib_audit_trail_pointer](../../StoredProcedures/me_01/dbo.sp_keith_ib_audit_trail_pointer.md)
- [me_01: dbo.sp_keith_ib_audit_trailBACKU20150511](../../StoredProcedures/me_01/dbo.sp_keith_ib_audit_trailBACKU20150511.md)
- [me_01: dbo.sp_keith_ib_audit_trailBAK20220801](../../StoredProcedures/me_01/dbo.sp_keith_ib_audit_trailBAK20220801.md)
- [me_01: dbo.sp_po_cancel](../../StoredProcedures/me_01/dbo.sp_po_cancel.md)
- [me_01: dbo.sp_po_deleted_lines](../../StoredProcedures/me_01/dbo.sp_po_deleted_lines.md)
- [me_01: dbo.sp_po_line_quantity_zero](../../StoredProcedures/me_01/dbo.sp_po_line_quantity_zero.md)
- [me_01: dbo.sp_po_new](../../StoredProcedures/me_01/dbo.sp_po_new.md)
- [me_01: dbo.sp_po_updates](../../StoredProcedures/me_01/dbo.sp_po_updates.md)
- [me_01: dbo.spMerchandisingDBSchenkerPOExport_3_SelectPoData](../../StoredProcedures/me_01/dbo.spMerchandisingDBSchenkerPOExport_3_SelectPoData.md)
- [me_01: dbo.spMerchandisingDBSchenkerPOExport_3_SelectPoDatabackup20180702](../../StoredProcedures/me_01/dbo.spMerchandisingDBSchenkerPOExport_3_SelectPoDatabackup20180702.md)
- [me_01: dbo.spMerchandisingDBSchenkerPOExport_5_SelectCanceledPO](../../StoredProcedures/me_01/dbo.spMerchandisingDBSchenkerPOExport_5_SelectCanceledPO.md)
- [me_01: dbo.spMerchandisingOutputFactoryChange](../../StoredProcedures/me_01/dbo.spMerchandisingOutputFactoryChange.md)
- [me_01: dbo.spMerchandisingOutputFOBRoyalty](../../StoredProcedures/me_01/dbo.spMerchandisingOutputFOBRoyalty.md)
- [me_01: dbo.spMerchandisingOutputPOData](../../StoredProcedures/me_01/dbo.spMerchandisingOutputPOData.md)
- [me_01: dbo.spMerchandisingReportRoyaltyUpdates](../../StoredProcedures/me_01/dbo.spMerchandisingReportRoyaltyUpdates.md)
- [me_01: dbo.spMerchandisingSelectCanceledPO](../../StoredProcedures/me_01/dbo.spMerchandisingSelectCanceledPO.md)
- [me_01: dbo.xfers_from_distro_$sp](../../StoredProcedures/me_01/dbo.xfers_from_distro_$sp.md)

