# dbo.dl_style_task

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| dl_style_task_id | bigint | 8 | 0 | YES |  |  |
| in_progress_flag | bit | 1 | 0 |  |  |  |
| start_date | smalldatetime | 4 | 0 |  |  |  |
| current_phase | tinyint | 1 | 0 |  |  |  |
| action_type | tinyint | 1 | 0 |  |  |  |
| file_name | nvarchar | 510 | 0 |  |  |  |
| encoding | tinyint | 1 | 0 |  |  |  |
| max_rejects | bigint | 8 | 0 |  |  |  |
| temp_folder | nvarchar | 510 | 0 |  |  |  |
| threads | int | 4 | 0 |  |  |  |
| max_rows_per_batch | int | 4 | 0 |  |  |  |
| pct_rows_per_batch | float | 8 | 0 |  |  |  |
| total_schema_rejects | bigint | 8 | 0 |  |  |  |
| max_dl_style_id | bigint | 8 | 0 |  |  |  |
| max_dl_style_retail_id | bigint | 8 | 0 |  |  |  |
| max_dl_style_vendor_id | bigint | 8 | 0 |  |  |  |
| max_dl_style_attribute_set_id | bigint | 8 | 0 |  |  |  |
| max_dl_style_custom_prop_id | bigint | 8 | 0 |  |  |  |
| max_dl_style_attachment_id | bigint | 8 | 0 |  |  |  |
| max_dl_style_description_id | bigint | 8 | 0 |  |  |  |
| max_dl_upc_id | bigint | 8 | 0 |  |  |  |
| max_dl_pack_upc_id | bigint | 8 | 0 |  |  |  |
| max_dl_style_color_retail_id | bigint | 8 | 0 |  |  |  |
| max_dl_style_pricing_group_id | bigint | 8 | 0 |  |  |  |
| max_dl_style_prc_grp_color_id | bigint | 8 | 0 |  |  |  |
| max_dl_style_location_id | bigint | 8 | 0 |  |  |  |
| max_dl_style_location_color_id | bigint | 8 | 0 |  |  |  |
| max_dl_style_color_desc_id | bigint | 8 | 0 |  |  |  |
| max_dl_style_size_desc_id | bigint | 8 | 0 |  |  |  |
| max_dl_style_retail_default_id | bigint | 8 | 0 |  |  |  |
| max_dl_style_att_set_def_id | bigint | 8 | 0 |  |  |  |
| max_dl_style_color_id | bigint | 8 | 0 |  |  |  |
| max_dl_style_size_id | bigint | 8 | 0 |  |  |  |
| max_dl_sku_id | bigint | 8 | 0 |  |  |  |
| max_dl_style_clr_att_set_df_id | bigint | 8 | 0 |  |  |  |
| tot_dl_style_br_rej | bigint | 8 | 0 |  |  |  |
| tot_dl_style_retail_br_rej | bigint | 8 | 0 |  |  |  |
| tot_dl_style_vendor_br_rej | bigint | 8 | 0 |  |  |  |
| tot_dl_style_attr_set_br_rej | bigint | 8 | 0 |  |  |  |
| tot_dl_style_cust_prop_br_rej | bigint | 8 | 0 |  |  |  |
| tot_dl_style_attach_br_rej | bigint | 8 | 0 |  |  |  |
| tot_dl_style_desc_br_rej | bigint | 8 | 0 |  |  |  |
| tot_dl_upc_br_rej | bigint | 8 | 0 |  |  |  |
| tot_dl_pack_upc_br_rej | bigint | 8 | 0 |  |  |  |
| tot_dl_style_color_ret_br_rej | bigint | 8 | 0 |  |  |  |
| tot_dl_style_prc_grp_br_rej | bigint | 8 | 0 |  |  |  |
| tot_dl_stl_prc_grp_clr_br_rej | bigint | 8 | 0 |  |  |  |
| tot_dl_style_location_br_rej | bigint | 8 | 0 |  |  |  |
| tot_dl_style_loc_color_br_rej | bigint | 8 | 0 |  |  |  |
| tot_dl_style_color_desc_br_rej | bigint | 8 | 0 |  |  |  |
| tot_dl_style_size_desc_br_rej | bigint | 8 | 0 |  |  |  |
| last_vld_dl_style_id | bigint | 8 | 0 |  |  |  |
| last_vld_dl_style_retail_id | bigint | 8 | 0 |  |  |  |
| last_vld_dl_style_vendor_id | bigint | 8 | 0 |  |  |  |
| last_vld_dl_style_attr_set_id | bigint | 8 | 0 |  |  |  |
| last_vld_dl_style_cust_prop_id | bigint | 8 | 0 |  |  |  |
| last_vld_dl_style_attach_id | bigint | 8 | 0 |  |  |  |
| last_vld_dl_style_desc_id | bigint | 8 | 0 |  |  |  |
| last_vld_dl_upc_id | bigint | 8 | 0 |  |  |  |
| last_vld_dl_pack_upc_id | bigint | 8 | 0 |  |  |  |
| last_vld_dl_style_color_ret_id | bigint | 8 | 0 |  |  |  |
| last_vld_dl_style_prc_grp_id | bigint | 8 | 0 |  |  |  |
| last_vld_dl_stl_prc_grp_clr_id | bigint | 8 | 0 |  |  |  |
| last_vld_dl_style_location_id | bigint | 8 | 0 |  |  |  |
| last_vld_dl_style_loc_clr_id | bigint | 8 | 0 |  |  |  |
| last_vld_dl_style_clr_desc_id | bigint | 8 | 0 |  |  |  |
| last_vld_dl_style_size_desc_id | bigint | 8 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.dl_style_task_add_$sp](../../StoredProcedures/me_01/dbo.dl_style_task_add_$sp.md)
- [me_01: dbo.dl_style_task_br_term_phs_$sp](../../StoredProcedures/me_01/dbo.dl_style_task_br_term_phs_$sp.md)
- [me_01: dbo.dl_style_task_bus_rule_phs_$sp](../../StoredProcedures/me_01/dbo.dl_style_task_bus_rule_phs_$sp.md)
- [me_01: dbo.dl_style_task_continue_$sp](../../StoredProcedures/me_01/dbo.dl_style_task_continue_$sp.md)
- [me_01: dbo.dl_style_task_end_$sp](../../StoredProcedures/me_01/dbo.dl_style_task_end_$sp.md)
- [me_01: dbo.dl_style_task_ld_term_phs_$sp](../../StoredProcedures/me_01/dbo.dl_style_task_ld_term_phs_$sp.md)
- [me_01: dbo.dl_style_task_load_phs_$sp](../../StoredProcedures/me_01/dbo.dl_style_task_load_phs_$sp.md)
- [me_01: dbo.dl_style_task_sch_term_phs_$sp](../../StoredProcedures/me_01/dbo.dl_style_task_sch_term_phs_$sp.md)
- [me_01: dbo.dl_style_task_validate_$sp](../../StoredProcedures/me_01/dbo.dl_style_task_validate_$sp.md)

