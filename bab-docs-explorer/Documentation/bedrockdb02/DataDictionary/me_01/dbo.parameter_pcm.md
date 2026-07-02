# dbo.parameter_pcm

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| parameter_pcm_id | tinyint | 1 | 0 | YES |  |  |
| pc_no_mask | nvarchar | 40 | 0 |  |  |  |
| first_pc_no | nvarchar | 40 | 0 |  |  |  |
| last_pc_no | nvarchar | 40 | 0 |  |  |  |
| last_generated_pc_no | nvarchar | 40 | 1 |  |  |  |
| deal_no_mask | nvarchar | 40 | 0 |  |  |  |
| first_deal_no | nvarchar | 40 | 0 |  |  |  |
| last_deal_no | nvarchar | 40 | 0 |  |  |  |
| last_generated_deal_no | nvarchar | 40 | 1 |  |  |  |
| assign_def_to_be_issued_date | smallint | 2 | 0 |  |  |  |
| auto_del_cancel_pc_after_days | smallint | 2 | 0 |  |  |  |
| auto_del_comp_pc_after_days | smallint | 2 | 0 |  |  |  |
| pc_approval_required_flag | bit | 1 | 0 |  |  |  |
| auto_approve_md_pc_flag | bit | 1 | 0 |  |  |  |
| auto_approve_mdc_pc_flag | bit | 1 | 0 |  |  |  |
| auto_approve_mixmatch_pc_flag | bit | 1 | 0 |  |  |  |
| auto_approve_mu_pc_flag | bit | 1 | 0 |  |  |  |
| auto_approve_muc_pc_flag | bit | 1 | 0 |  |  |  |
| remove_mixmatch_code_flag | bit | 1 | 0 |  |  |  |
| reset_retail_price_status_id | smallint | 2 | 1 |  |  |  |
| print_mix_match_doc_flag | bit | 1 | 0 |  |  |  |
| print_on_hand_styles_only_flag | bit | 1 | 0 |  |  |  |
| print_promo_pc_doc_flag | bit | 1 | 0 |  |  |  |
| print_units_on_hand_flag | bit | 1 | 0 |  |  |  |
| print_units_counted_col_flag | bit | 1 | 0 |  |  |  |
| print_upc_numbers_flag | bit | 1 | 0 |  |  |  |
| pc_no_rec_flag | bit | 1 | 0 |  |  |  |
| deal_no_rec_flag | bit | 1 | 0 |  |  |  |
| reapprove_pc_after_pg_flag | bit | 1 | 0 |  |  |  |
| auto_cancel_unapproved_pc | smallint | 2 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| auto_approve_deal_flag | bit | 1 | 0 |  |  |  |
| calculate_on_hand_flag | bit | 1 | 0 |  |  |  |
| price_by_instruction_flag | bit | 1 | 0 |  |  |  |
| allow_multi_jurisdiction_flag | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.copy_like_location_prices_$sp](../../StoredProcedures/me_01/dbo.copy_like_location_prices_$sp.md)
- [me_01: dbo.delete_pc_documents_$sp](../../StoredProcedures/me_01/dbo.delete_pc_documents_$sp.md)
- [me_01: dbo.get_pc_instruction_values_$sp](../../StoredProcedures/me_01/dbo.get_pc_instruction_values_$sp.md)
- [me_01: dbo.get_pricing_$sp](../../StoredProcedures/me_01/dbo.get_pricing_$sp.md)
- [me_01: dbo.import_pc_populate_temp_pc_$sp](../../StoredProcedures/me_01/dbo.import_pc_populate_temp_pc_$sp.md)
- [me_01: dbo.import_pc_validate_$sp](../../StoredProcedures/me_01/dbo.import_pc_validate_$sp.md)
- [me_01: dbo.move_pg_exceptions_to_locations_$sp](../../StoredProcedures/me_01/dbo.move_pg_exceptions_to_locations_$sp.md)
- [me_01: dbo.rpt_get_pos_$sp](../../StoredProcedures/me_01/dbo.rpt_get_pos_$sp.md)
- [me_01: dbo.upd_style_retails_pc_$sp](../../StoredProcedures/me_01/dbo.upd_style_retails_pc_$sp.md)

