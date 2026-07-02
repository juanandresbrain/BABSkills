# dbo.parameter_alloc_replen

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| parameter_alloc_replen_id | tinyint | 1 | 0 | YES |  |  |
| distribution_no_mask | nvarchar | 40 | 0 |  |  |  |
| first_distribution_no | nvarchar | 40 | 0 |  |  |  |
| last_distribution_no | nvarchar | 40 | 0 |  |  |  |
| last_generated_distribution_no | nvarchar | 40 | 1 |  |  |  |
| distribution_no_rec_flag | bit | 1 | 0 |  |  |  |
| cancel_cleanup_weeks | smallint | 2 | 0 |  |  |  |
| preliminary_cleanup_weeks | smallint | 2 | 0 |  |  |  |
| completed_cleanup_weeks | smallint | 2 | 0 |  |  |  |
| appr_rejected_cleanup_weeks | smallint | 2 | 0 |  |  |  |
| release_prior_days | smallint | 2 | 1 |  |  |  |
| include_unneeded_sku_loc_flag | bit | 1 | 0 |  |  |  |
| using_approval_flag | bit | 1 | 0 |  |  |  |
| curr_plan_hier_level_id | int | 4 | 0 |  |  |  |
| future_plan_hier_level_id | int | 4 | 1 |  |  |  |
| future_plan_period_id | numeric | 9 | 1 |  |  |  |
| plan_by_total_flag | bit | 1 | 0 |  |  |  |
| plan_element_sales_tot_units | smallint | 2 | 1 |  |  |  |
| plan_element_sales_tot_retail | smallint | 2 | 1 |  |  |  |
| plan_element_sales_reg_units | smallint | 2 | 1 |  |  |  |
| plan_element_sales_reg_retail | smallint | 2 | 1 |  |  |  |
| plan_element_sales_md_units | smallint | 2 | 1 |  |  |  |
| plan_element_sales_md_retail | smallint | 2 | 1 |  |  |  |
| plan_element_oh_tot_units | smallint | 2 | 1 |  |  |  |
| plan_element_oh_tot_retail | smallint | 2 | 1 |  |  |  |
| plan_element_oh_reg_units | smallint | 2 | 1 |  |  |  |
| plan_element_oh_reg_retail | smallint | 2 | 1 |  |  |  |
| plan_element_oh_md_units | smallint | 2 | 1 |  |  |  |
| plan_element_oh_md_retail | smallint | 2 | 1 |  |  |  |
| plan_version_id | smallint | 2 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |
| forecast_load_type | smallint | 2 | 0 |  |  |  |
| forecast_load_level_id | int | 4 | 1 |  |  |  |
| outlier_forward_obsv_periods | smallint | 2 | 0 |  |  |  |
| outlier_forward_obsv_weeks | smallint | 2 | 0 |  |  |  |
| outlier_back_obsv_periods | smallint | 2 | 0 |  |  |  |
| outlier_back_obsv_weeks | smallint | 2 | 0 |  |  |  |
| auto_update_min_max_flag | bit | 1 | 0 |  |  |  |
| safety_stock_rule | smallint | 2 | 1 |  |  |  |
| coverage_period_method | smallint | 2 | 0 |  |  |  |
| lost_extra_sales_obsv_weeks | smallint | 2 | 0 |  |  |  |
| keep_forecast_weeks | smallint | 2 | 0 |  |  |  |
| order_point | smallint | 2 | 0 |  |  |  |
| incl_pres_stock_order_point | bit | 1 | 0 |  |  |  |
| lost_extra_sales_load_level_id | int | 4 | 0 |  |  |  |
| lost_extra_sales_load_type | smallint | 2 | 0 |  |  |  |
| lost_extra_sales_rv_last_weeks | smallint | 2 | 0 |  |  |  |
| allow_size_substitution_flag | bit | 1 | 0 |  |  |  |
| consider_effect_inv_flag | bit | 1 | 0 |  |  |  |
| minimum_constraint | smallint | 2 | 0 |  |  |  |
| plan_grading_option | smallint | 2 | 0 |  |  |  |
| update_po_quantity_flag | bit | 1 | 0 |  |  |  |
| create_split_release_po_flag | bit | 1 | 0 |  |  |  |
| update_min | bit | 1 | 0 |  |  |  |
| update_max | bit | 1 | 0 |  |  |  |
| update_capacity | bit | 1 | 0 |  |  |  |
| update_presentation | bit | 1 | 0 |  |  |  |
| update_min_default | smallint | 2 | 0 |  |  |  |
| update_max_default | smallint | 2 | 0 |  |  |  |
| update_capacity_default | smallint | 2 | 0 |  |  |  |
| update_presentation_default | smallint | 2 | 0 |  |  |  |
| max_pack_type_per_loc | smallint | 2 | 0 |  |  |  |
| allow_pack_alloc_exceed_loc | smallint | 2 | 0 |  |  |  |
| allow_pk_alloc_exceed_sku_unit | smallint | 2 | 0 |  |  |  |
| keep_in_reserve | smallint | 2 | 0 |  |  |  |
| use_dynamic_start_date_flag | bit | 1 | 0 |  |  |  |
| dynamic_start_date_days_to_add | smallint | 2 | 0 |  |  |  |
| use_sale_date_in_forecast_flag | bit | 1 | 0 |  |  |  |
| forecast_sale_date_days_to_add | smallint | 2 | 0 |  |  |  |
| maintain_sz_scales_for_ap_flag | bit | 1 | 0 |  |  |  |
| manual_sz_scl_update_sync_type | tinyint | 1 | 1 |  |  |  |
| enforce_keep_in_reserve | bit | 1 | 0 |  |  |  |
| vendor_replen_generate_item | tinyint | 1 | 0 |  |  |  |
| excl_oh_hist_prior_first_sale | bit | 1 | 0 |  |  |  |
| pack_size_threshold | smallint | 2 | 0 |  |  |  |
| allow_pk_alloc_exceed_sku_pct | smallint | 2 | 0 |  |  |  |
| minimum_one_pack_per_loc_flag | bit | 1 | 0 |  |  |  |
| size_scale_type | smallint | 2 | 0 |  |  |  |
| wholesale_inventory_decrement_type | smallint | 2 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.retrieve_dist_$sp](../../StoredProcedures/me_01/dbo.retrieve_dist_$sp.md)

