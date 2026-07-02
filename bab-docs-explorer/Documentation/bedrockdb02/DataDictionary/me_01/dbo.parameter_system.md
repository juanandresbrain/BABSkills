# dbo.parameter_system

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| parameter_system_id | tinyint | 1 | 0 | YES |  |  |
| size_concatenation_delimiter | nvarchar | 2 | 1 |  |  |  |
| unit_weight_id | tinyint | 1 | 0 |  |  |  |
| unit_linear_id | tinyint | 1 | 0 |  |  |  |
| size_grid_link_style_req_flag | bit | 1 | 0 |  |  |  |
| default_price_status_id | smallint | 2 | 0 |  |  |  |
| pseudo_price_status_id | smallint | 2 | 0 |  |  |  |
| class_hierarchy_level_id | int | 4 | 1 |  |  |  |
| department_hierarchy_level_id | int | 4 | 1 |  |  |  |
| style_plu_description_default | smallint | 2 | 0 |  |  |  |
| auto_assign_style_flag | bit | 1 | 0 |  |  |  |
| style_mask_min_length | tinyint | 1 | 0 |  |  |  |
| style_mask_max_length | tinyint | 1 | 0 |  |  |  |
| style_mask_delimiter1 | nchar | 2 | 1 |  |  |  |
| style_mask_delimiter2 | nchar | 2 | 1 |  |  |  |
| style_mask_delimiter3 | nchar | 2 | 1 |  |  |  |
| style_mask_delimiter4 | nchar | 2 | 1 |  |  |  |
| style_mask_delimiter5 | nchar | 2 | 1 |  |  |  |
| style_mask_start_position1 | tinyint | 1 | 1 |  |  |  |
| style_mask_start_position2 | tinyint | 1 | 1 |  |  |  |
| style_mask_start_position3 | tinyint | 1 | 1 |  |  |  |
| style_mask_start_position4 | tinyint | 1 | 1 |  |  |  |
| style_mask_start_position5 | tinyint | 1 | 1 |  |  |  |
| style_mask_end_position1 | tinyint | 1 | 1 |  |  |  |
| style_mask_end_position2 | tinyint | 1 | 1 |  |  |  |
| style_mask_end_position3 | tinyint | 1 | 1 |  |  |  |
| style_mask_end_position4 | tinyint | 1 | 1 |  |  |  |
| style_mask_end_position5 | tinyint | 1 | 1 |  |  |  |
| style_mask_source1 | nvarchar | 2 | 1 |  |  |  |
| style_mask_source2 | nvarchar | 2 | 1 |  |  |  |
| style_mask_source3 | nvarchar | 2 | 1 |  |  |  |
| style_mask_source4 | nvarchar | 2 | 1 |  |  |  |
| style_mask_source5 | nvarchar | 2 | 1 |  |  |  |
| z_number_mask | tinyint | 1 | 1 |  |  |  |
| z_number_from_range | nvarchar | 40 | 1 |  |  |  |
| z_number_to_range | nvarchar | 40 | 1 |  |  |  |
| unit_area_id | tinyint | 1 | 0 |  |  |  |
| comp_date_weeks_aft_open_date | smallint | 2 | 0 |  |  |  |
| vendor_code_mask | nvarchar | 40 | 0 |  |  |  |
| location_code_mask | nvarchar | 40 | 0 |  |  |  |
| edi_interchange_id_qualifier | nvarchar | 4 | 0 |  |  |  |
| edi_interchange_id_code | nvarchar | 20 | 0 |  |  |  |
| edi_send_loc_id_qualifier | nvarchar | 4 | 0 |  |  |  |
| edi_send_loc_id_code | nvarchar | 20 | 1 |  |  |  |
| edi_rec_loc_id_qualifier | nvarchar | 4 | 0 |  |  |  |
| edi_version_id | tinyint | 1 | 0 |  |  |  |
| edi_850_dtm_cancel_after_flag | bit | 1 | 0 |  |  |  |
| edi_850_dtm_delivery_req_flag | bit | 1 | 0 |  |  |  |
| edi_850_dtm_effective_flag | bit | 1 | 0 |  |  |  |
| edi_850_ctp_msr_flag | bit | 1 | 0 |  |  |  |
| edi_850_ctp_resale_flag | bit | 1 | 0 |  |  |  |
| upc_z_number_from_range | decimal | 9 | 0 |  |  |  |
| upc_z_number_to_range | decimal | 9 | 0 |  |  |  |
| upc_internal_chck_dgt_req_flag | bit | 1 | 0 |  |  |  |
| upc_inh_mask_start_position1 | tinyint | 1 | 1 |  |  |  |
| upc_inh_mask_start_position2 | tinyint | 1 | 1 |  |  |  |
| upc_inh_mask_start_position3 | tinyint | 1 | 1 |  |  |  |
| upc_inh_mask_start_position4 | tinyint | 1 | 1 |  |  |  |
| upc_inh_mask_start_position5 | tinyint | 1 | 1 |  |  |  |
| upc_inh_mask_end_position1 | tinyint | 1 | 1 |  |  |  |
| upc_inh_mask_end_position2 | tinyint | 1 | 1 |  |  |  |
| upc_inh_mask_end_position3 | tinyint | 1 | 1 |  |  |  |
| upc_inh_mask_end_position4 | tinyint | 1 | 1 |  |  |  |
| upc_inh_mask_end_position5 | tinyint | 1 | 1 |  |  |  |
| upc_inh_mask_source1 | nvarchar | 2 | 1 |  |  |  |
| upc_inh_mask_source2 | nvarchar | 2 | 1 |  |  |  |
| upc_inh_mask_source3 | nvarchar | 2 | 1 |  |  |  |
| upc_inh_mask_source4 | nvarchar | 2 | 1 |  |  |  |
| upc_inh_mask_source5 | nvarchar | 2 | 1 |  |  |  |
| ib_price_discrep_inc_pc_type | smallint | 2 | 0 |  |  |  |
| ib_price_discrep_inc_location | smallint | 2 | 0 |  |  |  |
| ib_price_discrep_decr_pc_type | smallint | 2 | 0 |  |  |  |
| ib_price_discrep_decr_location | smallint | 2 | 0 |  |  |  |
| ib_unit_discrepancy | smallint | 2 | 0 |  |  |  |
| ib_promotions | smallint | 2 | 0 |  |  |  |
| rtp_gen_upon_uns_rec_flag | bit | 1 | 0 |  |  |  |
| rtp_gen_upon_pc_appr_flag | bit | 1 | 0 |  |  |  |
| rtp_gen_frm_asn_for_edi_flag | bit | 1 | 0 |  |  |  |
| rtp_print_options | smallint | 2 | 0 |  |  |  |
| rtp_allow_override_flag | bit | 1 | 0 |  |  |  |
| tkt_override_tkt_price_flag | bit | 1 | 0 |  |  |  |
| tkt_safety_stock_amt | int | 4 | 0 |  |  |  |
| tkt_safety_stock_percent | decimal | 5 | 0 |  |  |  |
| tkt_safety_stock_max_safe_unit | int | 4 | 0 |  |  |  |
| tkt_cleanup_batch_size | smallint | 2 | 0 |  |  |  |
| tkt_days_to_keep_printed_tkts | smallint | 2 | 0 |  |  |  |
| tkt_days_to_keep_non_print_tkt | smallint | 2 | 0 |  |  |  |
| tkt_override_tkt_upc_val_flag | bit | 1 | 0 |  |  |  |
| tkt_upc_type_order | smallint | 2 | 0 |  |  |  |
| sl_history_retention | tinyint | 1 | 0 |  |  |  |
| sku_transaction_retention | smallint | 2 | 0 |  |  |  |
| installed_4wall_flag | bit | 1 | 0 |  |  |  |
| installed_envue_flag | bit | 1 | 0 |  |  |  |
| installed_im_flag | bit | 1 | 0 |  |  |  |
| installed_invmtch_flag | bit | 1 | 0 |  |  |  |
| installed_mms_flag | bit | 1 | 0 |  |  |  |
| installed_om_flag | bit | 1 | 0 |  |  |  |
| installed_pcm_flag | bit | 1 | 0 |  |  |  |
| installed_plu_flag | bit | 1 | 0 |  |  |  |
| installed_pom_flag | bit | 1 | 0 |  |  |  |
| installed_replen_flag | bit | 1 | 0 |  |  |  |
| installed_sl_flag | bit | 1 | 0 |  |  |  |
| installed_sourcing_flag | bit | 1 | 0 |  |  |  |
| installed_upc_lu_flag | bit | 1 | 0 |  |  |  |
| company_name | nvarchar | 80 | 1 |  |  |  |
| default_register_type_id | tinyint | 1 | 1 |  |  |  |
| restrict_by_employee_pos_flag | bit | 1 | 0 |  |  |  |
| multi_sales_jurisdiction_flag | bit | 1 | 0 |  |  |  |
| ma_reclass_history_to_move | smallint | 2 | 0 |  |  |  |
| reclass_adj_trans_reason_id | smallint | 2 | 1 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| last_item_id | decimal | 9 | 1 |  |  |  |
| installed_oim_flag | bit | 1 | 0 |  |  |  |
| size_category_code_max_length | tinyint | 1 | 1 |  |  |  |
| size_code_max_length | tinyint | 1 | 1 |  |  |  |
| company_id | decimal | 5 | 1 |  |  |  |
| om_transfer_evaluation | tinyint | 1 | 0 |  |  |  |
| installed_distro_no_wms_flag | bit | 1 | 0 |  |  |  |
| tkt_print_on_hand_pcm_flag | bit | 1 | 0 |  |  |  |
| tkt_print_on_order_pcm_flag | bit | 1 | 0 |  |  |  |
| installed_planning_flag | bit | 1 | 0 |  |  |  |
| copy_style_attributes_flag | bit | 1 | 0 |  |  |  |
| allow_non_empty_trees_flag | bit | 1 | 0 |  |  |  |
| send_rim_cost_to_ma_flag | bit | 1 | 0 |  |  |  |
| ib_average_cost_location_level | tinyint | 1 | 0 |  |  |  |
| installed_imweb_flag | bit | 1 | 0 |  |  |  |
| installed_es_flag | bit | 1 | 0 |  |  |  |
| es_location_group_level_id | int | 4 | 1 |  |  |  |
| es_refresh_dest_directory | nvarchar | 100 | 1 |  |  |  |
| last_ib_inventory_id | decimal | 9 | 0 |  |  |  |
| last_ib_allocation_id | decimal | 9 | 0 |  |  |  |
| ib_po_rcpt_posting_date_type | tinyint | 1 | 0 |  |  |  |
| installed_asrtmnt_plng_flag | bit | 1 | 0 |  |  |  |
| send_rtv_to_sourcing_flag | bit | 1 | 0 |  |  |  |
| apply_inv_cost_factors_flag | bit | 1 | 0 |  |  |  |
| sell_thru_weeks | smallint | 2 | 0 |  |  |  |
| sell_thru_inventory_status | smallint | 2 | 0 |  |  |  |
| installed_standalone_ar_flag | bit | 1 | 0 |  |  |  |
| maintain_sz_scales_for_ap_flag | bit | 1 | 0 |  |  |  |
| ib_average_cost_type | nchar | 2 | 0 |  |  |  |
| ib_average_cost_cleanup_days | smallint | 2 | 1 |  |  |  |
| es_refresh_inprog_directory | nvarchar | 100 | 1 |  |  |  |
| address_state_max_length | tinyint | 1 | 0 |  |  |  |
| ib_po_rcpt_keep_in_transit_days | smallint | 2 | 1 |  |  |  |
| ib_po_rcpt_move_in_transit_to_discrepancy | smallint | 2 | 0 |  |  |  |
| ib_average_cost_merch_level | tinyint | 1 | 0 |  |  |  |
| ib_om_cost_discrep_location | smallint | 2 | 0 |  |  |  |
| installed_eom_flag | bit | 1 | 0 |  |  |  |
| use_future_inventory_flag | bit | 1 | 0 |  |  |  |
| system_unique_vendor_style_flag | bit | 1 | 0 |  |  |  |
| eom_use_vendor_style_flag | bit | 1 | 0 |  |  |  |
| eom_send_vendor_upc_flag | bit | 1 | 0 |  |  |  |
| track_intercompany_transactions_flag | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.adjust_future_reserve_$sp](../../StoredProcedures/me_01/dbo.adjust_future_reserve_$sp.md)
- [me_01: dbo.adjust_reserve_remnant_cost_$sp](../../StoredProcedures/me_01/dbo.adjust_reserve_remnant_cost_$sp.md)
- [me_01: dbo.complete_sales_posting_$sp](../../StoredProcedures/me_01/dbo.complete_sales_posting_$sp.md)
- [me_01: dbo.delete_asn_documents_$sp](../../StoredProcedures/me_01/dbo.delete_asn_documents_$sp.md)
- [me_01: dbo.delete_imrd_documents_$sp](../../StoredProcedures/me_01/dbo.delete_imrd_documents_$sp.md)
- [me_01: dbo.delete_inv_control_documents_$sp](../../StoredProcedures/me_01/dbo.delete_inv_control_documents_$sp.md)
- [me_01: dbo.dl_style_task_validate_$sp](../../StoredProcedures/me_01/dbo.dl_style_task_validate_$sp.md)
- [me_01: dbo.dl_validate_import_upc_$sp](../../StoredProcedures/me_01/dbo.dl_validate_import_upc_$sp.md)
- [me_01: dbo.eom_complete_$sp](../../StoredProcedures/me_01/dbo.eom_complete_$sp.md)
- [me_01: dbo.eom_reserve_$sp](../../StoredProcedures/me_01/dbo.eom_reserve_$sp.md)
- [me_01: dbo.es_init_worktables_$sp](../../StoredProcedures/me_01/dbo.es_init_worktables_$sp.md)
- [me_01: dbo.get_avg_cost_$sp](../../StoredProcedures/me_01/dbo.get_avg_cost_$sp.md)
- [me_01: dbo.get_pc_instruction_values_$sp](../../StoredProcedures/me_01/dbo.get_pc_instruction_values_$sp.md)
- [me_01: dbo.get_pricing_$sp](../../StoredProcedures/me_01/dbo.get_pricing_$sp.md)
- [me_01: dbo.get_pricing_pg_$sp](../../StoredProcedures/me_01/dbo.get_pricing_pg_$sp.md)
- [me_01: dbo.get_retails_MA_$sp](../../StoredProcedures/me_01/dbo.get_retails_MA_$sp.md)
- [me_01: dbo.import_asn_batch_$sp](../../StoredProcedures/me_01/dbo.import_asn_batch_$sp.md)
- [me_01: dbo.import_asn_first_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_first_step_$sp.md)
- [me_01: dbo.import_asn_second_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_second_step_$sp.md)
- [me_01: dbo.import_pc_batch_$sp](../../StoredProcedures/me_01/dbo.import_pc_batch_$sp.md)
- [me_01: dbo.import_pc_validate_$sp](../../StoredProcedures/me_01/dbo.import_pc_validate_$sp.md)
- [me_01: dbo.no_wms_create_ss_$sp](../../StoredProcedures/me_01/dbo.no_wms_create_ss_$sp.md)
- [me_01: dbo.on_order_cancel_$sp](../../StoredProcedures/me_01/dbo.on_order_cancel_$sp.md)
- [me_01: dbo.on_order_reduction_$sp](../../StoredProcedures/me_01/dbo.on_order_reduction_$sp.md)
- [me_01: dbo.on_order_reduction_pseudo_$sp](../../StoredProcedures/me_01/dbo.on_order_reduction_pseudo_$sp.md)
- [me_01: dbo.on_order_reinstate_$sp](../../StoredProcedures/me_01/dbo.on_order_reinstate_$sp.md)
- [me_01: dbo.pi_post_actual_shrink_loc_$sp](../../StoredProcedures/me_01/dbo.pi_post_actual_shrink_loc_$sp.md)
- [me_01: dbo.pi_post_pending_shrink_loc_$sp](../../StoredProcedures/me_01/dbo.pi_post_pending_shrink_loc_$sp.md)
- [me_01: dbo.pop_25Nov25_temp_ib_inv_$sp](../../StoredProcedures/me_01/dbo.pop_25Nov25_temp_ib_inv_$sp.md)
- [me_01: dbo.pop_25nov25_temp_sale_master_$sp](../../StoredProcedures/me_01/dbo.pop_25nov25_temp_sale_master_$sp.md)
- [me_01: dbo.pop_fixed_avg_cost_by_jurisdiction_$sp](../../StoredProcedures/me_01/dbo.pop_fixed_avg_cost_by_jurisdiction_$sp.md)
- [me_01: dbo.pop_fixed_avg_cost_for_pseudo_style_$sp](../../StoredProcedures/me_01/dbo.pop_fixed_avg_cost_for_pseudo_style_$sp.md)
- [me_01: dbo.populate_dynamic_average_cost_$sp](../../StoredProcedures/me_01/dbo.populate_dynamic_average_cost_$sp.md)
- [me_01: dbo.populate_fixed_average_cost_by_location_$sp](../../StoredProcedures/me_01/dbo.populate_fixed_average_cost_by_location_$sp.md)
- [me_01: dbo.populate_im_sale_from_file_$sp](../../StoredProcedures/me_01/dbo.populate_im_sale_from_file_$sp.md)
- [me_01: dbo.populate_im_sale_from_SA_$sp](../../StoredProcedures/me_01/dbo.populate_im_sale_from_SA_$sp.md)
- [me_01: dbo.populate_multi_currency_location_$sp](../../StoredProcedures/me_01/dbo.populate_multi_currency_location_$sp.md)
- [me_01: dbo.populate_temp_ib_inventory_$sp](../../StoredProcedures/me_01/dbo.populate_temp_ib_inventory_$sp.md)
- [me_01: dbo.populate_temp_po_receipt_$sp](../../StoredProcedures/me_01/dbo.populate_temp_po_receipt_$sp.md)
- [me_01: dbo.populate_temp_sale_master_$sp](../../StoredProcedures/me_01/dbo.populate_temp_sale_master_$sp.md)
- [me_01: dbo.post_25Nov25_cust_order_sale_$sp](../../StoredProcedures/me_01/dbo.post_25Nov25_cust_order_sale_$sp.md)
- [me_01: dbo.post_beg_inv_loc_$sp](../../StoredProcedures/me_01/dbo.post_beg_inv_loc_$sp.md)
- [me_01: dbo.post_cust_order_return_$sp](../../StoredProcedures/me_01/dbo.post_cust_order_return_$sp.md)
- [me_01: dbo.post_cust_order_sale_$sp](../../StoredProcedures/me_01/dbo.post_cust_order_sale_$sp.md)
- [me_01: dbo.post_inventory_loc_$sp](../../StoredProcedures/me_01/dbo.post_inventory_loc_$sp.md)
- [me_01: dbo.post_pending_loc_$sp](../../StoredProcedures/me_01/dbo.post_pending_loc_$sp.md)
- [me_01: dbo.post_sales_batch_$sp](../../StoredProcedures/me_01/dbo.post_sales_batch_$sp.md)
- [me_01: dbo.prep_fixed_avg_cost_calculation_$sp](../../StoredProcedures/me_01/dbo.prep_fixed_avg_cost_calculation_$sp.md)
- [me_01: dbo.process_modified_transactions_$sp](../../StoredProcedures/me_01/dbo.process_modified_transactions_$sp.md)
- [me_01: dbo.retrieve_dist_$sp](../../StoredProcedures/me_01/dbo.retrieve_dist_$sp.md)
- [me_01: dbo.set_delivery_dates_$sp](../../StoredProcedures/me_01/dbo.set_delivery_dates_$sp.md)
- [me_01: dbo.startup_discrepancy_ib_cfd_$sp](../../StoredProcedures/me_01/dbo.startup_discrepancy_ib_cfd_$sp.md)
- [me_01: dbo.startup_discrepancy_ib_inv_$sp](../../StoredProcedures/me_01/dbo.startup_discrepancy_ib_inv_$sp.md)
- [me_01: dbo.startup_discrepancy_ib_oo_$sp](../../StoredProcedures/me_01/dbo.startup_discrepancy_ib_oo_$sp.md)
- [me_01: dbo.startup_ib_cost_factor_discount_$sp](../../StoredProcedures/me_01/dbo.startup_ib_cost_factor_discount_$sp.md)
- [me_01: dbo.startup_ib_inventory_$sp](../../StoredProcedures/me_01/dbo.startup_ib_inventory_$sp.md)
- [me_01: dbo.startup_ib_on_order_$sp](../../StoredProcedures/me_01/dbo.startup_ib_on_order_$sp.md)

