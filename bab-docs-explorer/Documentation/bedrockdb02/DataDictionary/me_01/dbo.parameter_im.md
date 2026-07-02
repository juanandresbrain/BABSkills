# dbo.parameter_im

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| parameter_im_id | tinyint | 1 | 0 | YES |  |  |
| po_receipt_no_mask | nvarchar | 40 | 0 |  |  |  |
| first_po_receipt_no | nvarchar | 40 | 0 |  |  |  |
| last_po_receipt_no | nvarchar | 40 | 0 |  |  |  |
| last_generated_po_receipt_no | nvarchar | 40 | 1 |  |  |  |
| po_receipt_no_rec_flag | bit | 1 | 0 |  |  |  |
| po_receipt_cleanup_weeks | smallint | 2 | 1 |  |  |  |
| transfer_no_mask | nvarchar | 40 | 0 |  |  |  |
| first_transfer_no | nvarchar | 40 | 0 |  |  |  |
| last_transfer_no | nvarchar | 40 | 0 |  |  |  |
| last_generated_transfer_no | nvarchar | 40 | 1 |  |  |  |
| transfer_no_rec_flag | bit | 1 | 0 |  |  |  |
| last_generated_xfer_carton_no | nvarchar | 40 | 0 |  |  |  |
| transfer_complete_sent_days | smallint | 2 | 1 |  |  |  |
| transfer_cleanup_weeks | smallint | 2 | 1 |  |  |  |
| rtv_no_mask | nvarchar | 40 | 0 |  |  |  |
| first_rtv_no | nvarchar | 40 | 0 |  |  |  |
| last_rtv_no | nvarchar | 40 | 0 |  |  |  |
| last_generated_rtv_no | nvarchar | 40 | 1 |  |  |  |
| rtv_no_rec_flag | bit | 1 | 0 |  |  |  |
| last_generated_rtv_carton_no | nvarchar | 40 | 0 |  |  |  |
| rtv_cleanup_weeks | smallint | 2 | 1 |  |  |  |
| rtv_flag_default | smallint | 2 | 0 |  |  |  |
| rtv_acknowledge_flag_default | bit | 1 | 0 |  |  |  |
| user_def_adj_no_mask | nvarchar | 40 | 0 |  |  |  |
| first_user_def_adj_no | nvarchar | 40 | 0 |  |  |  |
| last_user_def_adj_no | nvarchar | 40 | 0 |  |  |  |
| last_generated_user_def_adj_no | nvarchar | 40 | 1 |  |  |  |
| user_def_adj_no_rec_flag | bit | 1 | 0 |  |  |  |
| user_def_adj_cleanup_weeks | smallint | 2 | 1 |  |  |  |
| avg_cost_adj_no_mask | nvarchar | 40 | 0 |  |  |  |
| first_avg_cost_adj_no | nvarchar | 40 | 0 |  |  |  |
| last_avg_cost_adj_no | nvarchar | 40 | 0 |  |  |  |
| last_generated_avg_cost_adj_no | nvarchar | 40 | 1 |  |  |  |
| avg_cost_adj_no_rec_flag | bit | 1 | 0 |  |  |  |
| avg_cost_adj_cleanup_weeks | smallint | 2 | 1 |  |  |  |
| shrink_adj_no_mask | nvarchar | 40 | 0 |  |  |  |
| first_shrink_adj_no | nvarchar | 40 | 0 |  |  |  |
| last_shrink_adj_no | nvarchar | 40 | 0 |  |  |  |
| last_generated_shrink_adj_no | nvarchar | 40 | 1 |  |  |  |
| shrink_adj_no_rec_flag | bit | 1 | 0 |  |  |  |
| shrink_adj_cleanup_weeks | smallint | 2 | 1 |  |  |  |
| stock_status_adj_no_mask | nvarchar | 40 | 0 |  |  |  |
| first_stock_status_adj_no | nvarchar | 40 | 0 |  |  |  |
| last_stock_status_adj_no | nvarchar | 40 | 0 |  |  |  |
| last_generated_ss_adj_no | nvarchar | 40 | 1 |  |  |  |
| stock_status_adj_no_rec_flag | bit | 1 | 0 |  |  |  |
| stock_status_adj_cleanup_weeks | smallint | 2 | 1 |  |  |  |
| inventory_move_req_no_mask | nvarchar | 40 | 0 |  |  |  |
| first_inventory_move_req_no | nvarchar | 40 | 0 |  |  |  |
| last_inventory_move_req_no | nvarchar | 40 | 0 |  |  |  |
| last_generated_inv_move_req_no | nvarchar | 40 | 1 |  |  |  |
| inv_move_req_no_rec_flag | bit | 1 | 0 |  |  |  |
| inventory_move_cleanup_weeks | smallint | 2 | 1 |  |  |  |
| unsolicited_receipt_no_mask | nvarchar | 40 | 0 |  |  |  |
| first_unsolicited_receipt_no | nvarchar | 40 | 0 |  |  |  |
| last_unsolicited_receipt_no | nvarchar | 40 | 0 |  |  |  |
| last_generated_uns_receipt_no | nvarchar | 40 | 1 |  |  |  |
| uns_receipt_no_rec_flag | bit | 1 | 0 |  |  |  |
| uns_receipt_cleanup_weeks | smallint | 2 | 1 |  |  |  |
| advance_ship_notice_no_mask | nvarchar | 40 | 0 |  |  |  |
| first_advance_ship_notice_no | nvarchar | 40 | 0 |  |  |  |
| last_advance_ship_notice_no | nvarchar | 40 | 0 |  |  |  |
| last_generated_asn_no | nvarchar | 40 | 1 |  |  |  |
| asn_no_rec_flag | bit | 1 | 0 |  |  |  |
| asn_cleanup_weeks | smallint | 2 | 1 |  |  |  |
| force_receive_store_ship_flag | bit | 1 | 0 |  |  |  |
| store_ship_cleanup_weeks | smallint | 2 | 1 |  |  |  |
| cost_default | smallint | 2 | 0 |  |  |  |
| rtv_address_type_id | smallint | 2 | 1 |  |  |  |
| default_xfer_address_type_id | smallint | 2 | 1 |  |  |  |
| carton_no_mask | nvarchar | 40 | 0 |  |  |  |
| allowable_backdate_days | smallint | 2 | 0 |  |  |  |
| gen_po_receipt_for_asn_flag | bit | 1 | 0 |  |  |  |
| inventory_count_no_mask | nvarchar | 40 | 0 |  |  |  |
| first_inventory_count_no | nvarchar | 40 | 0 |  |  |  |
| last_inventory_count_no | nvarchar | 40 | 0 |  |  |  |
| last_generated_inv_count_no | nvarchar | 40 | 1 |  |  |  |
| inv_count_no_rec_flag | bit | 1 | 0 |  |  |  |
| inventory_count_cleanup_weeks | smallint | 2 | 1 |  |  |  |
| inventory_count_max_days | smallint | 2 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| oim_count_action | smallint | 2 | 0 |  |  |  |
| count_import_in_prog_flag | bit | 1 | 0 |  |  |  |
| store_ship_no_mask | nvarchar | 40 | 0 |  |  |  |
| first_store_ship_no | nvarchar | 40 | 0 |  |  |  |
| last_store_ship_no | nvarchar | 40 | 0 |  |  |  |
| last_generated_store_ship_no | nvarchar | 40 | 1 |  |  |  |
| store_ship_no_rec_flag | bit | 1 | 0 |  |  |  |
| store_ship_force_substit_flag | bit | 1 | 0 |  |  |  |
| transfer_force_substit_flag | bit | 1 | 0 |  |  |  |
| store_ship_dupl_doc_action | smallint | 2 | 0 |  |  |  |
| transfer_dupl_doc_action | smallint | 2 | 0 |  |  |  |
| pi_count_import_path | nvarchar | -1 | 1 |  |  |  |
| gen_po_receipt_for_oim_loc_flag | bit | 1 | 0 |  |  |  |
| post_layaway_as_sale | bit | 1 | 0 |  |  |  |
| sale_transaction_source_is_sa | bit | 1 | 0 |  |  |  |
| sale_transaction_source_folder | nvarchar | 400 | 0 |  |  |  |
| days_to_keep_sale_import_file | smallint | 2 | 1 |  |  |  |
| ib_store_ship_retain_in_transit | bit | 1 | 0 |  |  |  |
| ib_store_ship_keep_in_transit_days | smallint | 2 | 1 |  |  |  |
| ib_store_ship_posting_date_type | tinyint | 1 | 0 |  |  |  |
| returned_inv_status_id | smallint | 2 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.delete_asn_documents_$sp](../../StoredProcedures/me_01/dbo.delete_asn_documents_$sp.md)
- [me_01: dbo.delete_avg_cost_adj_documents_$sp](../../StoredProcedures/me_01/dbo.delete_avg_cost_adj_documents_$sp.md)
- [me_01: dbo.delete_imrd_documents_$sp](../../StoredProcedures/me_01/dbo.delete_imrd_documents_$sp.md)
- [me_01: dbo.delete_inv_control_documents_$sp](../../StoredProcedures/me_01/dbo.delete_inv_control_documents_$sp.md)
- [me_01: dbo.delete_po_receipt_documents_$sp](../../StoredProcedures/me_01/dbo.delete_po_receipt_documents_$sp.md)
- [me_01: dbo.delete_rtv_documents_$sp](../../StoredProcedures/me_01/dbo.delete_rtv_documents_$sp.md)
- [me_01: dbo.delete_shrink_adj_documents_$sp](../../StoredProcedures/me_01/dbo.delete_shrink_adj_documents_$sp.md)
- [me_01: dbo.delete_ss_adj_documents_$sp](../../StoredProcedures/me_01/dbo.delete_ss_adj_documents_$sp.md)
- [me_01: dbo.delete_store_shipment_documents_$sp](../../StoredProcedures/me_01/dbo.delete_store_shipment_documents_$sp.md)
- [me_01: dbo.delete_transfer_documents_$sp](../../StoredProcedures/me_01/dbo.delete_transfer_documents_$sp.md)
- [me_01: dbo.delete_udt_documents_$sp](../../StoredProcedures/me_01/dbo.delete_udt_documents_$sp.md)
- [me_01: dbo.delete_uns_receipt_documents_$sp](../../StoredProcedures/me_01/dbo.delete_uns_receipt_documents_$sp.md)
- [me_01: dbo.import_asn_batch_$sp](../../StoredProcedures/me_01/dbo.import_asn_batch_$sp.md)
- [me_01: dbo.import_asn_seventh_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_seventh_step_$sp.md)
- [me_01: dbo.no_wms_create_ss_$sp](../../StoredProcedures/me_01/dbo.no_wms_create_ss_$sp.md)
- [me_01: dbo.pop_25Nov25_temp_ib_inv_$sp](../../StoredProcedures/me_01/dbo.pop_25Nov25_temp_ib_inv_$sp.md)
- [me_01: dbo.populate_im_sale_from_file_$sp](../../StoredProcedures/me_01/dbo.populate_im_sale_from_file_$sp.md)
- [me_01: dbo.populate_im_sale_from_SA_$sp](../../StoredProcedures/me_01/dbo.populate_im_sale_from_SA_$sp.md)
- [me_01: dbo.populate_temp_asn_$sp](../../StoredProcedures/me_01/dbo.populate_temp_asn_$sp.md)
- [me_01: dbo.populate_temp_ib_inventory_$sp](../../StoredProcedures/me_01/dbo.populate_temp_ib_inventory_$sp.md)
- [me_01: dbo.populate_temp_po_receipt_$sp](../../StoredProcedures/me_01/dbo.populate_temp_po_receipt_$sp.md)
- [me_01: dbo.post_cust_order_return_$sp](../../StoredProcedures/me_01/dbo.post_cust_order_return_$sp.md)
- [me_01: dbo.process_modified_transactions_$sp](../../StoredProcedures/me_01/dbo.process_modified_transactions_$sp.md)
- [me_01: dbo.validate_import_asn_tables_$sp](../../StoredProcedures/me_01/dbo.validate_import_asn_tables_$sp.md)
- [me_01: dbo.xfers_from_distro_$sp](../../StoredProcedures/me_01/dbo.xfers_from_distro_$sp.md)

