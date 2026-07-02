# dbo.dl_style

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| dl_style_id | bigint | 8 | 0 | YES |  |  |
| record_no | bigint | 8 | 0 |  |  |  |
| style_code | nvarchar | 40 | 1 |  |  |  |
| hierarchy_group_code | nvarchar | 40 | 0 |  |  |  |
| merch_type | tinyint | 1 | 0 |  |  |  |
| style_status | smallint | 2 | 0 |  |  |  |
| long_desc | nvarchar | 240 | 1 |  |  |  |
| short_desc | nvarchar | 40 | 1 |  |  |  |
| season_code | nvarchar | 4 | 0 |  |  |  |
| calendar_year_code | smallint | 2 | 1 |  |  |  |
| ticket_format_code | nvarchar | 4 | 1 |  |  |  |
| weight | decimal | 9 | 1 |  |  |  |
| height | decimal | 9 | 1 |  |  |  |
| width | decimal | 9 | 1 |  |  |  |
| depth | decimal | 9 | 1 |  |  |  |
| plu_desc | nvarchar | 80 | 1 |  |  |  |
| position_code | nvarchar | 40 | 0 |  |  |  |
| promo_flag | bit | 1 | 1 |  |  |  |
| inhouse_upc_flag | bit | 1 | 1 |  |  |  |
| vendor_upc_flag | bit | 1 | 1 |  |  |  |
| reorder_flag | bit | 1 | 1 |  |  |  |
| fashion_flag | bit | 1 | 1 |  |  |  |
| consignment_flag | bit | 1 | 1 |  |  |  |
| replenishable_flag | bit | 1 | 1 |  |  |  |
| create_date | smalldatetime | 4 | 1 |  |  |  |
| order_multiple | int | 4 | 1 |  |  |  |
| distribution_multiple | int | 4 | 1 |  |  |  |
| target_selling_from_week | tinyint | 1 | 1 |  |  |  |
| target_selling_from_year | int | 4 | 1 |  |  |  |
| target_selling_to_week | tinyint | 1 | 1 |  |  |  |
| target_selling_to_year | int | 4 | 1 |  |  |  |
| original_selling_retail | decimal | 9 | 1 |  |  |  |
| original_price_status_code | nvarchar | 6 | 1 |  |  |  |
| compare_at_retail | decimal | 9 | 1 |  |  |  |
| size_grid_code | nvarchar | 16 | 1 |  |  |  |
| vendor_code | nvarchar | 40 | 1 |  |  |  |
| vendor_style | nvarchar | 80 | 1 |  |  |  |
| current_cost | decimal | 9 | 1 |  |  |  |
| current_cost_currency_code | nvarchar | 6 | 1 |  |  |  |
| active_flag | bit | 1 | 1 |  |  |  |
| mix_match_rule_code_1 | int | 4 | 1 |  |  |  |
| mix_match_rule_code_2 | int | 4 | 1 |  |  |  |
| mix_match_rule_code_3 | int | 4 | 1 |  |  |  |
| mix_match_rule_code_4 | int | 4 | 1 |  |  |  |
| current_selling_retail | decimal | 9 | 1 |  |  |  |
| current_price_status_code | nvarchar | 6 | 1 |  |  |  |
| last_net_final_po_cost | decimal | 9 | 1 |  |  |  |
| last_receipt_date | smalldatetime | 4 | 1 |  |  |  |
| allow_customer_back_order_flag | bit | 1 | 1 |  |  |  |
| resulting_po_predistrib_type | smallint | 2 | 1 |  |  |  |
| valid_flag | bit | 1 | 0 |  |  |  |
| style_code_not_upper_flag | bit | 1 | 0 |  |  |  |
| vendor_style_not_upper_flag | bit | 1 | 0 |  |  |  |
| dup_style_code_flag | bit | 1 | 0 |  |  |  |
| dup_vndr_code_vndr_style_flag | bit | 1 | 0 |  |  |  |
| stl_cd_vd_cd_in_dl_stl_vd_flag | bit | 1 | 0 |  |  |  |
| vd_cd_vd_stl_in_dl_stl_vd_flg | bit | 1 | 0 |  |  |  |
| stl_cd_jr_cd_in_dl_stl_ret_flg | bit | 1 | 0 |  |  |  |
| style_cd_on_file_flag | bit | 1 | 0 |  |  |  |
| vndr_cd_vndr_style_on_file_flg | bit | 1 | 0 |  |  |  |
| style_code_missing_flag | bit | 1 | 0 |  |  |  |
| style_code_length_invalid_flag | bit | 1 | 0 |  |  |  |
| merch_group_cd_fk_invalid_flag | bit | 1 | 0 |  |  |  |
| long_desc_missing_flag | bit | 1 | 0 |  |  |  |
| season_code_fk_invalid_flag | bit | 1 | 0 |  |  |  |
| calendar_yr_code_missing_flag | bit | 1 | 0 |  |  |  |
| calendar_yr_cd_fk_invalid_flag | bit | 1 | 0 |  |  |  |
| ticket_fmt_cd_fk_invalid_flag | bit | 1 | 0 |  |  |  |
| position_code_fk_invalid_flag | bit | 1 | 0 |  |  |  |
| order_distro_mult_incompat_flg | bit | 1 | 0 |  |  |  |
| target_from_wk_missing_flag | bit | 1 | 0 |  |  |  |
| target_from_yr_missing_flag | bit | 1 | 0 |  |  |  |
| target_from_yr_fk_invalid_flag | bit | 1 | 0 |  |  |  |
| target_from_wk_fk_invalid_flag | bit | 1 | 0 |  |  |  |
| target_to_wk_missing_flag | bit | 1 | 0 |  |  |  |
| target_to_yr_missing_flag | bit | 1 | 0 |  |  |  |
| target_to_yr_fk_invalid_flag | bit | 1 | 0 |  |  |  |
| target_to_wk_fk_invalid_flag | bit | 1 | 0 |  |  |  |
| target_to_wk_before_frm_wk_flg | bit | 1 | 0 |  |  |  |
| original_retail_missing_flag | bit | 1 | 0 |  |  |  |
| original_retail_for_pseudo_flg | bit | 1 | 0 |  |  |  |
| orig_prc_stat_cd_fk_invld_flg | bit | 1 | 0 |  |  |  |
| orig_prc_stat_cd_for_psdo_flag | bit | 1 | 0 |  |  |  |
| comp_retail_under_original_flg | bit | 1 | 0 |  |  |  |
| comp_retail_under_current_flg | bit | 1 | 0 |  |  |  |
| comp_retail_for_pseudo_flag | bit | 1 | 0 |  |  |  |
| size_grid_cd_missing_flag | bit | 1 | 0 |  |  |  |
| size_grid_cd_fk_invalid_flag | bit | 1 | 0 |  |  |  |
| size_grid_cd_for_non_sized_flg | bit | 1 | 0 |  |  |  |
| vendor_code_missing_flag | bit | 1 | 0 |  |  |  |
| vendor_code_fk_invalid_flag | bit | 1 | 0 |  |  |  |
| vendor_style_missing_flag | bit | 1 | 0 |  |  |  |
| vendor_style_for_pseudo_flag | bit | 1 | 0 |  |  |  |
| current_cost_missing_flag | bit | 1 | 0 |  |  |  |
| current_cost_for_pseudo_flag | bit | 1 | 0 |  |  |  |
| curr_cost_curn_cd_fk_invld_flg | bit | 1 | 0 |  |  |  |
| curr_cost_curn_cd_for_psdo_flg | bit | 1 | 0 |  |  |  |
| mix_match_rl_cd_1_fk_invld_flg | bit | 1 | 0 |  |  |  |
| mix_match_rl_cd_1_for_psdo_flg | bit | 1 | 0 |  |  |  |
| mix_match_rl_cd_2_fk_invld_flg | bit | 1 | 0 |  |  |  |
| mix_match_rl_cd_2_repeat_flag | bit | 1 | 0 |  |  |  |
| mix_match_rl_cd_2_for_psdo_flg | bit | 1 | 0 |  |  |  |
| mix_match_rl_cd_3_fk_invld_flg | bit | 1 | 0 |  |  |  |
| mix_match_rl_cd_3_repeat_flag | bit | 1 | 0 |  |  |  |
| mix_match_rl_cd_3_for_psdo_flg | bit | 1 | 0 |  |  |  |
| mix_match_rl_cd_4_fk_invld_flg | bit | 1 | 0 |  |  |  |
| mix_match_rl_cd_4_repeat_flag | bit | 1 | 0 |  |  |  |
| mix_match_rl_cd_4_for_psdo_flg | bit | 1 | 0 |  |  |  |
| current_retail_for_pseudo_flag | bit | 1 | 0 |  |  |  |
| curr_prc_stat_cd_fk_invld_flg | bit | 1 | 0 |  |  |  |
| curr_prc_stat_cd_for_psdo_flag | bit | 1 | 0 |  |  |  |
| last_receipt_date_missing_flag | bit | 1 | 0 |  |  |  |
| result_po_type_missing_flag | bit | 1 | 0 |  |  |  |
| result_po_type_when_no_ar_flag | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.dl_style_task_imp_ld_prep_$sp](../../StoredProcedures/me_01/dbo.dl_style_task_imp_ld_prep_$sp.md)
- [me_01: dbo.dl_style_task_imp_trunc_$sp](../../StoredProcedures/me_01/dbo.dl_style_task_imp_trunc_$sp.md)
- [me_01: dbo.dl_style_task_validate_$sp](../../StoredProcedures/me_01/dbo.dl_style_task_validate_$sp.md)

