# dbo.parameter_pom

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| parameter_pom_id | tinyint | 1 | 0 | YES |  |  |
| gen_tkts_frm_warehouse_code | smallint | 2 | 0 |  |  |  |
| update_current_cost_code | smallint | 2 | 0 |  |  |  |
| manual_po_no_mask | nvarchar | 40 | 0 |  |  |  |
| first_manual_po_no | nvarchar | 40 | 0 |  |  |  |
| last_manual_po_no | nvarchar | 40 | 0 |  |  |  |
| system_po_no_mask | nvarchar | 40 | 0 |  |  |  |
| first_system_po_no | nvarchar | 40 | 0 |  |  |  |
| last_system_po_no | nvarchar | 40 | 0 |  |  |  |
| last_generated_po_no | nvarchar | 40 | 1 |  |  |  |
| last_generated_allocation_no | nvarchar | 40 | 0 |  |  |  |
| def_expected_receipt_date_days | smallint | 2 | 1 |  |  |  |
| def_expected_sys_cancel_days | smallint | 2 | 1 |  |  |  |
| using_po_approval_flag | bit | 1 | 0 |  |  |  |
| approve_sending_edi_flag | bit | 1 | 0 |  |  |  |
| approve_printing_flag | bit | 1 | 0 |  |  |  |
| approve_blanket_po_flag | bit | 1 | 0 |  |  |  |
| approve_release_po_flag | bit | 1 | 0 |  |  |  |
| approve_standalone_po_flag | bit | 1 | 0 |  |  |  |
| approve_special_po_flag | bit | 1 | 0 |  |  |  |
| approval_sets_order_date_flag | bit | 1 | 0 |  |  |  |
| reapprove_cost_changes_flag | bit | 1 | 0 |  |  |  |
| reapprove_unit_changes_flag | bit | 1 | 0 |  |  |  |
| reapprove_otb_period_flag | bit | 1 | 0 |  |  |  |
| reapprove_reinstated_flag | bit | 1 | 0 |  |  |  |
| reapprove_location_flag | bit | 1 | 0 |  |  |  |
| auto_resend_after_reapp_flag | bit | 1 | 0 |  |  |  |
| auto_reprint_after_reapp_flag | bit | 1 | 0 |  |  |  |
| prompt_to_print_mods_flag | bit | 1 | 0 |  |  |  |
| po_no_rec_flag | bit | 1 | 0 |  |  |  |
| update_blanket_po_units_flag | bit | 1 | 0 |  |  |  |
| po_cancel_days_late | smallint | 2 | 1 |  |  |  |
| po_cancel_percent_complete | decimal | 5 | 1 |  |  |  |
| po_cancel_calculation_level | smallint | 2 | 1 |  |  |  |
| rec_loc_address_type_to_print | smallint | 2 | 1 |  |  |  |
| ven_loc_address_type_to_print | smallint | 2 | 1 |  |  |  |
| po_cancel_cleanup_weeks | smallint | 2 | 0 |  |  |  |
| po_preliminary_cleanup_weeks | smallint | 2 | 0 |  |  |  |
| exchange_rate_in_effect_on | smallint | 2 | 0 |  |  |  |
| upc_type | tinyint | 1 | 0 |  |  |  |
| po_cancel_days_and_percnt_flag | bit | 1 | 0 |  |  |  |
| prevent_po_cancel_rcpts_flag | bit | 1 | 0 |  |  |  |
| system_cancel_date_to_sourcing | smallint | 2 | 1 |  |  |  |
| from_delivery_date_to_sourcing | smallint | 2 | 1 |  |  |  |
| to_delivery_date_to_sourcing | smallint | 2 | 1 |  |  |  |
| in_warehouse_po_date_type_id | decimal | 9 | 1 |  |  |  |
| ship_date_po_date_type_id | decimal | 9 | 1 |  |  |  |
| po_header_msg_type_id | decimal | 9 | 1 |  |  |  |
| po_line_msg_type_id | decimal | 9 | 1 |  |  |  |
| send_po_modify_to_ar_flag | bit | 1 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| update_blanket_po_incrs_flag | bit | 1 | 0 |  |  |  |
| update_blanket_po_decrs_flag | bit | 1 | 0 |  |  |  |
| auto_retrieve_retails_flag | bit | 1 | 0 |  |  |  |
| auto_export_po_sku_upc | smallint | 2 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.import_asn_forth_step_$sp](../../StoredProcedures/me_01/dbo.import_asn_forth_step_$sp.md)
- [me_01: dbo.retrieve_dist_$sp](../../StoredProcedures/me_01/dbo.retrieve_dist_$sp.md)
- [me_01: dbo.rpt_get_address_for_po_$sp](../../StoredProcedures/me_01/dbo.rpt_get_address_for_po_$sp.md)
- [me_01: dbo.rpt_get_pos_$sp](../../StoredProcedures/me_01/dbo.rpt_get_pos_$sp.md)

