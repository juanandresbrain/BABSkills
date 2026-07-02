# Stored Procedures: ma_01

| Schema | Name | Table Dependencies |
|---|---|---|
| dbo | [add_partitions_$sp](dbo.add_partitions_$sp.md) | dbo.calendar_merch_week, dbo.get_current_period_$sp, dbo.get_current_week_$sp, dbo.get_current_year_$sp, dbo.job_error_handler_$sp, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.user_partition |
| dbo | [cleanup_wrk_cmp_$sp](dbo.cleanup_wrk_cmp_$sp.md) | dbo.job_error_handler_$sp, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_cmp_group_loc_wk, dbo.wrk_cmp_sku_loc_wk, dbo.wrk_cmp_style_loc_wk, dbo.wrk_cmp_styleclr_loc_wk |
| dbo | [cleanup_wrk_flash_$sp](dbo.cleanup_wrk_flash_$sp.md) | dbo.job_error_handler_$sp, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_flsh_group_loc_da, dbo.wrk_flsh_style_loc_da |
| dbo | [cleanup_wrk_hist_$sp](dbo.cleanup_wrk_hist_$sp.md) | dbo.job_error_handler_$sp, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_group_loc_wk, dbo.wrk_sku_loc_wk, dbo.wrk_style_loc_wk, dbo.wrk_styleclr_loc_wk |
| dbo | [cleanup_wrk_ib_$sp](dbo.cleanup_wrk_ib_$sp.md) | dbo.cleanup_wrk_ib_allocation_$sp, dbo.cleanup_wrk_ib_cost_factor_$sp, dbo.cleanup_wrk_ib_inventory_$sp, dbo.cleanup_wrk_ib_on_order_$sp, dbo.job_error_handler_$sp, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp |
| dbo | [cleanup_wrk_ib_allocation_$sp](dbo.cleanup_wrk_ib_allocation_$sp.md) | dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_all_style_alt_group, dbo.wrk_ib_allocation |
| dbo | [cleanup_wrk_ib_cost_factor_$sp](dbo.cleanup_wrk_ib_cost_factor_$sp.md) | dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_cfd_style_alt_group, dbo.wrk_ib_cost_factor_discount |
| dbo | [cleanup_wrk_ib_inventory_$sp](dbo.cleanup_wrk_ib_inventory_$sp.md) | dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_inventory, dbo.wrk_ib_iv_style_alt_group |
| dbo | [cleanup_wrk_ib_on_order_$sp](dbo.cleanup_wrk_ib_on_order_$sp.md) | dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_on_order, dbo.wrk_ib_oo_style_alt_group |
| dbo | [cleanup_wrk_oh_$sp](dbo.cleanup_wrk_oh_$sp.md) | dbo.job_error_handler_$sp, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_oh_group_loc_wk, dbo.wrk_oh_sku_loc_wk, dbo.wrk_oh_style_loc_wk, dbo.wrk_oh_styleclr_loc_wk |
| dbo | [cleanup_wrk_oo_all_$sp](dbo.cleanup_wrk_oo_all_$sp.md) | dbo.job_error_handler_$sp, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_oo_all_group_loc_wk, dbo.wrk_oo_all_sku_loc_wk, dbo.wrk_oo_all_style_loc_wk, dbo.wrk_oo_all_styleclr_loc_wk |
| dbo | [create_initial_history_partitions_$sp](dbo.create_initial_history_partitions_$sp.md) | dbo.calendar_merch_week, dbo.hist_oh_group_chn_pd, dbo.hist_oh_group_chn_wk, dbo.hist_oh_group_chn_yr, dbo.user_partition |
| Version:1.01 | [(R3 Version)](Version_1_01._R3_Version.md) |  |
| SET @v_min_year_wk | [= @starting_year_week](SET_@v_min_year_wk.=_@starting_year_week.md) |  |
| SET @v_min_year_pd | [= @starting_year_period](SET_@v_min_year_pd.=_@starting_year_period.md) |  |
| dbo | [dl_hist_group_vld_$sp](dbo.dl_hist_group_vld_$sp.md) | dbo.calendar_merch_week, dbo.dl_hist_group, dbo.dl_hist_task, dbo.hierarchy, dbo.hierarchy_group, dbo.hierarchy_level, dbo.hist_group_loc_wk, dbo.location, dbo.post_parameter |
| dbo | [dl_hist_oh_group_vld_$sp](dbo.dl_hist_oh_group_vld_$sp.md) | dbo.calendar_merch_week, dbo.dl_hist_oh_group, dbo.dl_hist_task, dbo.hierarchy, dbo.hierarchy_group, dbo.hierarchy_level, dbo.hist_oh_group_loc_wk, dbo.inventory_status, dbo.location, dbo.post_parameter, dbo.price_status |
| dbo | [dl_hist_oh_sku_vld_$sp](dbo.dl_hist_oh_sku_vld_$sp.md) | dbo.calendar_merch_week, dbo.dl_hist_oh_sku, dbo.dl_hist_task, dbo.hist_oh_sku_loc_wk, dbo.inventory_status, dbo.location, dbo.post_parameter, dbo.price_status, dbo.sku, dbo.upc |
| dbo | [dl_hist_oh_style_vld_$sp](dbo.dl_hist_oh_style_vld_$sp.md) | dbo.calendar_merch_week, dbo.dl_hist_oh_style, dbo.dl_hist_task, dbo.hist_oh_style_loc_wk, dbo.inventory_status, dbo.location, dbo.post_parameter, dbo.price_status, dbo.style |
| dbo | [dl_hist_oh_styleclr_vld_$sp](dbo.dl_hist_oh_styleclr_vld_$sp.md) | dbo.calendar_merch_week, dbo.color, dbo.dl_hist_oh_styleclr, dbo.dl_hist_task, dbo.hist_oh_styleclr_loc_wk, dbo.inventory_status, dbo.location, dbo.post_parameter, dbo.price_status, dbo.style, dbo.style_color |
| dbo | [dl_hist_sku_vld_$sp](dbo.dl_hist_sku_vld_$sp.md) | dbo.calendar_merch_week, dbo.dl_hist_sku, dbo.dl_hist_task, dbo.hist_sku_loc_wk, dbo.location, dbo.post_parameter, dbo.sku, dbo.upc |
| dbo | [dl_hist_style_vld_$sp](dbo.dl_hist_style_vld_$sp.md) | dbo.calendar_merch_week, dbo.dl_hist_style, dbo.dl_hist_task, dbo.hist_style_loc_wk, dbo.location, dbo.post_parameter, dbo.style |
| dbo | [dl_hist_styleclr_vld_$sp](dbo.dl_hist_styleclr_vld_$sp.md) | dbo.calendar_merch_week, dbo.color, dbo.dl_hist_styleclr, dbo.dl_hist_task, dbo.hist_styleclr_loc_wk, dbo.location, dbo.post_parameter, dbo.style, dbo.style_color |
| dbo | [dl_hist_task_add_$sp](dbo.dl_hist_task_add_$sp.md) | dbo.dl_hist_task |
| dbo | [dl_hist_task_br_term_phs_$sp](dbo.dl_hist_task_br_term_phs_$sp.md) | dbo.dl_hist_task |
| dbo | [dl_hist_task_bus_rule_phs_$sp](dbo.dl_hist_task_bus_rule_phs_$sp.md) | dbo.dl_hist_task |
| dbo | [dl_hist_task_continue_$sp](dbo.dl_hist_task_continue_$sp.md) | dbo.dl_hist_task |
| dbo | [dl_hist_task_end_$sp](dbo.dl_hist_task_end_$sp.md) | dbo.dl_hist_task |
| dbo | [dl_hist_task_imp_ld_compl_$sp](dbo.dl_hist_task_imp_ld_compl_$sp.md) |  |
| dbo | [dl_hist_task_imp_ld_prep_$sp](dbo.dl_hist_task_imp_ld_prep_$sp.md) | dbo.dl_hist_group, dbo.dl_hist_oh_group, dbo.dl_hist_oh_sku, dbo.dl_hist_oh_style, dbo.dl_hist_oh_styleclr, dbo.dl_hist_sku, dbo.dl_hist_style, dbo.dl_hist_styleclr |
| dbo | [dl_hist_task_imp_trunc_$sp](dbo.dl_hist_task_imp_trunc_$sp.md) | dbo.dl_hist_group, dbo.dl_hist_oh_group, dbo.dl_hist_oh_sku, dbo.dl_hist_oh_style, dbo.dl_hist_oh_styleclr, dbo.dl_hist_sku, dbo.dl_hist_style, dbo.dl_hist_styleclr |
| dbo | [dl_hist_task_ld_term_phs_$sp](dbo.dl_hist_task_ld_term_phs_$sp.md) | dbo.dl_hist_task |
| dbo | [dl_hist_task_load_phs_$sp](dbo.dl_hist_task_load_phs_$sp.md) | dbo.dl_hist_task |
| dbo | [dl_hist_task_sch_term_phs_$sp](dbo.dl_hist_task_sch_term_phs_$sp.md) | dbo.dl_hist_task |
| dbo | [es_calc_sell_thru_$sp](dbo.es_calc_sell_thru_$sp.md) | dbo.calendar_date, dbo.es_sell_thru, dbo.hist_oh_sku_loc_li, dbo.hist_oh_sku_loc_wk, dbo.hist_sku_loc_li, dbo.hist_sku_loc_wk, dbo.sku |
| dbo | [filter_forecasting_styles_ma_$sp](dbo.filter_forecasting_styles_ma_$sp.md) | dbo.calendar_date, dbo.comp_set_style_color, dbo.hist_oh_style_loc_li, dbo.hist_style_chn_wk, dbo.location, dbo.oo_all_style_loc_li, dbo.style, dbo.style_color, dbo.view_calendar_merch_week_rel |
| dbo | [get_beg_wk_cur_period_ly_$fn](dbo.get_beg_wk_cur_period_ly_$fn.md) | dbo.calendar_merch_week, dbo.post_parameter |
| dbo | [get_curr_pd_$fn](dbo.get_curr_pd_$fn.md) | dbo.calendar_merch_week, dbo.post_parameter |
| dbo | [get_curr_pd_ly_$fn](dbo.get_curr_pd_ly_$fn.md) | dbo.calendar_merch_week, dbo.post_parameter |
| dbo | [get_curr_wk_$fn](dbo.get_curr_wk_$fn.md) | dbo.post_parameter |
| dbo | [get_curr_wk_ly_$fn](dbo.get_curr_wk_ly_$fn.md) | dbo.post_parameter |
| dbo | [get_curr_yr_$fn](dbo.get_curr_yr_$fn.md) | dbo.calendar_merch_week, dbo.post_parameter |
| dbo | [get_current_period_$sp](dbo.get_current_period_$sp.md) | dbo.calendar_date, dbo.job_error_handler_$sp, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_inventory |
| dbo | [get_current_week_$sp](dbo.get_current_week_$sp.md) | dbo.calendar_date, dbo.job_error_handler_$sp, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_inventory |
| dbo | [get_current_year_$sp](dbo.get_current_year_$sp.md) | dbo.calendar_date, dbo.job_error_handler_$sp, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_inventory |
| dbo | [get_job_params_$sp](dbo.get_job_params_$sp.md) | dbo.job_error_handler_$sp, dbo.job_params, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp |
| dbo | [get_last_pd_$fn](dbo.get_last_pd_$fn.md) | dbo.calendar_merch_period, dbo.calendar_merch_week, dbo.post_parameter |
| dbo | [get_last_range_end_$sp](dbo.get_last_range_end_$sp.md) | dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp |
| dbo | [get_last_range_end_phase2_$sp](dbo.get_last_range_end_phase2_$sp.md) | dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.posting_parameter, dbo.return_debug_flag_$sp |
| dbo | [get_last_wk_$fn](dbo.get_last_wk_$fn.md) | dbo.calendar_merch_week, dbo.post_parameter |
| dbo | [get_last_x_days_$fn](dbo.get_last_x_days_$fn.md) |  |
| dbo | [get_last_x_pds_$fn](dbo.get_last_x_pds_$fn.md) | dbo.calendar_merch_period, dbo.calendar_merch_week, dbo.post_parameter |
| dbo | [get_last_x_pds_ly_$fn](dbo.get_last_x_pds_ly_$fn.md) | dbo.calendar_merch_period, dbo.calendar_merch_week, dbo.post_parameter |
| dbo | [get_last_x_wks_$fn](dbo.get_last_x_wks_$fn.md) | dbo.calendar_merch_week, dbo.post_parameter |
| dbo | [get_last_x_wks_ly_$fn](dbo.get_last_x_wks_ly_$fn.md) | dbo.calendar_merch_week, dbo.post_parameter |
| dbo | [get_last_x_yrs_$fn](dbo.get_last_x_yrs_$fn.md) | dbo.calendar_merch_period, dbo.calendar_merch_week, dbo.post_parameter |
| dbo | [get_last_yr_$fn](dbo.get_last_yr_$fn.md) | dbo.calendar, dbo.calendar_merch_week, dbo.post_parameter |
| dbo | [get_last_yr_beg_prd_$fn](dbo.get_last_yr_beg_prd_$fn.md) | dbo.calendar, dbo.calendar_merch_week, dbo.post_parameter |
| dbo | [get_last_yr_beg_wk_$fn](dbo.get_last_yr_beg_wk_$fn.md) | dbo.calendar, dbo.calendar_merch_week, dbo.post_parameter |
| dbo | [get_max_ib_allocation_id_$sp](dbo.get_max_ib_allocation_id_$sp.md) | dbo.job_error_handler_$sp, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.syn_ib_allocation |
| dbo | [get_max_ib_cost_factor_id_$sp](dbo.get_max_ib_cost_factor_id_$sp.md) | dbo.job_error_handler_$sp, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.syn_ib_cost_factor_discount |
| dbo | [get_max_ib_inventory_id_$sp](dbo.get_max_ib_inventory_id_$sp.md) | dbo.job_error_handler_$sp, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.syn_ib_inventory |
| dbo | [get_max_ib_on_order_id_$sp](dbo.get_max_ib_on_order_id_$sp.md) | dbo.job_error_handler_$sp, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.syn_ib_on_order |
| dbo | [get_max_wrk_ib_allocation_id_$sp](dbo.get_max_wrk_ib_allocation_id_$sp.md) | dbo.job_error_handler_$sp, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_allocation |
| dbo | [get_max_wrk_ib_cf_id_$sp](dbo.get_max_wrk_ib_cf_id_$sp.md) | dbo.job_error_handler_$sp, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_cost_factor_discount |
| dbo | [get_max_wrk_ib_inventory_id_$sp](dbo.get_max_wrk_ib_inventory_id_$sp.md) | dbo.job_error_handler_$sp, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_inventory |
| dbo | [get_max_wrk_ib_on_order_id_$sp](dbo.get_max_wrk_ib_on_order_id_$sp.md) | dbo.job_error_handler_$sp, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_on_order |
| dbo | [get_next_x_pds_$fn](dbo.get_next_x_pds_$fn.md) | dbo.calendar_merch_period, dbo.calendar_merch_week, dbo.post_parameter |
| dbo | [get_next_x_wks_$fn](dbo.get_next_x_wks_$fn.md) | dbo.calendar_merch_week, dbo.post_parameter |
| dbo | [get_next_x_yrs_$fn](dbo.get_next_x_yrs_$fn.md) | dbo.calendar_merch_period, dbo.calendar_merch_week, dbo.post_parameter |
| dbo | [get_prev_last_x_pds_$fn](dbo.get_prev_last_x_pds_$fn.md) | dbo.calendar_merch_period, dbo.calendar_merch_week, dbo.post_parameter |
| dbo | [get_prev_last_x_pds_ly_$fn](dbo.get_prev_last_x_pds_ly_$fn.md) | dbo.calendar_merch_period, dbo.calendar_merch_week, dbo.post_parameter |
| dbo | [get_prev_last_x_wks_$fn](dbo.get_prev_last_x_wks_$fn.md) | dbo.calendar_merch_week, dbo.post_parameter |
| dbo | [get_prev_last_x_wks_ly_$fn](dbo.get_prev_last_x_wks_ly_$fn.md) | dbo.calendar_merch_week, dbo.post_parameter |
| dbo | [get_prev_last_x_yrs_$fn](dbo.get_prev_last_x_yrs_$fn.md) | dbo.calendar_merch_period, dbo.calendar_merch_week, dbo.post_parameter |
| dbo | [get_prev_pd_$fn](dbo.get_prev_pd_$fn.md) | dbo.calendar_merch_period |
| dbo | [get_prev_wk_$fn](dbo.get_prev_wk_$fn.md) | dbo.calendar_merch_week |
| dbo | [get_prev_yr_$fn](dbo.get_prev_yr_$fn.md) | dbo.calendar |
| dbo | [get_this_yr_beg_prd_$fn](dbo.get_this_yr_beg_prd_$fn.md) | dbo.calendar, dbo.calendar_merch_week, dbo.post_parameter |
| dbo | [get_this_yr_beg_wk_$fn](dbo.get_this_yr_beg_wk_$fn.md) | dbo.calendar_merch_week, dbo.post_parameter |
| dbo | [get_yesterday_$fn](dbo.get_yesterday_$fn.md) |  |
| dbo | [hist_currency_exchange_rate_$sp](dbo.hist_currency_exchange_rate_$sp.md) | dbo.calendar_date, dbo.imp_cd_hist_group, dbo.imp_cd_hist_group_home, dbo.imp_cd_hist_group_local, dbo.imp_cd_hist_oh_group, dbo.imp_cd_hist_oh_group_home, dbo.imp_cd_hist_oh_group_local, dbo.imp_cd_hist_oh_style, dbo.imp_cd_hist_oh_style_home, dbo.imp_cd_hist_oh_style_local, dbo.imp_cd_hist_oh_styleclr, dbo.imp_cd_hist_oh_styleclr_home, dbo.imp_cd_hist_oh_styleclr_local, dbo.imp_cd_hist_style, dbo.imp_cd_hist_style_home, dbo.imp_cd_hist_style_local, dbo.imp_cd_hist_styleclr, dbo.imp_cd_hist_styleclr_home, dbo.imp_cd_hist_styleclr_local |
| dbo | [hist_currency_exchange_rate_pd_$sp](dbo.hist_currency_exchange_rate_pd_$sp.md) | dbo.calendar_date, dbo.imp_cd_rim_oh_group_home, dbo.imp_cd_rim_oh_group_local |
| dbo | [hk_sku_modify_hist_$sp](dbo.hk_sku_modify_hist_$sp.md) | dbo.hist_sku_chn_li, dbo.hist_sku_chn_pd, dbo.hist_sku_chn_wk, dbo.hist_sku_chn_yr, dbo.hist_sku_loc_li, dbo.hist_sku_loc_pd, dbo.hist_sku_loc_wk, dbo.hist_sku_loc_yr |
| dbo | [hk_sku_modify_hist_cmp_$sp](dbo.hk_sku_modify_hist_cmp_$sp.md) | dbo.hist_cmp_sku_chn_li, dbo.hist_cmp_sku_chn_pd, dbo.hist_cmp_sku_chn_wk, dbo.hist_cmp_sku_chn_yr, dbo.hist_cmp_sku_loc_li, dbo.hist_cmp_sku_loc_pd, dbo.hist_cmp_sku_loc_wk, dbo.hist_cmp_sku_loc_yr |
| dbo | [hk_sku_modify_hist_oh_$sp](dbo.hk_sku_modify_hist_oh_$sp.md) | dbo.hist_oh_sku_chn_li, dbo.hist_oh_sku_chn_pd, dbo.hist_oh_sku_chn_wk, dbo.hist_oh_sku_chn_yr, dbo.hist_oh_sku_loc_li, dbo.hist_oh_sku_loc_pd, dbo.hist_oh_sku_loc_wk, dbo.hist_oh_sku_loc_yr |
| dbo | [hk_sku_modify_oo_all_$sp](dbo.hk_sku_modify_oo_all_$sp.md) | dbo.oo_all_sku_chn_li, dbo.oo_all_sku_chn_pd, dbo.oo_all_sku_chn_wk, dbo.oo_all_sku_chn_yr, dbo.oo_all_sku_loc_li, dbo.oo_all_sku_loc_pd, dbo.oo_all_sku_loc_wk, dbo.oo_all_sku_loc_yr |
| dbo | [hk_style_delete_hist_$sp](dbo.hk_style_delete_hist_$sp.md) | dbo.hist_sku_chn_li, dbo.hist_sku_chn_pd, dbo.hist_sku_chn_wk, dbo.hist_sku_chn_yr, dbo.hist_sku_loc_li, dbo.hist_sku_loc_pd, dbo.hist_sku_loc_wk, dbo.hist_sku_loc_yr, dbo.hist_style_chn_li, dbo.hist_style_chn_pd, dbo.hist_style_chn_wk, dbo.hist_style_chn_yr, dbo.hist_style_loc_li, dbo.hist_style_loc_pd, dbo.hist_style_loc_wk, dbo.hist_style_loc_yr, dbo.hist_styleclr_chn_li, dbo.hist_styleclr_chn_pd, dbo.hist_styleclr_chn_wk, dbo.hist_styleclr_chn_yr, dbo.hist_styleclr_loc_li, dbo.hist_styleclr_loc_pd, dbo.hist_styleclr_loc_wk, dbo.hist_styleclr_loc_yr |
| dbo | [hk_style_delete_hist_cmp_$sp](dbo.hk_style_delete_hist_cmp_$sp.md) | dbo.hist_cmp_sku_chn_li, dbo.hist_cmp_sku_chn_pd, dbo.hist_cmp_sku_chn_wk, dbo.hist_cmp_sku_chn_yr, dbo.hist_cmp_sku_loc_li, dbo.hist_cmp_sku_loc_pd, dbo.hist_cmp_sku_loc_wk, dbo.hist_cmp_sku_loc_yr, dbo.hist_cmp_style_chn_li, dbo.hist_cmp_style_chn_pd, dbo.hist_cmp_style_chn_wk, dbo.hist_cmp_style_chn_yr, dbo.hist_cmp_style_loc_li, dbo.hist_cmp_style_loc_pd, dbo.hist_cmp_style_loc_wk, dbo.hist_cmp_style_loc_yr, dbo.hist_cmp_styleclr_chn_li, dbo.hist_cmp_styleclr_chn_pd, dbo.hist_cmp_styleclr_chn_wk, dbo.hist_cmp_styleclr_chn_yr, dbo.hist_cmp_styleclr_loc_li, dbo.hist_cmp_styleclr_loc_pd, dbo.hist_cmp_styleclr_loc_wk, dbo.hist_cmp_styleclr_loc_yr |
| dbo | [hk_style_delete_hist_flsh_$sp](dbo.hk_style_delete_hist_flsh_$sp.md) | dbo.hist_flsh_style_chn_da, dbo.hist_flsh_style_loc_da |
| dbo | [hk_style_delete_hist_le_$sp](dbo.hk_style_delete_hist_le_$sp.md) | dbo.hist_le_sku_chn_li, dbo.hist_le_sku_chn_pd, dbo.hist_le_sku_chn_wk, dbo.hist_le_sku_chn_yr, dbo.hist_le_sku_loc_li, dbo.hist_le_sku_loc_pd, dbo.hist_le_sku_loc_wk, dbo.hist_le_sku_loc_yr, dbo.hist_le_style_chn_li, dbo.hist_le_style_chn_pd, dbo.hist_le_style_chn_wk, dbo.hist_le_style_chn_yr, dbo.hist_le_style_loc_li, dbo.hist_le_style_loc_pd, dbo.hist_le_style_loc_wk, dbo.hist_le_style_loc_yr, dbo.hist_le_styleclr_chn_li, dbo.hist_le_styleclr_chn_pd, dbo.hist_le_styleclr_chn_wk, dbo.hist_le_styleclr_chn_yr, dbo.hist_le_styleclr_loc_li, dbo.hist_le_styleclr_loc_pd, dbo.hist_le_styleclr_loc_wk, dbo.hist_le_styleclr_loc_yr |
| dbo | [hk_style_delete_hist_oh_$sp](dbo.hk_style_delete_hist_oh_$sp.md) | dbo.hist_oh_sku_chn_li, dbo.hist_oh_sku_chn_pd, dbo.hist_oh_sku_chn_wk, dbo.hist_oh_sku_chn_yr, dbo.hist_oh_sku_loc_li, dbo.hist_oh_sku_loc_pd, dbo.hist_oh_sku_loc_wk, dbo.hist_oh_sku_loc_yr, dbo.hist_oh_style_chn_li, dbo.hist_oh_style_chn_pd, dbo.hist_oh_style_chn_wk, dbo.hist_oh_style_chn_yr, dbo.hist_oh_style_loc_li, dbo.hist_oh_style_loc_pd, dbo.hist_oh_style_loc_wk, dbo.hist_oh_style_loc_yr, dbo.hist_oh_styleclr_chn_li, dbo.hist_oh_styleclr_chn_pd, dbo.hist_oh_styleclr_chn_wk, dbo.hist_oh_styleclr_chn_yr, dbo.hist_oh_styleclr_loc_li, dbo.hist_oh_styleclr_loc_pd, dbo.hist_oh_styleclr_loc_wk, dbo.hist_oh_styleclr_loc_yr |
| dbo | [hk_style_delete_oo_all_$sp](dbo.hk_style_delete_oo_all_$sp.md) | dbo.oo_all_sku_chn_li, dbo.oo_all_sku_chn_pd, dbo.oo_all_sku_chn_wk, dbo.oo_all_sku_chn_yr, dbo.oo_all_sku_loc_li, dbo.oo_all_sku_loc_pd, dbo.oo_all_sku_loc_wk, dbo.oo_all_sku_loc_yr, dbo.oo_all_style_chn_li, dbo.oo_all_style_chn_pd, dbo.oo_all_style_chn_wk, dbo.oo_all_style_chn_yr, dbo.oo_all_style_loc_li, dbo.oo_all_style_loc_pd, dbo.oo_all_style_loc_wk, dbo.oo_all_style_loc_yr, dbo.oo_all_styleclr_chn_li, dbo.oo_all_styleclr_chn_pd, dbo.oo_all_styleclr_chn_wk, dbo.oo_all_styleclr_chn_yr, dbo.oo_all_styleclr_loc_li, dbo.oo_all_styleclr_loc_pd, dbo.oo_all_styleclr_loc_wk, dbo.oo_all_styleclr_loc_yr |
| dbo | [hk_style_reclass_hist_$sp](dbo.hk_style_reclass_hist_$sp.md) | dbo.hist_style_loc_wk, dbo.post_hist_group, dbo.post_hist_style |
| dbo | [hk_style_reclass_hist_cmp_$sp](dbo.hk_style_reclass_hist_cmp_$sp.md) | dbo.hist_cmp_style_loc_wk, dbo.post_cmp_work_group, dbo.post_hist_cmp_group, dbo.post_hist_cmp_style |
| dbo | [hk_style_reclass_hist_flsh_$sp](dbo.hk_style_reclass_hist_flsh_$sp.md) | dbo.hist_flsh_style_loc_da, dbo.post_flsh_group_sum, dbo.post_flsh_style_sum |
| dbo | [hk_style_reclass_hist_oh_$sp](dbo.hk_style_reclass_hist_oh_$sp.md) | dbo.hist_oh_style_loc_li, dbo.hist_oh_style_loc_pd, dbo.hist_oh_style_loc_wk, dbo.hist_oh_style_loc_yr, dbo.post_hist_oh_group, dbo.post_hist_oh_style, dbo.post_oh_work_group_li, dbo.post_oh_work_group_pd, dbo.post_oh_work_group_wk, dbo.post_oh_work_group_yr |
| dbo | [hk_style_reclass_oo_all_$sp](dbo.hk_style_reclass_oo_all_$sp.md) | dbo.oo_all_style_loc_wk, dbo.post_oo_all_group_sum, dbo.post_oo_all_style_sum |
| dbo | [import_hist_cmp_group_$sp](dbo.import_hist_cmp_group_$sp.md) | dbo.calendar_date, dbo.calendar_merch_week, dbo.cost_factor, dbo.discount, dbo.group_currency_rate, dbo.hierarchy_group, dbo.hist_cmp_group_loc_wk, dbo.history_component, dbo.imp_cd_hist_cmp_group, dbo.imp_cd_hist_cmp_group_home, dbo.imp_cd_hist_cmp_group_local, dbo.imp_id_hist_cmp_group, dbo.location, dbo.multi_currency_location_cost_wk, dbo.multi_currency_location_retail_wk, dbo.post_parameter, dbo.price_status, dbo.syn_transaction_reason |
| dbo | [import_hist_cmp_sku_$sp](dbo.import_hist_cmp_sku_$sp.md) | dbo.calendar_merch_week, dbo.hist_cmp_sku_loc_wk, dbo.history_component, dbo.imp_cd_hist_cmp_sku, dbo.imp_cd_hist_cmp_sku_error, dbo.imp_id_hist_cmp_sku, dbo.location, dbo.post_parameter, dbo.price_status, dbo.sku, dbo.syn_transaction_reason, dbo.upc |
| dbo | [import_hist_cmp_style_$sp](dbo.import_hist_cmp_style_$sp.md) | dbo.calendar_date, dbo.calendar_merch_week, dbo.cost_factor, dbo.discount, dbo.hist_cmp_style_loc_wk, dbo.history_component, dbo.imp_cd_hist_cmp_style, dbo.imp_cd_hist_cmp_style_home, dbo.imp_cd_hist_cmp_style_local, dbo.imp_id_hist_cmp_style, dbo.location, dbo.multi_currency_location_cost_wk, dbo.multi_currency_location_retail_wk, dbo.post_parameter, dbo.price_status, dbo.style, dbo.style_currency_rate, dbo.syn_transaction_reason |
| dbo | [import_hist_cmp_styleclr_$sp](dbo.import_hist_cmp_styleclr_$sp.md) | dbo.calendar_date, dbo.calendar_merch_week, dbo.color, dbo.cost_factor, dbo.discount, dbo.hist_cmp_styleclr_loc_wk, dbo.history_component, dbo.imp_cd_hist_cmp_styleclr, dbo.imp_cd_hist_cmp_styleclr_home, dbo.imp_cd_hist_cmp_styleclr_local, dbo.imp_id_hist_cmp_styleclr, dbo.location, dbo.multi_currency_location_cost_wk, dbo.multi_currency_location_retail_wk, dbo.post_parameter, dbo.price_status, dbo.style, dbo.styleclr_currency_rate, dbo.syn_transaction_reason |
| dbo | [initial_load_job_header_$sp](dbo.initial_load_job_header_$sp.md) | dbo.calendar_merch_week, dbo.job_header, dbo.post_parameter |
| dbo | [initial_load_posting_parameter_$sp](dbo.initial_load_posting_parameter_$sp.md) | dbo.post_parameter, dbo.posting_parameter |
| dbo | [is_tax_exclusive_$sp](dbo.is_tax_exclusive_$sp.md) | dbo.job_error_handler_$sp, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.syn_jurisdiction_tax |
| dbo | [job_error_handler_$sp](dbo.job_error_handler_$sp.md) | dbo.job_error |
| create proc [dbo].[job_error_handler_$sp] | [( @job_type INT](create_proc_dbo_job_error_handler_$sp_._@job_type_INT.md) |  |
| dbo | [job_progress_handler_$sp](dbo.job_progress_handler_$sp.md) | dbo.job_debug, dbo.job_error_handler_$sp |
| create proc [dbo].[job_progress_handler_$sp] | [( @job_type INT](create_proc_dbo_job_progress_handler_$sp_._@job_type_INT.md) |  |
| dbo | [nsb_core_chain_$sp](dbo.nsb_core_chain_$sp.md) | dbo.calendar_merch_week, dbo.hierarchy_group, dbo.hierarchy_level, dbo.hist_group_chn_wk, dbo.hist_oh_group_chn_wk, dbo.merch_group_parent, dbo.oo_all_group_chn_wk, dbo.parameter_plan_elements, dbo.plan_group_chn_pd |
| dbo | [nsb_core_location_$sp](dbo.nsb_core_location_$sp.md) | dbo.calendar_merch_week, dbo.hierarchy_group, dbo.hierarchy_level, dbo.hist_group_loc_wk, dbo.hist_oh_group_loc_wk, dbo.location, dbo.merch_group_parent, dbo.oo_all_group_loc_wk, dbo.parameter_plan_elements, dbo.plan_group_loc_pd |
| dbo | [nsb_mar_chain_md_$sp](dbo.nsb_mar_chain_md_$sp.md) | dbo.calendar_merch_week, dbo.hierarchy_group, dbo.hierarchy_level, dbo.hist_cmp_group_chn_wk, dbo.hist_group_chn_wk, dbo.hist_oh_group_chn_wk, dbo.history_component, dbo.merch_group_parent, dbo.oo_all_group_chn_wk, dbo.parameter_plan_elements, dbo.plan_group_chn_wk, dbo.price_status |
| dbo | [nsb_mar_location_md_$sp](dbo.nsb_mar_location_md_$sp.md) | dbo.calendar_merch_week, dbo.hierarchy_group, dbo.hierarchy_level, dbo.hist_cmp_group_loc_wk, dbo.hist_group_loc_wk, dbo.hist_oh_group_loc_wk, dbo.history_component, dbo.location, dbo.merch_group_parent, dbo.oo_all_group_loc_wk, dbo.parameter_plan_elements, dbo.plan_group_loc_wk, dbo.price_status |
| dbo | [nsb_otb_chain_$sp](dbo.nsb_otb_chain_$sp.md) | dbo.calendar_merch_period, dbo.calendar_merch_week, dbo.hierarchy_group, dbo.hierarchy_level, dbo.hist_group_chn_pd, dbo.hist_oh_group_chn_pd, dbo.merch_group_parent, dbo.oo_all_group_chn_pd, dbo.parameter_plan_elements, dbo.plan_group_chn_pd, dbo.post_parameter, dbo.view_calendar_merch_pd_rel |
| dbo | [nsb_otb_location_$sp](dbo.nsb_otb_location_$sp.md) | dbo.calendar_merch_period, dbo.calendar_merch_week, dbo.hierarchy_group, dbo.hierarchy_level, dbo.hist_group_loc_pd, dbo.hist_oh_group_loc_pd, dbo.location, dbo.location_parent, dbo.merch_group_parent, dbo.oo_all_group_loc_pd, dbo.parameter_plan_elements, dbo.plan_group_loc_pd, dbo.post_parameter, dbo.view_calendar_merch_pd_rel |
| dbo | [nsb_par_chain_$sp](dbo.nsb_par_chain_$sp.md) | dbo.calendar_merch_period, dbo.calendar_merch_week, dbo.hierarchy_group, dbo.hierarchy_level, dbo.hist_group_chn_pd, dbo.hist_oh_group_chn_pd, dbo.merch_group_parent, dbo.oo_all_group_chn_pd, dbo.parameter_plan_elements, dbo.plan_element, dbo.plan_group_chn_pd, dbo.post_parameter |
| dbo | [nsb_par_chain_rim_$sp](dbo.nsb_par_chain_rim_$sp.md) | dbo.calendar_merch_period, dbo.calendar_merch_week, dbo.hierarchy_group, dbo.hierarchy_level, dbo.hist_group_chn_pd, dbo.hist_oh_group_chn_pd, dbo.hist_rim_oh_group_chn_pd, dbo.merch_group_parent, dbo.oo_all_group_chn_pd, dbo.parameter_plan_elements, dbo.plan_element, dbo.plan_group_chn_pd, dbo.post_parameter |
| dbo | [nsb_par_location_$sp](dbo.nsb_par_location_$sp.md) | dbo.calendar_merch_period, dbo.calendar_merch_week, dbo.hierarchy_group, dbo.hierarchy_level, dbo.hist_group_loc_pd, dbo.hist_oh_group_loc_pd, dbo.location, dbo.location_parent, dbo.merch_group_parent, dbo.oo_all_group_loc_pd, dbo.parameter_plan_elements, dbo.plan_element, dbo.plan_group_loc_pd, dbo.post_parameter |
| dbo | [nsb_style_analysis_$sp](dbo.nsb_style_analysis_$sp.md) | dbo.attribute, dbo.attribute_set, dbo.calendar_date, dbo.calendar_merch_week, dbo.entity_attribute_set, dbo.hierarchy, dbo.hierarchy_group, dbo.hierarchy_level, dbo.hist_oh_style_loc_li, dbo.hist_oh_style_loc_wk, dbo.hist_style_loc_li, dbo.hist_style_loc_wk, dbo.ib_activity_date, dbo.location, dbo.location_parent, dbo.oo_all_style_chn_wk, dbo.oo_all_style_loc_li, dbo.post_parameter, dbo.price_status, dbo.style, dbo.style_list, dbo.style_list_item, dbo.style_parent |
| dbo | [nsb_vendor_analysis_$sp](dbo.nsb_vendor_analysis_$sp.md) | dbo.calendar_merch_week, dbo.hierarchy_group, dbo.hierarchy_level, dbo.hist_cmp_style_chn_wk, dbo.hist_oh_style_chn_wk, dbo.hist_style_chn_wk, dbo.history_component, dbo.oo_all_style_chn_wk, dbo.style, dbo.style_parent |
| dbo | [populate_multi_currency_by_loc_pd_$sp](dbo.populate_multi_currency_by_loc_pd_$sp.md) | dbo.a, dbo.calendar_merch_period, dbo.calendar_merch_week, dbo.m, dbo.multi_currency_location_cost_pd, dbo.multi_currency_location_cost_wk, dbo.multi_currency_location_retail_pd, dbo.multi_currency_location_retail_wk |
| Date | [Name](Date.Name.md) |  |
| Mar. 31,2010 | [Pierrette Lemay](Mar_31,2010.Pierrette_Lemay.md) |  |
| Apr. 07,2010 | [Pierrette Lemay](Apr_07,2010.Pierrette_Lemay.md) |  |
| May. 04,2011 | [Pierrette Lemay](May_04,2011.Pierrette_Lemay.md) |  |
| May. 02,2012 | [Michel Benoit](May_02,2012.Michel_Benoit.md) |  |
| May. 23,2012 | [Michel Benoit](May_23,2012.Michel_Benoit.md) |  |
| dbo | [populate_multi_currency_by_loc_wk_$sp](dbo.populate_multi_currency_by_loc_wk_$sp.md) | dbo.a, dbo.calendar_date, dbo.calendar_merch_week, dbo.m, dbo.multi_currency_location_cost_wk, dbo.multi_currency_location_retail_wk, dbo.syn_multi_currency_location |
| Date | [Name](Date.Name.md) |  |
| Mar. 31,2010 | [Pierrette Lemay](Mar_31,2010.Pierrette_Lemay.md) |  |
| Apr. 07,2010 | [Pierrette Lemay](Apr_07,2010.Pierrette_Lemay.md) |  |
| May. 04,2011 | [Pierrette Lemay](May_04,2011.Pierrette_Lemay.md) |  |
| May. 02,2012 | [Michel Benoit](May_02,2012.Michel_Benoit.md) |  |
| May. 23,2012 | [Michel Benoit](May_23,2012.Michel_Benoit.md) |  |
| dbo | [post_binv_group_$sp](dbo.post_binv_group_$sp.md) | dbo.a, dbo.calendar, dbo.calendar_merch_period, dbo.calendar_merch_week, dbo.hist_oh_group_chn_li, dbo.hist_oh_group_chn_pd, dbo.hist_oh_group_chn_wk, dbo.hist_oh_group_chn_yr, dbo.hist_oh_group_loc_li, dbo.hist_oh_group_loc_pd, dbo.hist_oh_group_loc_wk, dbo.hist_oh_group_loc_yr, dbo.post_binv_group_adj |
| SELECT | [hierarchy_group_id,](SELECT.hierarchy_group_id,.md) |  |
| a.on_hand_retail = | [a.on_hand_retail + b.adjustment_retail,](a_on_hand_retail_=_a_on_hand_retail_+_b.adjustment_retail,.md) |  |
| dbo | [post_binv_group_adj_$sp](dbo.post_binv_group_adj_$sp.md) | dbo.post_binv_group_adj, dbo.post_binv_group_sum |
| dbo | [post_binv_group_adj_hist_$sp](dbo.post_binv_group_adj_hist_$sp.md) | dbo.hist_oh_group_loc_wk, dbo.post_binv_group_adj, dbo.post_binv_group_sum |
| dbo | [post_binv_sku_$sp](dbo.post_binv_sku_$sp.md) | dbo.a, dbo.calendar, dbo.calendar_merch_period, dbo.calendar_merch_week, dbo.hist_oh_sku_chn_li, dbo.hist_oh_sku_chn_pd, dbo.hist_oh_sku_chn_wk, dbo.hist_oh_sku_chn_yr, dbo.hist_oh_sku_loc_li, dbo.hist_oh_sku_loc_pd, dbo.hist_oh_sku_loc_wk, dbo.hist_oh_sku_loc_yr, dbo.post_binv_sku_adj |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| dbo | [post_binv_sku_adj_$sp](dbo.post_binv_sku_adj_$sp.md) | dbo.j, dbo.post_binv_sku_adj, dbo.post_binv_sku_sum, dbo.sku |
| dbo | [post_binv_sku_adj_hist_$sp](dbo.post_binv_sku_adj_hist_$sp.md) | dbo.hist_oh_sku_loc_wk, dbo.post_binv_sku_adj, dbo.post_binv_sku_sum |
| dbo | [post_binv_stlclr_adj_hist_$sp](dbo.post_binv_stlclr_adj_hist_$sp.md) | dbo.hist_oh_styleclr_loc_wk, dbo.post_binv_styleclr_adj, dbo.post_binv_styleclr_sum |
| dbo | [post_binv_style_$sp](dbo.post_binv_style_$sp.md) | dbo.a, dbo.calendar, dbo.calendar_merch_period, dbo.calendar_merch_week, dbo.hist_oh_style_chn_li, dbo.hist_oh_style_chn_pd, dbo.hist_oh_style_chn_wk, dbo.hist_oh_style_chn_yr, dbo.hist_oh_style_loc_li, dbo.hist_oh_style_loc_pd, dbo.hist_oh_style_loc_wk, dbo.hist_oh_style_loc_yr, dbo.post_binv_style_adj |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| dbo | [post_binv_style_adj_$sp](dbo.post_binv_style_adj_$sp.md) | dbo.post_binv_style_adj, dbo.post_binv_style_sum |
| dbo | [post_binv_style_adj_hist_$sp](dbo.post_binv_style_adj_hist_$sp.md) | dbo.hist_oh_style_loc_wk, dbo.post_binv_style_adj, dbo.post_binv_style_sum |
| dbo | [post_binv_styleclr_$sp](dbo.post_binv_styleclr_$sp.md) | dbo.a, dbo.calendar, dbo.calendar_merch_period, dbo.calendar_merch_week, dbo.hist_oh_styleclr_chn_li, dbo.hist_oh_styleclr_chn_pd, dbo.hist_oh_styleclr_chn_wk, dbo.hist_oh_styleclr_chn_yr, dbo.hist_oh_styleclr_loc_li, dbo.hist_oh_styleclr_loc_pd, dbo.hist_oh_styleclr_loc_wk, dbo.hist_oh_styleclr_loc_yr, dbo.post_binv_styleclr_adj |
| a.on_hand_retail = | [a.on_hand_retail + b.adjustment_retail,](a_on_hand_retail_=_a_on_hand_retail_+_b.adjustment_retail,.md) |  |
| a.on_hand_retail = | [a.on_hand_retail + b.adjustment_retail,](a_on_hand_retail_=_a_on_hand_retail_+_b.adjustment_retail,.md) |  |
| dbo | [post_binv_styleclr_adj_$sp](dbo.post_binv_styleclr_adj_$sp.md) | dbo.post_binv_styleclr_adj, dbo.post_binv_styleclr_sum |
| dbo | [post_cmp_group_$sp](dbo.post_cmp_group_$sp.md) | dbo.calendar_merch_week, dbo.hist_cmp_group_chn_li, dbo.hist_cmp_group_chn_pd, dbo.hist_cmp_group_chn_wk, dbo.hist_cmp_group_chn_yr, dbo.hist_cmp_group_loc_li, dbo.hist_cmp_group_loc_pd, dbo.hist_cmp_group_loc_wk, dbo.hist_cmp_group_loc_yr, dbo.job_detail, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.return_step_exists_$sp, dbo.wrk_cmp_group_loc_wk |
| dbo | [post_cmp_sku_$sp](dbo.post_cmp_sku_$sp.md) | dbo.calendar_merch_week, dbo.hist_cmp_sku_chn_li, dbo.hist_cmp_sku_chn_pd, dbo.hist_cmp_sku_chn_wk, dbo.hist_cmp_sku_chn_yr, dbo.hist_cmp_sku_loc_li, dbo.hist_cmp_sku_loc_pd, dbo.hist_cmp_sku_loc_wk, dbo.hist_cmp_sku_loc_yr, dbo.job_detail, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.return_step_exists_$sp, dbo.wrk_cmp_sku_loc_wk |
| dbo | [post_cmp_style_$sp](dbo.post_cmp_style_$sp.md) | dbo.calendar_merch_week, dbo.hist_cmp_style_chn_li, dbo.hist_cmp_style_chn_pd, dbo.hist_cmp_style_chn_wk, dbo.hist_cmp_style_chn_yr, dbo.hist_cmp_style_loc_li, dbo.hist_cmp_style_loc_pd, dbo.hist_cmp_style_loc_wk, dbo.hist_cmp_style_loc_yr, dbo.job_detail, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.return_step_exists_$sp, dbo.wrk_cmp_style_loc_wk |
| dbo | [post_cmp_style_color_$sp](dbo.post_cmp_style_color_$sp.md) | dbo.calendar_merch_week, dbo.hist_cmp_styleclr_chn_li, dbo.hist_cmp_styleclr_chn_pd, dbo.hist_cmp_styleclr_chn_wk, dbo.hist_cmp_styleclr_chn_yr, dbo.hist_cmp_styleclr_loc_li, dbo.hist_cmp_styleclr_loc_pd, dbo.hist_cmp_styleclr_loc_wk, dbo.hist_cmp_styleclr_loc_yr, dbo.job_detail, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.return_step_exists_$sp, dbo.wrk_cmp_styleclr_loc_wk |
| dbo | [post_cmp_work_group_$sp](dbo.post_cmp_work_group_$sp.md) | dbo.a, dbo.component_xref, dbo.history_component, dbo.post_cmp_work_group, dbo.post_hist_cmp_group |
| Jul21,07 Yan Ding | [87495](Jul21,07_Yan_Ding.87495.md) |  |
| FROM | [post_hist_cmp_group a,](FROM.post_hist_cmp_group_a,.md) |  |
| WHERE | [a.hierarchy_group_id = @curr_hierarchy_group_id](WHERE_a.hierarchy_group_id_=_@curr_hierarchy_group_id.md) |  |
| AND | [a.transaction_type_code = b.transaction_type_code](AND_a_transaction_type_code_=_b.transaction_type_code.md) |  |
| AND | [b.component_type_code IS NOT NULL](AND_b.component_type_code_IS_NOT_NULL.md) |  |
| AND | [b.component_type_code = c.component_type_code](AND_b_component_type_code_=_c.component_type_code.md) |  |
| DELETE | [a](DELETE.a.md) |  |
| FROM | [post_hist_cmp_group a](FROM.post_hist_cmp_group_a.md) |  |
| WHERE | [a.hierarchy_group_id = @curr_hierarchy_group_id](WHERE_a.hierarchy_group_id_=_@curr_hierarchy_group_id.md) |  |
| AND | [EXISTS](AND.EXISTS.md) |  |
| DELETE | [a](DELETE.a.md) |  |
| FROM | [post_hist_cmp_group a](FROM.post_hist_cmp_group_a.md) |  |
| WHERE | [a.hierarchy_group_id = @curr_hierarchy_group_id](WHERE_a.hierarchy_group_id_=_@curr_hierarchy_group_id.md) |  |
| AND | [EXISTS](AND.EXISTS.md) |  |
| dbo | [post_cmp_work_sku_$sp](dbo.post_cmp_work_sku_$sp.md) | dbo.component_xref, dbo.history_component, dbo.post_cmp_work_sku, dbo.post_hist_cmp_sku |
| dbo | [post_cmp_work_style_$sp](dbo.post_cmp_work_style_$sp.md) | dbo.a, dbo.component_xref, dbo.history_component, dbo.post_cmp_work_style, dbo.post_hist_cmp_style |
| Jul21,07 Yan Ding | [87495](Jul21,07_Yan_Ding.87495.md) |  |
| FROM | [post_hist_cmp_style a,](FROM.post_hist_cmp_style_a,.md) |  |
| WHERE | [a.style_id = @curr_style_id](WHERE_a.style_id_=_@curr_style_id.md) |  |
| AND | [a.transaction_type_code = b.transaction_type_code](AND_a_transaction_type_code_=_b.transaction_type_code.md) |  |
| AND | [b.component_type_code IS NOT NULL](AND_b.component_type_code_IS_NOT_NULL.md) |  |
| AND | [b.component_type_code = c.component_type_code](AND_b_component_type_code_=_c.component_type_code.md) |  |
| DELETE | [a](DELETE.a.md) |  |
| FROM | [post_hist_cmp_style a](FROM.post_hist_cmp_style_a.md) |  |
| WHERE | [a.style_id = @curr_style_id](WHERE_a.style_id_=_@curr_style_id.md) |  |
| AND | [EXISTS](AND.EXISTS.md) |  |
| DELETE | [a](DELETE.a.md) |  |
| FROM | [post_hist_cmp_style a](FROM.post_hist_cmp_style_a.md) |  |
| WHERE | [a.style_id = @curr_style_id](WHERE_a.style_id_=_@curr_style_id.md) |  |
| AND | [EXISTS](AND.EXISTS.md) |  |
| dbo | [post_cmp_work_styleclr_$sp](dbo.post_cmp_work_styleclr_$sp.md) | dbo.a, dbo.component_xref, dbo.history_component, dbo.post_cmp_work_styleclr, dbo.post_hist_cmp_styleclr |
| Jul21,07 Yan Ding | [87495](Jul21,07_Yan_Ding.87495.md) |  |
| FROM | [post_hist_cmp_styleclr a,](FROM.post_hist_cmp_styleclr_a,.md) |  |
| WHERE | [a.style_id = @curr_style_id](WHERE_a.style_id_=_@curr_style_id.md) |  |
| AND | [a.transaction_type_code = b.transaction_type_code](AND_a_transaction_type_code_=_b.transaction_type_code.md) |  |
| AND | [b.component_type_code IS NOT NULL](AND_b.component_type_code_IS_NOT_NULL.md) |  |
| AND | [b.component_type_code = c.component_type_code](AND_b_component_type_code_=_c.component_type_code.md) |  |
| DELETE | [a](DELETE.a.md) |  |
| FROM | [post_hist_cmp_styleclr a](FROM.post_hist_cmp_styleclr_a.md) |  |
| WHERE | [a.style_id = @curr_style_id](WHERE_a.style_id_=_@curr_style_id.md) |  |
| AND | [EXISTS](AND.EXISTS.md) |  |
| DELETE | [a](DELETE.a.md) |  |
| FROM | [post_hist_cmp_styleclr a](FROM.post_hist_cmp_styleclr_a.md) |  |
| WHERE | [a.style_id = @curr_style_id](WHERE_a.style_id_=_@curr_style_id.md) |  |
| AND | [EXISTS](AND.EXISTS.md) |  |
| dbo | [post_flash_group_$sp](dbo.post_flash_group_$sp.md) | dbo.hist_flsh_chn_da, dbo.hist_flsh_group_chn_da, dbo.hist_flsh_group_loc_da, dbo.hist_flsh_loc_da, dbo.job_detail, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.return_step_exists_$sp, dbo.wrk_flsh_group_loc_da |
| dbo | [post_flash_style_$sp](dbo.post_flash_style_$sp.md) | dbo.hist_flsh_style_chn_da, dbo.hist_flsh_style_loc_da, dbo.job_detail, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.return_step_exists_$sp, dbo.wrk_flsh_style_loc_da |
| dbo | [post_flsh_ent_$sp](dbo.post_flsh_ent_$sp.md) | dbo.a, dbo.hist_flsh_chn_da, dbo.hist_flsh_loc_da, dbo.post_flsh_ent_sum |
| sales_date                   smalldatetime | [NOT NULL,](sales_date_smalldatetime.NOT_NULL,.md) |  |
| sales_net_units | [int](sales_net_units.int.md) |  |
| sales_net_retail | [decimal(14,2)](sales_net_retail.decimal_14,2.md) |  |
| sales_net_cost | [decimal(14,2)](sales_net_cost.decimal_14,2.md) |  |
| sales_date                  smalldatetime | [NOT NULL,](sales_date_smalldatetime.NOT_NULL,.md) |  |
| sales_net_units | [int](sales_net_units.int.md) |  |
| sales_net_retail | [decimal(14,2)](sales_net_retail.decimal_14,2.md) |  |
| sales_net_cost | [decimal(14,2)](sales_net_cost.decimal_14,2.md) |  |
| SELECT | [location_id,](SELECT.location_id,.md) |  |
| FROM | [post_flsh_ent_sum WITH (NOLOCK)](FROM.post_flsh_ent_sum_WITH_NOLOCK.md) |  |
| WHERE | [sales_date = @curr_sales_date](WHERE.sales_date_=_@curr_sales_date.md) |  |
| SELECT | [sales_date,](SELECT.sales_date,.md) |  |
| FROM | [post_flsh_ent_sum  WITH (NOLOCK)](FROM.post_flsh_ent_sum_WITH_NOLOCK.md) |  |
| WHERE | [sales_date = @curr_sales_date](WHERE.sales_date_=_@curr_sales_date.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [sales_net_units = a.sales_net_units + b.sales_net_units,](SET_sales_net_units_=_a_sales_net_units_+_b.sales_net_units,.md) |  |
| FROM | [hist_flsh_loc_da a,](FROM.hist_flsh_loc_da_a,.md) |  |
| WHERE | [a.location_id = b.location_id](WHERE_a_location_id_=_b.location_id.md) |  |
| AND | [a.sales_date = b.sales_date](AND_a_sales_date_=_b.sales_date.md) |  |
| SELECT | [a.location_id,](SELECT_a.location_id,.md) |  |
| FROM | [#ent_loc_da a  WITH (NOLOCK)](FROM.#ent_loc_da_a_WITH_NOLOCK.md) |  |
| WHERE | [NOT EXISTS](WHERE.NOT_EXISTS.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [sales_net_units = a.sales_net_units + b.sales_net_units,](SET_sales_net_units_=_a_sales_net_units_+_b.sales_net_units,.md) |  |
| FROM | [hist_flsh_chn_da a,](FROM.hist_flsh_chn_da_a,.md) |  |
| WHERE | [a.sales_date = b.sales_date](WHERE_a_sales_date_=_b.sales_date.md) |  |
| SELECT | [a.sales_date,](SELECT_a.sales_date,.md) |  |
| FROM | [#ent_chn_da a  WITH (NOLOCK)](FROM.#ent_chn_da_a_WITH_NOLOCK.md) |  |
| WHERE | [NOT EXISTS](WHERE.NOT_EXISTS.md) |  |
| DELETE | [post_flsh_ent_sum](DELETE.post_flsh_ent_sum.md) |  |
| WHERE | [sales_date = @curr_sales_date](WHERE.sales_date_=_@curr_sales_date.md) |  |
| dbo | [post_hist_cmp_group_$sp](dbo.post_hist_cmp_group_$sp.md) | dbo.a, dbo.calendar_merch_week, dbo.hist_cmp_group_chn_li, dbo.hist_cmp_group_chn_pd, dbo.hist_cmp_group_chn_wk, dbo.hist_cmp_group_chn_yr, dbo.hist_cmp_group_loc_li, dbo.hist_cmp_group_loc_pd, dbo.hist_cmp_group_loc_wk, dbo.hist_cmp_group_loc_yr, dbo.mv_fact_queue, dbo.plan_exp_table_group, dbo.post_cmp_work_group |
| SELECT | [hierarchy_group_id,](SELECT.hierarchy_group_id,.md) |  |
| FROM | [post_cmp_work_group  WITH (NOLOCK)](FROM.post_cmp_work_group_WITH_NOLOCK.md) |  |
| WHERE | [hierarchy_group_id BETWEEN @from_group_id AND @to_group_id](WHERE.hierarchy_group_id_BETWEEN_@from_group_id_AND_@to_group_id.md) |  |
| SELECT | [hierarchy_group_id,](SELECT.hierarchy_group_id,.md) |  |
| FROM | [post_cmp_work_group WITH (NOLOCK)](FROM.post_cmp_work_group_WITH_NOLOCK.md) |  |
| WHERE | [hierarchy_group_id BETWEEN @from_group_id AND @to_group_id](WHERE.hierarchy_group_id_BETWEEN_@from_group_id_AND_@to_group_id.md) |  |
| SELECT | [a.hierarchy_group_id,](SELECT_a.hierarchy_group_id,.md) |  |
| FROM | [post_cmp_work_group a,](FROM.post_cmp_work_group_a,.md) |  |
| WHERE | [a.hierarchy_group_id BETWEEN @from_group_id AND @to_group_id](WHERE_a.hierarchy_group_id_BETWEEN_@from_group_id_AND_@to_group_id.md) |  |
| AND | [a.merch_year_wk / 100 = c.merch_year](AND_a_merch_year_wk_100_=_c.merch_year.md) |  |
| AND | [a.merch_year_wk % 100 = c.merch_week](AND_a_merch_year_wk_%_100_=_c.merch_week.md) |  |
| SELECT | [a.hierarchy_group_id,](SELECT_a.hierarchy_group_id,.md) |  |
| FROM | [post_cmp_work_group a,](FROM.post_cmp_work_group_a,.md) |  |
| WHERE | [a.hierarchy_group_id BETWEEN @from_group_id AND @to_group_id](WHERE_a.hierarchy_group_id_BETWEEN_@from_group_id_AND_@to_group_id.md) |  |
| AND | [a.merch_year_wk / 100 = c.merch_year](AND_a_merch_year_wk_100_=_c.merch_year.md) |  |
| AND | [a.merch_year_wk % 100 = c.merch_week](AND_a_merch_year_wk_%_100_=_c.merch_week.md) |  |
| SELECT | [hierarchy_group_id,](SELECT.hierarchy_group_id,.md) |  |
| FROM | [post_cmp_work_group WITH (NOLOCK)](FROM.post_cmp_work_group_WITH_NOLOCK.md) |  |
| WHERE | [hierarchy_group_id BETWEEN @from_group_id AND @to_group_id](WHERE.hierarchy_group_id_BETWEEN_@from_group_id_AND_@to_group_id.md) |  |
| SELECT | [hierarchy_group_id,](SELECT.hierarchy_group_id,.md) |  |
| FROM | [post_cmp_work_group WITH (NOLOCK)](FROM.post_cmp_work_group_WITH_NOLOCK.md) |  |
| WHERE | [hierarchy_group_id BETWEEN @from_group_id AND @to_group_id](WHERE.hierarchy_group_id_BETWEEN_@from_group_id_AND_@to_group_id.md) |  |
| SELECT | [hierarchy_group_id,](SELECT.hierarchy_group_id,.md) |  |
| FROM | [post_cmp_work_group WITH (NOLOCK)](FROM.post_cmp_work_group_WITH_NOLOCK.md) |  |
| WHERE | [hierarchy_group_id BETWEEN @from_group_id AND @to_group_id](WHERE.hierarchy_group_id_BETWEEN_@from_group_id_AND_@to_group_id.md) |  |
| SELECT | [hierarchy_group_id,](SELECT.hierarchy_group_id,.md) |  |
| FROM | [post_cmp_work_group WITH (NOLOCK)](FROM.post_cmp_work_group_WITH_NOLOCK.md) |  |
| WHERE | [hierarchy_group_id BETWEEN @from_group_id AND @to_group_id](WHERE.hierarchy_group_id_BETWEEN_@from_group_id_AND_@to_group_id.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.component_units = a.component_units + b.component_units,](SET_a_component_units_=_a_component_units_+_b.component_units,.md) |  |
| FROM | [hist_cmp_group_loc_wk a,](FROM.hist_cmp_group_loc_wk_a,.md) |  |
| WHERE | [b.hierarchy_group_id = a.hierarchy_group_id](WHERE_b_hierarchy_group_id_=_a.hierarchy_group_id.md) |  |
| AND | [b.merch_year_wk = a.merch_year_wk](AND_b_merch_year_wk_=_a.merch_year_wk.md) |  |
| AND | [b.location_id = a.location_id](AND_b_location_id_=_a.location_id.md) |  |
| AND | [b.component_type_code = a.component_type_code](AND_b_component_type_code_=_a.component_type_code.md) |  |
| AND | [b.history_component_id = a.history_component_id](AND_b_history_component_id_=_a.history_component_id.md) |  |
| SELECT | [a.hierarchy_group_id,](SELECT_a.hierarchy_group_id,.md) |  |
| FROM | [#group_loc_wk a](FROM.#group_loc_wk_a.md) |  |
| WHERE | [NOT EXISTS (SELECT *](WHERE.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.component_units = a.component_units + b.component_units,](SET_a_component_units_=_a_component_units_+_b.component_units,.md) |  |
| FROM | [hist_cmp_group_chn_wk a,](FROM.hist_cmp_group_chn_wk_a,.md) |  |
| WHERE | [b.hierarchy_group_id = a.hierarchy_group_id](WHERE_b_hierarchy_group_id_=_a.hierarchy_group_id.md) |  |
| AND | [b.merch_year_wk = a.merch_year_wk](AND_b_merch_year_wk_=_a.merch_year_wk.md) |  |
| AND | [b.component_type_code = a.component_type_code](AND_b_component_type_code_=_a.component_type_code.md) |  |
| AND | [b.history_component_id = a.history_component_id](AND_b_history_component_id_=_a.history_component_id.md) |  |
| SELECT | [a.hierarchy_group_id,](SELECT_a.hierarchy_group_id,.md) |  |
| FROM | [#group_chn_wk a](FROM.#group_chn_wk_a.md) |  |
| WHERE | [NOT EXISTS (SELECT *](WHERE.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.component_units = a.component_units + b.component_units,](SET_a_component_units_=_a_component_units_+_b.component_units,.md) |  |
| FROM | [hist_cmp_group_loc_pd a,](FROM.hist_cmp_group_loc_pd_a,.md) |  |
| WHERE | [b.hierarchy_group_id = a.hierarchy_group_id](WHERE_b_hierarchy_group_id_=_a.hierarchy_group_id.md) |  |
| AND | [b.merch_year_pd = a.merch_year_pd](AND_b_merch_year_pd_=_a.merch_year_pd.md) |  |
| AND | [b.location_id = a.location_id](AND_b_location_id_=_a.location_id.md) |  |
| AND | [b.component_type_code = a.component_type_code](AND_b_component_type_code_=_a.component_type_code.md) |  |
| AND | [b.history_component_id = a.history_component_id](AND_b_history_component_id_=_a.history_component_id.md) |  |
| SELECT | [a.hierarchy_group_id,](SELECT_a.hierarchy_group_id,.md) |  |
| FROM | [#group_loc_pd a](FROM.#group_loc_pd_a.md) |  |
| WHERE | [NOT EXISTS (SELECT *](WHERE.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.component_units = a.component_units + b.component_units,](SET_a_component_units_=_a_component_units_+_b.component_units,.md) |  |
| FROM | [hist_cmp_group_chn_pd a,](FROM.hist_cmp_group_chn_pd_a,.md) |  |
| WHERE | [b.hierarchy_group_id = a.hierarchy_group_id](WHERE_b_hierarchy_group_id_=_a.hierarchy_group_id.md) |  |
| AND | [b.merch_year_pd = a.merch_year_pd](AND_b_merch_year_pd_=_a.merch_year_pd.md) |  |
| AND | [b.component_type_code = a.component_type_code](AND_b_component_type_code_=_a.component_type_code.md) |  |
| AND | [b.history_component_id = a.history_component_id](AND_b_history_component_id_=_a.history_component_id.md) |  |
| SELECT | [a.hierarchy_group_id,](SELECT_a.hierarchy_group_id,.md) |  |
| FROM | [#group_chn_pd a](FROM.#group_chn_pd_a.md) |  |
| WHERE | [NOT EXISTS (SELECT *](WHERE.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.component_units = a.component_units + b.component_units,](SET_a_component_units_=_a_component_units_+_b.component_units,.md) |  |
| FROM | [hist_cmp_group_loc_yr a,](FROM.hist_cmp_group_loc_yr_a,.md) |  |
| WHERE | [b.hierarchy_group_id = a.hierarchy_group_id](WHERE_b_hierarchy_group_id_=_a.hierarchy_group_id.md) |  |
| AND | [b.merch_year = a.merch_year](AND_b_merch_year_=_a.merch_year.md) |  |
| AND | [b.location_id = a.location_id](AND_b_location_id_=_a.location_id.md) |  |
| AND | [b.component_type_code = a.component_type_code](AND_b_component_type_code_=_a.component_type_code.md) |  |
| AND | [b.history_component_id = a.history_component_id](AND_b_history_component_id_=_a.history_component_id.md) |  |
| SELECT | [a.hierarchy_group_id,](SELECT_a.hierarchy_group_id,.md) |  |
| FROM | [#group_loc_yr a](FROM.#group_loc_yr_a.md) |  |
| WHERE | [NOT EXISTS (SELECT *](WHERE.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.component_units = a.component_units + b.component_units,](SET_a_component_units_=_a_component_units_+_b.component_units,.md) |  |
| FROM | [hist_cmp_group_chn_yr a,](FROM.hist_cmp_group_chn_yr_a,.md) |  |
| WHERE | [b.hierarchy_group_id = a.hierarchy_group_id](WHERE_b_hierarchy_group_id_=_a.hierarchy_group_id.md) |  |
| AND | [b.merch_year = a.merch_year](AND_b_merch_year_=_a.merch_year.md) |  |
| AND | [b.component_type_code = a.component_type_code](AND_b_component_type_code_=_a.component_type_code.md) |  |
| AND | [b.history_component_id = a.history_component_id](AND_b_history_component_id_=_a.history_component_id.md) |  |
| SELECT | [a.hierarchy_group_id,](SELECT_a.hierarchy_group_id,.md) |  |
| FROM | [#group_chn_yr a](FROM.#group_chn_yr_a.md) |  |
| WHERE | [NOT EXISTS (SELECT *](WHERE.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.component_units = a.component_units + b.component_units,](SET_a_component_units_=_a_component_units_+_b.component_units,.md) |  |
| FROM | [hist_cmp_group_loc_li a,](FROM.hist_cmp_group_loc_li_a,.md) |  |
| WHERE | [b.hierarchy_group_id = a.hierarchy_group_id](WHERE_b_hierarchy_group_id_=_a.hierarchy_group_id.md) |  |
| AND | [b.location_id = a.location_id](AND_b_location_id_=_a.location_id.md) |  |
| AND | [b.component_type_code = a.component_type_code](AND_b_component_type_code_=_a.component_type_code.md) |  |
| AND | [b.history_component_id = a.history_component_id](AND_b_history_component_id_=_a.history_component_id.md) |  |
| SELECT | [a.hierarchy_group_id,](SELECT_a.hierarchy_group_id,.md) |  |
| FROM | [#group_loc_li a](FROM.#group_loc_li_a.md) |  |
| WHERE | [NOT EXISTS (SELECT *](WHERE.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.component_units = a.component_units + b.component_units,](SET_a_component_units_=_a_component_units_+_b.component_units,.md) |  |
| FROM | [hist_cmp_group_chn_li a,](FROM.hist_cmp_group_chn_li_a,.md) |  |
| WHERE | [b.hierarchy_group_id = a.hierarchy_group_id](WHERE_b_hierarchy_group_id_=_a.hierarchy_group_id.md) |  |
| AND | [b.component_type_code = a.component_type_code](AND_b_component_type_code_=_a.component_type_code.md) |  |
| AND | [b.history_component_id = a.history_component_id](AND_b_history_component_id_=_a.history_component_id.md) |  |
| SELECT | [a.hierarchy_group_id,](SELECT_a.hierarchy_group_id,.md) |  |
| FROM | [#group_chn_li a](FROM.#group_chn_li_a.md) |  |
| WHERE | [NOT EXISTS (SELECT *](WHERE.NOT_EXISTS_SELECT.md) |  |
| FROM | [post_cmp_work_group a, plan_exp_table_group](FROM.post_cmp_work_group_a,_plan_exp_table_group.md) |  |
| WHERE | [a.hierarchy_group_id BETWEEN @from_group_id AND @to_group_id](WHERE_a.hierarchy_group_id_BETWEEN_@from_group_id_AND_@to_group_id.md) |  |
| AND | [plan_exp_table_group_id = 3;](AND.plan_exp_table_group_id_=_3;.md) |  |
| dbo | [post_hist_cmp_sku_$sp](dbo.post_hist_cmp_sku_$sp.md) | dbo.a, dbo.calendar_merch_week, dbo.hist_cmp_sku_chn_li, dbo.hist_cmp_sku_chn_pd, dbo.hist_cmp_sku_chn_wk, dbo.hist_cmp_sku_chn_yr, dbo.hist_cmp_sku_loc_li, dbo.hist_cmp_sku_loc_pd, dbo.hist_cmp_sku_loc_wk, dbo.hist_cmp_sku_loc_yr, dbo.post_cmp_work_sku |
| create proc dbo.post_hist_cmp_sku_$sp | [@curr_style_id decimal(12,0),](create_proc_dbo_post_hist_cmp_sku_$sp.@curr_style_id_decimal_12,0_,.md) |  |
| component_type_code | [smallint  NOT NULL,](component_type_code.smallint_NOT_NULL,.md) |  |
| component_type_code | [smallint  NOT NULL,](component_type_code.smallint_NOT_NULL,.md) |  |
| component_type_code | [smallint  NOT NULL,](component_type_code.smallint_NOT_NULL,.md) |  |
| component_type_code | [smallint  NOT NULL,](component_type_code.smallint_NOT_NULL,.md) |  |
| component_type_code | [smallint  NOT NULL,](component_type_code.smallint_NOT_NULL,.md) |  |
| component_type_code | [smallint  NOT NULL,](component_type_code.smallint_NOT_NULL,.md) |  |
| component_type_code | [smallint  NOT NULL,](component_type_code.smallint_NOT_NULL,.md) |  |
| component_type_code | [smallint  NOT NULL,](component_type_code.smallint_NOT_NULL,.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| dbo | [post_hist_cmp_style_$sp](dbo.post_hist_cmp_style_$sp.md) | dbo.a, dbo.calendar_merch_week, dbo.hist_cmp_style_chn_li, dbo.hist_cmp_style_chn_pd, dbo.hist_cmp_style_chn_wk, dbo.hist_cmp_style_chn_yr, dbo.hist_cmp_style_loc_li, dbo.hist_cmp_style_loc_pd, dbo.hist_cmp_style_loc_wk, dbo.hist_cmp_style_loc_yr, dbo.post_cmp_work_style |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [post_cmp_work_style](FROM.post_cmp_work_style.md) |  |
| WHERE | [style_id BETWEEN @from_style_id AND @to_style_id](WHERE.style_id_BETWEEN_@from_style_id_AND_@to_style_id.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [post_cmp_work_style](FROM.post_cmp_work_style.md) |  |
| WHERE | [style_id BETWEEN @from_style_id AND @to_style_id](WHERE.style_id_BETWEEN_@from_style_id_AND_@to_style_id.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [post_cmp_work_style a,](FROM.post_cmp_work_style_a,.md) |  |
| WHERE | [a.style_id BETWEEN @from_style_id AND @to_style_id](WHERE_a.style_id_BETWEEN_@from_style_id_AND_@to_style_id.md) |  |
| AND | [a.merch_year_wk / 100 = c.merch_year](AND_a_merch_year_wk_100_=_c.merch_year.md) |  |
| AND | [a.merch_year_wk % 100 = c.merch_week](AND_a_merch_year_wk_%_100_=_c.merch_week.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [post_cmp_work_style a,](FROM.post_cmp_work_style_a,.md) |  |
| WHERE | [a.style_id BETWEEN @from_style_id AND @to_style_id](WHERE_a.style_id_BETWEEN_@from_style_id_AND_@to_style_id.md) |  |
| AND | [a.merch_year_wk / 100 = c.merch_year](AND_a_merch_year_wk_100_=_c.merch_year.md) |  |
| AND | [a.merch_year_wk % 100 = c.merch_week](AND_a_merch_year_wk_%_100_=_c.merch_week.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [post_cmp_work_style](FROM.post_cmp_work_style.md) |  |
| WHERE | [style_id BETWEEN @from_style_id AND @to_style_id](WHERE.style_id_BETWEEN_@from_style_id_AND_@to_style_id.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [post_cmp_work_style](FROM.post_cmp_work_style.md) |  |
| WHERE | [style_id BETWEEN @from_style_id AND @to_style_id](WHERE.style_id_BETWEEN_@from_style_id_AND_@to_style_id.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [post_cmp_work_style](FROM.post_cmp_work_style.md) |  |
| WHERE | [style_id BETWEEN @from_style_id AND @to_style_id](WHERE.style_id_BETWEEN_@from_style_id_AND_@to_style_id.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [post_cmp_work_style](FROM.post_cmp_work_style.md) |  |
| WHERE | [style_id BETWEEN @from_style_id AND @to_style_id](WHERE.style_id_BETWEEN_@from_style_id_AND_@to_style_id.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.component_units = a.component_units + b.component_units,](SET_a_component_units_=_a_component_units_+_b.component_units,.md) |  |
| FROM | [hist_cmp_style_loc_wk a,](FROM.hist_cmp_style_loc_wk_a,.md) |  |
| WHERE | [b.style_id = a.style_id](WHERE_b_style_id_=_a.style_id.md) |  |
| AND | [b.merch_year_wk = a.merch_year_wk](AND_b_merch_year_wk_=_a.merch_year_wk.md) |  |
| AND | [b.location_id = a.location_id](AND_b_location_id_=_a.location_id.md) |  |
| AND | [b.component_type_code = a.component_type_code](AND_b_component_type_code_=_a.component_type_code.md) |  |
| AND | [b.history_component_id = a.history_component_id](AND_b_history_component_id_=_a.history_component_id.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [#style_loc_wk a](FROM.#style_loc_wk_a.md) |  |
| WHERE | [NOT EXISTS (SELECT *](WHERE.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.component_units = a.component_units + b.component_units,](SET_a_component_units_=_a_component_units_+_b.component_units,.md) |  |
| FROM | [hist_cmp_style_chn_wk a,](FROM.hist_cmp_style_chn_wk_a,.md) |  |
| WHERE | [b.style_id = a.style_id](WHERE_b_style_id_=_a.style_id.md) |  |
| AND | [b.merch_year_wk = a.merch_year_wk](AND_b_merch_year_wk_=_a.merch_year_wk.md) |  |
| AND | [b.component_type_code = a.component_type_code](AND_b_component_type_code_=_a.component_type_code.md) |  |
| AND | [b.history_component_id = a.history_component_id](AND_b_history_component_id_=_a.history_component_id.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [#style_chn_wk a](FROM.#style_chn_wk_a.md) |  |
| WHERE | [NOT EXISTS (SELECT *](WHERE.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.component_units = a.component_units + b.component_units,](SET_a_component_units_=_a_component_units_+_b.component_units,.md) |  |
| FROM | [hist_cmp_style_loc_pd a,](FROM.hist_cmp_style_loc_pd_a,.md) |  |
| WHERE | [b.style_id = a.style_id](WHERE_b_style_id_=_a.style_id.md) |  |
| AND | [b.merch_year_pd = a.merch_year_pd](AND_b_merch_year_pd_=_a.merch_year_pd.md) |  |
| AND | [b.location_id = a.location_id](AND_b_location_id_=_a.location_id.md) |  |
| AND | [b.component_type_code = a.component_type_code](AND_b_component_type_code_=_a.component_type_code.md) |  |
| AND | [b.history_component_id = a.history_component_id](AND_b_history_component_id_=_a.history_component_id.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [#style_loc_pd a](FROM.#style_loc_pd_a.md) |  |
| WHERE | [NOT EXISTS (SELECT *](WHERE.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.component_units = a.component_units + b.component_units,](SET_a_component_units_=_a_component_units_+_b.component_units,.md) |  |
| FROM | [hist_cmp_style_chn_pd a,](FROM.hist_cmp_style_chn_pd_a,.md) |  |
| WHERE | [b.style_id = a.style_id](WHERE_b_style_id_=_a.style_id.md) |  |
| AND | [b.merch_year_pd = a.merch_year_pd](AND_b_merch_year_pd_=_a.merch_year_pd.md) |  |
| AND | [b.component_type_code = a.component_type_code](AND_b_component_type_code_=_a.component_type_code.md) |  |
| AND | [b.history_component_id = a.history_component_id](AND_b_history_component_id_=_a.history_component_id.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [#style_chn_pd a](FROM.#style_chn_pd_a.md) |  |
| WHERE | [NOT EXISTS (SELECT *](WHERE.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.component_units = a.component_units + b.component_units,](SET_a_component_units_=_a_component_units_+_b.component_units,.md) |  |
| FROM | [hist_cmp_style_loc_yr a,](FROM.hist_cmp_style_loc_yr_a,.md) |  |
| WHERE | [b.style_id = a.style_id](WHERE_b_style_id_=_a.style_id.md) |  |
| AND | [b.merch_year = a.merch_year](AND_b_merch_year_=_a.merch_year.md) |  |
| AND | [b.location_id = a.location_id](AND_b_location_id_=_a.location_id.md) |  |
| AND | [b.component_type_code = a.component_type_code](AND_b_component_type_code_=_a.component_type_code.md) |  |
| AND | [b.history_component_id = a.history_component_id](AND_b_history_component_id_=_a.history_component_id.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [#style_loc_yr a](FROM.#style_loc_yr_a.md) |  |
| WHERE | [NOT EXISTS (SELECT *](WHERE.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.component_units = a.component_units + b.component_units,](SET_a_component_units_=_a_component_units_+_b.component_units,.md) |  |
| FROM | [hist_cmp_style_chn_yr a,](FROM.hist_cmp_style_chn_yr_a,.md) |  |
| WHERE | [b.style_id = a.style_id](WHERE_b_style_id_=_a.style_id.md) |  |
| AND | [b.merch_year = a.merch_year](AND_b_merch_year_=_a.merch_year.md) |  |
| AND | [b.component_type_code = a.component_type_code](AND_b_component_type_code_=_a.component_type_code.md) |  |
| AND | [b.history_component_id = a.history_component_id](AND_b_history_component_id_=_a.history_component_id.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [#style_chn_yr a](FROM.#style_chn_yr_a.md) |  |
| WHERE | [NOT EXISTS (SELECT *](WHERE.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.component_units = a.component_units + b.component_units,](SET_a_component_units_=_a_component_units_+_b.component_units,.md) |  |
| FROM | [hist_cmp_style_loc_li a,](FROM.hist_cmp_style_loc_li_a,.md) |  |
| WHERE | [b.style_id = a.style_id](WHERE_b_style_id_=_a.style_id.md) |  |
| AND | [b.location_id = a.location_id](AND_b_location_id_=_a.location_id.md) |  |
| AND | [b.component_type_code = a.component_type_code](AND_b_component_type_code_=_a.component_type_code.md) |  |
| AND | [b.history_component_id = a.history_component_id](AND_b_history_component_id_=_a.history_component_id.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [#style_loc_li a](FROM.#style_loc_li_a.md) |  |
| WHERE | [NOT EXISTS (SELECT *](WHERE.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.component_units = a.component_units + b.component_units,](SET_a_component_units_=_a_component_units_+_b.component_units,.md) |  |
| FROM | [hist_cmp_style_chn_li a,](FROM.hist_cmp_style_chn_li_a,.md) |  |
| WHERE | [b.style_id = a.style_id](WHERE_b_style_id_=_a.style_id.md) |  |
| AND | [b.component_type_code = a.component_type_code](AND_b_component_type_code_=_a.component_type_code.md) |  |
| AND | [b.history_component_id = a.history_component_id](AND_b_history_component_id_=_a.history_component_id.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [#style_chn_li a](FROM.#style_chn_li_a.md) |  |
| WHERE | [NOT EXISTS (SELECT *](WHERE.NOT_EXISTS_SELECT.md) |  |
| dbo | [post_hist_cmp_styleclr_$sp](dbo.post_hist_cmp_styleclr_$sp.md) | dbo.a, dbo.calendar_merch_week, dbo.hist_cmp_styleclr_chn_li, dbo.hist_cmp_styleclr_chn_pd, dbo.hist_cmp_styleclr_chn_wk, dbo.hist_cmp_styleclr_chn_yr, dbo.hist_cmp_styleclr_loc_li, dbo.hist_cmp_styleclr_loc_pd, dbo.hist_cmp_styleclr_loc_wk, dbo.hist_cmp_styleclr_loc_yr, dbo.post_cmp_work_styleclr |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [post_cmp_work_styleclr](FROM.post_cmp_work_styleclr.md) |  |
| WHERE | [style_id BETWEEN @curr_style_id AND @curr_style_id_2](WHERE.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [post_cmp_work_styleclr](FROM.post_cmp_work_styleclr.md) |  |
| WHERE | [style_id BETWEEN @curr_style_id AND @curr_style_id_2](WHERE.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [post_cmp_work_styleclr a,](FROM.post_cmp_work_styleclr_a,.md) |  |
| WHERE | [a.style_id BETWEEN @curr_style_id AND @curr_style_id_2](WHERE_a.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| AND | [a.merch_year_wk / 100 = c.merch_year](AND_a_merch_year_wk_100_=_c.merch_year.md) |  |
| AND | [a.merch_year_wk % 100 = c.merch_week](AND_a_merch_year_wk_%_100_=_c.merch_week.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [post_cmp_work_styleclr a,](FROM.post_cmp_work_styleclr_a,.md) |  |
| WHERE | [a.style_id BETWEEN @curr_style_id AND @curr_style_id_2](WHERE_a.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| AND | [a.merch_year_wk / 100 = c.merch_year](AND_a_merch_year_wk_100_=_c.merch_year.md) |  |
| AND | [a.merch_year_wk % 100 = c.merch_week](AND_a_merch_year_wk_%_100_=_c.merch_week.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [post_cmp_work_styleclr](FROM.post_cmp_work_styleclr.md) |  |
| WHERE | [style_id BETWEEN @curr_style_id AND @curr_style_id_2](WHERE.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [post_cmp_work_styleclr](FROM.post_cmp_work_styleclr.md) |  |
| WHERE | [style_id BETWEEN @curr_style_id AND @curr_style_id_2](WHERE.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [post_cmp_work_styleclr](FROM.post_cmp_work_styleclr.md) |  |
| WHERE | [style_id BETWEEN @curr_style_id AND @curr_style_id_2](WHERE.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [post_cmp_work_styleclr](FROM.post_cmp_work_styleclr.md) |  |
| WHERE | [style_id BETWEEN @curr_style_id AND @curr_style_id_2](WHERE.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.component_units = a.component_units + b.component_units,](SET_a_component_units_=_a_component_units_+_b.component_units,.md) |  |
| FROM | [hist_cmp_styleclr_loc_wk a,](FROM.hist_cmp_styleclr_loc_wk_a,.md) |  |
| WHERE | [b.style_id = a.style_id](WHERE_b_style_id_=_a.style_id.md) |  |
| AND | [b.color_id = a.color_id](AND_b_color_id_=_a.color_id.md) |  |
| AND | [b.merch_year_wk = a.merch_year_wk](AND_b_merch_year_wk_=_a.merch_year_wk.md) |  |
| AND | [b.location_id = a.location_id](AND_b_location_id_=_a.location_id.md) |  |
| AND | [b.component_type_code = a.component_type_code](AND_b_component_type_code_=_a.component_type_code.md) |  |
| AND | [b.history_component_id = a.history_component_id](AND_b_history_component_id_=_a.history_component_id.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [#styleclr_loc_wk a](FROM.#styleclr_loc_wk_a.md) |  |
| WHERE | [NOT EXISTS (SELECT](WHERE.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.component_units = a.component_units + b.component_units,](SET_a_component_units_=_a_component_units_+_b.component_units,.md) |  |
| FROM | [hist_cmp_styleclr_chn_wk a,](FROM.hist_cmp_styleclr_chn_wk_a,.md) |  |
| WHERE | [b.style_id = a.style_id](WHERE_b_style_id_=_a.style_id.md) |  |
| AND | [b.color_id = a.color_id](AND_b_color_id_=_a.color_id.md) |  |
| AND | [b.merch_year_wk = a.merch_year_wk](AND_b_merch_year_wk_=_a.merch_year_wk.md) |  |
| AND | [b.component_type_code = a.component_type_code](AND_b_component_type_code_=_a.component_type_code.md) |  |
| AND | [b.history_component_id = a.history_component_id](AND_b_history_component_id_=_a.history_component_id.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [#styleclr_chn_wk a](FROM.#styleclr_chn_wk_a.md) |  |
| WHERE | [NOT EXISTS (SELECT](WHERE.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.component_units = a.component_units + b.component_units,](SET_a_component_units_=_a_component_units_+_b.component_units,.md) |  |
| FROM | [hist_cmp_styleclr_loc_pd a,](FROM.hist_cmp_styleclr_loc_pd_a,.md) |  |
| WHERE | [b.style_id = a.style_id](WHERE_b_style_id_=_a.style_id.md) |  |
| AND | [b.color_id = a.color_id](AND_b_color_id_=_a.color_id.md) |  |
| AND | [b.merch_year_pd = a.merch_year_pd](AND_b_merch_year_pd_=_a.merch_year_pd.md) |  |
| AND | [b.location_id = a.location_id](AND_b_location_id_=_a.location_id.md) |  |
| AND | [b.component_type_code = a.component_type_code](AND_b_component_type_code_=_a.component_type_code.md) |  |
| AND | [b.history_component_id = a.history_component_id](AND_b_history_component_id_=_a.history_component_id.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [#styleclr_loc_pd a](FROM.#styleclr_loc_pd_a.md) |  |
| WHERE | [NOT EXISTS (SELECT](WHERE.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.component_units = a.component_units + b.component_units,](SET_a_component_units_=_a_component_units_+_b.component_units,.md) |  |
| FROM | [hist_cmp_styleclr_chn_pd a,](FROM.hist_cmp_styleclr_chn_pd_a,.md) |  |
| WHERE | [b.style_id = a.style_id](WHERE_b_style_id_=_a.style_id.md) |  |
| AND | [b.color_id = a.color_id](AND_b_color_id_=_a.color_id.md) |  |
| AND | [b.merch_year_pd = a.merch_year_pd](AND_b_merch_year_pd_=_a.merch_year_pd.md) |  |
| AND | [b.component_type_code = a.component_type_code](AND_b_component_type_code_=_a.component_type_code.md) |  |
| AND | [b.history_component_id = a.history_component_id](AND_b_history_component_id_=_a.history_component_id.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [#styleclr_chn_pd a](FROM.#styleclr_chn_pd_a.md) |  |
| WHERE | [NOT EXISTS (SELECT](WHERE.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.component_units = a.component_units + b.component_units,](SET_a_component_units_=_a_component_units_+_b.component_units,.md) |  |
| FROM | [hist_cmp_styleclr_loc_yr a,](FROM.hist_cmp_styleclr_loc_yr_a,.md) |  |
| WHERE | [b.style_id = a.style_id](WHERE_b_style_id_=_a.style_id.md) |  |
| AND | [b.color_id = a.color_id](AND_b_color_id_=_a.color_id.md) |  |
| AND | [b.merch_year = a.merch_year](AND_b_merch_year_=_a.merch_year.md) |  |
| AND | [b.location_id = a.location_id](AND_b_location_id_=_a.location_id.md) |  |
| AND | [b.component_type_code = a.component_type_code](AND_b_component_type_code_=_a.component_type_code.md) |  |
| AND | [b.history_component_id = a.history_component_id](AND_b_history_component_id_=_a.history_component_id.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [#styleclr_loc_yr a](FROM.#styleclr_loc_yr_a.md) |  |
| WHERE | [NOT EXISTS (SELECT](WHERE.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.component_units = a.component_units + b.component_units,](SET_a_component_units_=_a_component_units_+_b.component_units,.md) |  |
| FROM | [hist_cmp_styleclr_chn_yr a,](FROM.hist_cmp_styleclr_chn_yr_a,.md) |  |
| WHERE | [b.style_id = a.style_id](WHERE_b_style_id_=_a.style_id.md) |  |
| AND | [b.color_id = a.color_id](AND_b_color_id_=_a.color_id.md) |  |
| AND | [b.merch_year = a.merch_year](AND_b_merch_year_=_a.merch_year.md) |  |
| AND | [b.component_type_code = a.component_type_code](AND_b_component_type_code_=_a.component_type_code.md) |  |
| AND | [b.history_component_id = a.history_component_id](AND_b_history_component_id_=_a.history_component_id.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [#styleclr_chn_yr a](FROM.#styleclr_chn_yr_a.md) |  |
| WHERE | [NOT EXISTS (SELECT](WHERE.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.component_units = a.component_units + b.component_units,](SET_a_component_units_=_a_component_units_+_b.component_units,.md) |  |
| FROM | [hist_cmp_styleclr_loc_li a,](FROM.hist_cmp_styleclr_loc_li_a,.md) |  |
| WHERE | [b.style_id = a.style_id](WHERE_b_style_id_=_a.style_id.md) |  |
| AND | [b.color_id = a.color_id](AND_b_color_id_=_a.color_id.md) |  |
| AND | [b.location_id = a.location_id](AND_b_location_id_=_a.location_id.md) |  |
| AND | [b.component_type_code = a.component_type_code](AND_b_component_type_code_=_a.component_type_code.md) |  |
| AND | [b.history_component_id = a.history_component_id](AND_b_history_component_id_=_a.history_component_id.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [#styleclr_loc_li a](FROM.#styleclr_loc_li_a.md) |  |
| WHERE | [NOT EXISTS (SELECT](WHERE.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.component_units = a.component_units + b.component_units,](SET_a_component_units_=_a_component_units_+_b.component_units,.md) |  |
| FROM | [hist_cmp_styleclr_chn_li a,](FROM.hist_cmp_styleclr_chn_li_a,.md) |  |
| WHERE | [b.style_id = a.style_id](WHERE_b_style_id_=_a.style_id.md) |  |
| AND | [b.color_id = a.color_id](AND_b_color_id_=_a.color_id.md) |  |
| AND | [b.component_type_code = a.component_type_code](AND_b_component_type_code_=_a.component_type_code.md) |  |
| AND | [b.history_component_id = a.history_component_id](AND_b_history_component_id_=_a.history_component_id.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [#styleclr_chn_li a](FROM.#styleclr_chn_li_a.md) |  |
| WHERE | [NOT EXISTS (SELECT](WHERE.NOT_EXISTS_SELECT.md) |  |
| dbo | [post_hist_group_$sp](dbo.post_hist_group_$sp.md) | dbo.calendar_merch_week, dbo.hist_group_chn_li, dbo.hist_group_chn_pd, dbo.hist_group_chn_wk, dbo.hist_group_chn_yr, dbo.hist_group_loc_li, dbo.hist_group_loc_pd, dbo.hist_group_loc_wk, dbo.hist_group_loc_yr, dbo.job_detail, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.return_step_exists_$sp, dbo.wrk_group_loc_wk |
| dbo | [post_hist_group_rim_$sp](dbo.post_hist_group_rim_$sp.md) | dbo.calendar_merch_period, dbo.calendar_merch_week, dbo.h, dbo.hist_group_chn_li, dbo.hist_group_chn_pd, dbo.hist_group_chn_wk, dbo.hist_group_chn_yr, dbo.hist_group_loc_li, dbo.hist_group_loc_pd, dbo.hist_group_loc_wk, dbo.hist_group_loc_yr, dbo.hist_rim_oh_group_chn_li, dbo.hist_rim_oh_group_chn_pd, dbo.hist_rim_oh_group_chn_yr, dbo.hist_rim_oh_group_loc_li, dbo.hist_rim_oh_group_loc_pd, dbo.hist_rim_oh_group_loc_yr, dbo.mv_fact_queue, dbo.plan_exp_table_group, dbo.post_hist_group_rim, dbo.post_parameter |
| dbo | [post_hist_le_$sp](dbo.post_hist_le_$sp.md) | dbo.calendar_merch_week, dbo.h, dbo.hist_le_group_chn_li, dbo.hist_le_group_chn_pd, dbo.hist_le_group_chn_wk, dbo.hist_le_group_chn_yr, dbo.hist_le_group_loc_li, dbo.hist_le_group_loc_pd, dbo.hist_le_group_loc_wk, dbo.hist_le_group_loc_yr, dbo.hist_le_sku_chn_li, dbo.hist_le_sku_chn_pd, dbo.hist_le_sku_chn_wk, dbo.hist_le_sku_chn_yr, dbo.hist_le_sku_loc_li, dbo.hist_le_sku_loc_pd, dbo.hist_le_sku_loc_wk, dbo.hist_le_sku_loc_yr, dbo.hist_le_style_chn_li, dbo.hist_le_style_chn_pd, dbo.hist_le_style_chn_wk, dbo.hist_le_style_chn_yr, dbo.hist_le_style_loc_li, dbo.hist_le_style_loc_pd, dbo.hist_le_style_loc_wk, dbo.hist_le_style_loc_yr, dbo.hist_le_styleclr_chn_li, dbo.hist_le_styleclr_chn_pd, dbo.hist_le_styleclr_chn_wk, dbo.hist_le_styleclr_chn_yr, dbo.hist_le_styleclr_loc_li, dbo.hist_le_styleclr_loc_pd, dbo.hist_le_styleclr_loc_wk, dbo.hist_le_styleclr_loc_yr, dbo.style_group |
| dbo | [post_hist_le_group_$sp](dbo.post_hist_le_group_$sp.md) | dbo.calendar_merch_week, dbo.h, dbo.hist_le_group_chn_li, dbo.hist_le_group_chn_pd, dbo.hist_le_group_chn_wk, dbo.hist_le_group_chn_yr, dbo.hist_le_group_loc_li, dbo.hist_le_group_loc_pd, dbo.hist_le_group_loc_wk, dbo.hist_le_group_loc_yr, dbo.post_hist_le_group |
| dbo | [post_hist_oh_cmp_group_$sp](dbo.post_hist_oh_cmp_group_$sp.md) | dbo.post_hist_cmp_group, dbo.post_hist_group, dbo.post_hist_group_sum, dbo.post_hist_oh_group |
| Date: | [April 04, 2001](Date_.April_04,_2001.md) |  |
| Date: | [December 27, 2001](Date_.December_27,_2001.md) |  |
| Description: | [Added 603, 703, 605, 615, 510](Description_.Added_603,_703,_605,_615,_510.md) |  |
| Desc: | [This procedure posts transactions from post_hist_group_sum to post_hist_group, post_hist_oh_group](Desc_.This_procedure_posts_transactions_from_post_hist_group_sum_to_post_hist_group,_post_hist_oh_group.md) |  |
| Sept20,05 Michel Benoit | [60672](Sept20,05_Michel_Benoit.60672.md) |  |
| FROM | [post_hist_group_sum a](FROM.post_hist_group_sum_a.md) |  |
| SELECT | [a.hierarchy_group_id,](SELECT_a.hierarchy_group_id,.md) |  |
| FROM | [post_hist_group_sum a](FROM.post_hist_group_sum_a.md) |  |
| WHERE | [a.hierarchy_group_id = @curr_hierarchy_group_id](WHERE_a.hierarchy_group_id_=_@curr_hierarchy_group_id.md) |  |
| AND | [a.transaction_type_code NOT IN (290,292,590)](AND_a.transaction_type_code_NOT_IN_290,292,590.md) |  |
| SELECT | [a.hierarchy_group_id,](SELECT_a.hierarchy_group_id,.md) |  |
| FROM | [post_hist_group_sum a](FROM.post_hist_group_sum_a.md) |  |
| WHERE | [a.hierarchy_group_id = @curr_hierarchy_group_id](WHERE_a.hierarchy_group_id_=_@curr_hierarchy_group_id.md) |  |
| AND | [(a.transaction_type_code IN (600, 605, 610, 615, 630)](AND_a.transaction_type_code_IN_600,_605,_610,_615,_630.md) |  |
| dbo | [post_hist_oh_cmp_sku_$sp](dbo.post_hist_oh_cmp_sku_$sp.md) | dbo.post_hist_cmp_sku, dbo.post_hist_oh_sku, dbo.post_hist_sku, dbo.post_hist_sku_sum, dbo.sku |
| Date: | [January 3rd, 2002](Date_.January_3rd,_2002.md) |  |
| Description: | [Added 603, 703, 605, 615, 510](Description_.Added_603,_703,_605,_615,_510.md) |  |
| Date: | [July 30, 2002](Date_.July_30,_2002.md) |  |
| Description: | [Removed the reference to component_xRef table when](Description_.Removed_the_reference_to_component_xRef_table_when.md) |  |
| Sept20,05 Michel Benoit | [60672](Sept20,05_Michel_Benoit.60672.md) |  |
| dbo | [post_hist_oh_cmp_style_$sp](dbo.post_hist_oh_cmp_style_$sp.md) | dbo.post_hist_cmp_style, dbo.post_hist_oh_style, dbo.post_hist_style, dbo.post_hist_style_sum |
| Date: | [December 27, 2001](Date_.December_27,_2001.md) |  |
| Description: | [Added 603, 703, 605, 615, 510](Description_.Added_603,_703,_605,_615,_510.md) |  |
| Desc: | [This procedure posts transactions from post_hist_style_sum to post_hist_style, post_hist_oh_style](Desc_.This_procedure_posts_transactions_from_post_hist_style_sum_to_post_hist_style,_post_hist_oh_style.md) |  |
| Sept20,05 Michel Benoit | [60672](Sept20,05_Michel_Benoit.60672.md) |  |
| Jul21,07 Yan Ding | [87495](Jul21,07_Yan_Ding.87495.md) |  |
| FROM | [post_hist_style_sum a](FROM.post_hist_style_sum_a.md) |  |
| WHERE | [a.style_id = @curr_style_id](WHERE_a.style_id_=_@curr_style_id.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [post_hist_style_sum a](FROM.post_hist_style_sum_a.md) |  |
| WHERE | [a.style_id = @curr_style_id](WHERE_a.style_id_=_@curr_style_id.md) |  |
| AND | [a.transaction_type_code NOT IN (290,292,590)](AND_a.transaction_type_code_NOT_IN_290,292,590.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [post_hist_style_sum a](FROM.post_hist_style_sum_a.md) |  |
| WHERE | [a.style_id = @curr_style_id](WHERE_a.style_id_=_@curr_style_id.md) |  |
| AND | [(a.transaction_type_code IN (600, 605, 610, 615, 630)](AND_a.transaction_type_code_IN_600,_605,_610,_615,_630.md) |  |
| dbo | [post_hist_oh_cmp_styleclr_$sp](dbo.post_hist_oh_cmp_styleclr_$sp.md) | dbo.post_hist_cmp_styleclr, dbo.post_hist_oh_styleclr, dbo.post_hist_styleclr, dbo.post_hist_styleclr_sum |
| Date: | [January 3rd, 2002](Date_.January_3rd,_2002.md) |  |
| Description: | [Added 603, 703, 605, 615, 510](Description_.Added_603,_703,_605,_615,_510.md) |  |
| Jan15,03   Udani | [1-ITI7B    Added following fields:](Jan15,03_Udani.1-ITI7B_Added_following_fields.md) |  |
| Sept20,05 Michel Benoit 60672 | [trans type 930 not mapped into ma](Sept20,05_Michel_Benoit_60672.trans_type_930_not_mapped_into_ma.md) |  |
| Jul21,07 Yan Ding | [87495](Jul21,07_Yan_Ding.87495.md) |  |
| FROM | [post_hist_styleclr_sum a](FROM.post_hist_styleclr_sum_a.md) |  |
| WHERE | [a.style_id = @curr_style_id](WHERE_a.style_id_=_@curr_style_id.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [post_hist_styleclr_sum a](FROM.post_hist_styleclr_sum_a.md) |  |
| WHERE | [a.style_id = @curr_style_id](WHERE_a.style_id_=_@curr_style_id.md) |  |
| AND | [a.transaction_type_code NOT IN (290,292,590)](AND_a.transaction_type_code_NOT_IN_290,292,590.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [post_hist_styleclr_sum a](FROM.post_hist_styleclr_sum_a.md) |  |
| WHERE | [a.style_id = @curr_style_id](WHERE_a.style_id_=_@curr_style_id.md) |  |
| AND | [(a.transaction_type_code IN (600, 605, 610, 615, 630)](AND_a.transaction_type_code_IN_600,_605,_610,_615,_630.md) |  |
| dbo | [post_hist_oh_group_$sp](dbo.post_hist_oh_group_$sp.md) | dbo.a, dbo.hist_oh_group_chn_li, dbo.hist_oh_group_chn_pd, dbo.hist_oh_group_chn_wk, dbo.hist_oh_group_chn_yr, dbo.hist_oh_group_loc_li, dbo.hist_oh_group_loc_pd, dbo.hist_oh_group_loc_wk, dbo.hist_oh_group_loc_yr, dbo.mv_fact_queue, dbo.plan_exp_table_group, dbo.post_oh_work_group_li, dbo.post_oh_work_group_pd, dbo.post_oh_work_group_wk, dbo.post_oh_work_group_yr |
| inventory_status_id | [smallint  NOT NULL,](inventory_status_id.smallint_NOT_NULL,.md) |  |
| price_status_id | [smallint  NOT NULL,](price_status_id.smallint_NOT_NULL,.md) |  |
| inventory_status_id | [smallint NOT NULL,](inventory_status_id.smallint_NOT_NULL,.md) |  |
| price_status_id | [smallint  NOT NULL,](price_status_id.smallint_NOT_NULL,.md) |  |
| inventory_status_id | [smallint  NOT NULL,](inventory_status_id.smallint_NOT_NULL,.md) |  |
| price_status_id | [smallint  NOT NULL,](price_status_id.smallint_NOT_NULL,.md) |  |
| inventory_status_id | [smallint  NOT NULL,](inventory_status_id.smallint_NOT_NULL,.md) |  |
| price_status_id | [smallint  NOT NULL,](price_status_id.smallint_NOT_NULL,.md) |  |
| INSERT | [#group_loc_wk](INSERT.#group_loc_wk.md) |  |
| SELECT | [hierarchy_group_id,](SELECT.hierarchy_group_id,.md) |  |
| FROM | [post_oh_work_group_wk WITH (NOLOCK)](FROM.post_oh_work_group_wk_WITH_NOLOCK.md) |  |
| WHERE | [hierarchy_group_id BETWEEN @from_group_id AND @to_group_id](WHERE.hierarchy_group_id_BETWEEN_@from_group_id_AND_@to_group_id.md) |  |
| SELECT | [hierarchy_group_id,](SELECT.hierarchy_group_id,.md) |  |
| FROM | [post_oh_work_group_wk WITH (NOLOCK)](FROM.post_oh_work_group_wk_WITH_NOLOCK.md) |  |
| WHERE | [hierarchy_group_id BETWEEN @from_group_id AND @to_group_id](WHERE.hierarchy_group_id_BETWEEN_@from_group_id_AND_@to_group_id.md) |  |
| SELECT | [b.hierarchy_group_id,](SELECT_b.hierarchy_group_id,.md) |  |
| FROM | [post_oh_work_group_pd b WITH (NOLOCK)](FROM.post_oh_work_group_pd_b_WITH_NOLOCK.md) |  |
| WHERE | [b.hierarchy_group_id BETWEEN @from_group_id AND @to_group_id](WHERE_b.hierarchy_group_id_BETWEEN_@from_group_id_AND_@to_group_id.md) |  |
| SELECT | [hierarchy_group_id,](SELECT.hierarchy_group_id,.md) |  |
| FROM | [post_oh_work_group_pd WITH (NOLOCK)](FROM.post_oh_work_group_pd_WITH_NOLOCK.md) |  |
| WHERE | [hierarchy_group_id BETWEEN @from_group_id AND @to_group_id](WHERE.hierarchy_group_id_BETWEEN_@from_group_id_AND_@to_group_id.md) |  |
| SELECT | [hierarchy_group_id,](SELECT.hierarchy_group_id,.md) |  |
| FROM | [post_oh_work_group_yr WITH (NOLOCK)](FROM.post_oh_work_group_yr_WITH_NOLOCK.md) |  |
| WHERE | [hierarchy_group_id BETWEEN @from_group_id AND @to_group_id](WHERE.hierarchy_group_id_BETWEEN_@from_group_id_AND_@to_group_id.md) |  |
| SELECT | [hierarchy_group_id,](SELECT.hierarchy_group_id,.md) |  |
| FROM | [post_oh_work_group_yr WITH (NOLOCK)](FROM.post_oh_work_group_yr_WITH_NOLOCK.md) |  |
| WHERE | [hierarchy_group_id BETWEEN @from_group_id AND @to_group_id](WHERE.hierarchy_group_id_BETWEEN_@from_group_id_AND_@to_group_id.md) |  |
| SELECT | [hierarchy_group_id,](SELECT.hierarchy_group_id,.md) |  |
| FROM | [post_oh_work_group_li WITH (NOLOCK)](FROM.post_oh_work_group_li_WITH_NOLOCK.md) |  |
| WHERE | [hierarchy_group_id BETWEEN @from_group_id AND @to_group_id](WHERE.hierarchy_group_id_BETWEEN_@from_group_id_AND_@to_group_id.md) |  |
| SELECT | [hierarchy_group_id,](SELECT.hierarchy_group_id,.md) |  |
| FROM | [post_oh_work_group_li WITH (NOLOCK)](FROM.post_oh_work_group_li_WITH_NOLOCK.md) |  |
| WHERE | [hierarchy_group_id BETWEEN @from_group_id AND @to_group_id](WHERE.hierarchy_group_id_BETWEEN_@from_group_id_AND_@to_group_id.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.on_hand_units = a.on_hand_units + b.on_hand_units,](SET_a_on_hand_units_=_a_on_hand_units_+_b.on_hand_units,.md) |  |
| WHERE | [b.hierarchy_group_id = a.hierarchy_group_id](WHERE_b_hierarchy_group_id_=_a.hierarchy_group_id.md) |  |
| AND | [b.merch_year_wk = a.merch_year_wk](AND_b_merch_year_wk_=_a.merch_year_wk.md) |  |
| AND | [b.location_id = a.location_id](AND_b_location_id_=_a.location_id.md) |  |
| AND | [b.inventory_status_id = a.inventory_status_id](AND_b_inventory_status_id_=_a.inventory_status_id.md) |  |
| AND | [b.price_status_id = a.price_status_id](AND_b_price_status_id_=_a.price_status_id.md) |  |
| SELECT | [a.hierarchy_group_id,](SELECT_a.hierarchy_group_id,.md) |  |
| FROM | [#group_loc_wk a](FROM.#group_loc_wk_a.md) |  |
| WHERE | [NOT EXISTS (SELECT *](WHERE.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.on_hand_units = a.on_hand_units + b.on_hand_units,](SET_a_on_hand_units_=_a_on_hand_units_+_b.on_hand_units,.md) |  |
| FROM | [hist_oh_group_chn_wk a,](FROM.hist_oh_group_chn_wk_a,.md) |  |
| WHERE | [b.hierarchy_group_id = a.hierarchy_group_id](WHERE_b_hierarchy_group_id_=_a.hierarchy_group_id.md) |  |
| AND | [b.merch_year_wk = a.merch_year_wk](AND_b_merch_year_wk_=_a.merch_year_wk.md) |  |
| AND | [b.inventory_status_id = a.inventory_status_id](AND_b_inventory_status_id_=_a.inventory_status_id.md) |  |
| AND | [b.price_status_id = a.price_status_id](AND_b_price_status_id_=_a.price_status_id.md) |  |
| SELECT | [a.hierarchy_group_id,](SELECT_a.hierarchy_group_id,.md) |  |
| FROM | [#group_chn_wk a](FROM.#group_chn_wk_a.md) |  |
| WHERE | [NOT EXISTS (SELECT *](WHERE.NOT_EXISTS_SELECT.md) |  |
| FROM | [post_oh_work_group_wk a, plan_exp_table_group](FROM.post_oh_work_group_wk_a,_plan_exp_table_group.md) |  |
| WHERE | [a.hierarchy_group_id BETWEEN @from_group_id AND @to_group_id](WHERE_a.hierarchy_group_id_BETWEEN_@from_group_id_AND_@to_group_id.md) |  |
| AND | [plan_exp_table_group_id = 2;](AND.plan_exp_table_group_id_=_2;.md) |  |
| DELETE | [post_oh_work_group_wk](DELETE.post_oh_work_group_wk.md) |  |
| WHERE | [hierarchy_group_id BETWEEN @from_group_id AND @to_group_id](WHERE.hierarchy_group_id_BETWEEN_@from_group_id_AND_@to_group_id.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.on_hand_units = a.on_hand_units + b.on_hand_units,](SET_a_on_hand_units_=_a_on_hand_units_+_b.on_hand_units,.md) |  |
| WHERE | [b.hierarchy_group_id = a.hierarchy_group_id](WHERE_b_hierarchy_group_id_=_a.hierarchy_group_id.md) |  |
| AND | [b.merch_year_pd = a.merch_year_pd](AND_b_merch_year_pd_=_a.merch_year_pd.md) |  |
| AND | [b.location_id = a.location_id](AND_b_location_id_=_a.location_id.md) |  |
| AND | [b.inventory_status_id = a.inventory_status_id](AND_b_inventory_status_id_=_a.inventory_status_id.md) |  |
| AND | [b.price_status_id = a.price_status_id](AND_b_price_status_id_=_a.price_status_id.md) |  |
| SELECT | [a.hierarchy_group_id,](SELECT_a.hierarchy_group_id,.md) |  |
| FROM | [#group_loc_pd a](FROM.#group_loc_pd_a.md) |  |
| WHERE | [NOT EXISTS (SELECT *](WHERE.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.on_hand_units = a.on_hand_units + b.on_hand_units,](SET_a_on_hand_units_=_a_on_hand_units_+_b.on_hand_units,.md) |  |
| WHERE | [b.hierarchy_group_id = a.hierarchy_group_id](WHERE_b_hierarchy_group_id_=_a.hierarchy_group_id.md) |  |
| AND | [b.merch_year_pd = a.merch_year_pd](AND_b_merch_year_pd_=_a.merch_year_pd.md) |  |
| AND | [b.inventory_status_id = a.inventory_status_id](AND_b_inventory_status_id_=_a.inventory_status_id.md) |  |
| AND | [b.price_status_id = a.price_status_id](AND_b_price_status_id_=_a.price_status_id.md) |  |
| SELECT | [a.hierarchy_group_id,](SELECT_a.hierarchy_group_id,.md) |  |
| FROM | [#group_chn_pd a](FROM.#group_chn_pd_a.md) |  |
| WHERE | [NOT EXISTS (SELECT *](WHERE.NOT_EXISTS_SELECT.md) |  |
| DELETE | [post_oh_work_group_pd](DELETE.post_oh_work_group_pd.md) |  |
| WHERE | [hierarchy_group_id BETWEEN @from_group_id AND @to_group_id](WHERE.hierarchy_group_id_BETWEEN_@from_group_id_AND_@to_group_id.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.on_hand_units = a.on_hand_units + b.on_hand_units,](SET_a_on_hand_units_=_a_on_hand_units_+_b.on_hand_units,.md) |  |
| FROM | [hist_oh_group_loc_yr a,](FROM.hist_oh_group_loc_yr_a,.md) |  |
| WHERE | [b.hierarchy_group_id = a.hierarchy_group_id](WHERE_b_hierarchy_group_id_=_a.hierarchy_group_id.md) |  |
| AND | [b.merch_year = a.merch_year](AND_b_merch_year_=_a.merch_year.md) |  |
| AND | [b.location_id = a.location_id](AND_b_location_id_=_a.location_id.md) |  |
| AND | [b.inventory_status_id = a.inventory_status_id](AND_b_inventory_status_id_=_a.inventory_status_id.md) |  |
| AND | [b.price_status_id = a.price_status_id](AND_b_price_status_id_=_a.price_status_id.md) |  |
| SELECT | [a.hierarchy_group_id,](SELECT_a.hierarchy_group_id,.md) |  |
| FROM | [#group_loc_yr a](FROM.#group_loc_yr_a.md) |  |
| WHERE | [NOT EXISTS (SELECT *](WHERE.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.on_hand_units = a.on_hand_units + b.on_hand_units,](SET_a_on_hand_units_=_a_on_hand_units_+_b.on_hand_units,.md) |  |
| FROM | [hist_oh_group_chn_yr a,](FROM.hist_oh_group_chn_yr_a,.md) |  |
| WHERE | [b.hierarchy_group_id = a.hierarchy_group_id](WHERE_b_hierarchy_group_id_=_a.hierarchy_group_id.md) |  |
| AND | [b.merch_year = a.merch_year](AND_b_merch_year_=_a.merch_year.md) |  |
| AND | [b.inventory_status_id = a.inventory_status_id](AND_b_inventory_status_id_=_a.inventory_status_id.md) |  |
| AND | [b.price_status_id = a.price_status_id](AND_b_price_status_id_=_a.price_status_id.md) |  |
| SELECT | [a.hierarchy_group_id,](SELECT_a.hierarchy_group_id,.md) |  |
| FROM | [#group_chn_yr a](FROM.#group_chn_yr_a.md) |  |
| WHERE | [NOT EXISTS (SELECT *](WHERE.NOT_EXISTS_SELECT.md) |  |
| DELETE | [post_oh_work_group_yr](DELETE.post_oh_work_group_yr.md) |  |
| WHERE | [hierarchy_group_id BETWEEN @from_group_id AND @to_group_id](WHERE.hierarchy_group_id_BETWEEN_@from_group_id_AND_@to_group_id.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.on_hand_units = a.on_hand_units + b.on_hand_units,](SET_a_on_hand_units_=_a_on_hand_units_+_b.on_hand_units,.md) |  |
| WHERE | [b.hierarchy_group_id = a.hierarchy_group_id](WHERE_b_hierarchy_group_id_=_a.hierarchy_group_id.md) |  |
| AND | [b.location_id = a.location_id](AND_b_location_id_=_a.location_id.md) |  |
| AND | [b.inventory_status_id = a.inventory_status_id](AND_b_inventory_status_id_=_a.inventory_status_id.md) |  |
| AND | [b.price_status_id = a.price_status_id](AND_b_price_status_id_=_a.price_status_id.md) |  |
| SELECT | [a.hierarchy_group_id,](SELECT_a.hierarchy_group_id,.md) |  |
| FROM | [#group_loc_li a](FROM.#group_loc_li_a.md) |  |
| WHERE | [NOT EXISTS (SELECT *](WHERE.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.on_hand_units = a.on_hand_units + b.on_hand_units,](SET_a_on_hand_units_=_a_on_hand_units_+_b.on_hand_units,.md) |  |
| FROM | [hist_oh_group_chn_li a,](FROM.hist_oh_group_chn_li_a,.md) |  |
| WHERE | [b.hierarchy_group_id = a.hierarchy_group_id](WHERE_b_hierarchy_group_id_=_a.hierarchy_group_id.md) |  |
| AND | [b.inventory_status_id = a.inventory_status_id](AND_b_inventory_status_id_=_a.inventory_status_id.md) |  |
| AND | [b.price_status_id = a.price_status_id](AND_b_price_status_id_=_a.price_status_id.md) |  |
| SELECT | [a.hierarchy_group_id,](SELECT_a.hierarchy_group_id,.md) |  |
| FROM | [#group_chn_li a](FROM.#group_chn_li_a.md) |  |
| WHERE | [NOT EXISTS (SELECT *](WHERE.NOT_EXISTS_SELECT.md) |  |
| DELETE | [post_oh_work_group_li](DELETE.post_oh_work_group_li.md) |  |
| WHERE | [hierarchy_group_id BETWEEN @from_group_id AND @to_group_id](WHERE.hierarchy_group_id_BETWEEN_@from_group_id_AND_@to_group_id.md) |  |
| dbo | [post_hist_oh_sku_$sp](dbo.post_hist_oh_sku_$sp.md) | dbo.a, dbo.hist_oh_sku_chn_li, dbo.hist_oh_sku_chn_pd, dbo.hist_oh_sku_chn_wk, dbo.hist_oh_sku_chn_yr, dbo.hist_oh_sku_loc_li, dbo.hist_oh_sku_loc_pd, dbo.hist_oh_sku_loc_wk, dbo.hist_oh_sku_loc_yr, dbo.post_oh_work_sku_li, dbo.post_oh_work_sku_pd, dbo.post_oh_work_sku_wk, dbo.post_oh_work_sku_yr |
| create proc dbo.post_hist_oh_sku_$sp | [@curr_style_id decimal(12,0),](create_proc_dbo_post_hist_oh_sku_$sp.@curr_style_id_decimal_12,0_,.md) |  |
| inventory_status_id | [smallint  NOT NULL,](inventory_status_id.smallint_NOT_NULL,.md) |  |
| price_status_id | [smallint  NOT NULL,](price_status_id.smallint_NOT_NULL,.md) |  |
| inventory_status_id | [smallint NOT NULL,](inventory_status_id.smallint_NOT_NULL,.md) |  |
| price_status_id | [smallint  NOT NULL,](price_status_id.smallint_NOT_NULL,.md) |  |
| inventory_status_id | [smallint  NOT NULL,](inventory_status_id.smallint_NOT_NULL,.md) |  |
| price_status_id | [smallint  NOT NULL,](price_status_id.smallint_NOT_NULL,.md) |  |
| inventory_status_id | [smallint  NOT NULL,](inventory_status_id.smallint_NOT_NULL,.md) |  |
| price_status_id | [smallint  NOT NULL,](price_status_id.smallint_NOT_NULL,.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| dbo | [post_hist_oh_style_$sp](dbo.post_hist_oh_style_$sp.md) | dbo.a, dbo.hist_oh_style_chn_li, dbo.hist_oh_style_chn_pd, dbo.hist_oh_style_chn_wk, dbo.hist_oh_style_chn_yr, dbo.hist_oh_style_loc_li, dbo.hist_oh_style_loc_pd, dbo.hist_oh_style_loc_wk, dbo.hist_oh_style_loc_yr, dbo.post_oh_work_style_li, dbo.post_oh_work_style_pd, dbo.post_oh_work_style_wk, dbo.post_oh_work_style_yr |
| inventory_status_id | [smallint  NOT NULL,](inventory_status_id.smallint_NOT_NULL,.md) |  |
| price_status_id | [smallint  NOT NULL,](price_status_id.smallint_NOT_NULL,.md) |  |
| inventory_status_id | [smallint NOT NULL,](inventory_status_id.smallint_NOT_NULL,.md) |  |
| price_status_id | [smallint  NOT NULL,](price_status_id.smallint_NOT_NULL,.md) |  |
| inventory_status_id | [smallint  NOT NULL,](inventory_status_id.smallint_NOT_NULL,.md) |  |
| price_status_id | [smallint  NOT NULL,](price_status_id.smallint_NOT_NULL,.md) |  |
| inventory_status_id | [smallint  NOT NULL,](inventory_status_id.smallint_NOT_NULL,.md) |  |
| price_status_id | [smallint  NOT NULL,](price_status_id.smallint_NOT_NULL,.md) |  |
| INSERT | [#style_loc_wk](INSERT.#style_loc_wk.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [post_oh_work_style_wk](FROM.post_oh_work_style_wk.md) |  |
| WHERE | [style_id BETWEEN @from_style_id and @to_style_id](WHERE.style_id_BETWEEN_@from_style_id_and_@to_style_id.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [post_oh_work_style_wk](FROM.post_oh_work_style_wk.md) |  |
| WHERE | [style_id BETWEEN @from_style_id and @to_style_id](WHERE.style_id_BETWEEN_@from_style_id_and_@to_style_id.md) |  |
| SELECT | [b.style_id,](SELECT_b.style_id,.md) |  |
| FROM | [post_oh_work_style_pd b](FROM.post_oh_work_style_pd_b.md) |  |
| WHERE | [b.style_id BETWEEN @from_style_id and @to_style_id](WHERE_b.style_id_BETWEEN_@from_style_id_and_@to_style_id.md) |  |
| SELECT | [b.style_id,](SELECT_b.style_id,.md) |  |
| FROM | [post_oh_work_style_pd b](FROM.post_oh_work_style_pd_b.md) |  |
| WHERE | [b.style_id BETWEEN @from_style_id and @to_style_id](WHERE_b.style_id_BETWEEN_@from_style_id_and_@to_style_id.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [post_oh_work_style_yr](FROM.post_oh_work_style_yr.md) |  |
| WHERE | [style_id BETWEEN @from_style_id and @to_style_id](WHERE.style_id_BETWEEN_@from_style_id_and_@to_style_id.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [post_oh_work_style_yr](FROM.post_oh_work_style_yr.md) |  |
| WHERE | [style_id BETWEEN @from_style_id and @to_style_id](WHERE.style_id_BETWEEN_@from_style_id_and_@to_style_id.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [post_oh_work_style_li](FROM.post_oh_work_style_li.md) |  |
| WHERE | [style_id BETWEEN @from_style_id and @to_style_id](WHERE.style_id_BETWEEN_@from_style_id_and_@to_style_id.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [post_oh_work_style_li](FROM.post_oh_work_style_li.md) |  |
| WHERE | [style_id BETWEEN @from_style_id AND @to_style_id](WHERE.style_id_BETWEEN_@from_style_id_AND_@to_style_id.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.on_hand_units](SET_a.on_hand_units.md) |  |
| FROM | [hist_oh_style_loc_wk a,](FROM.hist_oh_style_loc_wk_a,.md) |  |
| WHERE | [b.style_id = a.style_id](WHERE_b_style_id_=_a.style_id.md) |  |
| AND | [b.merch_year_wk = a.merch_year_wk](AND_b_merch_year_wk_=_a.merch_year_wk.md) |  |
| AND | [b.location_id = a.location_id](AND_b_location_id_=_a.location_id.md) |  |
| AND | [b.inventory_status_id = a.inventory_status_id](AND_b_inventory_status_id_=_a.inventory_status_id.md) |  |
| AND | [b.price_status_id = a.price_status_id](AND_b_price_status_id_=_a.price_status_id.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [#style_loc_wk a](FROM.#style_loc_wk_a.md) |  |
| WHERE | [NOT EXISTS (SELECT *](WHERE.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.on_hand_units](SET_a.on_hand_units.md) |  |
| FROM | [hist_oh_style_chn_wk a,](FROM.hist_oh_style_chn_wk_a,.md) |  |
| WHERE | [b.style_id = a.style_id](WHERE_b_style_id_=_a.style_id.md) |  |
| AND | [b.merch_year_wk = a.merch_year_wk](AND_b_merch_year_wk_=_a.merch_year_wk.md) |  |
| AND | [b.inventory_status_id = a.inventory_status_id](AND_b_inventory_status_id_=_a.inventory_status_id.md) |  |
| AND | [b.price_status_id = a.price_status_id](AND_b_price_status_id_=_a.price_status_id.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [#style_chn_wk a](FROM.#style_chn_wk_a.md) |  |
| WHERE | [NOT EXISTS (SELECT *](WHERE.NOT_EXISTS_SELECT.md) |  |
| DELETE | [post_oh_work_style_wk](DELETE.post_oh_work_style_wk.md) |  |
| WHERE | [style_id BETWEEN @from_style_id AND @to_style_id](WHERE.style_id_BETWEEN_@from_style_id_AND_@to_style_id.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.on_hand_units](SET_a.on_hand_units.md) |  |
| FROM | [hist_oh_style_loc_pd a,](FROM.hist_oh_style_loc_pd_a,.md) |  |
| WHERE | [b.style_id = a.style_id](WHERE_b_style_id_=_a.style_id.md) |  |
| AND | [b.merch_year_pd = a.merch_year_pd](AND_b_merch_year_pd_=_a.merch_year_pd.md) |  |
| AND | [b.location_id = a.location_id](AND_b_location_id_=_a.location_id.md) |  |
| AND | [b.inventory_status_id = a.inventory_status_id](AND_b_inventory_status_id_=_a.inventory_status_id.md) |  |
| AND | [b.price_status_id = a.price_status_id](AND_b_price_status_id_=_a.price_status_id.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [#style_loc_pd a](FROM.#style_loc_pd_a.md) |  |
| WHERE | [NOT EXISTS (SELECT *](WHERE.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.on_hand_units = a.on_hand_units + b.on_hand_units,](SET_a_on_hand_units_=_a_on_hand_units_+_b.on_hand_units,.md) |  |
| FROM | [hist_oh_style_chn_pd a,](FROM.hist_oh_style_chn_pd_a,.md) |  |
| WHERE | [b.style_id = a.style_id](WHERE_b_style_id_=_a.style_id.md) |  |
| AND | [b.merch_year_pd = a.merch_year_pd](AND_b_merch_year_pd_=_a.merch_year_pd.md) |  |
| AND | [b.inventory_status_id = a.inventory_status_id](AND_b_inventory_status_id_=_a.inventory_status_id.md) |  |
| AND | [b.price_status_id = a.price_status_id](AND_b_price_status_id_=_a.price_status_id.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [#style_chn_pd a](FROM.#style_chn_pd_a.md) |  |
| WHERE | [NOT EXISTS (SELECT *](WHERE.NOT_EXISTS_SELECT.md) |  |
| DELETE | [post_oh_work_style_pd](DELETE.post_oh_work_style_pd.md) |  |
| WHERE | [style_id BETWEEN @from_style_id AND @to_style_id](WHERE.style_id_BETWEEN_@from_style_id_AND_@to_style_id.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.on_hand_units = a.on_hand_units + b.on_hand_units,](SET_a_on_hand_units_=_a_on_hand_units_+_b.on_hand_units,.md) |  |
| WHERE | [b.style_id = a.style_id](WHERE_b_style_id_=_a.style_id.md) |  |
| AND | [b.merch_year = a.merch_year](AND_b_merch_year_=_a.merch_year.md) |  |
| AND | [b.location_id = a.location_id](AND_b_location_id_=_a.location_id.md) |  |
| AND | [b.inventory_status_id = a.inventory_status_id](AND_b_inventory_status_id_=_a.inventory_status_id.md) |  |
| AND | [b.price_status_id = a.price_status_id](AND_b_price_status_id_=_a.price_status_id.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [#style_loc_yr a](FROM.#style_loc_yr_a.md) |  |
| WHERE | [NOT EXISTS (SELECT *](WHERE.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.on_hand_units = a.on_hand_units + b.on_hand_units,](SET_a_on_hand_units_=_a_on_hand_units_+_b.on_hand_units,.md) |  |
| WHERE | [b.style_id = a.style_id](WHERE_b_style_id_=_a.style_id.md) |  |
| AND | [b.merch_year = a.merch_year](AND_b_merch_year_=_a.merch_year.md) |  |
| AND | [b.inventory_status_id = a.inventory_status_id](AND_b_inventory_status_id_=_a.inventory_status_id.md) |  |
| AND | [b.price_status_id = a.price_status_id](AND_b_price_status_id_=_a.price_status_id.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [#style_chn_yr a](FROM.#style_chn_yr_a.md) |  |
| WHERE | [NOT EXISTS (SELECT *](WHERE.NOT_EXISTS_SELECT.md) |  |
| DELETE | [post_oh_work_style_yr](DELETE.post_oh_work_style_yr.md) |  |
| WHERE | [style_id BETWEEN @from_style_id AND @to_style_id](WHERE.style_id_BETWEEN_@from_style_id_AND_@to_style_id.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.on_hand_units = a.on_hand_units + b.on_hand_units,](SET_a_on_hand_units_=_a_on_hand_units_+_b.on_hand_units,.md) |  |
| FROM | [hist_oh_style_loc_li a,](FROM.hist_oh_style_loc_li_a,.md) |  |
| WHERE | [b.style_id = a.style_id](WHERE_b_style_id_=_a.style_id.md) |  |
| AND | [b.location_id = a.location_id](AND_b_location_id_=_a.location_id.md) |  |
| AND | [b.inventory_status_id = a.inventory_status_id](AND_b_inventory_status_id_=_a.inventory_status_id.md) |  |
| AND | [b.price_status_id = a.price_status_id](AND_b_price_status_id_=_a.price_status_id.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [#style_loc_li a](FROM.#style_loc_li_a.md) |  |
| WHERE | [NOT EXISTS (SELECT *](WHERE.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.on_hand_units = a.on_hand_units + b.on_hand_units,](SET_a_on_hand_units_=_a_on_hand_units_+_b.on_hand_units,.md) |  |
| FROM | [hist_oh_style_chn_li a,](FROM.hist_oh_style_chn_li_a,.md) |  |
| WHERE | [b.style_id = a.style_id](WHERE_b_style_id_=_a.style_id.md) |  |
| AND | [b.inventory_status_id = a.inventory_status_id](AND_b_inventory_status_id_=_a.inventory_status_id.md) |  |
| AND | [b.price_status_id = a.price_status_id](AND_b_price_status_id_=_a.price_status_id.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [#style_chn_li a](FROM.#style_chn_li_a.md) |  |
| WHERE | [NOT EXISTS (SELECT *](WHERE.NOT_EXISTS_SELECT.md) |  |
| DELETE | [post_oh_work_style_li](DELETE.post_oh_work_style_li.md) |  |
| WHERE | [style_id BETWEEN @from_style_id AND @to_style_id](WHERE.style_id_BETWEEN_@from_style_id_AND_@to_style_id.md) |  |
| dbo | [post_hist_oh_styleclr_$sp](dbo.post_hist_oh_styleclr_$sp.md) | dbo.a, dbo.hist_oh_styleclr_chn_li, dbo.hist_oh_styleclr_chn_pd, dbo.hist_oh_styleclr_chn_wk, dbo.hist_oh_styleclr_chn_yr, dbo.hist_oh_styleclr_loc_li, dbo.hist_oh_styleclr_loc_pd, dbo.hist_oh_styleclr_loc_wk, dbo.hist_oh_styleclr_loc_yr, dbo.post_oh_work_styleclr_li, dbo.post_oh_work_styleclr_pd, dbo.post_oh_work_styleclr_wk, dbo.post_oh_work_styleclr_yr |
| inventory_status_id | [smallint  NOT NULL,](inventory_status_id.smallint_NOT_NULL,.md) |  |
| price_status_id | [smallint  NOT NULL,](price_status_id.smallint_NOT_NULL,.md) |  |
| inventory_status_id | [smallint NOT NULL,](inventory_status_id.smallint_NOT_NULL,.md) |  |
| price_status_id | [smallint  NOT NULL,](price_status_id.smallint_NOT_NULL,.md) |  |
| inventory_status_id | [smallint  NOT NULL,](inventory_status_id.smallint_NOT_NULL,.md) |  |
| price_status_id | [smallint  NOT NULL,](price_status_id.smallint_NOT_NULL,.md) |  |
| inventory_status_id | [smallint  NOT NULL,](inventory_status_id.smallint_NOT_NULL,.md) |  |
| price_status_id | [smallint  NOT NULL,](price_status_id.smallint_NOT_NULL,.md) |  |
| INSERT | [#styleclr_loc_wk](INSERT.#styleclr_loc_wk.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [post_oh_work_styleclr_wk](FROM.post_oh_work_styleclr_wk.md) |  |
| WHERE | [style_id BETWEEN @curr_style_id AND @curr_style_id_2](WHERE.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [post_oh_work_styleclr_wk](FROM.post_oh_work_styleclr_wk.md) |  |
| WHERE | [style_id  BETWEEN @curr_style_id AND @curr_style_id_2](WHERE.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [post_oh_work_styleclr_pd a](FROM.post_oh_work_styleclr_pd_a.md) |  |
| WHERE | [a.style_id  BETWEEN @curr_style_id AND @curr_style_id_2](WHERE_a.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [post_oh_work_styleclr_pd a](FROM.post_oh_work_styleclr_pd_a.md) |  |
| WHERE | [a.style_id  BETWEEN @curr_style_id AND @curr_style_id_2](WHERE_a.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [post_oh_work_styleclr_yr](FROM.post_oh_work_styleclr_yr.md) |  |
| WHERE | [style_id  BETWEEN @curr_style_id AND @curr_style_id_2](WHERE.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [post_oh_work_styleclr_yr](FROM.post_oh_work_styleclr_yr.md) |  |
| WHERE | [style_id  BETWEEN @curr_style_id AND @curr_style_id_2](WHERE.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [post_oh_work_styleclr_li](FROM.post_oh_work_styleclr_li.md) |  |
| WHERE | [style_id  BETWEEN @curr_style_id AND @curr_style_id_2](WHERE.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [post_oh_work_styleclr_li](FROM.post_oh_work_styleclr_li.md) |  |
| WHERE | [style_id  BETWEEN @curr_style_id AND @curr_style_id_2](WHERE.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.on_hand_units = a.on_hand_units + b.on_hand_units,](SET_a_on_hand_units_=_a_on_hand_units_+_b.on_hand_units,.md) |  |
| FROM | [hist_oh_styleclr_loc_wk a,](FROM.hist_oh_styleclr_loc_wk_a,.md) |  |
| WHERE | [b.style_id = a.style_id](WHERE_b_style_id_=_a.style_id.md) |  |
| AND | [b.color_id = a.color_id](AND_b_color_id_=_a.color_id.md) |  |
| AND | [b.merch_year_wk = a.merch_year_wk](AND_b_merch_year_wk_=_a.merch_year_wk.md) |  |
| AND | [b.location_id = a.location_id](AND_b_location_id_=_a.location_id.md) |  |
| AND | [b.inventory_status_id = a.inventory_status_id](AND_b_inventory_status_id_=_a.inventory_status_id.md) |  |
| AND | [b.price_status_id = a.price_status_id](AND_b_price_status_id_=_a.price_status_id.md) |  |
| INSERT | [hist_oh_styleclr_loc_wk](INSERT.hist_oh_styleclr_loc_wk.md) |  |
| FROM | [#styleclr_loc_wk a](FROM.#styleclr_loc_wk_a.md) |  |
| WHERE | [NOT EXISTS (SELECT](WHERE.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.on_hand_units = a.on_hand_units + b.on_hand_units,](SET_a_on_hand_units_=_a_on_hand_units_+_b.on_hand_units,.md) |  |
| FROM | [hist_oh_styleclr_chn_wk a,](FROM.hist_oh_styleclr_chn_wk_a,.md) |  |
| WHERE | [b.style_id = a.style_id](WHERE_b_style_id_=_a.style_id.md) |  |
| AND | [b.color_id = a.color_id](AND_b_color_id_=_a.color_id.md) |  |
| AND | [b.merch_year_wk = a.merch_year_wk](AND_b_merch_year_wk_=_a.merch_year_wk.md) |  |
| AND | [b.inventory_status_id = a.inventory_status_id](AND_b_inventory_status_id_=_a.inventory_status_id.md) |  |
| AND | [b.price_status_id = a.price_status_id](AND_b_price_status_id_=_a.price_status_id.md) |  |
| INSERT | [hist_oh_styleclr_chn_wk](INSERT.hist_oh_styleclr_chn_wk.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [#styleclr_chn_wk a](FROM.#styleclr_chn_wk_a.md) |  |
| WHERE | [NOT EXISTS (SELECT](WHERE.NOT_EXISTS_SELECT.md) |  |
| DELETE | [post_oh_work_styleclr_wk](DELETE.post_oh_work_styleclr_wk.md) |  |
| WHERE | [style_id  BETWEEN @curr_style_id AND @curr_style_id_2](WHERE.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.on_hand_units = a.on_hand_units + b.on_hand_units,](SET_a_on_hand_units_=_a_on_hand_units_+_b.on_hand_units,.md) |  |
| WHERE | [b.style_id = a.style_id](WHERE_b_style_id_=_a.style_id.md) |  |
| AND | [b.color_id = a.color_id](AND_b_color_id_=_a.color_id.md) |  |
| AND | [b.merch_year_pd = a.merch_year_pd](AND_b_merch_year_pd_=_a.merch_year_pd.md) |  |
| AND | [b.location_id = a.location_id](AND_b_location_id_=_a.location_id.md) |  |
| AND | [b.inventory_status_id = a.inventory_status_id](AND_b_inventory_status_id_=_a.inventory_status_id.md) |  |
| AND | [b.price_status_id = a.price_status_id](AND_b_price_status_id_=_a.price_status_id.md) |  |
| INSERT | [hist_oh_styleclr_loc_pd](INSERT.hist_oh_styleclr_loc_pd.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [#styleclr_loc_pd a](FROM.#styleclr_loc_pd_a.md) |  |
| WHERE | [NOT EXISTS (SELECT](WHERE.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.on_hand_units = a.on_hand_units + b.on_hand_units,](SET_a_on_hand_units_=_a_on_hand_units_+_b.on_hand_units,.md) |  |
| AND | [b.color_id = a.color_id](AND_b_color_id_=_a.color_id.md) |  |
| AND | [b.merch_year_pd = a.merch_year_pd](AND_b_merch_year_pd_=_a.merch_year_pd.md) |  |
| AND | [b.inventory_status_id = a.inventory_status_id](AND_b_inventory_status_id_=_a.inventory_status_id.md) |  |
| AND | [b.price_status_id = a.price_status_id](AND_b_price_status_id_=_a.price_status_id.md) |  |
| INSERT | [hist_oh_styleclr_chn_pd](INSERT.hist_oh_styleclr_chn_pd.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [#styleclr_chn_pd a](FROM.#styleclr_chn_pd_a.md) |  |
| WHERE | [NOT EXISTS (SELECT](WHERE.NOT_EXISTS_SELECT.md) |  |
| DELETE | [post_oh_work_styleclr_pd](DELETE.post_oh_work_styleclr_pd.md) |  |
| WHERE | [style_id  BETWEEN @curr_style_id AND @curr_style_id_2](WHERE.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.on_hand_units = a.on_hand_units + b.on_hand_units,](SET_a_on_hand_units_=_a_on_hand_units_+_b.on_hand_units,.md) |  |
| WHERE | [b.style_id = a.style_id](WHERE_b_style_id_=_a.style_id.md) |  |
| AND | [b.color_id = a.color_id](AND_b_color_id_=_a.color_id.md) |  |
| AND | [b.merch_year = a.merch_year](AND_b_merch_year_=_a.merch_year.md) |  |
| AND | [b.location_id = a.location_id](AND_b_location_id_=_a.location_id.md) |  |
| AND | [b.inventory_status_id = a.inventory_status_id](AND_b_inventory_status_id_=_a.inventory_status_id.md) |  |
| AND | [b.price_status_id = a.price_status_id](AND_b_price_status_id_=_a.price_status_id.md) |  |
| INSERT | [hist_oh_styleclr_loc_yr](INSERT.hist_oh_styleclr_loc_yr.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [#styleclr_loc_yr a](FROM.#styleclr_loc_yr_a.md) |  |
| WHERE | [NOT EXISTS (SELECT](WHERE.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.on_hand_units = a.on_hand_units + b.on_hand_units,](SET_a_on_hand_units_=_a_on_hand_units_+_b.on_hand_units,.md) |  |
| FROM | [hist_oh_styleclr_chn_yr a,](FROM.hist_oh_styleclr_chn_yr_a,.md) |  |
| WHERE | [b.style_id = a.style_id](WHERE_b_style_id_=_a.style_id.md) |  |
| AND | [b.color_id = a.color_id](AND_b_color_id_=_a.color_id.md) |  |
| AND | [b.merch_year = a.merch_year](AND_b_merch_year_=_a.merch_year.md) |  |
| AND | [b.inventory_status_id = a.inventory_status_id](AND_b_inventory_status_id_=_a.inventory_status_id.md) |  |
| AND | [b.price_status_id = a.price_status_id](AND_b_price_status_id_=_a.price_status_id.md) |  |
| INSERT | [hist_oh_styleclr_chn_yr](INSERT.hist_oh_styleclr_chn_yr.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [#styleclr_chn_yr a](FROM.#styleclr_chn_yr_a.md) |  |
| WHERE | [NOT EXISTS (SELECT](WHERE.NOT_EXISTS_SELECT.md) |  |
| DELETE | [post_oh_work_styleclr_yr](DELETE.post_oh_work_styleclr_yr.md) |  |
| WHERE | [style_id  BETWEEN @curr_style_id AND @curr_style_id_2](WHERE.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.on_hand_units = a.on_hand_units + b.on_hand_units,](SET_a_on_hand_units_=_a_on_hand_units_+_b.on_hand_units,.md) |  |
| FROM | [hist_oh_styleclr_loc_li a,](FROM.hist_oh_styleclr_loc_li_a,.md) |  |
| WHERE | [b.style_id = a.style_id](WHERE_b_style_id_=_a.style_id.md) |  |
| AND | [b.color_id = a.color_id](AND_b_color_id_=_a.color_id.md) |  |
| AND | [b.location_id = a.location_id](AND_b_location_id_=_a.location_id.md) |  |
| AND | [b.inventory_status_id = a.inventory_status_id](AND_b_inventory_status_id_=_a.inventory_status_id.md) |  |
| AND | [b.price_status_id = a.price_status_id](AND_b_price_status_id_=_a.price_status_id.md) |  |
| INSERT | [hist_oh_styleclr_loc_li](INSERT.hist_oh_styleclr_loc_li.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [#styleclr_loc_li a](FROM.#styleclr_loc_li_a.md) |  |
| WHERE | [NOT EXISTS (SELECT](WHERE.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.on_hand_units = a.on_hand_units + b.on_hand_units,](SET_a_on_hand_units_=_a_on_hand_units_+_b.on_hand_units,.md) |  |
| FROM | [hist_oh_styleclr_chn_li a,](FROM.hist_oh_styleclr_chn_li_a,.md) |  |
| WHERE | [b.style_id = a.style_id](WHERE_b_style_id_=_a.style_id.md) |  |
| AND | [b.color_id = a.color_id](AND_b_color_id_=_a.color_id.md) |  |
| AND | [b.inventory_status_id = a.inventory_status_id](AND_b_inventory_status_id_=_a.inventory_status_id.md) |  |
| AND | [b.price_status_id = a.price_status_id](AND_b_price_status_id_=_a.price_status_id.md) |  |
| INSERT | [hist_oh_styleclr_chn_li](INSERT.hist_oh_styleclr_chn_li.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [#styleclr_chn_li a](FROM.#styleclr_chn_li_a.md) |  |
| WHERE | [NOT EXISTS (SELECT](WHERE.NOT_EXISTS_SELECT.md) |  |
| DELETE | [post_oh_work_styleclr_li](DELETE.post_oh_work_styleclr_li.md) |  |
| WHERE | [style_id  BETWEEN @curr_style_id AND @curr_style_id_2](WHERE.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| dbo | [post_hist_sku_$sp](dbo.post_hist_sku_$sp.md) | dbo.calendar_merch_week, dbo.hist_sku_chn_li, dbo.hist_sku_chn_pd, dbo.hist_sku_chn_wk, dbo.hist_sku_chn_yr, dbo.hist_sku_loc_li, dbo.hist_sku_loc_pd, dbo.hist_sku_loc_wk, dbo.hist_sku_loc_yr, dbo.job_detail, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.return_step_exists_$sp, dbo.wrk_sku_loc_wk |
| dbo | [post_hist_style_$sp](dbo.post_hist_style_$sp.md) | dbo.calendar_merch_week, dbo.hist_style_chn_li, dbo.hist_style_chn_pd, dbo.hist_style_chn_wk, dbo.hist_style_chn_yr, dbo.hist_style_loc_li, dbo.hist_style_loc_pd, dbo.hist_style_loc_wk, dbo.hist_style_loc_yr, dbo.job_detail, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.return_step_exists_$sp, dbo.wrk_style_loc_wk |
| dbo | [post_hist_style_color_$sp](dbo.post_hist_style_color_$sp.md) | dbo.calendar_merch_week, dbo.hist_styleclr_chn_li, dbo.hist_styleclr_chn_pd, dbo.hist_styleclr_chn_wk, dbo.hist_styleclr_chn_yr, dbo.hist_styleclr_loc_li, dbo.hist_styleclr_loc_pd, dbo.hist_styleclr_loc_wk, dbo.hist_styleclr_loc_yr, dbo.job_detail, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.return_step_exists_$sp, dbo.wrk_styleclr_loc_wk |
| dbo | [post_hist_styleclr_$sp](dbo.post_hist_styleclr_$sp.md) | dbo.a, dbo.calendar_merch_week, dbo.hist_styleclr_chn_li, dbo.hist_styleclr_chn_pd, dbo.hist_styleclr_chn_wk, dbo.hist_styleclr_chn_yr, dbo.hist_styleclr_loc_li, dbo.hist_styleclr_loc_pd, dbo.hist_styleclr_loc_wk, dbo.hist_styleclr_loc_yr, dbo.post_hist_styleclr |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [post_hist_styleclr](FROM.post_hist_styleclr.md) |  |
| WHERE | [style_id  BETWEEN @curr_style_id AND @curr_style_id_2](WHERE.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [post_hist_styleclr](FROM.post_hist_styleclr.md) |  |
| WHERE | [style_id  BETWEEN @curr_style_id AND @curr_style_id_2](WHERE.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| SELECT | [b.style_id,](SELECT_b.style_id,.md) |  |
| FROM | [post_hist_styleclr b,](FROM.post_hist_styleclr_b,.md) |  |
| WHERE | [b.style_id  BETWEEN @curr_style_id AND @curr_style_id_2](WHERE_b.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| AND | [b.merch_year_wk/100 = c.merch_year](AND_b_merch_year_wk_100_=_c.merch_year.md) |  |
| AND | [b.merch_year_wk % 100 = c.merch_week](AND_b_merch_year_wk_%_100_=_c.merch_week.md) |  |
| SELECT | [b.style_id,](SELECT_b.style_id,.md) |  |
| FROM | [post_hist_styleclr b,](FROM.post_hist_styleclr_b,.md) |  |
| WHERE | [b.style_id  BETWEEN @curr_style_id AND @curr_style_id_2](WHERE_b.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| AND | [b.merch_year_wk/100 = c.merch_year](AND_b_merch_year_wk_100_=_c.merch_year.md) |  |
| AND | [b.merch_year_wk % 100 = c.merch_week](AND_b_merch_year_wk_%_100_=_c.merch_week.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [post_hist_styleclr](FROM.post_hist_styleclr.md) |  |
| WHERE | [style_id  BETWEEN @curr_style_id AND @curr_style_id_2](WHERE.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [post_hist_styleclr](FROM.post_hist_styleclr.md) |  |
| WHERE | [style_id  BETWEEN @curr_style_id AND @curr_style_id_2](WHERE.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [post_hist_styleclr](FROM.post_hist_styleclr.md) |  |
| WHERE | [style_id  BETWEEN @curr_style_id AND @curr_style_id_2](WHERE.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [post_hist_styleclr](FROM.post_hist_styleclr.md) |  |
| WHERE | [style_id  BETWEEN @curr_style_id AND @curr_style_id_2](WHERE.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| FROM | [hist_styleclr_loc_wk a,](FROM.hist_styleclr_loc_wk_a,.md) |  |
| WHERE | [b.style_id = a.style_id](WHERE_b_style_id_=_a.style_id.md) |  |
| AND | [b.color_id = a.color_id](AND_b_color_id_=_a.color_id.md) |  |
| AND | [b.merch_year_wk = a.merch_year_wk](AND_b_merch_year_wk_=_a.merch_year_wk.md) |  |
| AND | [b.location_id = a.location_id](AND_b_location_id_=_a.location_id.md) |  |
| INSERT | [hist_styleclr_loc_wk](INSERT.hist_styleclr_loc_wk.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [#styleclr_loc_wk a](FROM.#styleclr_loc_wk_a.md) |  |
| WHERE | [NOT EXISTS (SELECT 1](WHERE.NOT_EXISTS_SELECT_1.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.perm_md_retail = a.perm_md_retail + b.perm_md_retail,](SET_a_perm_md_retail_=_a_perm_md_retail_+_b.perm_md_retail,.md) |  |
| FROM | [hist_styleclr_chn_wk a,](FROM.hist_styleclr_chn_wk_a,.md) |  |
| WHERE | [b.style_id = a.style_id](WHERE_b_style_id_=_a.style_id.md) |  |
| AND | [b.color_id = a.color_id](AND_b_color_id_=_a.color_id.md) |  |
| AND | [b.merch_year_wk = a.merch_year_wk](AND_b_merch_year_wk_=_a.merch_year_wk.md) |  |
| INSERT | [hist_styleclr_chn_wk](INSERT.hist_styleclr_chn_wk.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [#styleclr_chn_wk a](FROM.#styleclr_chn_wk_a.md) |  |
| WHERE | [NOT EXISTS (SELECT 1](WHERE.NOT_EXISTS_SELECT_1.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| FROM | [hist_styleclr_loc_pd a,](FROM.hist_styleclr_loc_pd_a,.md) |  |
| WHERE | [b.style_id = a.style_id](WHERE_b_style_id_=_a.style_id.md) |  |
| AND | [b.color_id = a.color_id](AND_b_color_id_=_a.color_id.md) |  |
| AND | [b.merch_year_pd = a.merch_year_pd](AND_b_merch_year_pd_=_a.merch_year_pd.md) |  |
| AND | [b.location_id = a.location_id](AND_b_location_id_=_a.location_id.md) |  |
| INSERT | [hist_styleclr_loc_pd](INSERT.hist_styleclr_loc_pd.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [#styleclr_loc_pd a](FROM.#styleclr_loc_pd_a.md) |  |
| WHERE | [NOT EXISTS (SELECT 1](WHERE.NOT_EXISTS_SELECT_1.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.perm_md_retail = a.perm_md_retail + b.perm_md_retail,](SET_a_perm_md_retail_=_a_perm_md_retail_+_b.perm_md_retail,.md) |  |
| FROM | [hist_styleclr_chn_pd a,](FROM.hist_styleclr_chn_pd_a,.md) |  |
| WHERE | [b.style_id = a.style_id](WHERE_b_style_id_=_a.style_id.md) |  |
| AND | [b.color_id = a.color_id](AND_b_color_id_=_a.color_id.md) |  |
| AND | [b.merch_year_pd = a.merch_year_pd](AND_b_merch_year_pd_=_a.merch_year_pd.md) |  |
| INSERT | [hist_styleclr_chn_pd](INSERT.hist_styleclr_chn_pd.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [#styleclr_chn_pd a](FROM.#styleclr_chn_pd_a.md) |  |
| WHERE | [NOT EXISTS (SELECT 1](WHERE.NOT_EXISTS_SELECT_1.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| FROM | [hist_styleclr_loc_yr a,](FROM.hist_styleclr_loc_yr_a,.md) |  |
| WHERE | [b.style_id = a.style_id](WHERE_b_style_id_=_a.style_id.md) |  |
| AND | [b.color_id = a.color_id](AND_b_color_id_=_a.color_id.md) |  |
| AND | [b.merch_year = a.merch_year](AND_b_merch_year_=_a.merch_year.md) |  |
| AND | [b.location_id = a.location_id](AND_b_location_id_=_a.location_id.md) |  |
| INSERT | [hist_styleclr_loc_yr](INSERT.hist_styleclr_loc_yr.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [#styleclr_loc_yr a](FROM.#styleclr_loc_yr_a.md) |  |
| WHERE | [NOT EXISTS (SELECT 1](WHERE.NOT_EXISTS_SELECT_1.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.perm_md_retail = a.perm_md_retail + b.perm_md_retail,](SET_a_perm_md_retail_=_a_perm_md_retail_+_b.perm_md_retail,.md) |  |
| FROM | [hist_styleclr_chn_yr a,](FROM.hist_styleclr_chn_yr_a,.md) |  |
| WHERE | [b.style_id = a.style_id](WHERE_b_style_id_=_a.style_id.md) |  |
| AND | [b.color_id = a.color_id](AND_b_color_id_=_a.color_id.md) |  |
| AND | [b.merch_year = a.merch_year](AND_b_merch_year_=_a.merch_year.md) |  |
| INSERT | [hist_styleclr_chn_yr](INSERT.hist_styleclr_chn_yr.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [#styleclr_chn_yr a](FROM.#styleclr_chn_yr_a.md) |  |
| WHERE | [NOT EXISTS (SELECT 1](WHERE.NOT_EXISTS_SELECT_1.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| FROM | [hist_styleclr_loc_li a,](FROM.hist_styleclr_loc_li_a,.md) |  |
| WHERE | [b.style_id = a.style_id](WHERE_b_style_id_=_a.style_id.md) |  |
| AND | [b.color_id = a.color_id](AND_b_color_id_=_a.color_id.md) |  |
| AND | [b.location_id = a.location_id](AND_b_location_id_=_a.location_id.md) |  |
| INSERT | [hist_styleclr_loc_li](INSERT.hist_styleclr_loc_li.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [#styleclr_loc_li a](FROM.#styleclr_loc_li_a.md) |  |
| WHERE | [NOT EXISTS (SELECT 1](WHERE.NOT_EXISTS_SELECT_1.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| FROM | [hist_styleclr_chn_li a,](FROM.hist_styleclr_chn_li_a,.md) |  |
| WHERE | [b.style_id = a.style_id](WHERE_b_style_id_=_a.style_id.md) |  |
| AND | [b.color_id = a.color_id](AND_b_color_id_=_a.color_id.md) |  |
| INSERT | [hist_styleclr_chn_li](INSERT.hist_styleclr_chn_li.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [#styleclr_chn_li a](FROM.#styleclr_chn_li_a.md) |  |
| WHERE | [NOT EXISTS (SELECT 1](WHERE.NOT_EXISTS_SELECT_1.md) |  |
| DELETE | [post_hist_styleclr](DELETE.post_hist_styleclr.md) |  |
| WHERE | [style_id  BETWEEN @curr_style_id AND @curr_style_id_2](WHERE.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| dbo | [post_oh_group_$sp](dbo.post_oh_group_$sp.md) | dbo.calendar_merch_week, dbo.hist_oh_group_chn_li, dbo.hist_oh_group_chn_pd, dbo.hist_oh_group_chn_wk, dbo.hist_oh_group_chn_yr, dbo.hist_oh_group_loc_li, dbo.hist_oh_group_loc_pd, dbo.hist_oh_group_loc_wk, dbo.hist_oh_group_loc_yr, dbo.job_detail, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.return_step_exists_$sp, dbo.wrk_oh_group_loc_wk |
| dbo | [post_oh_sku_$sp](dbo.post_oh_sku_$sp.md) | dbo.calendar_merch_week, dbo.hist_oh_sku_chn_li, dbo.hist_oh_sku_chn_pd, dbo.hist_oh_sku_chn_wk, dbo.hist_oh_sku_chn_yr, dbo.hist_oh_sku_loc_li, dbo.hist_oh_sku_loc_pd, dbo.hist_oh_sku_loc_wk, dbo.hist_oh_sku_loc_yr, dbo.job_detail, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.return_step_exists_$sp, dbo.wrk_oh_sku_loc_wk |
| dbo | [post_oh_style_$sp](dbo.post_oh_style_$sp.md) | dbo.calendar_merch_week, dbo.hist_oh_style_chn_li, dbo.hist_oh_style_chn_pd, dbo.hist_oh_style_chn_wk, dbo.hist_oh_style_chn_yr, dbo.hist_oh_style_loc_li, dbo.hist_oh_style_loc_pd, dbo.hist_oh_style_loc_wk, dbo.hist_oh_style_loc_yr, dbo.job_detail, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.return_step_exists_$sp, dbo.wrk_oh_style_loc_wk |
| dbo | [post_oh_style_color_$sp](dbo.post_oh_style_color_$sp.md) | dbo.calendar_merch_week, dbo.hist_oh_styleclr_chn_li, dbo.hist_oh_styleclr_chn_pd, dbo.hist_oh_styleclr_chn_wk, dbo.hist_oh_styleclr_chn_yr, dbo.hist_oh_styleclr_loc_li, dbo.hist_oh_styleclr_loc_pd, dbo.hist_oh_styleclr_loc_wk, dbo.hist_oh_styleclr_loc_yr, dbo.job_detail, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.return_step_exists_$sp, dbo.wrk_oh_styleclr_loc_wk |
| dbo | [post_oh_work_group_$sp](dbo.post_oh_work_group_$sp.md) | dbo.calendar, dbo.calendar_merch_period, dbo.calendar_merch_week, dbo.post_hist_oh_group, dbo.post_oh_work_group_li, dbo.post_oh_work_group_pd, dbo.post_oh_work_group_wk, dbo.post_oh_work_group_yr |
| SELECT | [a.hierarchy_group_id,](SELECT_a.hierarchy_group_id,.md) |  |
| FROM | [post_hist_oh_group a,](FROM.post_hist_oh_group_a,.md) |  |
| WHERE | [a.hierarchy_group_id = @curr_hierarchy_group_id](WHERE_a.hierarchy_group_id_=_@curr_hierarchy_group_id.md) |  |
| AND | [d.merch_year * 100 + d.merch_week BETWEEN a.merch_year_wk AND @last_week](AND_d_merch_year_100_+_d_merch_week_BETWEEN_a.merch_year_wk_AND_@last_week.md) |  |
| SELECT | [a.hierarchy_group_id,](SELECT_a.hierarchy_group_id,.md) |  |
| FROM | [post_hist_oh_group a,](FROM.post_hist_oh_group_a,.md) |  |
| WHERE | [a.hierarchy_group_id = @curr_hierarchy_group_id](WHERE_a.hierarchy_group_id_=_@curr_hierarchy_group_id.md) |  |
| AND | [a.merch_year_wk/100 = b.merch_year](AND_a_merch_year_wk_100_=_b.merch_year.md) |  |
| AND | [a.merch_year_wk % 100 = b.merch_week](AND_a_merch_year_wk_%_100_=_b.merch_week.md) |  |
| AND | [c.merch_year * 100 + c.merch_period BETWEEN  b.merch_year * 100 + b.merch_period AND @last_period](AND_c_merch_year_100_+_c_merch_period_BETWEEN_b_merch_year_100_+_b.merch_period_AND_@last_period.md) |  |
| SELECT | [a.hierarchy_group_id,](SELECT_a.hierarchy_group_id,.md) |  |
| WHERE | [a.hierarchy_group_id = @curr_hierarchy_group_id](WHERE_a.hierarchy_group_id_=_@curr_hierarchy_group_id.md) |  |
| AND | [b.calendar_code BETWEEN a.merch_year_wk/100 AND @last_year](AND_b_calendar_code_BETWEEN_a.merch_year_wk_100_AND_@last_year.md) |  |
| SELECT | [hierarchy_group_id,](SELECT.hierarchy_group_id,.md) |  |
| FROM | [post_hist_oh_group](FROM.post_hist_oh_group.md) |  |
| WHERE | [hierarchy_group_id = @curr_hierarchy_group_id](WHERE.hierarchy_group_id_=_@curr_hierarchy_group_id.md) |  |
| dbo | [post_oh_work_sku_$sp](dbo.post_oh_work_sku_$sp.md) | dbo.calendar, dbo.calendar_merch_period, dbo.calendar_merch_week, dbo.post_hist_oh_sku, dbo.post_oh_work_sku_li, dbo.post_oh_work_sku_pd, dbo.post_oh_work_sku_wk, dbo.post_oh_work_sku_yr |
| dbo | [post_oh_work_style_$sp](dbo.post_oh_work_style_$sp.md) | dbo.calendar, dbo.calendar_merch_period, dbo.calendar_merch_week, dbo.post_hist_oh_style, dbo.post_oh_work_style_li, dbo.post_oh_work_style_pd, dbo.post_oh_work_style_wk, dbo.post_oh_work_style_yr |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [post_hist_oh_style a,](FROM.post_hist_oh_style_a,.md) |  |
| WHERE | [style_id = @curr_style_id](WHERE.style_id_=_@curr_style_id.md) |  |
| AND | [d.merch_year * 100 + d.merch_week BETWEEN a.merch_year_wk AND @last_week](AND_d_merch_year_100_+_d_merch_week_BETWEEN_a.merch_year_wk_AND_@last_week.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [post_hist_oh_style a,](FROM.post_hist_oh_style_a,.md) |  |
| WHERE | [style_id = @curr_style_id](WHERE.style_id_=_@curr_style_id.md) |  |
| AND | [a.merch_year_wk/100 = b.merch_year](AND_a_merch_year_wk_100_=_b.merch_year.md) |  |
| AND | [a.merch_year_wk % 100 = b.merch_week](AND_a_merch_year_wk_%_100_=_b.merch_week.md) |  |
| AND | [c.merch_year * 100 + c.merch_period BETWEEN  b.merch_year * 100 + b.merch_period AND @last_period](AND_c_merch_year_100_+_c_merch_period_BETWEEN_b_merch_year_100_+_b.merch_period_AND_@last_period.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [post_hist_oh_style a,](FROM.post_hist_oh_style_a,.md) |  |
| WHERE | [a.style_id = @curr_style_id](WHERE_a.style_id_=_@curr_style_id.md) |  |
| AND | [b.calendar_code BETWEEN a.merch_year_wk / 100 AND @last_year](AND_b_calendar_code_BETWEEN_a.merch_year_wk_100_AND_@last_year.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [post_hist_oh_style](FROM.post_hist_oh_style.md) |  |
| WHERE | [style_id = @curr_style_id](WHERE.style_id_=_@curr_style_id.md) |  |
| dbo | [post_oh_work_styleclr_$sp](dbo.post_oh_work_styleclr_$sp.md) | dbo.calendar, dbo.calendar_merch_period, dbo.calendar_merch_week, dbo.post_hist_oh_styleclr, dbo.post_oh_work_styleclr_li, dbo.post_oh_work_styleclr_pd, dbo.post_oh_work_styleclr_wk, dbo.post_oh_work_styleclr_yr |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| WHERE | [style_id = @curr_style_id](WHERE.style_id_=_@curr_style_id.md) |  |
| AND | [d.merch_year * 100 + d.merch_week BETWEEN a.merch_year_wk AND @last_week](AND_d_merch_year_100_+_d_merch_week_BETWEEN_a.merch_year_wk_AND_@last_week.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| WHERE | [style_id = @curr_style_id](WHERE.style_id_=_@curr_style_id.md) |  |
| AND | [a.merch_year_wk/100 = b.merch_year](AND_a_merch_year_wk_100_=_b.merch_year.md) |  |
| AND | [a.merch_year_wk % 100 = b.merch_week](AND_a_merch_year_wk_%_100_=_b.merch_week.md) |  |
| AND | [c.merch_year * 100 + c.merch_period BETWEEN b.merch_year * 100 + b.merch_period AND @last_period](AND_c_merch_year_100_+_c_merch_period_BETWEEN_b_merch_year_100_+_b.merch_period_AND_@last_period.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [post_hist_oh_styleclr a,](FROM.post_hist_oh_styleclr_a,.md) |  |
| WHERE | [a.style_id = @curr_style_id](WHERE_a.style_id_=_@curr_style_id.md) |  |
| AND | [b.calendar_code BETWEEN a.merch_year_wk / 100  AND @last_year](AND_b_calendar_code_BETWEEN_a.merch_year_wk_100_AND_@last_year.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [post_hist_oh_styleclr](FROM.post_hist_oh_styleclr.md) |  |
| WHERE | [style_id = @curr_style_id](WHERE.style_id_=_@curr_style_id.md) |  |
| dbo | [post_oo_all_group_$sp](dbo.post_oo_all_group_$sp.md) | dbo.a, dbo.calendar_merch_week, dbo.mv_fact_queue, dbo.oo_all_group_chn_li, dbo.oo_all_group_chn_pd, dbo.oo_all_group_chn_wk, dbo.oo_all_group_chn_yr, dbo.oo_all_group_loc_li, dbo.oo_all_group_loc_pd, dbo.oo_all_group_loc_wk, dbo.oo_all_group_loc_yr, dbo.plan_exp_table_group, dbo.post_oo_all_group_sum |
| on_order_units | [int](on_order_units.int.md) |  |
| on_order_retail | [decimal(14,2)](on_order_retail.decimal_14,2.md) |  |
| on_order_cost | [decimal(14,2)](on_order_cost.decimal_14,2.md) |  |
| on_order_retail_te | [decimal(14,2) NULL)](on_order_retail_te.decimal_14,2_NULL.md) |  |
| on_order_units | [int](on_order_units.int.md) |  |
| on_order_retail | [decimal(14,2)](on_order_retail.decimal_14,2.md) |  |
| on_order_cost | [decimal(14,2)](on_order_cost.decimal_14,2.md) |  |
| on_order_retail_te | [decimal(14,2) NULL)](on_order_retail_te.decimal_14,2_NULL.md) |  |
| on_order_units | [int](on_order_units.int.md) |  |
| on_order_retail | [decimal(14,2)](on_order_retail.decimal_14,2.md) |  |
| on_order_cost | [decimal(14,2)](on_order_cost.decimal_14,2.md) |  |
| on_order_retail_te | [decimal(14,2) NULL)](on_order_retail_te.decimal_14,2_NULL.md) |  |
| on_order_units | [int](on_order_units.int.md) |  |
| on_order_retail | [decimal(14,2)](on_order_retail.decimal_14,2.md) |  |
| on_order_cost | [decimal(14,2)](on_order_cost.decimal_14,2.md) |  |
| on_order_retail_te | [decimal(14,2) NULL)](on_order_retail_te.decimal_14,2_NULL.md) |  |
| on_order_units | [int](on_order_units.int.md) |  |
| on_order_retail | [decimal(14,2)](on_order_retail.decimal_14,2.md) |  |
| on_order_cost | [decimal(14,2)](on_order_cost.decimal_14,2.md) |  |
| on_order_retail_te | [decimal(14,2) NULL)](on_order_retail_te.decimal_14,2_NULL.md) |  |
| on_order_units | [int](on_order_units.int.md) |  |
| on_order_retail | [decimal(14,2)](on_order_retail.decimal_14,2.md) |  |
| on_order_cost | [decimal(14,2)](on_order_cost.decimal_14,2.md) |  |
| on_order_retail_te | [decimal(14,2) NULL)](on_order_retail_te.decimal_14,2_NULL.md) |  |
| on_order_units | [int](on_order_units.int.md) |  |
| on_order_retail | [decimal(14,2)](on_order_retail.decimal_14,2.md) |  |
| on_order_cost | [decimal(14,2)](on_order_cost.decimal_14,2.md) |  |
| on_order_retail_te | [decimal(14,2) NULL)](on_order_retail_te.decimal_14,2_NULL.md) |  |
| on_order_units | [int](on_order_units.int.md) |  |
| on_order_retail | [decimal(14,2)](on_order_retail.decimal_14,2.md) |  |
| on_order_cost | [decimal(14,2)](on_order_cost.decimal_14,2.md) |  |
| on_order_retail_te | [decimal(14,2) NULL)](on_order_retail_te.decimal_14,2_NULL.md) |  |
| INSERT | [#group_loc_wk](INSERT.#group_loc_wk.md) |  |
| SELECT | [hierarchy_group_id,](SELECT.hierarchy_group_id,.md) |  |
| FROM | [post_oo_all_group_sum WITH (NOLOCK)](FROM.post_oo_all_group_sum_WITH_NOLOCK.md) |  |
| WHERE | [hierarchy_group_id BETWEEN @from_group_id AND @to_group_id](WHERE.hierarchy_group_id_BETWEEN_@from_group_id_AND_@to_group_id.md) |  |
| INSERT | [#group_chn_wk](INSERT.#group_chn_wk.md) |  |
| SELECT | [hierarchy_group_id,](SELECT.hierarchy_group_id,.md) |  |
| FROM | [post_oo_all_group_sum WITH (NOLOCK)](FROM.post_oo_all_group_sum_WITH_NOLOCK.md) |  |
| WHERE | [hierarchy_group_id BETWEEN @from_group_id AND @to_group_id](WHERE.hierarchy_group_id_BETWEEN_@from_group_id_AND_@to_group_id.md) |  |
| INSERT | [#group_loc_pd](INSERT.#group_loc_pd.md) |  |
| SELECT | [a.hierarchy_group_id,](SELECT_a.hierarchy_group_id,.md) |  |
| FROM | [post_oo_all_group_sum a,](FROM.post_oo_all_group_sum_a,.md) |  |
| WHERE | [a.hierarchy_group_id BETWEEN @from_group_id AND @to_group_id](WHERE_a.hierarchy_group_id_BETWEEN_@from_group_id_AND_@to_group_id.md) |  |
| AND | [a.merch_year_wk / 100 = c.merch_year](AND_a_merch_year_wk_100_=_c.merch_year.md) |  |
| AND | [a.merch_year_wk % 100 = c.merch_week](AND_a_merch_year_wk_%_100_=_c.merch_week.md) |  |
| INSERT | [#group_chn_pd](INSERT.#group_chn_pd.md) |  |
| SELECT | [a.hierarchy_group_id,](SELECT_a.hierarchy_group_id,.md) |  |
| FROM | [post_oo_all_group_sum a,](FROM.post_oo_all_group_sum_a,.md) |  |
| WHERE | [a.hierarchy_group_id BETWEEN @from_group_id AND @to_group_id](WHERE_a.hierarchy_group_id_BETWEEN_@from_group_id_AND_@to_group_id.md) |  |
| AND | [a.merch_year_wk / 100 = c.merch_year](AND_a_merch_year_wk_100_=_c.merch_year.md) |  |
| AND | [a.merch_year_wk % 100 = c.merch_week](AND_a_merch_year_wk_%_100_=_c.merch_week.md) |  |
| INSERT | [#group_loc_yr](INSERT.#group_loc_yr.md) |  |
| SELECT | [hierarchy_group_id,](SELECT.hierarchy_group_id,.md) |  |
| FROM | [post_oo_all_group_sum WITH (NOLOCK)](FROM.post_oo_all_group_sum_WITH_NOLOCK.md) |  |
| WHERE | [hierarchy_group_id BETWEEN @from_group_id AND @to_group_id](WHERE.hierarchy_group_id_BETWEEN_@from_group_id_AND_@to_group_id.md) |  |
| INSERT | [#group_chn_yr](INSERT.#group_chn_yr.md) |  |
| SELECT | [hierarchy_group_id,](SELECT.hierarchy_group_id,.md) |  |
| FROM | [post_oo_all_group_sum WITH (NOLOCK)](FROM.post_oo_all_group_sum_WITH_NOLOCK.md) |  |
| WHERE | [hierarchy_group_id BETWEEN @from_group_id AND @to_group_id](WHERE.hierarchy_group_id_BETWEEN_@from_group_id_AND_@to_group_id.md) |  |
| INSERT | [#group_loc_li](INSERT.#group_loc_li.md) |  |
| SELECT | [hierarchy_group_id,](SELECT.hierarchy_group_id,.md) |  |
| FROM | [post_oo_all_group_sum WITH (NOLOCK)](FROM.post_oo_all_group_sum_WITH_NOLOCK.md) |  |
| WHERE | [hierarchy_group_id BETWEEN @from_group_id AND @to_group_id](WHERE.hierarchy_group_id_BETWEEN_@from_group_id_AND_@to_group_id.md) |  |
| INSERT | [#group_chn_li](INSERT.#group_chn_li.md) |  |
| SELECT | [hierarchy_group_id,](SELECT.hierarchy_group_id,.md) |  |
| FROM | [post_oo_all_group_sum WITH (NOLOCK)](FROM.post_oo_all_group_sum_WITH_NOLOCK.md) |  |
| WHERE | [hierarchy_group_id BETWEEN @from_group_id AND @to_group_id](WHERE.hierarchy_group_id_BETWEEN_@from_group_id_AND_@to_group_id.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.on_order_units = a.on_order_units + b.on_order_units,](SET_a_on_order_units_=_a_on_order_units_+_b.on_order_units,.md) |  |
| FROM | [oo_all_group_loc_wk a,](FROM.oo_all_group_loc_wk_a,.md) |  |
| WHERE | [a.hierarchy_group_id BETWEEN @from_group_id AND @to_group_id](WHERE_a.hierarchy_group_id_BETWEEN_@from_group_id_AND_@to_group_id.md) |  |
| AND | [a.hierarchy_group_id = b.hierarchy_group_id](AND_a_hierarchy_group_id_=_b.hierarchy_group_id.md) |  |
| AND | [a.merch_year_wk = b.merch_year_wk](AND_a_merch_year_wk_=_b.merch_year_wk.md) |  |
| AND | [a.location_id = b.location_id](AND_a_location_id_=_b.location_id.md) |  |
| SELECT | [a.hierarchy_group_id,](SELECT_a.hierarchy_group_id,.md) |  |
| FROM | [#group_loc_wk a](FROM.#group_loc_wk_a.md) |  |
| WHERE | [a.hierarchy_group_id BETWEEN @from_group_id AND @to_group_id](WHERE_a.hierarchy_group_id_BETWEEN_@from_group_id_AND_@to_group_id.md) |  |
| AND | [NOT EXISTS (SELECT *](AND.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.on_order_units = a.on_order_units + b.on_order_units,](SET_a_on_order_units_=_a_on_order_units_+_b.on_order_units,.md) |  |
| FROM | [oo_all_group_chn_wk a,](FROM.oo_all_group_chn_wk_a,.md) |  |
| WHERE | [a.hierarchy_group_id BETWEEN @from_group_id AND @to_group_id](WHERE_a.hierarchy_group_id_BETWEEN_@from_group_id_AND_@to_group_id.md) |  |
| AND | [a.hierarchy_group_id = b.hierarchy_group_id](AND_a_hierarchy_group_id_=_b.hierarchy_group_id.md) |  |
| AND | [a.merch_year_wk = b.merch_year_wk](AND_a_merch_year_wk_=_b.merch_year_wk.md) |  |
| SELECT | [a.hierarchy_group_id,](SELECT_a.hierarchy_group_id,.md) |  |
| FROM | [#group_chn_wk a](FROM.#group_chn_wk_a.md) |  |
| WHERE | [a.hierarchy_group_id BETWEEN @from_group_id AND @to_group_id](WHERE_a.hierarchy_group_id_BETWEEN_@from_group_id_AND_@to_group_id.md) |  |
| AND | [NOT EXISTS (SELECT *](AND.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.on_order_units = a.on_order_units + b.on_order_units,](SET_a_on_order_units_=_a_on_order_units_+_b.on_order_units,.md) |  |
| FROM | [oo_all_group_loc_pd a,](FROM.oo_all_group_loc_pd_a,.md) |  |
| WHERE | [a.hierarchy_group_id BETWEEN @from_group_id AND @to_group_id](WHERE_a.hierarchy_group_id_BETWEEN_@from_group_id_AND_@to_group_id.md) |  |
| AND | [a.hierarchy_group_id = b.hierarchy_group_id](AND_a_hierarchy_group_id_=_b.hierarchy_group_id.md) |  |
| AND | [a.merch_year_pd = b.merch_year_pd](AND_a_merch_year_pd_=_b.merch_year_pd.md) |  |
| AND | [a.location_id = b.location_id](AND_a_location_id_=_b.location_id.md) |  |
| SELECT | [a.hierarchy_group_id,](SELECT_a.hierarchy_group_id,.md) |  |
| FROM | [#group_loc_pd a](FROM.#group_loc_pd_a.md) |  |
| WHERE | [a.hierarchy_group_id BETWEEN @from_group_id AND @to_group_id](WHERE_a.hierarchy_group_id_BETWEEN_@from_group_id_AND_@to_group_id.md) |  |
| AND | [NOT EXISTS (SELECT *](AND.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.on_order_units = a.on_order_units + b.on_order_units,](SET_a_on_order_units_=_a_on_order_units_+_b.on_order_units,.md) |  |
| FROM | [oo_all_group_chn_pd a,](FROM.oo_all_group_chn_pd_a,.md) |  |
| WHERE | [a.hierarchy_group_id BETWEEN @from_group_id AND @to_group_id](WHERE_a.hierarchy_group_id_BETWEEN_@from_group_id_AND_@to_group_id.md) |  |
| AND | [a.hierarchy_group_id = b.hierarchy_group_id](AND_a_hierarchy_group_id_=_b.hierarchy_group_id.md) |  |
| AND | [a.merch_year_pd = b.merch_year_pd](AND_a_merch_year_pd_=_b.merch_year_pd.md) |  |
| SELECT | [a.hierarchy_group_id,](SELECT_a.hierarchy_group_id,.md) |  |
| FROM | [#group_chn_pd a](FROM.#group_chn_pd_a.md) |  |
| WHERE | [a.hierarchy_group_id BETWEEN @from_group_id AND @to_group_id](WHERE_a.hierarchy_group_id_BETWEEN_@from_group_id_AND_@to_group_id.md) |  |
| AND | [NOT EXISTS (SELECT *](AND.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.on_order_units = a.on_order_units + b.on_order_units,](SET_a_on_order_units_=_a_on_order_units_+_b.on_order_units,.md) |  |
| FROM | [oo_all_group_loc_yr a,](FROM.oo_all_group_loc_yr_a,.md) |  |
| WHERE | [a.hierarchy_group_id BETWEEN @from_group_id AND @to_group_id](WHERE_a.hierarchy_group_id_BETWEEN_@from_group_id_AND_@to_group_id.md) |  |
| AND | [a.hierarchy_group_id = b.hierarchy_group_id](AND_a_hierarchy_group_id_=_b.hierarchy_group_id.md) |  |
| AND | [a.merch_year = b.merch_year](AND_a_merch_year_=_b.merch_year.md) |  |
| AND | [a.location_id = b.location_id](AND_a_location_id_=_b.location_id.md) |  |
| SELECT | [a.hierarchy_group_id,](SELECT_a.hierarchy_group_id,.md) |  |
| FROM | [#group_loc_yr a](FROM.#group_loc_yr_a.md) |  |
| WHERE | [a.hierarchy_group_id BETWEEN @from_group_id AND @to_group_id](WHERE_a.hierarchy_group_id_BETWEEN_@from_group_id_AND_@to_group_id.md) |  |
| AND | [NOT EXISTS (SELECT *](AND.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.on_order_units = a.on_order_units + b.on_order_units,](SET_a_on_order_units_=_a_on_order_units_+_b.on_order_units,.md) |  |
| FROM | [oo_all_group_chn_yr a,](FROM.oo_all_group_chn_yr_a,.md) |  |
| WHERE | [a.hierarchy_group_id BETWEEN @from_group_id AND @to_group_id](WHERE_a.hierarchy_group_id_BETWEEN_@from_group_id_AND_@to_group_id.md) |  |
| AND | [a.hierarchy_group_id = b.hierarchy_group_id](AND_a_hierarchy_group_id_=_b.hierarchy_group_id.md) |  |
| AND | [a.merch_year = b.merch_year](AND_a_merch_year_=_b.merch_year.md) |  |
| SELECT | [a.hierarchy_group_id,](SELECT_a.hierarchy_group_id,.md) |  |
| FROM | [#group_chn_yr a](FROM.#group_chn_yr_a.md) |  |
| WHERE | [a.hierarchy_group_id BETWEEN @from_group_id AND @to_group_id](WHERE_a.hierarchy_group_id_BETWEEN_@from_group_id_AND_@to_group_id.md) |  |
| AND | [NOT EXISTS (SELECT *](AND.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.on_order_units = a.on_order_units + b.on_order_units,](SET_a_on_order_units_=_a_on_order_units_+_b.on_order_units,.md) |  |
| FROM | [oo_all_group_loc_li a,](FROM.oo_all_group_loc_li_a,.md) |  |
| WHERE | [a.hierarchy_group_id BETWEEN @from_group_id AND @to_group_id](WHERE_a.hierarchy_group_id_BETWEEN_@from_group_id_AND_@to_group_id.md) |  |
| AND | [a.hierarchy_group_id = b.hierarchy_group_id](AND_a_hierarchy_group_id_=_b.hierarchy_group_id.md) |  |
| AND | [a.location_id = b.location_id](AND_a_location_id_=_b.location_id.md) |  |
| SELECT | [a.hierarchy_group_id,](SELECT_a.hierarchy_group_id,.md) |  |
| FROM | [#group_loc_li a](FROM.#group_loc_li_a.md) |  |
| WHERE | [a.hierarchy_group_id BETWEEN @from_group_id AND @to_group_id](WHERE_a.hierarchy_group_id_BETWEEN_@from_group_id_AND_@to_group_id.md) |  |
| AND | [NOT EXISTS (SELECT *](AND.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.on_order_units = a.on_order_units + b.on_order_units,](SET_a_on_order_units_=_a_on_order_units_+_b.on_order_units,.md) |  |
| FROM | [oo_all_group_chn_li a,](FROM.oo_all_group_chn_li_a,.md) |  |
| WHERE | [a.hierarchy_group_id BETWEEN @from_group_id AND @to_group_id](WHERE_a.hierarchy_group_id_BETWEEN_@from_group_id_AND_@to_group_id.md) |  |
| AND | [a.hierarchy_group_id = b.hierarchy_group_id](AND_a_hierarchy_group_id_=_b.hierarchy_group_id.md) |  |
| SELECT | [a.hierarchy_group_id,](SELECT_a.hierarchy_group_id,.md) |  |
| FROM | [#group_chn_li a](FROM.#group_chn_li_a.md) |  |
| WHERE | [a.hierarchy_group_id BETWEEN @from_group_id AND @to_group_id](WHERE_a.hierarchy_group_id_BETWEEN_@from_group_id_AND_@to_group_id.md) |  |
| AND | [NOT EXISTS (SELECT *](AND.NOT_EXISTS_SELECT.md) |  |
| FROM | [post_oo_all_group_sum a, plan_exp_table_group](FROM.post_oo_all_group_sum_a,_plan_exp_table_group.md) |  |
| WHERE | [a.hierarchy_group_id BETWEEN @from_group_id AND @to_group_id](WHERE_a.hierarchy_group_id_BETWEEN_@from_group_id_AND_@to_group_id.md) |  |
| AND | [plan_exp_table_group_id = 4;](AND.plan_exp_table_group_id_=_4;.md) |  |
| DELETE | [post_oo_all_group_sum](DELETE.post_oo_all_group_sum.md) |  |
| WHERE | [hierarchy_group_id BETWEEN @from_group_id AND @to_group_id](WHERE.hierarchy_group_id_BETWEEN_@from_group_id_AND_@to_group_id.md) |  |
| dbo | [post_oo_all_sku_$sp](dbo.post_oo_all_sku_$sp.md) | dbo.a, dbo.calendar_merch_week, dbo.oo_all_sku_chn_li, dbo.oo_all_sku_chn_pd, dbo.oo_all_sku_chn_wk, dbo.oo_all_sku_chn_yr, dbo.oo_all_sku_loc_li, dbo.oo_all_sku_loc_pd, dbo.oo_all_sku_loc_wk, dbo.oo_all_sku_loc_yr, dbo.post_oo_all_sku_sum, dbo.sku |
| on_order_units | [int  NOT NULL,](on_order_units.int_NOT_NULL,.md) |  |
| on_order_units | [int  NOT NULL,](on_order_units.int_NOT_NULL,.md) |  |
| on_order_units | [int  NOT NULL,](on_order_units.int_NOT_NULL,.md) |  |
| on_order_units | [int  NOT NULL,](on_order_units.int_NOT_NULL,.md) |  |
| on_order_units | [int  NOT NULL,](on_order_units.int_NOT_NULL,.md) |  |
| on_order_units | [int  NOT NULL,](on_order_units.int_NOT_NULL,.md) |  |
| on_order_units | [int  NOT NULL,](on_order_units.int_NOT_NULL,.md) |  |
| on_order_units | [int  NOT NULL,](on_order_units.int_NOT_NULL,.md) |  |
| SELECT | [b.style_id,](SELECT_b.style_id,.md) |  |
| dbo | [post_oo_all_style_$sp](dbo.post_oo_all_style_$sp.md) | dbo.a, dbo.calendar_merch_week, dbo.oo_all_style_chn_li, dbo.oo_all_style_chn_pd, dbo.oo_all_style_chn_wk, dbo.oo_all_style_chn_yr, dbo.oo_all_style_loc_li, dbo.oo_all_style_loc_pd, dbo.oo_all_style_loc_wk, dbo.oo_all_style_loc_yr, dbo.post_oo_all_style_sum |
| style_id                    decimal(12,0) | [NOT NULL,](style_id_decimal_12,0_.NOT_NULL,.md) |  |
| on_order_units | [int](on_order_units.int.md) |  |
| on_order_retail | [decimal(14,2)](on_order_retail.decimal_14,2.md) |  |
| on_order_cost | [decimal(14,2)](on_order_cost.decimal_14,2.md) |  |
| on_order_retail_te | [decimal(14,2) NULL)](on_order_retail_te.decimal_14,2_NULL.md) |  |
| style_id                    decimal(12,0) | [NOT NULL,](style_id_decimal_12,0_.NOT_NULL,.md) |  |
| on_order_units | [int](on_order_units.int.md) |  |
| on_order_retail | [decimal(14,2)](on_order_retail.decimal_14,2.md) |  |
| on_order_cost | [decimal(14,2)](on_order_cost.decimal_14,2.md) |  |
| on_order_retail_te | [decimal(14,2) NULL)](on_order_retail_te.decimal_14,2_NULL.md) |  |
| style_id                    decimal(12,0) | [NOT NULL,](style_id_decimal_12,0_.NOT_NULL,.md) |  |
| on_order_units | [int](on_order_units.int.md) |  |
| on_order_retail | [decimal(14,2)](on_order_retail.decimal_14,2.md) |  |
| on_order_cost | [decimal(14,2)](on_order_cost.decimal_14,2.md) |  |
| on_order_retail_te | [decimal(14,2) NULL)](on_order_retail_te.decimal_14,2_NULL.md) |  |
| style_id                    decimal(12,0) | [NOT NULL,](style_id_decimal_12,0_.NOT_NULL,.md) |  |
| on_order_units | [int](on_order_units.int.md) |  |
| on_order_retail | [decimal(14,2)](on_order_retail.decimal_14,2.md) |  |
| on_order_cost | [decimal(14,2)](on_order_cost.decimal_14,2.md) |  |
| on_order_retail_te | [decimal(14,2) NULL)](on_order_retail_te.decimal_14,2_NULL.md) |  |
| style_id                    decimal(12,0) | [NOT NULL,](style_id_decimal_12,0_.NOT_NULL,.md) |  |
| on_order_units | [int](on_order_units.int.md) |  |
| on_order_retail | [decimal(14,2)](on_order_retail.decimal_14,2.md) |  |
| on_order_cost | [decimal(14,2)](on_order_cost.decimal_14,2.md) |  |
| on_order_retail_te | [decimal(14,2) NULL)](on_order_retail_te.decimal_14,2_NULL.md) |  |
| style_id                    decimal(12,0) | [NOT NULL,](style_id_decimal_12,0_.NOT_NULL,.md) |  |
| on_order_units | [int](on_order_units.int.md) |  |
| on_order_retail | [decimal(14,2)](on_order_retail.decimal_14,2.md) |  |
| on_order_cost | [decimal(14,2)](on_order_cost.decimal_14,2.md) |  |
| on_order_retail_te | [decimal(14,2) NULL)](on_order_retail_te.decimal_14,2_NULL.md) |  |
| style_id                    decimal(12,0) | [NOT NULL,](style_id_decimal_12,0_.NOT_NULL,.md) |  |
| on_order_units | [int](on_order_units.int.md) |  |
| on_order_retail | [decimal(14,2)](on_order_retail.decimal_14,2.md) |  |
| on_order_cost | [decimal(14,2)](on_order_cost.decimal_14,2.md) |  |
| on_order_retail_te | [decimal(14,2) NULL)](on_order_retail_te.decimal_14,2_NULL.md) |  |
| style_id                    decimal(12,0) | [NOT NULL,](style_id_decimal_12,0_.NOT_NULL,.md) |  |
| on_order_units | [int](on_order_units.int.md) |  |
| on_order_retail | [decimal(14,2)](on_order_retail.decimal_14,2.md) |  |
| on_order_cost | [decimal(14,2)](on_order_cost.decimal_14,2.md) |  |
| on_order_retail_te | [decimal(14,2) NULL)](on_order_retail_te.decimal_14,2_NULL.md) |  |
| INSERT | [#style_loc_wk](INSERT.#style_loc_wk.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [post_oo_all_style_sum](FROM.post_oo_all_style_sum.md) |  |
| WHERE | [style_id BETWEEN @from_style_id AND @to_style_id](WHERE.style_id_BETWEEN_@from_style_id_AND_@to_style_id.md) |  |
| INSERT | [#style_chn_wk](INSERT.#style_chn_wk.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [post_oo_all_style_sum](FROM.post_oo_all_style_sum.md) |  |
| WHERE | [style_id BETWEEN @from_style_id AND @to_style_id](WHERE.style_id_BETWEEN_@from_style_id_AND_@to_style_id.md) |  |
| INSERT | [#style_loc_pd](INSERT.#style_loc_pd.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [post_oo_all_style_sum a,](FROM.post_oo_all_style_sum_a,.md) |  |
| WHERE | [a.style_id BETWEEN @from_style_id AND @to_style_id](WHERE_a.style_id_BETWEEN_@from_style_id_AND_@to_style_id.md) |  |
| AND | [a.merch_year_wk / 100 = c.merch_year](AND_a_merch_year_wk_100_=_c.merch_year.md) |  |
| AND | [a.merch_year_wk % 100 = c.merch_week](AND_a_merch_year_wk_%_100_=_c.merch_week.md) |  |
| INSERT | [#style_chn_pd](INSERT.#style_chn_pd.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [post_oo_all_style_sum a,](FROM.post_oo_all_style_sum_a,.md) |  |
| WHERE | [a.style_id BETWEEN @from_style_id AND @to_style_id](WHERE_a.style_id_BETWEEN_@from_style_id_AND_@to_style_id.md) |  |
| AND | [a.merch_year_wk / 100 = c.merch_year](AND_a_merch_year_wk_100_=_c.merch_year.md) |  |
| AND | [a.merch_year_wk % 100 = c.merch_week](AND_a_merch_year_wk_%_100_=_c.merch_week.md) |  |
| INSERT | [#style_loc_yr](INSERT.#style_loc_yr.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [post_oo_all_style_sum](FROM.post_oo_all_style_sum.md) |  |
| WHERE | [style_id BETWEEN @from_style_id AND @to_style_id](WHERE.style_id_BETWEEN_@from_style_id_AND_@to_style_id.md) |  |
| INSERT | [#style_chn_yr](INSERT.#style_chn_yr.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [post_oo_all_style_sum](FROM.post_oo_all_style_sum.md) |  |
| WHERE | [style_id BETWEEN @from_style_id AND @to_style_id](WHERE.style_id_BETWEEN_@from_style_id_AND_@to_style_id.md) |  |
| INSERT | [#style_loc_li](INSERT.#style_loc_li.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [post_oo_all_style_sum](FROM.post_oo_all_style_sum.md) |  |
| WHERE | [style_id BETWEEN @from_style_id AND @to_style_id](WHERE.style_id_BETWEEN_@from_style_id_AND_@to_style_id.md) |  |
| INSERT | [#style_chn_li](INSERT.#style_chn_li.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [post_oo_all_style_sum](FROM.post_oo_all_style_sum.md) |  |
| WHERE | [style_id BETWEEN @from_style_id AND @to_style_id](WHERE.style_id_BETWEEN_@from_style_id_AND_@to_style_id.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.on_order_units = a.on_order_units + b.on_order_units,](SET_a_on_order_units_=_a_on_order_units_+_b.on_order_units,.md) |  |
| FROM | [oo_all_style_loc_wk a,](FROM.oo_all_style_loc_wk_a,.md) |  |
| WHERE | [a.style_id BETWEEN @from_style_id AND @to_style_id](WHERE_a.style_id_BETWEEN_@from_style_id_AND_@to_style_id.md) |  |
| AND | [b.style_id BETWEEN @from_style_id AND @to_style_id](AND_b.style_id_BETWEEN_@from_style_id_AND_@to_style_id.md) |  |
| AND | [a.style_id = b.style_id](AND_a_style_id_=_b.style_id.md) |  |
| AND | [a.merch_year_wk = b.merch_year_wk](AND_a_merch_year_wk_=_b.merch_year_wk.md) |  |
| AND | [a.location_id = b.location_id](AND_a_location_id_=_b.location_id.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [#style_loc_wk a](FROM.#style_loc_wk_a.md) |  |
| WHERE | [a.style_id BETWEEN @from_style_id AND @to_style_id](WHERE_a.style_id_BETWEEN_@from_style_id_AND_@to_style_id.md) |  |
| AND | [NOT EXISTS (SELECT *](AND.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.on_order_units = a.on_order_units + b.on_order_units,](SET_a_on_order_units_=_a_on_order_units_+_b.on_order_units,.md) |  |
| FROM | [oo_all_style_chn_wk a,](FROM.oo_all_style_chn_wk_a,.md) |  |
| WHERE | [a.style_id BETWEEN @from_style_id AND @to_style_id](WHERE_a.style_id_BETWEEN_@from_style_id_AND_@to_style_id.md) |  |
| AND | [b.style_id BETWEEN @from_style_id AND @to_style_id](AND_b.style_id_BETWEEN_@from_style_id_AND_@to_style_id.md) |  |
| AND | [a.style_id = b.style_id](AND_a_style_id_=_b.style_id.md) |  |
| AND | [a.merch_year_wk = b.merch_year_wk](AND_a_merch_year_wk_=_b.merch_year_wk.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [#style_chn_wk a](FROM.#style_chn_wk_a.md) |  |
| WHERE | [a.style_id BETWEEN @from_style_id AND @to_style_id](WHERE_a.style_id_BETWEEN_@from_style_id_AND_@to_style_id.md) |  |
| AND | [NOT EXISTS (SELECT *](AND.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.on_order_units = a.on_order_units + b.on_order_units,](SET_a_on_order_units_=_a_on_order_units_+_b.on_order_units,.md) |  |
| FROM | [oo_all_style_loc_pd a,](FROM.oo_all_style_loc_pd_a,.md) |  |
| WHERE | [a.style_id BETWEEN @from_style_id AND @to_style_id](WHERE_a.style_id_BETWEEN_@from_style_id_AND_@to_style_id.md) |  |
| AND | [b.style_id BETWEEN @from_style_id AND @to_style_id](AND_b.style_id_BETWEEN_@from_style_id_AND_@to_style_id.md) |  |
| AND | [a.style_id = b.style_id](AND_a_style_id_=_b.style_id.md) |  |
| AND | [a.merch_year_pd = b.merch_year_pd](AND_a_merch_year_pd_=_b.merch_year_pd.md) |  |
| AND | [a.location_id = b.location_id](AND_a_location_id_=_b.location_id.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [#style_loc_pd a](FROM.#style_loc_pd_a.md) |  |
| WHERE | [a.style_id BETWEEN @from_style_id AND @to_style_id](WHERE_a.style_id_BETWEEN_@from_style_id_AND_@to_style_id.md) |  |
| AND | [NOT EXISTS (SELECT *](AND.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.on_order_units = a.on_order_units + b.on_order_units,](SET_a_on_order_units_=_a_on_order_units_+_b.on_order_units,.md) |  |
| FROM | [oo_all_style_chn_pd a,](FROM.oo_all_style_chn_pd_a,.md) |  |
| WHERE | [a.style_id BETWEEN @from_style_id AND @to_style_id](WHERE_a.style_id_BETWEEN_@from_style_id_AND_@to_style_id.md) |  |
| AND | [b.style_id BETWEEN @from_style_id AND @to_style_id](AND_b.style_id_BETWEEN_@from_style_id_AND_@to_style_id.md) |  |
| AND | [a.style_id = b.style_id](AND_a_style_id_=_b.style_id.md) |  |
| AND | [a.merch_year_pd = b.merch_year_pd](AND_a_merch_year_pd_=_b.merch_year_pd.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [#style_chn_pd a](FROM.#style_chn_pd_a.md) |  |
| WHERE | [a.style_id BETWEEN @from_style_id AND @to_style_id](WHERE_a.style_id_BETWEEN_@from_style_id_AND_@to_style_id.md) |  |
| AND | [NOT EXISTS (SELECT *](AND.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.on_order_units = a.on_order_units + b.on_order_units,](SET_a_on_order_units_=_a_on_order_units_+_b.on_order_units,.md) |  |
| FROM | [oo_all_style_loc_yr a,](FROM.oo_all_style_loc_yr_a,.md) |  |
| WHERE | [a.style_id BETWEEN @from_style_id AND @to_style_id](WHERE_a.style_id_BETWEEN_@from_style_id_AND_@to_style_id.md) |  |
| AND | [b.style_id BETWEEN @from_style_id AND @to_style_id](AND_b.style_id_BETWEEN_@from_style_id_AND_@to_style_id.md) |  |
| AND | [a.style_id = b.style_id](AND_a_style_id_=_b.style_id.md) |  |
| AND | [a.merch_year = b.merch_year](AND_a_merch_year_=_b.merch_year.md) |  |
| AND | [a.location_id = b.location_id](AND_a_location_id_=_b.location_id.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [#style_loc_yr a](FROM.#style_loc_yr_a.md) |  |
| WHERE | [a.style_id BETWEEN @from_style_id AND @to_style_id](WHERE_a.style_id_BETWEEN_@from_style_id_AND_@to_style_id.md) |  |
| AND | [NOT EXISTS (SELECT *](AND.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.on_order_units = a.on_order_units + b.on_order_units,](SET_a_on_order_units_=_a_on_order_units_+_b.on_order_units,.md) |  |
| FROM | [oo_all_style_chn_yr a,](FROM.oo_all_style_chn_yr_a,.md) |  |
| WHERE | [a.style_id BETWEEN @from_style_id AND @to_style_id](WHERE_a.style_id_BETWEEN_@from_style_id_AND_@to_style_id.md) |  |
| AND | [b.style_id BETWEEN @from_style_id AND @to_style_id](AND_b.style_id_BETWEEN_@from_style_id_AND_@to_style_id.md) |  |
| AND | [a.style_id = b.style_id](AND_a_style_id_=_b.style_id.md) |  |
| AND | [a.merch_year = b.merch_year](AND_a_merch_year_=_b.merch_year.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [#style_chn_yr a](FROM.#style_chn_yr_a.md) |  |
| WHERE | [a.style_id BETWEEN @from_style_id AND @to_style_id](WHERE_a.style_id_BETWEEN_@from_style_id_AND_@to_style_id.md) |  |
| AND | [NOT EXISTS (SELECT *](AND.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.on_order_units = a.on_order_units + b.on_order_units,](SET_a_on_order_units_=_a_on_order_units_+_b.on_order_units,.md) |  |
| FROM | [oo_all_style_loc_li a,](FROM.oo_all_style_loc_li_a,.md) |  |
| WHERE | [a.style_id BETWEEN @from_style_id AND @to_style_id](WHERE_a.style_id_BETWEEN_@from_style_id_AND_@to_style_id.md) |  |
| AND | [b.style_id BETWEEN @from_style_id AND @to_style_id](AND_b.style_id_BETWEEN_@from_style_id_AND_@to_style_id.md) |  |
| AND | [a.style_id = b.style_id](AND_a_style_id_=_b.style_id.md) |  |
| AND | [a.location_id = b.location_id](AND_a_location_id_=_b.location_id.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [#style_loc_li a](FROM.#style_loc_li_a.md) |  |
| WHERE | [a.style_id BETWEEN @from_style_id AND @to_style_id](WHERE_a.style_id_BETWEEN_@from_style_id_AND_@to_style_id.md) |  |
| AND | [NOT EXISTS (SELECT *](AND.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.on_order_units = a.on_order_units + b.on_order_units,](SET_a_on_order_units_=_a_on_order_units_+_b.on_order_units,.md) |  |
| FROM | [oo_all_style_chn_li a,](FROM.oo_all_style_chn_li_a,.md) |  |
| WHERE | [a.style_id BETWEEN @from_style_id AND @to_style_id](WHERE_a.style_id_BETWEEN_@from_style_id_AND_@to_style_id.md) |  |
| AND | [b.style_id BETWEEN @from_style_id AND @to_style_id](AND_b.style_id_BETWEEN_@from_style_id_AND_@to_style_id.md) |  |
| AND | [a.style_id = b.style_id](AND_a_style_id_=_b.style_id.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [#style_chn_li a](FROM.#style_chn_li_a.md) |  |
| WHERE | [a.style_id BETWEEN @from_style_id AND @to_style_id](WHERE_a.style_id_BETWEEN_@from_style_id_AND_@to_style_id.md) |  |
| AND | [NOT EXISTS (SELECT *](AND.NOT_EXISTS_SELECT.md) |  |
| DELETE | [post_oo_all_style_sum](DELETE.post_oo_all_style_sum.md) |  |
| WHERE | [style_id BETWEEN @from_style_id AND @to_style_id](WHERE.style_id_BETWEEN_@from_style_id_AND_@to_style_id.md) |  |
| dbo | [post_oo_all_styleclr_$sp](dbo.post_oo_all_styleclr_$sp.md) | dbo.a, dbo.calendar_merch_week, dbo.oo_all_styleclr_chn_li, dbo.oo_all_styleclr_chn_pd, dbo.oo_all_styleclr_chn_wk, dbo.oo_all_styleclr_chn_yr, dbo.oo_all_styleclr_loc_li, dbo.oo_all_styleclr_loc_pd, dbo.oo_all_styleclr_loc_wk, dbo.oo_all_styleclr_loc_yr, dbo.post_oo_all_styleclr_sum |
| create proc dbo.post_oo_all_styleclr_$sp | [@curr_style_id decimal(12,0),](create_proc_dbo_post_oo_all_styleclr_$sp.@curr_style_id_decimal_12,0_,.md) |  |
| style_id                    decimal(12,0) | [NOT NULL,](style_id_decimal_12,0_.NOT_NULL,.md) |  |
| on_order_units | [int](on_order_units.int.md) |  |
| on_order_retail | [decimal(14,2)](on_order_retail.decimal_14,2.md) |  |
| on_order_retail_te | [decimal(14,2) NULL)](on_order_retail_te.decimal_14,2_NULL.md) |  |
| style_id                    decimal(12,0) | [NOT NULL,](style_id_decimal_12,0_.NOT_NULL,.md) |  |
| on_order_units | [int](on_order_units.int.md) |  |
| on_order_retail | [decimal(14,2)](on_order_retail.decimal_14,2.md) |  |
| on_order_retail_te | [decimal(14,2) NULL)](on_order_retail_te.decimal_14,2_NULL.md) |  |
| style_id                    decimal(12,0) | [NOT NULL,](style_id_decimal_12,0_.NOT_NULL,.md) |  |
| on_order_units | [int](on_order_units.int.md) |  |
| on_order_retail | [decimal(14,2)](on_order_retail.decimal_14,2.md) |  |
| on_order_retail_te | [decimal(14,2) NULL)](on_order_retail_te.decimal_14,2_NULL.md) |  |
| style_id                    decimal(12,0) | [NOT NULL,](style_id_decimal_12,0_.NOT_NULL,.md) |  |
| on_order_units | [int](on_order_units.int.md) |  |
| on_order_retail | [decimal(14,2)](on_order_retail.decimal_14,2.md) |  |
| on_order_retail_te | [decimal(14,2) NULL)](on_order_retail_te.decimal_14,2_NULL.md) |  |
| style_id                    decimal(12,0) | [NOT NULL,](style_id_decimal_12,0_.NOT_NULL,.md) |  |
| on_order_units | [int](on_order_units.int.md) |  |
| on_order_retail | [decimal(14,2)](on_order_retail.decimal_14,2.md) |  |
| on_order_retail_te | [decimal(14,2) NULL)](on_order_retail_te.decimal_14,2_NULL.md) |  |
| style_id                    decimal(12,0) | [NOT NULL,](style_id_decimal_12,0_.NOT_NULL,.md) |  |
| on_order_units | [int](on_order_units.int.md) |  |
| on_order_retail | [decimal(14,2)](on_order_retail.decimal_14,2.md) |  |
| on_order_retail_te | [decimal(14,2) NULL)](on_order_retail_te.decimal_14,2_NULL.md) |  |
| style_id                    decimal(12,0) | [NOT NULL,](style_id_decimal_12,0_.NOT_NULL,.md) |  |
| on_order_units | [int](on_order_units.int.md) |  |
| on_order_retail | [decimal(14,2)](on_order_retail.decimal_14,2.md) |  |
| on_order_retail_te | [decimal(14,2) NULL)](on_order_retail_te.decimal_14,2_NULL.md) |  |
| style_id                    decimal(12,0) | [NOT NULL,](style_id_decimal_12,0_.NOT_NULL,.md) |  |
| on_order_units | [int](on_order_units.int.md) |  |
| on_order_retail | [decimal(14,2)](on_order_retail.decimal_14,2.md) |  |
| on_order_retail_te | [decimal(14,2) NULL)](on_order_retail_te.decimal_14,2_NULL.md) |  |
| INSERT | [#styleclr_loc_wk](INSERT.#styleclr_loc_wk.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [post_oo_all_styleclr_sum](FROM.post_oo_all_styleclr_sum.md) |  |
| WHERE | [style_id BETWEEN @curr_style_id AND @curr_style_id_2](WHERE.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| INSERT | [#styleclr_chn_wk](INSERT.#styleclr_chn_wk.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [post_oo_all_styleclr_sum](FROM.post_oo_all_styleclr_sum.md) |  |
| WHERE | [style_id BETWEEN @curr_style_id AND @curr_style_id_2](WHERE.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| INSERT | [#styleclr_loc_pd](INSERT.#styleclr_loc_pd.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [post_oo_all_styleclr_sum a,](FROM.post_oo_all_styleclr_sum_a,.md) |  |
| WHERE | [a.style_id BETWEEN @curr_style_id AND @curr_style_id_2](WHERE_a.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| AND | [a.merch_year_wk / 100 = c.merch_year](AND_a_merch_year_wk_100_=_c.merch_year.md) |  |
| AND | [a.merch_year_wk % 100 = c.merch_week](AND_a_merch_year_wk_%_100_=_c.merch_week.md) |  |
| INSERT | [#styleclr_chn_pd](INSERT.#styleclr_chn_pd.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [post_oo_all_styleclr_sum a,](FROM.post_oo_all_styleclr_sum_a,.md) |  |
| WHERE | [a.style_id BETWEEN @curr_style_id AND @curr_style_id_2](WHERE_a.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| AND | [a.merch_year_wk / 100 = c.merch_year](AND_a_merch_year_wk_100_=_c.merch_year.md) |  |
| AND | [a.merch_year_wk % 100 = c.merch_week](AND_a_merch_year_wk_%_100_=_c.merch_week.md) |  |
| INSERT | [#styleclr_loc_yr](INSERT.#styleclr_loc_yr.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [post_oo_all_styleclr_sum](FROM.post_oo_all_styleclr_sum.md) |  |
| WHERE | [style_id BETWEEN @curr_style_id AND @curr_style_id_2](WHERE.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| INSERT | [#styleclr_chn_yr](INSERT.#styleclr_chn_yr.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [post_oo_all_styleclr_sum](FROM.post_oo_all_styleclr_sum.md) |  |
| WHERE | [style_id BETWEEN @curr_style_id AND @curr_style_id_2](WHERE.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| INSERT | [#styleclr_loc_li](INSERT.#styleclr_loc_li.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [post_oo_all_styleclr_sum](FROM.post_oo_all_styleclr_sum.md) |  |
| WHERE | [style_id BETWEEN @curr_style_id AND @curr_style_id_2](WHERE.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| INSERT | [#styleclr_chn_li](INSERT.#styleclr_chn_li.md) |  |
| SELECT | [style_id,](SELECT.style_id,.md) |  |
| FROM | [post_oo_all_styleclr_sum](FROM.post_oo_all_styleclr_sum.md) |  |
| WHERE | [style_id BETWEEN @curr_style_id AND @curr_style_id_2](WHERE.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.on_order_units = a.on_order_units + b.on_order_units,](SET_a_on_order_units_=_a_on_order_units_+_b.on_order_units,.md) |  |
| FROM | [oo_all_styleclr_loc_wk a,](FROM.oo_all_styleclr_loc_wk_a,.md) |  |
| WHERE | [a.style_id BETWEEN @curr_style_id AND @curr_style_id_2](WHERE_a.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| AND | [a.style_id = b.style_id](AND_a_style_id_=_b.style_id.md) |  |
| AND | [a.color_id = b.color_id](AND_a_color_id_=_b.color_id.md) |  |
| AND | [a.merch_year_wk = b.merch_year_wk](AND_a_merch_year_wk_=_b.merch_year_wk.md) |  |
| AND | [a.location_id = b.location_id](AND_a_location_id_=_b.location_id.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [#styleclr_loc_wk a](FROM.#styleclr_loc_wk_a.md) |  |
| WHERE | [a.style_id BETWEEN @curr_style_id AND @curr_style_id_2](WHERE_a.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| AND | [NOT EXISTS (SELECT](AND.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.on_order_units = a.on_order_units + b.on_order_units,](SET_a_on_order_units_=_a_on_order_units_+_b.on_order_units,.md) |  |
| FROM | [oo_all_styleclr_chn_wk a,](FROM.oo_all_styleclr_chn_wk_a,.md) |  |
| WHERE | [a.style_id BETWEEN @curr_style_id AND @curr_style_id_2](WHERE_a.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| AND | [a.style_id = b.style_id](AND_a_style_id_=_b.style_id.md) |  |
| AND | [a.color_id = b.color_id](AND_a_color_id_=_b.color_id.md) |  |
| AND | [a.merch_year_wk = b.merch_year_wk](AND_a_merch_year_wk_=_b.merch_year_wk.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [#styleclr_chn_wk a](FROM.#styleclr_chn_wk_a.md) |  |
| WHERE | [a.style_id BETWEEN @curr_style_id AND @curr_style_id_2](WHERE_a.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| AND | [NOT EXISTS (SELECT](AND.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.on_order_units = a.on_order_units + b.on_order_units,](SET_a_on_order_units_=_a_on_order_units_+_b.on_order_units,.md) |  |
| FROM | [oo_all_styleclr_loc_pd a,](FROM.oo_all_styleclr_loc_pd_a,.md) |  |
| WHERE | [a.style_id BETWEEN @curr_style_id AND @curr_style_id_2](WHERE_a.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| AND | [a.style_id = b.style_id](AND_a_style_id_=_b.style_id.md) |  |
| AND | [a.color_id = b.color_id](AND_a_color_id_=_b.color_id.md) |  |
| AND | [a.merch_year_pd = b.merch_year_pd](AND_a_merch_year_pd_=_b.merch_year_pd.md) |  |
| AND | [a.location_id = b.location_id](AND_a_location_id_=_b.location_id.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [#styleclr_loc_pd a](FROM.#styleclr_loc_pd_a.md) |  |
| WHERE | [a.style_id BETWEEN @curr_style_id AND @curr_style_id_2](WHERE_a.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| AND | [NOT EXISTS (SELECT](AND.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.on_order_units = a.on_order_units + b.on_order_units,](SET_a_on_order_units_=_a_on_order_units_+_b.on_order_units,.md) |  |
| FROM | [oo_all_styleclr_chn_pd a,](FROM.oo_all_styleclr_chn_pd_a,.md) |  |
| WHERE | [a.style_id BETWEEN @curr_style_id AND @curr_style_id_2](WHERE_a.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| AND | [a.style_id = b.style_id](AND_a_style_id_=_b.style_id.md) |  |
| AND | [a.color_id = b.color_id](AND_a_color_id_=_b.color_id.md) |  |
| AND | [a.merch_year_pd = b.merch_year_pd](AND_a_merch_year_pd_=_b.merch_year_pd.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [#styleclr_chn_pd a](FROM.#styleclr_chn_pd_a.md) |  |
| WHERE | [a.style_id BETWEEN @curr_style_id AND @curr_style_id_2](WHERE_a.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| AND | [NOT EXISTS (SELECT](AND.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.on_order_units = a.on_order_units + b.on_order_units,](SET_a_on_order_units_=_a_on_order_units_+_b.on_order_units,.md) |  |
| FROM | [oo_all_styleclr_loc_yr a,](FROM.oo_all_styleclr_loc_yr_a,.md) |  |
| WHERE | [a.style_id BETWEEN @curr_style_id AND @curr_style_id_2](WHERE_a.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| AND | [a.style_id = b.style_id](AND_a_style_id_=_b.style_id.md) |  |
| AND | [a.color_id = b.color_id](AND_a_color_id_=_b.color_id.md) |  |
| AND | [a.merch_year = b.merch_year](AND_a_merch_year_=_b.merch_year.md) |  |
| AND | [a.location_id = b.location_id](AND_a_location_id_=_b.location_id.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [#styleclr_loc_yr a](FROM.#styleclr_loc_yr_a.md) |  |
| WHERE | [a.style_id BETWEEN @curr_style_id AND @curr_style_id_2](WHERE_a.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| AND | [NOT EXISTS (SELECT](AND.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.on_order_units = a.on_order_units + b.on_order_units,](SET_a_on_order_units_=_a_on_order_units_+_b.on_order_units,.md) |  |
| FROM | [oo_all_styleclr_chn_yr a,](FROM.oo_all_styleclr_chn_yr_a,.md) |  |
| WHERE | [a.style_id BETWEEN @curr_style_id AND @curr_style_id_2](WHERE_a.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| AND | [a.style_id = b.style_id](AND_a_style_id_=_b.style_id.md) |  |
| AND | [a.color_id = b.color_id](AND_a_color_id_=_b.color_id.md) |  |
| AND | [a.merch_year = b.merch_year](AND_a_merch_year_=_b.merch_year.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [#styleclr_chn_yr a](FROM.#styleclr_chn_yr_a.md) |  |
| WHERE | [a.style_id BETWEEN @curr_style_id AND @curr_style_id_2](WHERE_a.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| AND | [NOT EXISTS (SELECT](AND.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.on_order_units = a.on_order_units + b.on_order_units,](SET_a_on_order_units_=_a_on_order_units_+_b.on_order_units,.md) |  |
| FROM | [oo_all_styleclr_loc_li a,](FROM.oo_all_styleclr_loc_li_a,.md) |  |
| WHERE | [a.style_id BETWEEN @curr_style_id AND @curr_style_id_2](WHERE_a.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| AND | [a.style_id = b.style_id](AND_a_style_id_=_b.style_id.md) |  |
| AND | [a.color_id = b.color_id](AND_a_color_id_=_b.color_id.md) |  |
| AND | [a.location_id = b.location_id](AND_a_location_id_=_b.location_id.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [#styleclr_loc_li a](FROM.#styleclr_loc_li_a.md) |  |
| WHERE | [a.style_id BETWEEN @curr_style_id AND @curr_style_id_2](WHERE_a.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| AND | [NOT EXISTS (SELECT](AND.NOT_EXISTS_SELECT.md) |  |
| UPDATE | [a](UPDATE.a.md) |  |
| SET | [a.on_order_units = a.on_order_units + b.on_order_units,](SET_a_on_order_units_=_a_on_order_units_+_b.on_order_units,.md) |  |
| FROM | [oo_all_styleclr_chn_li a,](FROM.oo_all_styleclr_chn_li_a,.md) |  |
| WHERE | [a.style_id BETWEEN @curr_style_id AND @curr_style_id_2](WHERE_a.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| AND | [a.style_id = b.style_id](AND_a_style_id_=_b.style_id.md) |  |
| AND | [a.color_id = b.color_id](AND_a_color_id_=_b.color_id.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [#styleclr_chn_li a](FROM.#styleclr_chn_li_a.md) |  |
| WHERE | [a.style_id BETWEEN @curr_style_id AND @curr_style_id_2](WHERE_a.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| AND | [NOT EXISTS (SELECT](AND.NOT_EXISTS_SELECT.md) |  |
| DELETE | [post_oo_all_styleclr_sum](DELETE.post_oo_all_styleclr_sum.md) |  |
| WHERE | [style_id BETWEEN @curr_style_id AND @curr_style_id_2](WHERE.style_id_BETWEEN_@curr_style_id_AND_@curr_style_id_2.md) |  |
| dbo | [post_oo_group_$sp](dbo.post_oo_group_$sp.md) | dbo.calendar_merch_week, dbo.job_detail, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.oo_all_group_chn_li, dbo.oo_all_group_chn_pd, dbo.oo_all_group_chn_wk, dbo.oo_all_group_chn_yr, dbo.oo_all_group_loc_li, dbo.oo_all_group_loc_pd, dbo.oo_all_group_loc_wk, dbo.oo_all_group_loc_yr, dbo.return_debug_flag_$sp, dbo.return_step_exists_$sp, dbo.wrk_oo_all_group_loc_wk |
| dbo | [post_oo_sku_$sp](dbo.post_oo_sku_$sp.md) | dbo.calendar_merch_week, dbo.job_detail, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.oo_all_sku_chn_li, dbo.oo_all_sku_chn_pd, dbo.oo_all_sku_chn_wk, dbo.oo_all_sku_chn_yr, dbo.oo_all_sku_loc_li, dbo.oo_all_sku_loc_pd, dbo.oo_all_sku_loc_wk, dbo.oo_all_sku_loc_yr, dbo.return_debug_flag_$sp, dbo.return_step_exists_$sp, dbo.wrk_oo_all_sku_loc_wk |
| dbo | [post_oo_style_$sp](dbo.post_oo_style_$sp.md) | dbo.calendar_merch_week, dbo.job_detail, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.oo_all_style_chn_li, dbo.oo_all_style_chn_pd, dbo.oo_all_style_chn_wk, dbo.oo_all_style_chn_yr, dbo.oo_all_style_loc_li, dbo.oo_all_style_loc_pd, dbo.oo_all_style_loc_wk, dbo.oo_all_style_loc_yr, dbo.return_debug_flag_$sp, dbo.return_step_exists_$sp, dbo.wrk_oo_all_style_loc_wk |
| dbo | [post_oo_style_color_$sp](dbo.post_oo_style_color_$sp.md) | dbo.calendar_merch_week, dbo.job_detail, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.oo_all_styleclr_chn_li, dbo.oo_all_styleclr_chn_pd, dbo.oo_all_styleclr_chn_wk, dbo.oo_all_styleclr_chn_yr, dbo.oo_all_styleclr_loc_li, dbo.oo_all_styleclr_loc_pd, dbo.oo_all_styleclr_loc_wk, dbo.oo_all_styleclr_loc_yr, dbo.return_debug_flag_$sp, dbo.return_step_exists_$sp, dbo.wrk_oo_all_styleclr_loc_wk |
| dbo | [post_oo_unc_$sp](dbo.post_oo_unc_$sp.md) | dbo.calendar_date, dbo.calendar_merch_period, dbo.calendar_merch_week, dbo.country, dbo.hierarchy_group, dbo.jurisdiction, dbo.location, dbo.oo_unc_group_chn_li, dbo.oo_unc_group_chn_pd, dbo.oo_unc_group_chn_wk, dbo.oo_unc_group_chn_yr, dbo.oo_unc_group_loc_li, dbo.oo_unc_group_loc_pd, dbo.oo_unc_group_loc_wk, dbo.oo_unc_group_loc_yr, dbo.syn_currency_conversion |
| dbo | [post_wrk_ib_allocation_$sp](dbo.post_wrk_ib_allocation_$sp.md) | dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.syn_ib_allocation, dbo.syn_sku, dbo.syn_style_color, dbo.syn_style_group, dbo.syn_style_size, dbo.wrk_ib_all_style_alt_group, dbo.wrk_ib_allocation |
| dbo | [post_wrk_ib_cost_fact_disc_$sp](dbo.post_wrk_ib_cost_fact_disc_$sp.md) | dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.syn_ib_cost_factor_discount, dbo.syn_sku, dbo.syn_style_color, dbo.syn_style_group, dbo.syn_style_size, dbo.wrk_ib_cfd_style_alt_group, dbo.wrk_ib_cost_factor_discount |
| dbo | [post_wrk_ib_inventory_$sp](dbo.post_wrk_ib_inventory_$sp.md) | dbo.is_tax_exclusive_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.syn_ib_inventory, dbo.syn_ib_notax_retail_work, dbo.syn_sku, dbo.syn_style_color, dbo.syn_style_group, dbo.syn_style_size, dbo.wrk_ib_inventory, dbo.wrk_ib_iv_style_alt_group |
| dbo | [post_wrk_ib_inventory_org_$sp](dbo.post_wrk_ib_inventory_org_$sp.md) | dbo.is_tax_exclusive_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.syn_ib_inventory, dbo.syn_ib_notax_retail_work, dbo.syn_sku, dbo.syn_style_color, dbo.syn_style_group, dbo.syn_style_size, dbo.wrk_ib_inventory, dbo.wrk_ib_iv_style_alt_group |
| dbo | [post_wrk_ib_on_order_$sp](dbo.post_wrk_ib_on_order_$sp.md) | dbo.is_tax_exclusive_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.syn_ib_on_order, dbo.syn_ib_oo_notax_retail_work, dbo.syn_sku, dbo.syn_style_color, dbo.syn_style_group, dbo.syn_style_size, dbo.wrk_ib_on_order, dbo.wrk_ib_oo_style_alt_group |
| dbo | [prep_cmp_$sp](dbo.prep_cmp_$sp.md) | dbo.job_error_handler_$sp, dbo.job_progress_handler_$sp, dbo.posting_parameter, dbo.prep_cmp_group_$sp, dbo.prep_cmp_sku_$sp, dbo.prep_cmp_style_$sp, dbo.prep_cmp_style_color_$sp, dbo.return_debug_flag_$sp |
| dbo | [prep_cmp_group_$sp](dbo.prep_cmp_group_$sp.md) | dbo.get_job_params_$sp, dbo.get_last_range_end_phase2_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_cmp_group_loc_wk |
| dbo | [prep_cmp_sku_$sp](dbo.prep_cmp_sku_$sp.md) | dbo.get_job_params_$sp, dbo.get_last_range_end_phase2_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_cmp_sku_loc_wk |
| dbo | [prep_cmp_style_$sp](dbo.prep_cmp_style_$sp.md) | dbo.get_job_params_$sp, dbo.get_last_range_end_phase2_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_cmp_style_loc_wk |
| dbo | [prep_cmp_style_color_$sp](dbo.prep_cmp_style_color_$sp.md) | dbo.get_job_params_$sp, dbo.get_last_range_end_phase2_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_cmp_styleclr_loc_wk |
| dbo | [prep_flash_$sp](dbo.prep_flash_$sp.md) | dbo.job_error_handler_$sp, dbo.job_progress_handler_$sp, dbo.posting_parameter, dbo.prep_flash_group_$sp, dbo.prep_flash_style_$sp, dbo.return_debug_flag_$sp |
| dbo | [prep_flash_group_$sp](dbo.prep_flash_group_$sp.md) | dbo.get_job_params_$sp, dbo.get_last_range_end_phase2_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_flsh_group_loc_da |
| dbo | [prep_flash_style_$sp](dbo.prep_flash_style_$sp.md) | dbo.get_job_params_$sp, dbo.get_last_range_end_phase2_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_flsh_style_loc_da |
| dbo | [prep_hist_$sp](dbo.prep_hist_$sp.md) | dbo.job_error_handler_$sp, dbo.job_progress_handler_$sp, dbo.posting_parameter, dbo.prep_hist_group_$sp, dbo.prep_hist_sku_$sp, dbo.prep_hist_style_$sp, dbo.prep_hist_style_color_$sp, dbo.return_debug_flag_$sp |
| dbo | [prep_hist_group_$sp](dbo.prep_hist_group_$sp.md) | dbo.get_job_params_$sp, dbo.get_last_range_end_phase2_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_group_loc_wk |
| dbo | [prep_hist_sku_$sp](dbo.prep_hist_sku_$sp.md) | dbo.get_job_params_$sp, dbo.get_last_range_end_phase2_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_sku_loc_wk |
| dbo | [prep_hist_style_$sp](dbo.prep_hist_style_$sp.md) | dbo.get_job_params_$sp, dbo.get_last_range_end_phase2_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_style_loc_wk |
| dbo | [prep_hist_style_color_$sp](dbo.prep_hist_style_color_$sp.md) | dbo.get_job_params_$sp, dbo.get_last_range_end_phase2_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_styleclr_loc_wk |
| dbo | [prep_new_posting_$sp](dbo.prep_new_posting_$sp.md) | dbo.add_partitions_$sp, dbo.cleanup_wrk_ib_allocation_$sp, dbo.cleanup_wrk_ib_cost_factor_$sp, dbo.cleanup_wrk_ib_inventory_$sp, dbo.cleanup_wrk_ib_on_order_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.posting_parameter, dbo.return_debug_flag_$sp |
| dbo | [prep_oh_$sp](dbo.prep_oh_$sp.md) | dbo.job_error_handler_$sp, dbo.job_progress_handler_$sp, dbo.posting_parameter, dbo.prep_oh_group_$sp, dbo.prep_oh_sku_$sp, dbo.prep_oh_style_$sp, dbo.prep_oh_style_color_$sp, dbo.return_debug_flag_$sp |
| dbo | [prep_oh_group_$sp](dbo.prep_oh_group_$sp.md) | dbo.get_job_params_$sp, dbo.get_last_range_end_phase2_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_oh_group_loc_wk |
| dbo | [prep_oh_sku_$sp](dbo.prep_oh_sku_$sp.md) | dbo.get_job_params_$sp, dbo.get_last_range_end_phase2_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_oh_sku_loc_wk |
| dbo | [prep_oh_style_$sp](dbo.prep_oh_style_$sp.md) | dbo.get_job_params_$sp, dbo.get_last_range_end_phase2_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_oh_style_loc_wk |
| dbo | [prep_oh_style_color_$sp](dbo.prep_oh_style_color_$sp.md) | dbo.get_job_params_$sp, dbo.get_last_range_end_phase2_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_oh_styleclr_loc_wk |
| dbo | [prep_oo_all_$sp](dbo.prep_oo_all_$sp.md) | dbo.job_error_handler_$sp, dbo.job_progress_handler_$sp, dbo.posting_parameter, dbo.prep_oo_group_$sp, dbo.prep_oo_sku_$sp, dbo.prep_oo_style_$sp, dbo.prep_oo_style_color_$sp, dbo.return_debug_flag_$sp |
| dbo | [prep_oo_group_$sp](dbo.prep_oo_group_$sp.md) | dbo.get_job_params_$sp, dbo.get_last_range_end_phase2_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_oo_all_group_loc_wk |
| dbo | [prep_oo_sku_$sp](dbo.prep_oo_sku_$sp.md) | dbo.get_job_params_$sp, dbo.get_last_range_end_phase2_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_oo_all_sku_loc_wk |
| dbo | [prep_oo_style_$sp](dbo.prep_oo_style_$sp.md) | dbo.get_job_params_$sp, dbo.get_last_range_end_phase2_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_oo_all_style_loc_wk |
| dbo | [prep_oo_style_color_$sp](dbo.prep_oo_style_color_$sp.md) | dbo.get_job_params_$sp, dbo.get_last_range_end_phase2_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_oo_all_styleclr_loc_wk |
| dbo | [prep_roll_oh_$sp](dbo.prep_roll_oh_$sp.md) | dbo.add_partitions_$sp, dbo.job_error_handler_$sp, dbo.job_progress_handler_$sp, dbo.posting_parameter, dbo.prep_roll_oh_color_chn_pd_$sp, dbo.prep_roll_oh_color_chn_wk_$sp, dbo.prep_roll_oh_color_chn_yr_$sp, dbo.prep_roll_oh_color_loc_pd_$sp, dbo.prep_roll_oh_color_loc_wk_$sp, dbo.prep_roll_oh_color_loc_yr_$sp, dbo.prep_roll_oh_group_chn_pd_$sp, dbo.prep_roll_oh_group_chn_wk_$sp, dbo.prep_roll_oh_group_chn_yr_$sp, dbo.prep_roll_oh_group_loc_pd_$sp, dbo.prep_roll_oh_group_loc_wk_$sp, dbo.prep_roll_oh_group_loc_yr_$sp, dbo.prep_roll_oh_sku_chn_pd_$sp, dbo.prep_roll_oh_sku_chn_wk_$sp, dbo.prep_roll_oh_sku_chn_yr_$sp, dbo.prep_roll_oh_sku_loc_pd_$sp, dbo.prep_roll_oh_sku_loc_wk_$sp, dbo.prep_roll_oh_sku_loc_yr_$sp, dbo.prep_roll_oh_style_chn_pd_$sp, dbo.prep_roll_oh_style_chn_wk_$sp, dbo.prep_roll_oh_style_chn_yr_$sp, dbo.prep_roll_oh_style_loc_pd_$sp, dbo.prep_roll_oh_style_loc_wk_$sp, dbo.prep_roll_oh_style_loc_yr_$sp, dbo.return_debug_flag_$sp |
| dbo | [prep_roll_oh_color_chn_pd_$sp](dbo.prep_roll_oh_color_chn_pd_$sp.md) | dbo.get_current_period_$sp, dbo.get_last_range_end_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp |
| dbo | [prep_roll_oh_color_chn_wk_$sp](dbo.prep_roll_oh_color_chn_wk_$sp.md) | dbo.get_current_week_$sp, dbo.get_last_range_end_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp |
| dbo | [prep_roll_oh_color_chn_yr_$sp](dbo.prep_roll_oh_color_chn_yr_$sp.md) | dbo.get_current_year_$sp, dbo.get_last_range_end_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp |
| dbo | [prep_roll_oh_color_loc_pd_$sp](dbo.prep_roll_oh_color_loc_pd_$sp.md) | dbo.get_current_period_$sp, dbo.get_last_range_end_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp |
| dbo | [prep_roll_oh_color_loc_wk_$sp](dbo.prep_roll_oh_color_loc_wk_$sp.md) | dbo.get_current_week_$sp, dbo.get_last_range_end_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp |
| dbo | [prep_roll_oh_color_loc_yr_$sp](dbo.prep_roll_oh_color_loc_yr_$sp.md) | dbo.get_current_year_$sp, dbo.get_last_range_end_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp |
| dbo | [prep_roll_oh_group_chn_pd_$sp](dbo.prep_roll_oh_group_chn_pd_$sp.md) | dbo.get_current_period_$sp, dbo.get_last_range_end_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp |
| dbo | [prep_roll_oh_group_chn_wk_$sp](dbo.prep_roll_oh_group_chn_wk_$sp.md) | dbo.get_current_week_$sp, dbo.get_last_range_end_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp |
| dbo | [prep_roll_oh_group_chn_yr_$sp](dbo.prep_roll_oh_group_chn_yr_$sp.md) | dbo.get_current_year_$sp, dbo.get_last_range_end_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp |
| dbo | [prep_roll_oh_group_loc_pd_$sp](dbo.prep_roll_oh_group_loc_pd_$sp.md) | dbo.get_current_period_$sp, dbo.get_last_range_end_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp |
| dbo | [prep_roll_oh_group_loc_wk_$sp](dbo.prep_roll_oh_group_loc_wk_$sp.md) | dbo.get_current_week_$sp, dbo.get_last_range_end_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp |
| dbo | [prep_roll_oh_group_loc_yr_$sp](dbo.prep_roll_oh_group_loc_yr_$sp.md) | dbo.get_current_year_$sp, dbo.get_last_range_end_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp |
| dbo | [prep_roll_oh_sku_chn_pd_$sp](dbo.prep_roll_oh_sku_chn_pd_$sp.md) | dbo.get_current_period_$sp, dbo.get_last_range_end_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp |
| dbo | [prep_roll_oh_sku_chn_wk_$sp](dbo.prep_roll_oh_sku_chn_wk_$sp.md) | dbo.get_current_week_$sp, dbo.get_last_range_end_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp |
| dbo | [prep_roll_oh_sku_chn_yr_$sp](dbo.prep_roll_oh_sku_chn_yr_$sp.md) | dbo.get_current_year_$sp, dbo.get_last_range_end_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp |
| dbo | [prep_roll_oh_sku_loc_pd_$sp](dbo.prep_roll_oh_sku_loc_pd_$sp.md) | dbo.get_current_period_$sp, dbo.get_last_range_end_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp |
| dbo | [prep_roll_oh_sku_loc_wk_$sp](dbo.prep_roll_oh_sku_loc_wk_$sp.md) | dbo.get_current_week_$sp, dbo.get_last_range_end_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp |
| dbo | [prep_roll_oh_sku_loc_yr_$sp](dbo.prep_roll_oh_sku_loc_yr_$sp.md) | dbo.get_current_year_$sp, dbo.get_last_range_end_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp |
| dbo | [prep_roll_oh_style_chn_pd_$sp](dbo.prep_roll_oh_style_chn_pd_$sp.md) | dbo.get_current_period_$sp, dbo.get_last_range_end_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp |
| dbo | [prep_roll_oh_style_chn_wk_$sp](dbo.prep_roll_oh_style_chn_wk_$sp.md) | dbo.get_current_week_$sp, dbo.get_last_range_end_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp |
| dbo | [prep_roll_oh_style_chn_yr_$sp](dbo.prep_roll_oh_style_chn_yr_$sp.md) | dbo.get_current_year_$sp, dbo.get_last_range_end_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp |
| dbo | [prep_roll_oh_style_loc_pd_$sp](dbo.prep_roll_oh_style_loc_pd_$sp.md) | dbo.get_current_period_$sp, dbo.get_last_range_end_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp |
| dbo | [prep_roll_oh_style_loc_wk_$sp](dbo.prep_roll_oh_style_loc_wk_$sp.md) | dbo.get_current_week_$sp, dbo.get_last_range_end_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp |
| dbo | [prep_roll_oh_style_loc_yr_$sp](dbo.prep_roll_oh_style_loc_yr_$sp.md) | dbo.get_current_year_$sp, dbo.get_last_range_end_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp |
| dbo | [prep_wrk_cmp_$sp](dbo.prep_wrk_cmp_$sp.md) | dbo.job_error_handler_$sp, dbo.job_progress_handler_$sp, dbo.posting_parameter, dbo.return_debug_flag_$sp, dbo.wprep_cf_cmp_group_$sp, dbo.wprep_cf_cmp_style_$sp, dbo.wprep_cf_cmp_style_color_$sp, dbo.wprep_cmp_sku_$sp, dbo.wprep_iv_cmp_group_$sp, dbo.wprep_iv_cmp_style_$sp, dbo.wprep_iv_cmp_style_color_$sp, dbo.wrk_cmp_group_loc_wk, dbo.wrk_cmp_sku_loc_wk, dbo.wrk_cmp_style_loc_wk, dbo.wrk_cmp_styleclr_loc_wk |
| dbo | [prep_wrk_flash_$sp](dbo.prep_wrk_flash_$sp.md) | dbo.job_error_handler_$sp, dbo.job_progress_handler_$sp, dbo.posting_parameter, dbo.return_debug_flag_$sp, dbo.wprep_flash_group_$sp, dbo.wprep_flash_style_$sp, dbo.wrk_flsh_group_loc_da, dbo.wrk_flsh_style_loc_da |
| dbo | [prep_wrk_hist_$sp](dbo.prep_wrk_hist_$sp.md) | dbo.job_error_handler_$sp, dbo.job_progress_handler_$sp, dbo.posting_parameter, dbo.return_debug_flag_$sp, dbo.wprep_cf_hist_group_$sp, dbo.wprep_cf_hist_style_$sp, dbo.wprep_hist_sku_$sp, dbo.wprep_hist_style_color_$sp, dbo.wprep_iv_hist_group_$sp, dbo.wprep_iv_hist_style_$sp, dbo.wrk_group_loc_wk, dbo.wrk_sku_loc_wk, dbo.wrk_style_loc_wk, dbo.wrk_styleclr_loc_wk |
| dbo | [prep_wrk_ib_$sp](dbo.prep_wrk_ib_$sp.md) | dbo.job_error_handler_$sp, dbo.job_progress_handler_$sp, dbo.posting_parameter, dbo.prep_wrk_ib_allocation_$sp, dbo.prep_wrk_ib_cost_fact_disc_$sp, dbo.prep_wrk_ib_inventory_$sp, dbo.prep_wrk_ib_on_order_$sp, dbo.return_debug_flag_$sp |
| dbo | [prep_wrk_ib_allocation_$sp](dbo.prep_wrk_ib_allocation_$sp.md) | dbo.get_job_params_$sp, dbo.get_last_range_end_$sp, dbo.get_max_ib_allocation_id_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.posting_parameter, dbo.return_debug_flag_$sp |
| dbo | [prep_wrk_ib_cost_fact_disc_$sp](dbo.prep_wrk_ib_cost_fact_disc_$sp.md) | dbo.get_job_params_$sp, dbo.get_last_range_end_$sp, dbo.get_max_ib_cost_factor_id_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.posting_parameter, dbo.return_debug_flag_$sp |
| dbo | [prep_wrk_ib_inventory_$sp](dbo.prep_wrk_ib_inventory_$sp.md) | dbo.get_job_params_$sp, dbo.get_last_range_end_$sp, dbo.get_max_ib_inventory_id_$sp, dbo.is_tax_exclusive_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.posting_parameter, dbo.return_debug_flag_$sp, dbo.syn_ib_populate_notax_retails_$sp |
| dbo | [prep_wrk_ib_on_order_$sp](dbo.prep_wrk_ib_on_order_$sp.md) | dbo.get_job_params_$sp, dbo.get_last_range_end_$sp, dbo.get_max_ib_on_order_id_$sp, dbo.is_tax_exclusive_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.posting_parameter, dbo.return_debug_flag_$sp, dbo.syn_oo_populate_notax_retails_$sp |
| dbo | [prep_wrk_oh_$sp](dbo.prep_wrk_oh_$sp.md) | dbo.job_error_handler_$sp, dbo.job_progress_handler_$sp, dbo.posting_parameter, dbo.return_debug_flag_$sp, dbo.wprep_oh_group_$sp, dbo.wprep_oh_sku_$sp, dbo.wprep_oh_style_$sp, dbo.wprep_oh_style_color_$sp, dbo.wrk_oh_group_loc_wk, dbo.wrk_oh_sku_loc_wk, dbo.wrk_oh_style_loc_wk, dbo.wrk_oh_styleclr_loc_wk |
| dbo | [prep_wrk_oo_all_$sp](dbo.prep_wrk_oo_all_$sp.md) | dbo.job_error_handler_$sp, dbo.job_progress_handler_$sp, dbo.posting_parameter, dbo.return_debug_flag_$sp, dbo.wprep_all_group_$sp, dbo.wprep_all_sku_$sp, dbo.wprep_all_style_$sp, dbo.wprep_all_style_color_$sp, dbo.wprep_oo_group_$sp, dbo.wprep_oo_sku_$sp, dbo.wprep_oo_style_$sp, dbo.wprep_oo_style_color_$sp, dbo.wrk_oo_all_group_loc_wk, dbo.wrk_oo_all_sku_loc_wk, dbo.wrk_oo_all_style_loc_wk, dbo.wrk_oo_all_styleclr_loc_wk |
| dbo | [reclass_hist_$sp](dbo.reclass_hist_$sp.md) | dbo.calendar_merch_week, dbo.hist_group_chn_li, dbo.hist_group_chn_pd, dbo.hist_group_chn_wk, dbo.hist_group_chn_yr, dbo.hist_group_loc_li, dbo.hist_group_loc_pd, dbo.hist_group_loc_wk, dbo.hist_group_loc_yr, dbo.hist_style_loc_wk, dbo.rc_style_chn_li, dbo.rc_style_chn_pd, dbo.rc_style_chn_wk, dbo.rc_style_chn_yr, dbo.rc_style_loc_li, dbo.rc_style_loc_pd, dbo.rc_style_loc_wk, dbo.rc_style_loc_yr, dbo.style_reclass_detail |
| Desc: | [style reclassification for History tables.](Desc_style_reclassification_for_History_tables..md) |  |
| Mar10,03   Udani | [1-ITI7J    New](Mar10,03_Udani.1-ITI7J_New.md) |  |
| Oct06,03   Udani | [16063](Oct06,03_Udani.16063.md) |  |
| Jul04,05   Yan Ding | [56880](Jul04,05_Yan_Ding.56880.md) |  |
| Jul20,07   Yan Ding | [87495](Jul20,07_Yan_Ding.87495.md) |  |
| February 2010 | [Modify for the Multi-Currency project.](February_2010_Modify_for_the_Multi-Currency_project..md) |  |
| dbo | [reclass_hist_cmp_$sp](dbo.reclass_hist_cmp_$sp.md) | dbo.calendar_merch_week, dbo.hist_cmp_group_chn_li, dbo.hist_cmp_group_chn_pd, dbo.hist_cmp_group_chn_wk, dbo.hist_cmp_group_chn_yr, dbo.hist_cmp_group_loc_li, dbo.hist_cmp_group_loc_pd, dbo.hist_cmp_group_loc_wk, dbo.hist_cmp_group_loc_yr, dbo.hist_cmp_style_loc_wk, dbo.rc_cmp_style_chn_li, dbo.rc_cmp_style_chn_pd, dbo.rc_cmp_style_chn_wk, dbo.rc_cmp_style_chn_yr, dbo.rc_cmp_style_loc_li, dbo.rc_cmp_style_loc_pd, dbo.rc_cmp_style_loc_wk, dbo.rc_cmp_style_loc_yr, dbo.style_reclass_detail |
| Desc: | [reclass for Hist Cmp](Desc_.reclass_for_Hist_Cmp.md) |  |
| Mar17,03   Udani | [1-ITI7J    New](Mar17,03_Udani.1-ITI7J_New.md) |  |
| Oct06,03   Udani        16063 | [Added the following new columns for Intenationlization:](Oct06,03_Udani_16063.Added_the_following_new_columns_for_Intenationlization.md) |  |
| Jul04,05   Yan Ding | [56880](Jul04,05_Yan_Ding.56880.md) |  |
| Jul20,07   Yan Ding | [87495](Jul20,07_Yan_Ding.87495.md) |  |
| Desc: | [Take the existing rows from hist_cmp_style_loc/chn_wk/pd/yr/li](Desc_.Take_the_existing_rows_from_hist_cmp_style_loc_chn_wk_pd_yr_li.md) |  |
| dbo | [reclass_hist_flsh_$sp](dbo.reclass_hist_flsh_$sp.md) | dbo.hist_flsh_group_chn_da, dbo.hist_flsh_group_loc_da, dbo.hist_flsh_style_chn_da, dbo.hist_flsh_style_loc_da, dbo.style_reclass_detail |
| Desc: | [reclass for Hist Flsh](Desc_.reclass_for_Hist_Flsh.md) |  |
| Mar17,03   Udani | [1-ITI7J   New](Mar17,03_Udani.1-ITI7J_New.md) |  |
| Oct07,03   Udani | [16063](Oct07,03_Udani.16063.md) |  |
| Jul04,05   Yan Ding | [56880](Jul04,05_Yan_Ding.56880.md) |  |
| Desc: | [Copy to hist_flsh_group_loc/chn_da from hist_flsh_style_loc_da for the stle being re-classified](Desc_.Copy_to_hist_flsh_group_loc_chn_da_from_hist_flsh_style_loc_da_for_the_stle_being_re-classified.md) |  |
| dbo | [reclass_hist_le_$sp](dbo.reclass_hist_le_$sp.md) | dbo.calendar_merch_week, dbo.hist_le_group_chn_li, dbo.hist_le_group_chn_pd, dbo.hist_le_group_chn_wk, dbo.hist_le_group_chn_yr, dbo.hist_le_group_loc_li, dbo.hist_le_group_loc_pd, dbo.hist_le_group_loc_wk, dbo.hist_le_group_loc_yr, dbo.hist_le_style_chn_wk, dbo.hist_le_style_loc_wk, dbo.style_reclass_detail |
| Dec 07, 2004   Yan Ding | [(Dev)   It copies the loss and extra sales values of a style from the HIST_LE_STYLE_LOC_WK table](Dec_07,_2004_Yan_Ding._Dev_It_copies_the_loss_and_extra_sales_values_of_a_style_from_the_HIST_LE_STYLE_LOC_WK_table.md) |  |
| Desc: | [Copy to hist_le_group_loc/chn/wk/pd/yr/li from hist_le_style_loc/chn_wk for the style being re-classified](Desc_.Copy_to_hist_le_group_loc_chn_wk_pd_yr_li_from_hist_le_style_loc_chn_wk_for_the_style_being_re-classified.md) |  |
| dbo | [reclass_hist_oh_$sp](dbo.reclass_hist_oh_$sp.md) | dbo.calendar_merch_week, dbo.hist_oh_group_chn_li, dbo.hist_oh_group_chn_pd, dbo.hist_oh_group_chn_wk, dbo.hist_oh_group_chn_yr, dbo.hist_oh_group_loc_li, dbo.hist_oh_group_loc_pd, dbo.hist_oh_group_loc_wk, dbo.hist_oh_group_loc_yr, dbo.hist_oh_style_loc_wk, dbo.history_component, dbo.p, dbo.post_parameter, dbo.rc_oh_style_chn_li, dbo.rc_oh_style_chn_pd, dbo.rc_oh_style_chn_wk, dbo.rc_oh_style_chn_yr, dbo.rc_oh_style_loc_li, dbo.rc_oh_style_loc_pd, dbo.rc_oh_style_loc_wk, dbo.rc_oh_style_loc_yr, dbo.reclass_oh_post_adjust_cmp_$sp, dbo.style_reclass_detail |
| Desc: | [reclass for Hist OH](Desc_.reclass_for_Hist_OH.md) |  |
| Mar17,03   Udani | [1-ITI7J    New](Mar17,03_Udani.1-ITI7J_New.md) |  |
| Oct06,03   Udani | [16063    Added the following new columns for Internationalization :](Oct06,03_Udani.16063_Added_the_following_new_columns_for_Internationalization.md) |  |
| Jul04,05   Yan Ding | [56880](Jul04,05_Yan_Ding.56880.md) |  |
| Jul20,07   Yan Ding | [87495](Jul20,07_Yan_Ding.87495.md) |  |
| Desc: | [style reclassification for Hist_OH.](Desc_style_reclassification_for_Hist_OH..md) |  |
| dbo | [reclass_oh_post_adjust_cmp_$sp](dbo.reclass_oh_post_adjust_cmp_$sp.md) | dbo.calendar_merch_week, dbo.hist_cmp_group_chn_li, dbo.hist_cmp_group_chn_pd, dbo.hist_cmp_group_chn_wk, dbo.hist_cmp_group_chn_yr, dbo.hist_cmp_group_loc_li, dbo.hist_cmp_group_loc_pd, dbo.hist_cmp_group_loc_wk, dbo.hist_cmp_group_loc_yr, dbo.post_parameter, dbo.rc_oh_style_chn_curr, dbo.rc_oh_style_chn_wk, dbo.rc_oh_style_loc_curr, dbo.rc_oh_style_loc_wk |
| -- | [CREATE TABLE #style_loc_wk](--.CREATE_TABLE_#style_loc_wk.md) |  |
| -- | [INSERT INTO #style_loc_wk](--.INSERT_INTO_#style_loc_wk.md) |  |
| -- | [SELECT](--.SELECT.md) |  |
| -- | [FROM](--.FROM.md) |  |
| -- | [WHERE](--.WHERE.md) |  |
| -- | [ALTER TABLE #style_loc_wk](--.ALTER_TABLE_#style_loc_wk.md) |  |
| -- | [ADD PRIMARY KEY ( style_id, old_hierarchy_group_id, new_hierarchy_group_id](--.ADD_PRIMARY_KEY_style_id,_old_hierarchy_group_id,_new_hierarchy_group_id.md) |  |
| -- | [IF NOT object_id('tempdb..#style_chn_wk') IS NULL](--_IF_NOT_object_id_'tempdb_.#style_chn_wk'_IS_NULL.md) |  |
| -- | [DROP TABLE #style_chn_wk](--.DROP_TABLE_#style_chn_wk.md) |  |
| -- | [CREATE TABLE #style_chn_wk](--.CREATE_TABLE_#style_chn_wk.md) |  |
| -- | [INSERT INTO #style_chn_wk](--.INSERT_INTO_#style_chn_wk.md) |  |
| -- | [SELECT](--.SELECT.md) |  |
| -- | [FROM](--.FROM.md) |  |
| -- | [GROUP BY](--.GROUP_BY.md) |  |
| -- | [ALTER TABLE #style_chn_wk](--.ALTER_TABLE_#style_chn_wk.md) |  |
| -- | [ADD PRIMARY KEY ( style_id, old_hierarchy_group_id, new_hierarchy_group_id](--.ADD_PRIMARY_KEY_style_id,_old_hierarchy_group_id,_new_hierarchy_group_id.md) |  |
| dbo | [reclass_oo_all_$sp](dbo.reclass_oo_all_$sp.md) | dbo.calendar_merch_week, dbo.oo_all_group_chn_li, dbo.oo_all_group_chn_pd, dbo.oo_all_group_chn_wk, dbo.oo_all_group_chn_yr, dbo.oo_all_group_loc_li, dbo.oo_all_group_loc_pd, dbo.oo_all_group_loc_wk, dbo.oo_all_group_loc_yr, dbo.oo_all_style_chn_wk, dbo.oo_all_style_loc_wk, dbo.style_reclass_detail |
| Desc: | [reclass for OO ALL](Desc_.reclass_for_OO_ALL.md) |  |
| Mar17,03   Udani | [1-ITI7J    New](Mar17,03_Udani.1-ITI7J_New.md) |  |
| Jul04,05   Yan Ding | [56880](Jul04,05_Yan_Ding.56880.md) |  |
| Jul20,07   Yan Ding | [87495](Jul20,07_Yan_Ding.87495.md) |  |
| Apr 21,11 | [Sameer Patel](Apr_21,11.Sameer_Patel.md) |  |
| dbo | [return_debug_flag_$sp](dbo.return_debug_flag_$sp.md) | dbo.job_error_handler_$sp, dbo.job_params |
| dbo | [return_step_exists_$sp](dbo.return_step_exists_$sp.md) | dbo.job_detail, dbo.job_error_handler_$sp |
| dbo | [roll_oh_group_chn_pd_$sp](dbo.roll_oh_group_chn_pd_$sp.md) | dbo.calendar_merch_period, dbo.hist_oh_group_chn_pd, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_params, dbo.job_progress_handler_$sp, dbo.merch_year_pd_pf, dbo.return_debug_flag_$sp, dbo.wrk_roll_oh_group_chn_pd |
| dbo | [roll_oh_group_chn_wk_$sp](dbo.roll_oh_group_chn_wk_$sp.md) | dbo.calendar_merch_week, dbo.hist_oh_group_chn_wk, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_params, dbo.job_progress_handler_$sp, dbo.merch_year_wk_pf, dbo.return_debug_flag_$sp, dbo.wrk_roll_oh_group_chn_wk |
| dbo | [roll_oh_group_chn_yr_$sp](dbo.roll_oh_group_chn_yr_$sp.md) | dbo.calendar, dbo.hist_oh_group_chn_yr, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_params, dbo.job_progress_handler_$sp, dbo.merch_year_pf, dbo.return_debug_flag_$sp, dbo.wrk_roll_oh_group_chn_yr |
| dbo | [roll_oh_group_loc_pd_$sp](dbo.roll_oh_group_loc_pd_$sp.md) | dbo.calendar_merch_period, dbo.hist_oh_group_loc_pd, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_params, dbo.job_progress_handler_$sp, dbo.merch_year_pd_pf, dbo.post_parameter, dbo.return_debug_flag_$sp, dbo.wrk_roll_oh_group_loc_pd |
| dbo | [roll_oh_group_loc_wk_$sp](dbo.roll_oh_group_loc_wk_$sp.md) | dbo.calendar_merch_week, dbo.hist_oh_group_loc_wk, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_params, dbo.job_progress_handler_$sp, dbo.merch_year_wk_pf, dbo.post_parameter, dbo.return_debug_flag_$sp, dbo.wrk_roll_oh_group_loc_wk |
| dbo | [roll_oh_group_loc_yr_$sp](dbo.roll_oh_group_loc_yr_$sp.md) | dbo.calendar, dbo.hist_oh_group_loc_yr, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_params, dbo.job_progress_handler_$sp, dbo.merch_year_pf, dbo.post_parameter, dbo.return_debug_flag_$sp, dbo.wrk_roll_oh_group_loc_yr |
| dbo | [roll_oh_group_pd_$sp](dbo.roll_oh_group_pd_$sp.md) | dbo.hist_oh_group_chn_pd, dbo.hist_oh_group_loc_pd, dbo.post_roll_oh_pd |
| SELECT | [a.hierarchy_group_id,](SELECT_a.hierarchy_group_id,.md) |  |
| FROM | [hist_oh_group_loc_pd a,](FROM.hist_oh_group_loc_pd_a,.md) |  |
| WHERE | [a.hierarchy_group_id = @curr_hierarchy_group_id](WHERE_a.hierarchy_group_id_=_@curr_hierarchy_group_id.md) |  |
| AND | [b.merch_level = 'group'](AND_b.merch_level_=_'group'.md) |  |
| AND | [a.merch_year_pd = @last_period](AND_a.merch_year_pd_=_@last_period.md) |  |
| SELECT | [a.hierarchy_group_id,](SELECT_a.hierarchy_group_id,.md) |  |
| FROM | [hist_oh_group_chn_pd a,](FROM.hist_oh_group_chn_pd_a,.md) |  |
| WHERE | [a.hierarchy_group_id = @curr_hierarchy_group_id](WHERE_a.hierarchy_group_id_=_@curr_hierarchy_group_id.md) |  |
| AND | [b.merch_level = 'group'](AND_b.merch_level_=_'group'.md) |  |
| AND | [a.merch_year_pd = @last_period](AND_a.merch_year_pd_=_@last_period.md) |  |
| dbo | [roll_oh_group_wk_$sp](dbo.roll_oh_group_wk_$sp.md) | dbo.hist_oh_group_chn_wk, dbo.hist_oh_group_loc_wk, dbo.post_roll_oh_wk |
| FROM | [hist_oh_group_loc_wk a,](FROM.hist_oh_group_loc_wk_a,.md) |  |
| WHERE | [a.hierarchy_group_id = @curr_hierarchy_group_id](WHERE_a.hierarchy_group_id_=_@curr_hierarchy_group_id.md) |  |
| AND | [b.merch_level = 'group'](AND_b.merch_level_=_'group'.md) |  |
| AND | [a.merch_year_wk = @last_week](AND_a.merch_year_wk_=_@last_week.md) |  |
| SELECT | [a.hierarchy_group_id,](SELECT_a.hierarchy_group_id,.md) |  |
| FROM | [hist_oh_group_chn_wk a,](FROM.hist_oh_group_chn_wk_a,.md) |  |
| WHERE | [a.hierarchy_group_id = @curr_hierarchy_group_id](WHERE_a.hierarchy_group_id_=_@curr_hierarchy_group_id.md) |  |
| AND | [b.merch_level = 'group'](AND_b.merch_level_=_'group'.md) |  |
| AND | [a.merch_year_wk = @last_week](AND_a.merch_year_wk_=_@last_week.md) |  |
| dbo | [roll_oh_group_yr_$sp](dbo.roll_oh_group_yr_$sp.md) | dbo.hist_oh_group_chn_yr, dbo.hist_oh_group_loc_yr, dbo.post_roll_oh_yr |
| SELECT | [a.hierarchy_group_id,](SELECT_a.hierarchy_group_id,.md) |  |
| FROM | [hist_oh_group_loc_yr a,](FROM.hist_oh_group_loc_yr_a,.md) |  |
| WHERE | [a.hierarchy_group_id = @curr_hierarchy_group_id](WHERE_a.hierarchy_group_id_=_@curr_hierarchy_group_id.md) |  |
| AND | [b.merch_level = 'group'](AND_b.merch_level_=_'group'.md) |  |
| AND | [a.merch_year = @last_year](AND_a.merch_year_=_@last_year.md) |  |
| SELECT | [a.hierarchy_group_id,](SELECT_a.hierarchy_group_id,.md) |  |
| FROM | [hist_oh_group_chn_yr a,](FROM.hist_oh_group_chn_yr_a,.md) |  |
| WHERE | [a.hierarchy_group_id = @curr_hierarchy_group_id](WHERE_a.hierarchy_group_id_=_@curr_hierarchy_group_id.md) |  |
| AND | [b.merch_level = 'group'](AND_b.merch_level_=_'group'.md) |  |
| AND | [a.merch_year = @last_year](AND_a.merch_year_=_@last_year.md) |  |
| dbo | [roll_oh_sku_chn_pd_$sp](dbo.roll_oh_sku_chn_pd_$sp.md) | dbo.calendar_merch_period, dbo.hist_oh_sku_chn_pd, dbo.hist_oh_sku_loc_pd, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_params, dbo.job_progress_handler_$sp, dbo.merch_year_pd_pf, dbo.return_debug_flag_$sp, dbo.wrk_roll_oh_sku_chn_pd |
| dbo | [roll_oh_sku_chn_wk_$sp](dbo.roll_oh_sku_chn_wk_$sp.md) | dbo.calendar_merch_week, dbo.hist_oh_sku_chn_wk, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_params, dbo.job_progress_handler_$sp, dbo.merch_year_wk_pf, dbo.return_debug_flag_$sp, dbo.wrk_roll_oh_sku_chn_wk |
| dbo | [roll_oh_sku_chn_yr_$sp](dbo.roll_oh_sku_chn_yr_$sp.md) | dbo.calendar, dbo.hist_oh_sku_chn_yr, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_params, dbo.job_progress_handler_$sp, dbo.merch_year_pf, dbo.return_debug_flag_$sp, dbo.wrk_roll_oh_sku_chn_yr |
| dbo | [roll_oh_sku_loc_pd_$sp](dbo.roll_oh_sku_loc_pd_$sp.md) | dbo.calendar_merch_period, dbo.hist_oh_sku_loc_pd, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_params, dbo.job_progress_handler_$sp, dbo.merch_year_pd_pf, dbo.post_parameter, dbo.return_debug_flag_$sp, dbo.wrk_roll_oh_sku_loc_pd |
| dbo | [roll_oh_sku_loc_wk_$sp](dbo.roll_oh_sku_loc_wk_$sp.md) | dbo.calendar_merch_week, dbo.hist_oh_sku_loc_wk, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_params, dbo.job_progress_handler_$sp, dbo.merch_year_wk_pf, dbo.post_parameter, dbo.return_debug_flag_$sp, dbo.wrk_roll_oh_sku_loc_wk |
| dbo | [roll_oh_sku_loc_yr_$sp](dbo.roll_oh_sku_loc_yr_$sp.md) | dbo.calendar, dbo.hist_oh_sku_loc_yr, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_params, dbo.job_progress_handler_$sp, dbo.merch_year_pf, dbo.post_parameter, dbo.return_debug_flag_$sp, dbo.wrk_roll_oh_sku_loc_yr |
| dbo | [roll_oh_sku_pd_$sp](dbo.roll_oh_sku_pd_$sp.md) | dbo.hist_oh_sku_chn_pd, dbo.hist_oh_sku_loc_pd, dbo.post_roll_oh_pd |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [hist_oh_sku_loc_pd a,](FROM.hist_oh_sku_loc_pd_a,.md) |  |
| WHERE | [a.style_id = @curr_style_id](WHERE_a.style_id_=_@curr_style_id.md) |  |
| AND | [b.merch_level = 'sku'](AND_b.merch_level_=_'sku'.md) |  |
| AND | [a.merch_year_pd = @last_period](AND_a.merch_year_pd_=_@last_period.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [hist_oh_sku_chn_pd a,](FROM.hist_oh_sku_chn_pd_a,.md) |  |
| WHERE | [a.style_id = @curr_style_id](WHERE_a.style_id_=_@curr_style_id.md) |  |
| AND | [b.merch_level = 'sku'](AND_b.merch_level_=_'sku'.md) |  |
| AND | [a.merch_year_pd = @last_period](AND_a.merch_year_pd_=_@last_period.md) |  |
| dbo | [roll_oh_sku_wk_$sp](dbo.roll_oh_sku_wk_$sp.md) | dbo.hist_oh_sku_chn_wk, dbo.hist_oh_sku_loc_wk, dbo.post_roll_oh_wk |
| FROM | [hist_oh_sku_loc_wk a,](FROM.hist_oh_sku_loc_wk_a,.md) |  |
| WHERE | [a.style_id = @curr_style_id](WHERE_a.style_id_=_@curr_style_id.md) |  |
| AND | [b.merch_level = 'sku'](AND_b.merch_level_=_'sku'.md) |  |
| AND | [a.merch_year_wk = @last_week](AND_a.merch_year_wk_=_@last_week.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [hist_oh_sku_chn_wk a,](FROM.hist_oh_sku_chn_wk_a,.md) |  |
| WHERE | [a.style_id = @curr_style_id](WHERE_a.style_id_=_@curr_style_id.md) |  |
| AND | [b.merch_level = 'sku'](AND_b.merch_level_=_'sku'.md) |  |
| AND | [a.merch_year_wk = @last_week](AND_a.merch_year_wk_=_@last_week.md) |  |
| dbo | [roll_oh_sku_yr_$sp](dbo.roll_oh_sku_yr_$sp.md) | dbo.hist_oh_sku_chn_yr, dbo.hist_oh_sku_loc_yr, dbo.post_roll_oh_yr |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [hist_oh_sku_loc_yr a,](FROM.hist_oh_sku_loc_yr_a,.md) |  |
| WHERE | [a.style_id = @curr_style_id](WHERE_a.style_id_=_@curr_style_id.md) |  |
| AND | [b.merch_level = 'sku'](AND_b.merch_level_=_'sku'.md) |  |
| AND | [a.merch_year = @last_year](AND_a.merch_year_=_@last_year.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [hist_oh_sku_chn_yr a,](FROM.hist_oh_sku_chn_yr_a,.md) |  |
| WHERE | [a.style_id = @curr_style_id](WHERE_a.style_id_=_@curr_style_id.md) |  |
| AND | [b.merch_level = 'sku'](AND_b.merch_level_=_'sku'.md) |  |
| AND | [a.merch_year = @last_year](AND_a.merch_year_=_@last_year.md) |  |
| dbo | [roll_oh_style_chn_pd_$sp](dbo.roll_oh_style_chn_pd_$sp.md) | dbo.calendar_merch_period, dbo.hist_oh_style_chn_pd, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_params, dbo.job_progress_handler_$sp, dbo.merch_year_pd_pf, dbo.return_debug_flag_$sp, dbo.wrk_roll_oh_style_chn_pd |
| dbo | [roll_oh_style_chn_wk_$sp](dbo.roll_oh_style_chn_wk_$sp.md) | dbo.calendar_merch_week, dbo.hist_oh_style_chn_wk, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_params, dbo.job_progress_handler_$sp, dbo.merch_year_wk_pf, dbo.return_debug_flag_$sp, dbo.wrk_roll_oh_style_chn_wk |
| dbo | [roll_oh_style_chn_yr_$sp](dbo.roll_oh_style_chn_yr_$sp.md) | dbo.calendar, dbo.hist_oh_style_chn_yr, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_params, dbo.job_progress_handler_$sp, dbo.merch_year_pf, dbo.return_debug_flag_$sp, dbo.wrk_roll_oh_style_chn_yr |
| dbo | [roll_oh_style_color_chn_pd_$sp](dbo.roll_oh_style_color_chn_pd_$sp.md) | dbo.calendar_merch_period, dbo.hist_oh_styleclr_chn_pd, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_params, dbo.job_progress_handler_$sp, dbo.merch_year_pd_pf, dbo.return_debug_flag_$sp, dbo.wrk_roll_oh_styleclr_chn_pd |
| dbo | [roll_oh_style_color_chn_wk_$sp](dbo.roll_oh_style_color_chn_wk_$sp.md) | dbo.calendar_merch_week, dbo.hist_oh_styleclr_chn_wk, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_params, dbo.job_progress_handler_$sp, dbo.merch_year_wk_pf, dbo.return_debug_flag_$sp, dbo.wrk_roll_oh_styleclr_chn_wk |
| dbo | [roll_oh_style_color_chn_yr_$sp](dbo.roll_oh_style_color_chn_yr_$sp.md) | dbo.calendar, dbo.hist_oh_styleclr_chn_yr, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_params, dbo.job_progress_handler_$sp, dbo.merch_year_pf, dbo.return_debug_flag_$sp, dbo.wrk_roll_oh_styleclr_chn_yr |
| dbo | [roll_oh_style_color_loc_pd_$sp](dbo.roll_oh_style_color_loc_pd_$sp.md) | dbo.calendar_merch_period, dbo.hist_oh_styleclr_loc_pd, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_params, dbo.job_progress_handler_$sp, dbo.merch_year_pd_pf, dbo.post_parameter, dbo.return_debug_flag_$sp, dbo.wrk_roll_oh_styleclr_loc_pd |
| dbo | [roll_oh_style_color_loc_wk_$sp](dbo.roll_oh_style_color_loc_wk_$sp.md) | dbo.calendar_merch_week, dbo.hist_oh_styleclr_loc_wk, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_params, dbo.job_progress_handler_$sp, dbo.merch_year_wk_pf, dbo.post_parameter, dbo.return_debug_flag_$sp, dbo.wrk_roll_oh_styleclr_loc_wk |
| dbo | [roll_oh_style_color_loc_yr_$sp](dbo.roll_oh_style_color_loc_yr_$sp.md) | dbo.calendar, dbo.hist_oh_styleclr_loc_yr, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_params, dbo.job_progress_handler_$sp, dbo.merch_year_pf, dbo.post_parameter, dbo.return_debug_flag_$sp, dbo.wrk_roll_oh_styleclr_loc_yr |
| dbo | [roll_oh_style_loc_pd_$sp](dbo.roll_oh_style_loc_pd_$sp.md) | dbo.calendar_merch_period, dbo.hist_oh_style_loc_pd, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_params, dbo.job_progress_handler_$sp, dbo.merch_year_pd_pf, dbo.post_parameter, dbo.return_debug_flag_$sp, dbo.wrk_roll_oh_style_loc_pd |
| dbo | [roll_oh_style_loc_wk_$sp](dbo.roll_oh_style_loc_wk_$sp.md) | dbo.calendar_merch_week, dbo.hist_oh_style_loc_wk, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_params, dbo.job_progress_handler_$sp, dbo.merch_year_wk_pf, dbo.post_parameter, dbo.return_debug_flag_$sp, dbo.wrk_roll_oh_style_loc_wk |
| dbo | [roll_oh_style_loc_yr_$sp](dbo.roll_oh_style_loc_yr_$sp.md) | dbo.calendar, dbo.hist_oh_style_loc_yr, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_params, dbo.job_progress_handler_$sp, dbo.merch_year_pf, dbo.post_parameter, dbo.return_debug_flag_$sp, dbo.wrk_roll_oh_style_loc_yr |
| dbo | [roll_oh_style_pd_$sp](dbo.roll_oh_style_pd_$sp.md) | dbo.hist_oh_style_chn_pd, dbo.hist_oh_style_loc_pd, dbo.post_roll_oh_pd |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [hist_oh_style_loc_pd a,](FROM.hist_oh_style_loc_pd_a,.md) |  |
| WHERE | [a.style_id = @curr_style_id](WHERE_a.style_id_=_@curr_style_id.md) |  |
| AND | [b.merch_level = 'style'](AND_b.merch_level_=_'style'.md) |  |
| AND | [a.merch_year_pd = @last_period](AND_a.merch_year_pd_=_@last_period.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [hist_oh_style_chn_pd a,](FROM.hist_oh_style_chn_pd_a,.md) |  |
| WHERE | [a.style_id = @curr_style_id](WHERE_a.style_id_=_@curr_style_id.md) |  |
| AND | [b.merch_level = 'style'](AND_b.merch_level_=_'style'.md) |  |
| AND | [a.merch_year_pd = @last_period](AND_a.merch_year_pd_=_@last_period.md) |  |
| dbo | [roll_oh_style_wk_$sp](dbo.roll_oh_style_wk_$sp.md) | dbo.hist_oh_style_chn_wk, dbo.hist_oh_style_loc_wk, dbo.post_roll_oh_wk |
| FROM | [hist_oh_style_loc_wk a,](FROM.hist_oh_style_loc_wk_a,.md) |  |
| WHERE | [a.style_id = @curr_style_id](WHERE_a.style_id_=_@curr_style_id.md) |  |
| AND | [b.merch_level = 'style'](AND_b.merch_level_=_'style'.md) |  |
| AND | [a.merch_year_wk = @last_week](AND_a.merch_year_wk_=_@last_week.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [hist_oh_style_chn_wk a,](FROM.hist_oh_style_chn_wk_a,.md) |  |
| WHERE | [a.style_id = @curr_style_id](WHERE_a.style_id_=_@curr_style_id.md) |  |
| AND | [b.merch_level = 'style'](AND_b.merch_level_=_'style'.md) |  |
| AND | [a.merch_year_wk = @last_week](AND_a.merch_year_wk_=_@last_week.md) |  |
| dbo | [roll_oh_style_yr_$sp](dbo.roll_oh_style_yr_$sp.md) | dbo.hist_oh_style_chn_yr, dbo.hist_oh_style_loc_yr, dbo.post_roll_oh_yr |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [hist_oh_style_loc_yr a,](FROM.hist_oh_style_loc_yr_a,.md) |  |
| WHERE | [a.style_id = @curr_style_id](WHERE_a.style_id_=_@curr_style_id.md) |  |
| AND | [b.merch_level = 'style'](AND_b.merch_level_=_'style'.md) |  |
| AND | [a.merch_year = @last_year](AND_a.merch_year_=_@last_year.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [hist_oh_style_chn_yr a,](FROM.hist_oh_style_chn_yr_a,.md) |  |
| WHERE | [a.style_id = @curr_style_id](WHERE_a.style_id_=_@curr_style_id.md) |  |
| AND | [b.merch_level = 'style'](AND_b.merch_level_=_'style'.md) |  |
| AND | [a.merch_year = @last_year](AND_a.merch_year_=_@last_year.md) |  |
| dbo | [roll_oh_styleclr_pd_$sp](dbo.roll_oh_styleclr_pd_$sp.md) | dbo.hist_oh_styleclr_chn_pd, dbo.hist_oh_styleclr_loc_pd, dbo.post_roll_oh_pd |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [hist_oh_styleclr_loc_pd a,](FROM.hist_oh_styleclr_loc_pd_a,.md) |  |
| WHERE | [a.style_id = @curr_style_id](WHERE_a.style_id_=_@curr_style_id.md) |  |
| AND | [b.merch_level = 'styleclr'](AND_b.merch_level_=_'styleclr'.md) |  |
| AND | [a.merch_year_pd = @last_period](AND_a.merch_year_pd_=_@last_period.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [hist_oh_styleclr_chn_pd a,](FROM.hist_oh_styleclr_chn_pd_a,.md) |  |
| WHERE | [a.style_id = @curr_style_id](WHERE_a.style_id_=_@curr_style_id.md) |  |
| AND | [b.merch_level = 'styleclr'](AND_b.merch_level_=_'styleclr'.md) |  |
| AND | [a.merch_year_pd = @last_period](AND_a.merch_year_pd_=_@last_period.md) |  |
| dbo | [roll_oh_styleclr_wk_$sp](dbo.roll_oh_styleclr_wk_$sp.md) | dbo.hist_oh_styleclr_chn_wk, dbo.hist_oh_styleclr_loc_wk, dbo.post_roll_oh_wk |
| FROM | [hist_oh_styleclr_loc_wk a,](FROM.hist_oh_styleclr_loc_wk_a,.md) |  |
| WHERE | [a.style_id = @curr_style_id](WHERE_a.style_id_=_@curr_style_id.md) |  |
| AND | [b.merch_level = 'styleclr'](AND_b.merch_level_=_'styleclr'.md) |  |
| AND | [a.merch_year_wk = @last_week](AND_a.merch_year_wk_=_@last_week.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [hist_oh_styleclr_chn_wk a,](FROM.hist_oh_styleclr_chn_wk_a,.md) |  |
| WHERE | [a.style_id = @curr_style_id](WHERE_a.style_id_=_@curr_style_id.md) |  |
| AND | [b.merch_level = 'styleclr'](AND_b.merch_level_=_'styleclr'.md) |  |
| AND | [a.merch_year_wk = @last_week](AND_a.merch_year_wk_=_@last_week.md) |  |
| dbo | [roll_oh_styleclr_yr_$sp](dbo.roll_oh_styleclr_yr_$sp.md) | dbo.hist_oh_styleclr_chn_yr, dbo.hist_oh_styleclr_loc_yr, dbo.post_roll_oh_yr |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [hist_oh_styleclr_loc_yr a,](FROM.hist_oh_styleclr_loc_yr_a,.md) |  |
| WHERE | [a.style_id = @curr_style_id](WHERE_a.style_id_=_@curr_style_id.md) |  |
| AND | [b.merch_level = 'styleclr'](AND_b.merch_level_=_'styleclr'.md) |  |
| AND | [a.merch_year = @last_year](AND_a.merch_year_=_@last_year.md) |  |
| SELECT | [a.style_id,](SELECT_a.style_id,.md) |  |
| FROM | [hist_oh_styleclr_chn_yr a,](FROM.hist_oh_styleclr_chn_yr_a,.md) |  |
| WHERE | [a.style_id = @curr_style_id](WHERE_a.style_id_=_@curr_style_id.md) |  |
| AND | [b.merch_level = 'styleclr'](AND_b.merch_level_=_'styleclr'.md) |  |
| AND | [a.merch_year = @last_year](AND_a.merch_year_=_@last_year.md) |  |
| dbo | [rpt_core_chain_$sp](dbo.rpt_core_chain_$sp.md) | dbo.calendar_merch_week, dbo.hist_group_chn_wk, dbo.hist_oh_group_chn_wk, dbo.oo_all_group_chn_wk, dbo.parameter_plan_elements, dbo.plan_group_chn_pd |
| dbo | [rpt_core_location_home_$sp](dbo.rpt_core_location_home_$sp.md) | dbo.calendar_merch_week, dbo.hist_group_loc_wk, dbo.hist_oh_group_loc_wk, dbo.oo_all_group_loc_wk, dbo.parameter_plan_elements, dbo.plan_group_loc_pd |
| dbo | [rpt_core_location_local_$sp](dbo.rpt_core_location_local_$sp.md) | dbo.calendar_merch_week, dbo.hist_group_loc_wk, dbo.hist_oh_group_loc_wk, dbo.oo_all_group_loc_wk, dbo.parameter_plan_elements, dbo.plan_group_loc_pd |
| dbo | [rpt_mar_chain_md_$sp](dbo.rpt_mar_chain_md_$sp.md) | dbo.calendar_merch_week, dbo.hist_cmp_group_chn_wk, dbo.hist_group_chn_wk, dbo.hist_oh_group_chn_wk, dbo.oo_all_group_chn_wk, dbo.parameter_plan_elements, dbo.plan_group_chn_wk |
| dbo | [rpt_mar_location_md_home_$sp](dbo.rpt_mar_location_md_home_$sp.md) | dbo.calendar_merch_week, dbo.hist_cmp_group_loc_wk, dbo.hist_group_loc_wk, dbo.hist_oh_group_loc_wk, dbo.oo_all_group_loc_wk, dbo.parameter_plan_elements, dbo.plan_group_loc_wk |
| dbo | [rpt_mar_location_md_local_$sp](dbo.rpt_mar_location_md_local_$sp.md) | dbo.calendar_merch_week, dbo.hist_cmp_group_loc_wk, dbo.hist_group_loc_wk, dbo.hist_oh_group_loc_wk, dbo.oo_all_group_loc_wk, dbo.parameter_plan_elements, dbo.plan_group_loc_wk |
| dbo | [rpt_merchandise_allocation_$sp](dbo.rpt_merchandise_allocation_$sp.md) | dbo.hist_group_loc_wk, dbo.hist_oh_group_loc_li, dbo.post_parameter, dbo.view_calendar_merch_week_rel |
| dbo | [rpt_otb_chain_$sp](dbo.rpt_otb_chain_$sp.md) | dbo.calendar_merch_period, dbo.calendar_merch_week, dbo.hierarchy_level, dbo.hist_group_chn_pd, dbo.hist_oh_group_chn_pd, dbo.oo_all_group_chn_pd, dbo.parameter_plan_elements, dbo.plan_group_chn_pd, dbo.post_parameter, dbo.view_calendar_merch_pd_rel |
| dbo | [rpt_otb_cost_retail_$sp](dbo.rpt_otb_cost_retail_$sp.md) | dbo.location_parent, dbo.merch_group_parent, dbo.oo_all_group_loc_pd, dbo.oo_unc_group_loc_pd, dbo.plan_element, dbo.plan_group_loc_pd, dbo.plan_version, dbo.view_calendar_merch_pd_rel, dbo.view_otb_proj_bop_inv |
| dbo | [rpt_otb_location_$sp](dbo.rpt_otb_location_$sp.md) | dbo.calendar_merch_period, dbo.calendar_merch_week, dbo.hierarchy_group, dbo.hierarchy_level, dbo.hist_group_loc_pd, dbo.hist_oh_group_loc_pd, dbo.location, dbo.location_parent, dbo.oo_all_group_loc_pd, dbo.parameter_plan_elements, dbo.plan_group_loc_pd, dbo.post_parameter, dbo.view_calendar_merch_pd_rel |
| dbo | [rpt_par_chain_$sp](dbo.rpt_par_chain_$sp.md) | dbo.calendar_merch_period, dbo.calendar_merch_week, dbo.hist_group_chn_pd, dbo.hist_oh_group_chn_pd, dbo.oo_all_group_chn_pd, dbo.parameter_plan_elements, dbo.plan_element, dbo.plan_group_chn_pd, dbo.post_parameter |
| dbo | [rpt_par_chain_rim_$sp](dbo.rpt_par_chain_rim_$sp.md) | dbo.calendar_merch_period, dbo.calendar_merch_week, dbo.hist_group_chn_pd, dbo.hist_oh_group_chn_pd, dbo.hist_rim_oh_group_chn_pd, dbo.oo_all_group_chn_pd, dbo.parameter_plan_elements, dbo.plan_element, dbo.plan_group_chn_pd, dbo.post_parameter |
| dbo | [rpt_par_location_home_$sp](dbo.rpt_par_location_home_$sp.md) | dbo.calendar_merch_period, dbo.calendar_merch_week, dbo.hist_group_loc_pd, dbo.hist_oh_group_loc_pd, dbo.oo_all_group_loc_pd, dbo.parameter_plan_elements, dbo.plan_element, dbo.plan_group_loc_pd, dbo.post_parameter |
| dbo | [rpt_par_location_local_$sp](dbo.rpt_par_location_local_$sp.md) | dbo.calendar_merch_period, dbo.calendar_merch_week, dbo.hist_group_loc_pd, dbo.hist_oh_group_loc_pd, dbo.oo_all_group_loc_pd, dbo.parameter_plan_elements, dbo.plan_element, dbo.plan_group_loc_pd, dbo.post_parameter |
| dbo | [rpt_style_analysis_$sp](dbo.rpt_style_analysis_$sp.md) | dbo.calendar_date, dbo.calendar_merch_week, dbo.hierarchy_group, dbo.hist_oh_style_loc_li, dbo.hist_oh_style_loc_wk, dbo.hist_style_loc_li, dbo.hist_style_loc_wk, dbo.ib_activity_date, dbo.location, dbo.location_status, dbo.oo_all_style_chn_wk, dbo.oo_all_style_loc_li, dbo.post_parameter, dbo.price_status, dbo.style, dbo.style_parent |
| dbo | [rpt_style_color_sell_thru_$sp](dbo.rpt_style_color_sell_thru_$sp.md) | dbo.calendar_merch_week, dbo.color, dbo.hierarchy_group, dbo.hist_oh_styleclr_chn_li, dbo.hist_styleclr_chn_li, dbo.hist_styleclr_chn_wk, dbo.ib_activity_date, dbo.oo_all_styleclr_chn_li, dbo.price_status, dbo.style, dbo.style_color, dbo.style_parent, dbo.style_vendor, dbo.vendor |
| dbo | [rpt_style_listing_class_vendor_$sp](dbo.rpt_style_listing_class_vendor_$sp.md) | dbo.hist_cmp_style_chn_wk, dbo.hist_oh_style_chn_li, dbo.hist_oh_style_loc_wk, dbo.hist_style_chn_li, dbo.hist_style_chn_wk, dbo.location, dbo.oo_all_style_chn_li, dbo.post_parameter, dbo.view_calendar_merch_week_rel, dbo.view_ib_activity_date |
| dbo | [rpt_vendor_analysis_$sp](dbo.rpt_vendor_analysis_$sp.md) | dbo.calendar_merch_week, dbo.hierarchy_group, dbo.hierarchy_level, dbo.hist_cmp_style_chn_wk, dbo.hist_oh_style_chn_wk, dbo.hist_style_chn_wk, dbo.history_component, dbo.oo_all_style_chn_wk, dbo.style, dbo.style_parent |
| dbo | [spDW_Inventory](dbo.spDW_Inventory.md) | dbo.attribute, dbo.attribute_set, dbo.date_dim, dbo.entity_attribute_set, dbo.hierarchy_group, dbo.hist_oh_style_loc_li, dbo.hist_oh_style_loc_wk, dbo.jurisdiction, dbo.location, dbo.style, dbo.style_parent |
| -- Description: | [SQL taken from Smartlook report (ma topic) 980/960/1000 INV, including all locations](--_Description_.SQL_taken_from_Smartlook_report_ma_topic_980_960_1000_INV,_including_all_locations.md) |  |
| dbo | [spDW_TopStyleTy](dbo.spDW_TopStyleTy.md) | dbo.date_dim, dbo.hierarchy_group, dbo.hist_oh_style_loc_wk, dbo.hist_style_loc_wk, dbo.hist_style_loc_yr, dbo.jurisdiction, dbo.location, dbo.oo_all_style_loc_pd, dbo.style, dbo.style_parent, dbo.view_oh_style_loctype_wk, dbo.view_style_attribute_outer, dbo.view_style_cust_prop_outer |
| -- Description: | [SQL taken from Smartlook report (ma topic) Top Style TY. Using it here for reporting.](--_Description_SQL_taken_from_Smartlook_report_ma_topic_Top_Style_TY_Using_it_here_for_reporting..md) |  |
| ------- | [WEB SALES ---------------](-------.WEB_SALES_---------------.md) |  |
| dbo | [spDW_TopStyleTyBACKUP20180108](dbo.spDW_TopStyleTyBACKUP20180108.md) | dbo.date_dim, dbo.hierarchy_group, dbo.hist_oh_style_loc_wk, dbo.hist_style_loc_wk, dbo.hist_style_loc_yr, dbo.jurisdiction, dbo.location, dbo.oo_all_style_loc_pd, dbo.style, dbo.style_parent, dbo.view_oh_style_loctype_wk, dbo.view_style_attribute_outer, dbo.view_style_cust_prop_outer |
| -- Description: | [SQL taken from Smartlook report (ma topic) Top Style TY. Using it here for reporting.](--_Description_SQL_taken_from_Smartlook_report_ma_topic_Top_Style_TY_Using_it_here_for_reporting..md) |  |
| ------- | [WEB SALES ---------------](-------.WEB_SALES_---------------.md) |  |
| dbo | [spMerchandisingTopStyleStage](dbo.spMerchandisingTopStyleStage.md) | dbo.rptCurrRetail, dbo.rptDoorCount, dbo.rptInventory, dbo.rptTopStyleTY, dbo.style, dbo.vwDW_AgedStyles |
| -- Description: | [Stages data for Domo.](--_Description_Stages_data_for_Domo..md) |  |
| dbo | [spMerchandisingValidation](dbo.spMerchandisingValidation.md) | dbo.product_dim, dbo.vwDW_WeeklyOnHand_StyleColor, dbo.vwDW_WeeklyOnOrder_StyleColor, dbo.vwDW_WeeklySales_StyleColor |
| -- File name: | [Oursmerchdb01-ma_01-dbo-spMerchandisingValidation.sql](--_File_name_Oursmerchdb01-ma_01-dbo-spMerchandisingValidation.sql.md) |  |
| -- | [name:](--.name.md) |  |
| -- | [Zac Doerr](--.Zac_Doerr.md) |  |
| dbo | [spTimCTopStyleTesting](dbo.spTimCTopStyleTesting.md) | dbo.hierarchy_group, dbo.jurisdiction, dbo.location, dbo.oo_all_style_loc_li, dbo.oo_all_style_loc_pd, dbo.style, dbo.style_parent, dbo.TimCTopStyleTesting, dbo.view_hist_oh_style_loc_wk, dbo.view_hist_style_loc_wk, dbo.view_hist_style_loc_yr, dbo.view_oh_style_loctype_wk, dbo.view_style_attribute_outer, dbo.view_style_cust_prop_outer |
| dbo | [startup_cmp_group_$sp](dbo.startup_cmp_group_$sp.md) | dbo.startup_cmp_group_loc_li_$sp, dbo.startup_cmp_group_loc_pd_$sp, dbo.startup_cmp_group_loc_wk_$sp, dbo.startup_cmp_group_loc_yr_$sp, dbo.startup_error_handler_$sp, dbo.startup_multi_currency_main_log |
| dbo | [startup_cmp_group_loc_li_$sp](dbo.startup_cmp_group_loc_li_$sp.md) | dbo.hist_cmp_group_loc_li, dbo.hist_cmp_group_loc_yr, dbo.startup_multi_currency_group_log |
| dbo | [startup_cmp_group_loc_pd_$sp](dbo.startup_cmp_group_loc_pd_$sp.md) | dbo.calendar_merch_period, dbo.calendar_merch_week, dbo.dummy_hist_cmp_group_loc_pd, dbo.hist_cmp_group_loc_pd, dbo.hist_cmp_group_loc_wk, dbo.merch_year_pd_pf, dbo.startup_multi_currency_group_log |
| dbo | [startup_cmp_group_loc_wk_$sp](dbo.startup_cmp_group_loc_wk_$sp.md) | dbo.calendar_date, dbo.calendar_merch_week, dbo.cmp_group_currency_rate, dbo.dummy_hist_cmp_group_loc_wk, dbo.hist_cmp_group_loc_wk, dbo.merch_year_wk_pf, dbo.multi_currency_location_cost_wk, dbo.startup_multi_currency_group_log |
| dbo | [startup_cmp_group_loc_yr_$sp](dbo.startup_cmp_group_loc_yr_$sp.md) | dbo.calendar_merch_period, dbo.dummy_hist_cmp_group_loc_yr, dbo.hist_cmp_group_loc_pd, dbo.hist_cmp_group_loc_yr, dbo.merch_year_pf, dbo.startup_multi_currency_group_log |
| dbo | [startup_cmp_style_$sp](dbo.startup_cmp_style_$sp.md) | dbo.startup_cmp_style_loc_li_$sp, dbo.startup_cmp_style_loc_pd_$sp, dbo.startup_cmp_style_loc_wk_$sp, dbo.startup_cmp_style_loc_yr_$sp, dbo.startup_error_handler_$sp, dbo.startup_multi_currency_main_log |
| dbo | [startup_cmp_style_loc_li_$sp](dbo.startup_cmp_style_loc_li_$sp.md) | dbo.hist_cmp_style_loc_li, dbo.hist_cmp_style_loc_yr, dbo.startup_multi_currency_style_log |
| dbo | [startup_cmp_style_loc_pd_$sp](dbo.startup_cmp_style_loc_pd_$sp.md) | dbo.calendar_merch_period, dbo.calendar_merch_week, dbo.dummy_hist_cmp_style_loc_pd, dbo.hist_cmp_style_loc_pd, dbo.hist_cmp_style_loc_wk, dbo.merch_year_pd_pf, dbo.startup_multi_currency_style_log |
| dbo | [startup_cmp_style_loc_wk_$sp](dbo.startup_cmp_style_loc_wk_$sp.md) | dbo.calendar_date, dbo.calendar_merch_week, dbo.cmp_style_currency_rate, dbo.dummy_hist_cmp_style_loc_wk, dbo.hist_cmp_style_loc_wk, dbo.merch_year_wk_pf, dbo.multi_currency_location_cost_wk, dbo.startup_multi_currency_style_log |
| dbo | [startup_cmp_style_loc_yr_$sp](dbo.startup_cmp_style_loc_yr_$sp.md) | dbo.calendar_merch_period, dbo.dummy_hist_cmp_style_loc_yr, dbo.hist_cmp_style_loc_pd, dbo.hist_cmp_style_loc_yr, dbo.merch_year_pf, dbo.startup_multi_currency_style_log |
| dbo | [startup_cmp_styleclr_$sp](dbo.startup_cmp_styleclr_$sp.md) | dbo.startup_cmp_styleclr_loc_li_$sp, dbo.startup_cmp_styleclr_loc_pd_$sp, dbo.startup_cmp_styleclr_loc_wk_$sp, dbo.startup_cmp_styleclr_loc_yr_$sp, dbo.startup_error_handler_$sp, dbo.startup_multi_currency_main_log |
| dbo | [startup_cmp_styleclr_loc_li_$sp](dbo.startup_cmp_styleclr_loc_li_$sp.md) | dbo.hist_cmp_styleclr_loc_li, dbo.hist_cmp_styleclr_loc_yr, dbo.startup_multi_currency_styleclr_log |
| dbo | [startup_cmp_styleclr_loc_pd_$sp](dbo.startup_cmp_styleclr_loc_pd_$sp.md) | dbo.calendar_merch_period, dbo.calendar_merch_week, dbo.dummy_hist_cmp_styleclr_loc_pd, dbo.hist_cmp_styleclr_loc_pd, dbo.hist_cmp_styleclr_loc_wk, dbo.merch_year_pd_pf, dbo.startup_multi_currency_styleclr_log |
| dbo | [startup_cmp_styleclr_loc_wk_$sp](dbo.startup_cmp_styleclr_loc_wk_$sp.md) | dbo.calendar_date, dbo.calendar_merch_week, dbo.cmp_styleclr_currency_rate, dbo.dummy_hist_cmp_styleclr_loc_wk, dbo.hist_cmp_styleclr_loc_wk, dbo.merch_year_wk_pf, dbo.multi_currency_location_cost_wk, dbo.startup_multi_currency_styleclr_log |
| dbo | [startup_cmp_styleclr_loc_yr_$sp](dbo.startup_cmp_styleclr_loc_yr_$sp.md) | dbo.calendar_merch_period, dbo.dummy_hist_cmp_styleclr_loc_yr, dbo.hist_cmp_styleclr_loc_pd, dbo.hist_cmp_styleclr_loc_yr, dbo.merch_year_pf, dbo.startup_multi_currency_styleclr_log |
| dbo | [startup_error_handler_$sp](dbo.startup_error_handler_$sp.md) | dbo.startup_error_log |
| CREATE proc [dbo].[startup_error_handler_$sp] | [( @job_type INT](CREATE_proc_dbo_startup_error_handler_$sp_._@job_type_INT.md) |  |
| dbo | [startup_flsh_$sp](dbo.startup_flsh_$sp.md) | dbo.startup_error_handler_$sp, dbo.startup_flsh_group_loc_da_$sp, dbo.startup_flsh_loc_da_$sp, dbo.startup_flsh_style_loc_da_$sp, dbo.startup_multi_currency_main_log |
| dbo | [startup_flsh_group_loc_da_$sp](dbo.startup_flsh_group_loc_da_$sp.md) | dbo.calendar_date, dbo.country, dbo.flsh_group_loc_rate_by_date, dbo.hist_flsh_group_loc_da, dbo.jurisdiction, dbo.location, dbo.startup_multi_currency_group_log, dbo.syn_currency_conversion |
| dbo | [startup_flsh_loc_da_$sp](dbo.startup_flsh_loc_da_$sp.md) | dbo.calendar_date, dbo.country, dbo.flsh_loc_rate_by_date, dbo.hist_flsh_loc_da, dbo.jurisdiction, dbo.location, dbo.startup_multi_currency_group_log, dbo.syn_currency_conversion |
| dbo | [startup_flsh_style_loc_da_$sp](dbo.startup_flsh_style_loc_da_$sp.md) | dbo.calendar_date, dbo.country, dbo.flsh_style_loc_rate_by_date, dbo.hist_flsh_style_loc_da, dbo.jurisdiction, dbo.location, dbo.startup_multi_currency_style_log, dbo.syn_currency_conversion |
| dbo | [startup_group_loc_li_$sp](dbo.startup_group_loc_li_$sp.md) | dbo.hist_group_loc_li, dbo.hist_group_loc_yr, dbo.startup_multi_currency_group_log |
| dbo | [startup_group_loc_pd_$sp](dbo.startup_group_loc_pd_$sp.md) | dbo.calendar_merch_period, dbo.calendar_merch_week, dbo.dummy_hist_group_loc_pd, dbo.hist_group_loc_pd, dbo.hist_group_loc_wk, dbo.merch_year_pd_pf, dbo.startup_multi_currency_group_log |
| dbo | [startup_group_loc_wk_$sp](dbo.startup_group_loc_wk_$sp.md) | dbo.calendar_date, dbo.calendar_merch_week, dbo.dummy_hist_group_loc_wk, dbo.group_currency_rate, dbo.hist_group_loc_wk, dbo.merch_year_wk_pf, dbo.multi_currency_location_cost_wk, dbo.multi_currency_location_retail_wk, dbo.startup_multi_currency_group_log |
| dbo | [startup_group_loc_yr_$sp](dbo.startup_group_loc_yr_$sp.md) | dbo.calendar_merch_period, dbo.dummy_hist_group_loc_yr, dbo.hist_group_loc_pd, dbo.hist_group_loc_yr, dbo.merch_year_pf, dbo.startup_multi_currency_group_log |
| dbo | [startup_hist_group_$sp](dbo.startup_hist_group_$sp.md) | dbo.startup_error_handler_$sp, dbo.startup_group_loc_li_$sp, dbo.startup_group_loc_pd_$sp, dbo.startup_group_loc_wk_$sp, dbo.startup_group_loc_yr_$sp, dbo.startup_multi_currency_main_log |
| dbo | [startup_hist_rim_oh_group_$sp](dbo.startup_hist_rim_oh_group_$sp.md) | dbo.calendar_merch_period, dbo.calendar_merch_week, dbo.h, dbo.hist_rim_oh_group_chn_li, dbo.hist_rim_oh_group_chn_pd, dbo.hist_rim_oh_group_chn_yr, dbo.hist_rim_oh_group_loc_li, dbo.hist_rim_oh_group_loc_pd, dbo.hist_rim_oh_group_loc_yr, dbo.post_parameter |
| dbo | [startup_hist_style_$sp](dbo.startup_hist_style_$sp.md) | dbo.startup_error_handler_$sp, dbo.startup_multi_currency_main_log, dbo.startup_style_loc_li_$sp, dbo.startup_style_loc_pd_$sp, dbo.startup_style_loc_wk_$sp, dbo.startup_style_loc_yr_$sp |
| dbo | [startup_hist_styleclr_$sp](dbo.startup_hist_styleclr_$sp.md) | dbo.startup_error_handler_$sp, dbo.startup_multi_currency_main_log, dbo.startup_styleclr_loc_li_$sp, dbo.startup_styleclr_loc_pd_$sp, dbo.startup_styleclr_loc_wk_$sp, dbo.startup_styleclr_loc_yr_$sp |
| dbo | [startup_oh_group_$sp](dbo.startup_oh_group_$sp.md) | dbo.startup_error_handler_$sp, dbo.startup_multi_currency_main_log, dbo.startup_oh_group_loc_li_$sp, dbo.startup_oh_group_loc_pd_$sp, dbo.startup_oh_group_loc_wk_$sp, dbo.startup_oh_group_loc_yr_$sp |
| dbo | [startup_oh_group_loc_li_$sp](dbo.startup_oh_group_loc_li_$sp.md) | dbo.hist_oh_group_loc_li, dbo.hist_oh_group_loc_yr, dbo.startup_multi_currency_group_log |
| dbo | [startup_oh_group_loc_pd_$sp](dbo.startup_oh_group_loc_pd_$sp.md) | dbo.calendar_merch_period, dbo.calendar_merch_week, dbo.dummy_hist_oh_group_loc_pd, dbo.hist_oh_group_loc_pd, dbo.hist_oh_group_loc_wk, dbo.merch_year_pd_pf, dbo.startup_multi_currency_group_log |
| dbo | [startup_oh_group_loc_wk_$sp](dbo.startup_oh_group_loc_wk_$sp.md) | dbo.calendar_date, dbo.calendar_merch_week, dbo.dummy_hist_oh_group_loc_wk, dbo.hist_oh_group_loc_wk, dbo.merch_year_wk_pf, dbo.multi_currency_location_cost_wk, dbo.multi_currency_location_retail_wk, dbo.oh_group_currency_rate, dbo.startup_multi_currency_group_log |
| dbo | [startup_oh_group_loc_yr_$sp](dbo.startup_oh_group_loc_yr_$sp.md) | dbo.calendar_merch_period, dbo.dummy_hist_oh_group_loc_yr, dbo.hist_oh_group_loc_pd, dbo.hist_oh_group_loc_yr, dbo.merch_year_pf, dbo.startup_multi_currency_group_log |
| dbo | [startup_oh_style_$sp](dbo.startup_oh_style_$sp.md) | dbo.startup_error_handler_$sp, dbo.startup_multi_currency_main_log, dbo.startup_oh_style_loc_li_$sp, dbo.startup_oh_style_loc_pd_$sp, dbo.startup_oh_style_loc_wk_$sp, dbo.startup_oh_style_loc_yr_$sp |
| dbo | [startup_oh_style_loc_li_$sp](dbo.startup_oh_style_loc_li_$sp.md) | dbo.hist_oh_style_loc_li, dbo.hist_oh_style_loc_yr, dbo.startup_multi_currency_style_log |
| dbo | [startup_oh_style_loc_pd_$sp](dbo.startup_oh_style_loc_pd_$sp.md) | dbo.calendar_merch_period, dbo.calendar_merch_week, dbo.dummy_hist_oh_style_loc_pd, dbo.hist_oh_style_loc_pd, dbo.hist_oh_style_loc_wk, dbo.merch_year_pd_pf, dbo.startup_multi_currency_style_log |
| dbo | [startup_oh_style_loc_wk_$sp](dbo.startup_oh_style_loc_wk_$sp.md) | dbo.calendar_date, dbo.calendar_merch_week, dbo.dummy_hist_oh_style_loc_wk, dbo.hist_oh_style_loc_wk, dbo.merch_year_wk_pf, dbo.multi_currency_location_cost_wk, dbo.multi_currency_location_retail_wk, dbo.oh_style_currency_rate, dbo.startup_multi_currency_style_log |
| dbo | [startup_oh_style_loc_yr_$sp](dbo.startup_oh_style_loc_yr_$sp.md) | dbo.calendar_merch_period, dbo.dummy_hist_oh_style_loc_yr, dbo.hist_oh_style_loc_pd, dbo.hist_oh_style_loc_yr, dbo.merch_year_pf, dbo.startup_multi_currency_style_log |
| dbo | [startup_oh_styleclr_$sp](dbo.startup_oh_styleclr_$sp.md) | dbo.startup_error_handler_$sp, dbo.startup_multi_currency_main_log, dbo.startup_oh_styleclr_loc_li_$sp, dbo.startup_oh_styleclr_loc_pd_$sp, dbo.startup_oh_styleclr_loc_wk_$sp, dbo.startup_oh_styleclr_loc_yr_$sp |
| dbo | [startup_oh_styleclr_loc_li_$sp](dbo.startup_oh_styleclr_loc_li_$sp.md) | dbo.hist_oh_styleclr_loc_li, dbo.hist_oh_styleclr_loc_yr, dbo.startup_multi_currency_styleclr_log |
| dbo | [startup_oh_styleclr_loc_pd_$sp](dbo.startup_oh_styleclr_loc_pd_$sp.md) | dbo.calendar_merch_period, dbo.calendar_merch_week, dbo.dummy_hist_oh_styleclr_loc_pd, dbo.hist_oh_styleclr_loc_pd, dbo.hist_oh_styleclr_loc_wk, dbo.merch_year_pd_pf, dbo.startup_multi_currency_styleclr_log |
| dbo | [startup_oh_styleclr_loc_wk_$sp](dbo.startup_oh_styleclr_loc_wk_$sp.md) | dbo.calendar_date, dbo.calendar_merch_week, dbo.dummy_hist_oh_styleclr_loc_wk, dbo.hist_oh_styleclr_loc_wk, dbo.merch_year_wk_pf, dbo.multi_currency_location_retail_wk, dbo.oh_styleclr_currency_rate, dbo.startup_multi_currency_styleclr_log |
| dbo | [startup_oh_styleclr_loc_yr_$sp](dbo.startup_oh_styleclr_loc_yr_$sp.md) | dbo.calendar_merch_period, dbo.dummy_hist_oh_styleclr_loc_yr, dbo.hist_oh_styleclr_loc_pd, dbo.hist_oh_styleclr_loc_yr, dbo.merch_year_pf, dbo.startup_multi_currency_styleclr_log |
| dbo | [startup_oo_all_$sp](dbo.startup_oo_all_$sp.md) | dbo.startup_error_handler_$sp, dbo.startup_multi_currency_main_log, dbo.startup_oo_all_group_$sp, dbo.startup_oo_all_style_$sp, dbo.startup_oo_all_styleclr_$sp |
| dbo | [startup_oo_all_group_$sp](dbo.startup_oo_all_group_$sp.md) | dbo.calendar_date, dbo.calendar_merch_week, dbo.multi_currency_location_cost_wk, dbo.multi_currency_location_retail_wk, dbo.oo_all_group_currency_rate, dbo.oo_all_group_loc_li, dbo.oo_all_group_loc_pd, dbo.oo_all_group_loc_wk, dbo.oo_all_group_loc_yr, dbo.startup_multi_currency_group_log |
| dbo | [startup_oo_all_style_$sp](dbo.startup_oo_all_style_$sp.md) | dbo.calendar_date, dbo.calendar_merch_week, dbo.multi_currency_location_cost_wk, dbo.multi_currency_location_retail_wk, dbo.oo_all_style_currency_rate, dbo.oo_all_style_loc_li, dbo.oo_all_style_loc_pd, dbo.oo_all_style_loc_wk, dbo.oo_all_style_loc_yr, dbo.startup_multi_currency_style_log |
| dbo | [startup_oo_all_styleclr_$sp](dbo.startup_oo_all_styleclr_$sp.md) | dbo.calendar_date, dbo.calendar_merch_week, dbo.multi_currency_location_retail_wk, dbo.oo_all_styleclr_currency_rate, dbo.oo_all_styleclr_loc_li, dbo.oo_all_styleclr_loc_pd, dbo.oo_all_styleclr_loc_wk, dbo.oo_all_styleclr_loc_yr, dbo.startup_multi_currency_styleclr_log |
| dbo | [startup_plan_$sp](dbo.startup_plan_$sp.md) | dbo.startup_error_handler_$sp, dbo.startup_multi_currency_main_log, dbo.startup_plan_group_chn_$sp, dbo.startup_plan_group_loc_pd_$sp, dbo.startup_plan_group_loc_wk_$sp |
| dbo | [startup_plan_group_chn_$sp](dbo.startup_plan_group_chn_$sp.md) | dbo.plan_group_chn_pd, dbo.plan_group_chn_wk, dbo.startup_multi_currency_group_log |
| dbo | [startup_plan_group_loc_pd_$sp](dbo.startup_plan_group_loc_pd_$sp.md) | dbo.calendar_date, dbo.multi_currency_location_cost_pd, dbo.multi_currency_location_retail_pd, dbo.plan_element, dbo.plan_group_loc_pd, dbo.plan_group_loc_pd_currency_rate, dbo.startup_multi_currency_group_log |
| dbo | [startup_plan_group_loc_wk_$sp](dbo.startup_plan_group_loc_wk_$sp.md) | dbo.calendar_date, dbo.multi_currency_location_cost_wk, dbo.multi_currency_location_retail_wk, dbo.plan_element, dbo.plan_group_loc_wk, dbo.plan_group_loc_wk_currency_rate, dbo.startup_multi_currency_group_log |
| dbo | [startup_style_loc_li_$sp](dbo.startup_style_loc_li_$sp.md) | dbo.hist_style_loc_li, dbo.hist_style_loc_yr, dbo.startup_multi_currency_style_log |
| dbo | [startup_style_loc_pd_$sp](dbo.startup_style_loc_pd_$sp.md) | dbo.calendar_merch_period, dbo.calendar_merch_week, dbo.dummy_hist_style_loc_pd, dbo.hist_style_loc_pd, dbo.hist_style_loc_wk, dbo.merch_year_pd_pf, dbo.startup_multi_currency_style_log |
| dbo | [startup_style_loc_wk_$sp](dbo.startup_style_loc_wk_$sp.md) | dbo.calendar_date, dbo.calendar_merch_week, dbo.dummy_hist_style_loc_wk, dbo.hist_style_loc_wk, dbo.merch_year_wk_pf, dbo.multi_currency_location_cost_wk, dbo.multi_currency_location_retail_wk, dbo.startup_multi_currency_style_log, dbo.style_currency_rate |
| dbo | [startup_style_loc_yr_$sp](dbo.startup_style_loc_yr_$sp.md) | dbo.calendar_merch_period, dbo.dummy_hist_style_loc_yr, dbo.hist_style_loc_pd, dbo.hist_style_loc_yr, dbo.merch_year_pf, dbo.startup_multi_currency_style_log |
| dbo | [startup_styleclr_loc_li_$sp](dbo.startup_styleclr_loc_li_$sp.md) | dbo.hist_styleclr_loc_li, dbo.hist_styleclr_loc_yr, dbo.startup_multi_currency_styleclr_log |
| dbo | [startup_styleclr_loc_pd_$sp](dbo.startup_styleclr_loc_pd_$sp.md) | dbo.calendar_merch_period, dbo.calendar_merch_week, dbo.dummy_hist_styleclr_loc_pd, dbo.hist_styleclr_loc_pd, dbo.hist_styleclr_loc_wk, dbo.merch_year_pd_pf, dbo.startup_multi_currency_styleclr_log |
| dbo | [startup_styleclr_loc_wk_$sp](dbo.startup_styleclr_loc_wk_$sp.md) | dbo.calendar_date, dbo.calendar_merch_week, dbo.dummy_hist_styleclr_loc_wk, dbo.hist_styleclr_loc_wk, dbo.merch_year_wk_pf, dbo.multi_currency_location_cost_wk, dbo.multi_currency_location_retail_wk, dbo.startup_multi_currency_styleclr_log, dbo.styleclr_currency_rate |
| dbo | [startup_styleclr_loc_yr_$sp](dbo.startup_styleclr_loc_yr_$sp.md) | dbo.calendar_merch_period, dbo.dummy_hist_styleclr_loc_yr, dbo.hist_styleclr_loc_pd, dbo.hist_styleclr_loc_yr, dbo.merch_year_pf, dbo.startup_multi_currency_styleclr_log |
| dbo | [summarize_hist_cmp_group_$sp](dbo.summarize_hist_cmp_group_$sp.md) | dbo.calendar_merch_period, dbo.calendar_merch_week, dbo.hist_cmp_group_chn_li, dbo.hist_cmp_group_chn_pd, dbo.hist_cmp_group_chn_wk, dbo.hist_cmp_group_chn_yr, dbo.hist_cmp_group_loc_li, dbo.hist_cmp_group_loc_pd, dbo.hist_cmp_group_loc_wk, dbo.hist_cmp_group_loc_yr |
| dbo | [summarize_hist_cmp_sku_$sp](dbo.summarize_hist_cmp_sku_$sp.md) | dbo.calendar_merch_period, dbo.calendar_merch_week, dbo.hist_cmp_sku_chn_li, dbo.hist_cmp_sku_chn_pd, dbo.hist_cmp_sku_chn_wk, dbo.hist_cmp_sku_chn_yr, dbo.hist_cmp_sku_loc_li, dbo.hist_cmp_sku_loc_pd, dbo.hist_cmp_sku_loc_wk, dbo.hist_cmp_sku_loc_yr |
| dbo | [summarize_hist_cmp_style_$sp](dbo.summarize_hist_cmp_style_$sp.md) | dbo.calendar_merch_period, dbo.calendar_merch_week, dbo.hist_cmp_style_chn_li, dbo.hist_cmp_style_chn_pd, dbo.hist_cmp_style_chn_wk, dbo.hist_cmp_style_chn_yr, dbo.hist_cmp_style_loc_li, dbo.hist_cmp_style_loc_pd, dbo.hist_cmp_style_loc_wk, dbo.hist_cmp_style_loc_yr |
| dbo | [summarize_hist_cmp_styleclr_$sp](dbo.summarize_hist_cmp_styleclr_$sp.md) | dbo.calendar_merch_period, dbo.calendar_merch_week, dbo.hist_cmp_styleclr_chn_li, dbo.hist_cmp_styleclr_chn_pd, dbo.hist_cmp_styleclr_chn_wk, dbo.hist_cmp_styleclr_chn_yr, dbo.hist_cmp_styleclr_loc_li, dbo.hist_cmp_styleclr_loc_pd, dbo.hist_cmp_styleclr_loc_wk, dbo.hist_cmp_styleclr_loc_yr |
| dbo | [validate_cmp_$sp](dbo.validate_cmp_$sp.md) | dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.posting_parameter, dbo.return_debug_flag_$sp, dbo.wrk_cmp_group_loc_wk, dbo.wrk_cmp_sku_loc_wk, dbo.wrk_cmp_style_loc_wk, dbo.wrk_cmp_styleclr_loc_wk |
| dbo | [validate_flash_$sp](dbo.validate_flash_$sp.md) | dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.posting_parameter, dbo.return_debug_flag_$sp, dbo.wrk_flsh_group_loc_da, dbo.wrk_flsh_style_loc_da |
| dbo | [validate_hist_$sp](dbo.validate_hist_$sp.md) | dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.posting_parameter, dbo.return_debug_flag_$sp, dbo.wrk_group_loc_wk, dbo.wrk_sku_loc_wk, dbo.wrk_style_loc_wk, dbo.wrk_styleclr_loc_wk |
| dbo | [validate_oh_$sp](dbo.validate_oh_$sp.md) | dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.posting_parameter, dbo.return_debug_flag_$sp, dbo.wrk_oh_group_loc_wk, dbo.wrk_oh_sku_loc_wk, dbo.wrk_oh_style_loc_wk, dbo.wrk_oh_styleclr_loc_wk |
| dbo | [validate_oo_all_$sp](dbo.validate_oo_all_$sp.md) | dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.posting_parameter, dbo.return_debug_flag_$sp, dbo.wrk_oo_all_group_loc_wk, dbo.wrk_oo_all_sku_loc_wk, dbo.wrk_oo_all_style_loc_wk, dbo.wrk_oo_all_styleclr_loc_wk |
| dbo | [validate_wrk_cmp_$sp](dbo.validate_wrk_cmp_$sp.md) | dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.posting_parameter, dbo.return_debug_flag_$sp |
| dbo | [validate_wrk_flash_$sp](dbo.validate_wrk_flash_$sp.md) | dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.posting_parameter, dbo.return_debug_flag_$sp |
| dbo | [validate_wrk_hist_$sp](dbo.validate_wrk_hist_$sp.md) | dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.posting_parameter, dbo.return_debug_flag_$sp |
| dbo | [validate_wrk_ib_$sp](dbo.validate_wrk_ib_$sp.md) | dbo.job_error_handler_$sp, dbo.job_progress_handler_$sp, dbo.posting_parameter, dbo.return_debug_flag_$sp, dbo.validate_wrk_ib_allocation_$sp, dbo.validate_wrk_ib_cost_fact_$sp, dbo.validate_wrk_ib_inventory_$sp, dbo.validate_wrk_ib_on_order_$sp |
| dbo | [validate_wrk_ib_allocation_$sp](dbo.validate_wrk_ib_allocation_$sp.md) | dbo.job_error_handler_$sp, dbo.job_header, dbo.job_info, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp |
| dbo | [validate_wrk_ib_cost_fact_$sp](dbo.validate_wrk_ib_cost_fact_$sp.md) | dbo.job_error_handler_$sp, dbo.job_header, dbo.job_info, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp |
| dbo | [validate_wrk_ib_inventory_$sp](dbo.validate_wrk_ib_inventory_$sp.md) | dbo.get_current_week_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_info, dbo.job_progress_handler_$sp, dbo.post_parameter, dbo.return_debug_flag_$sp, dbo.wrk_ib_inventory |
| dbo | [validate_wrk_ib_on_order_$sp](dbo.validate_wrk_ib_on_order_$sp.md) | dbo.job_error_handler_$sp, dbo.job_header, dbo.job_info, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp |
| dbo | [validate_wrk_oh_$sp](dbo.validate_wrk_oh_$sp.md) | dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.posting_parameter, dbo.return_debug_flag_$sp |
| dbo | [validate_wrk_oo_all_$sp](dbo.validate_wrk_oo_all_$sp.md) | dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.posting_parameter, dbo.return_debug_flag_$sp |
| dbo | [wpost_all_group_$sp](dbo.wpost_all_group_$sp.md) | dbo.calendar_date, dbo.is_tax_exclusive_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_all_style_alt_group, dbo.wrk_ib_allocation, dbo.wrk_oo_all_group_loc_wk |
| dbo | [wpost_all_sku_$sp](dbo.wpost_all_sku_$sp.md) | dbo.calendar_date, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_allocation, dbo.wrk_oo_all_sku_loc_wk |
| dbo | [wpost_all_style_$sp](dbo.wpost_all_style_$sp.md) | dbo.calendar_date, dbo.is_tax_exclusive_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_allocation, dbo.wrk_oo_all_style_loc_wk |
| dbo | [wpost_all_style_color_$sp](dbo.wpost_all_style_color_$sp.md) | dbo.calendar_date, dbo.is_tax_exclusive_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_allocation, dbo.wrk_oo_all_styleclr_loc_wk |
| dbo | [wpost_cf_cmp_group_$sp](dbo.wpost_cf_cmp_group_$sp.md) | dbo.calendar_date, dbo.component_xref, dbo.history_component, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_cmp_group_loc_wk, dbo.wrk_ib_cfd_style_alt_group, dbo.wrk_ib_cost_factor_discount, dbo.wrk_ib_iv_style_alt_group |
| dbo | [wpost_cf_cmp_style_$sp](dbo.wpost_cf_cmp_style_$sp.md) | dbo.calendar_date, dbo.component_xref, dbo.history_component, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_cmp_style_loc_wk, dbo.wrk_ib_cost_factor_discount |
| dbo | [wpost_cf_cmp_style_color_$sp](dbo.wpost_cf_cmp_style_color_$sp.md) | dbo.calendar_date, dbo.component_xref, dbo.history_component, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_cmp_styleclr_loc_wk, dbo.wrk_ib_cost_factor_discount |
| dbo | [wpost_cf_hist_group_$sp](dbo.wpost_cf_hist_group_$sp.md) | dbo.calendar_date, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_group_loc_wk, dbo.wrk_ib_cfd_style_alt_group, dbo.wrk_ib_cost_factor_discount |
| dbo | [wpost_cf_hist_style_$sp](dbo.wpost_cf_hist_style_$sp.md) | dbo.calendar_date, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_cost_factor_discount, dbo.wrk_style_loc_wk |
| dbo | [wpost_cmp_sku_$sp](dbo.wpost_cmp_sku_$sp.md) | dbo.calendar_date, dbo.component_xref, dbo.history_component, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_cmp_sku_loc_wk, dbo.wrk_ib_inventory |
| dbo | [wpost_flash_group_$sp](dbo.wpost_flash_group_$sp.md) | dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_flsh_group_loc_da, dbo.wrk_ib_inventory, dbo.wrk_ib_iv_style_alt_group |
| dbo | [wpost_flash_style_$sp](dbo.wpost_flash_style_$sp.md) | dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_flsh_style_loc_da, dbo.wrk_ib_inventory |
| dbo | [wpost_hist_sku_$sp](dbo.wpost_hist_sku_$sp.md) | dbo.calendar_date, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_inventory, dbo.wrk_sku_loc_wk |
| Created by | [: Pierrette Lemay](Created_by._Pierrette_Lemay.md) |  |
| dbo | [wpost_hist_style_color_$sp](dbo.wpost_hist_style_color_$sp.md) | dbo.calendar_date, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_inventory, dbo.wrk_styleclr_loc_wk |
| Created by | [: Pierrette Lemay](Created_by._Pierrette_Lemay.md) |  |
| dbo | [wpost_iv_cmp_group_$sp](dbo.wpost_iv_cmp_group_$sp.md) | dbo.calendar_date, dbo.component_xref, dbo.history_component, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_cmp_group_loc_wk, dbo.wrk_ib_inventory, dbo.wrk_ib_iv_style_alt_group |
| dbo | [wpost_iv_cmp_style_$sp](dbo.wpost_iv_cmp_style_$sp.md) | dbo.calendar_date, dbo.component_xref, dbo.history_component, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_cmp_style_loc_wk, dbo.wrk_ib_inventory |
| dbo | [wpost_iv_cmp_style_color_$sp](dbo.wpost_iv_cmp_style_color_$sp.md) | dbo.calendar_date, dbo.component_xref, dbo.history_component, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_cmp_styleclr_loc_wk, dbo.wrk_ib_inventory |
| dbo | [wpost_iv_hist_group_$sp](dbo.wpost_iv_hist_group_$sp.md) | dbo.calendar_date, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_group_loc_wk, dbo.wrk_ib_inventory, dbo.wrk_ib_iv_style_alt_group |
| Created by | [: Pierrette Lemay](Created_by._Pierrette_Lemay.md) |  |
| Modified | [: April 2009 Corrected the sign of transfer_out_units/retail/retail_te/cost in the INSERT statement.](Modified_April_2009_Corrected_the_sign_of_transfer_out_units_retail_retail_te_cost_in_the_INSERT_statement..md) |  |
| dbo | [wpost_iv_hist_style_$sp](dbo.wpost_iv_hist_style_$sp.md) | dbo.calendar_date, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_inventory, dbo.wrk_style_loc_wk |
| Created by | [: Pierrette Lemay](Created_by._Pierrette_Lemay.md) |  |
| Modified | [: April 2009 Corrected the sign of transfer_out_units/retail/retail_te/cost in the INSERT statement.](Modified_April_2009_Corrected_the_sign_of_transfer_out_units_retail_retail_te_cost_in_the_INSERT_statement..md) |  |
| dbo | [wpost_oh_group_$sp](dbo.wpost_oh_group_$sp.md) | dbo.calendar_date, dbo.calendar_merch_week, dbo.get_last_range_end_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_inventory, dbo.wrk_ib_iv_style_alt_group, dbo.wrk_oh_group_loc_wk |
| dbo | [wpost_oh_sku_$sp](dbo.wpost_oh_sku_$sp.md) | dbo.calendar_date, dbo.calendar_merch_week, dbo.get_last_range_end_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_inventory, dbo.wrk_oh_sku_loc_wk |
| dbo | [wpost_oh_style_$sp](dbo.wpost_oh_style_$sp.md) | dbo.calendar_date, dbo.calendar_merch_week, dbo.get_last_range_end_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_inventory, dbo.wrk_oh_style_loc_wk |
| dbo | [wpost_oh_style_color_$sp](dbo.wpost_oh_style_color_$sp.md) | dbo.calendar_date, dbo.calendar_merch_week, dbo.get_last_range_end_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_inventory, dbo.wrk_oh_styleclr_loc_wk |
| dbo | [wpost_oo_group_$sp](dbo.wpost_oo_group_$sp.md) | dbo.calendar_date, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_on_order, dbo.wrk_ib_oo_style_alt_group, dbo.wrk_oo_all_group_loc_wk |
| dbo | [wpost_oo_sku_$sp](dbo.wpost_oo_sku_$sp.md) | dbo.calendar_date, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_on_order, dbo.wrk_oo_all_sku_loc_wk |
| dbo | [wpost_oo_style_$sp](dbo.wpost_oo_style_$sp.md) | dbo.calendar_date, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_on_order, dbo.wrk_oo_all_style_loc_wk |
| dbo | [wpost_oo_style_color_$sp](dbo.wpost_oo_style_color_$sp.md) | dbo.calendar_date, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_on_order, dbo.wrk_oo_all_styleclr_loc_wk |
| dbo | [wprep_all_group_$sp](dbo.wprep_all_group_$sp.md) | dbo.get_job_params_$sp, dbo.get_last_range_end_$sp, dbo.get_max_wrk_ib_allocation_id_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_allocation |
| dbo | [wprep_all_sku_$sp](dbo.wprep_all_sku_$sp.md) | dbo.get_job_params_$sp, dbo.get_last_range_end_$sp, dbo.get_max_wrk_ib_allocation_id_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_allocation |
| dbo | [wprep_all_style_$sp](dbo.wprep_all_style_$sp.md) | dbo.get_job_params_$sp, dbo.get_last_range_end_$sp, dbo.get_max_wrk_ib_allocation_id_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_allocation |
| dbo | [wprep_all_style_color_$sp](dbo.wprep_all_style_color_$sp.md) | dbo.get_job_params_$sp, dbo.get_last_range_end_$sp, dbo.get_max_wrk_ib_allocation_id_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_allocation |
| dbo | [wprep_cf_cmp_group_$sp](dbo.wprep_cf_cmp_group_$sp.md) | dbo.get_job_params_$sp, dbo.get_last_range_end_$sp, dbo.get_max_wrk_ib_cf_id_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_cost_factor_discount |
| dbo | [wprep_cf_cmp_style_$sp](dbo.wprep_cf_cmp_style_$sp.md) | dbo.get_job_params_$sp, dbo.get_last_range_end_$sp, dbo.get_max_wrk_ib_cf_id_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_cost_factor_discount |
| dbo | [wprep_cf_cmp_style_color_$sp](dbo.wprep_cf_cmp_style_color_$sp.md) | dbo.get_job_params_$sp, dbo.get_last_range_end_$sp, dbo.get_max_wrk_ib_cf_id_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_cost_factor_discount |
| dbo | [wprep_cf_hist_group_$sp](dbo.wprep_cf_hist_group_$sp.md) | dbo.get_job_params_$sp, dbo.get_last_range_end_$sp, dbo.get_max_wrk_ib_cf_id_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_cost_factor_discount |
| dbo | [wprep_cf_hist_style_$sp](dbo.wprep_cf_hist_style_$sp.md) | dbo.get_job_params_$sp, dbo.get_last_range_end_$sp, dbo.get_max_wrk_ib_cf_id_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_cost_factor_discount |
| dbo | [wprep_cmp_sku_$sp](dbo.wprep_cmp_sku_$sp.md) | dbo.get_job_params_$sp, dbo.get_last_range_end_$sp, dbo.get_max_wrk_ib_inventory_id_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_inventory |
| dbo | [wprep_flash_group_$sp](dbo.wprep_flash_group_$sp.md) | dbo.get_job_params_$sp, dbo.get_last_range_end_$sp, dbo.get_max_wrk_ib_inventory_id_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_inventory |
| dbo | [wprep_flash_style_$sp](dbo.wprep_flash_style_$sp.md) | dbo.get_job_params_$sp, dbo.get_last_range_end_$sp, dbo.get_max_wrk_ib_inventory_id_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_inventory |
| dbo | [wprep_hist_sku_$sp](dbo.wprep_hist_sku_$sp.md) | dbo.get_job_params_$sp, dbo.get_last_range_end_$sp, dbo.get_max_wrk_ib_inventory_id_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_inventory |
| dbo | [wprep_hist_style_color_$sp](dbo.wprep_hist_style_color_$sp.md) | dbo.get_job_params_$sp, dbo.get_last_range_end_$sp, dbo.get_max_wrk_ib_inventory_id_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_inventory |
| dbo | [wprep_iv_cmp_group_$sp](dbo.wprep_iv_cmp_group_$sp.md) | dbo.get_job_params_$sp, dbo.get_last_range_end_$sp, dbo.get_max_wrk_ib_inventory_id_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_inventory |
| dbo | [wprep_iv_cmp_style_$sp](dbo.wprep_iv_cmp_style_$sp.md) | dbo.get_job_params_$sp, dbo.get_last_range_end_$sp, dbo.get_max_wrk_ib_inventory_id_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_inventory |
| dbo | [wprep_iv_cmp_style_color_$sp](dbo.wprep_iv_cmp_style_color_$sp.md) | dbo.get_job_params_$sp, dbo.get_last_range_end_$sp, dbo.get_max_wrk_ib_inventory_id_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_inventory |
| dbo | [wprep_iv_hist_group_$sp](dbo.wprep_iv_hist_group_$sp.md) | dbo.get_job_params_$sp, dbo.get_last_range_end_$sp, dbo.get_max_wrk_ib_inventory_id_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_inventory |
| dbo | [wprep_iv_hist_style_$sp](dbo.wprep_iv_hist_style_$sp.md) | dbo.get_job_params_$sp, dbo.get_last_range_end_$sp, dbo.get_max_wrk_ib_inventory_id_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_inventory |
| dbo | [wprep_oh_group_$sp](dbo.wprep_oh_group_$sp.md) | dbo.get_job_params_$sp, dbo.get_last_range_end_$sp, dbo.get_max_wrk_ib_inventory_id_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_inventory |
| dbo | [wprep_oh_sku_$sp](dbo.wprep_oh_sku_$sp.md) | dbo.get_job_params_$sp, dbo.get_last_range_end_$sp, dbo.get_max_wrk_ib_inventory_id_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_inventory |
| dbo | [wprep_oh_style_$sp](dbo.wprep_oh_style_$sp.md) | dbo.get_job_params_$sp, dbo.get_last_range_end_$sp, dbo.get_max_wrk_ib_inventory_id_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_inventory |
| dbo | [wprep_oh_style_color_$sp](dbo.wprep_oh_style_color_$sp.md) | dbo.get_job_params_$sp, dbo.get_last_range_end_$sp, dbo.get_max_wrk_ib_inventory_id_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_inventory |
| dbo | [wprep_oo_group_$sp](dbo.wprep_oo_group_$sp.md) | dbo.get_job_params_$sp, dbo.get_last_range_end_$sp, dbo.get_max_wrk_ib_on_order_id_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_on_order |
| dbo | [wprep_oo_sku_$sp](dbo.wprep_oo_sku_$sp.md) | dbo.get_job_params_$sp, dbo.get_last_range_end_$sp, dbo.get_max_wrk_ib_on_order_id_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_on_order |
| dbo | [wprep_oo_style_$sp](dbo.wprep_oo_style_$sp.md) | dbo.get_job_params_$sp, dbo.get_last_range_end_$sp, dbo.get_max_wrk_ib_on_order_id_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_on_order |
| dbo | [wprep_oo_style_color_$sp](dbo.wprep_oo_style_color_$sp.md) | dbo.get_job_params_$sp, dbo.get_last_range_end_$sp, dbo.get_max_wrk_ib_on_order_id_$sp, dbo.job_error_handler_$sp, dbo.job_header, dbo.job_progress_handler_$sp, dbo.return_debug_flag_$sp, dbo.wrk_ib_on_order |
| MerchandisingPlanning | [spTXTDataLoad_CompletionFile](MerchandisingPlanning.spTXTDataLoad_CompletionFile.md) |  |
| MerchandisingPlanning | [spTXTDataLoad_Dimension_Location](MerchandisingPlanning.spTXTDataLoad_Dimension_Location.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus |
| MerchandisingPlanning | [spTXTDataLoad_Dimension_Product](MerchandisingPlanning.spTXTDataLoad_Dimension_Product.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus |
| MerchandisingPlanning | [spTXTDataLoad_Dimension_Time](MerchandisingPlanning.spTXTDataLoad_Dimension_Time.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus |
| MerchandisingPlanning | [spTXTDataLoad_Measure_hs Inv Ch Tfr Cost Value_SingleFiscalWeek](MerchandisingPlanning.spTXTDataLoad_Measure_hs_Inv_Ch_Tfr_Cost_Value_SingleFiscalWeek.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus |
| MerchandisingPlanning | [spTXTDataLoad_Measure_hs Inv Ch Tfr Cost Value_SingleFiscalWeek_Validation](MerchandisingPlanning.spTXTDataLoad_Measure_hs_Inv_Ch_Tfr_Cost_Value_SingleFiscalWeek_Validation.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateValidation, MerchandisingPlanning.TXTDataLoad_ValidationEmailDetailLog |
| MerchandisingPlanning | [spTXTDataLoad_Measure_hs Inv Ch Tfr Unit_SingleFiscalWeek](MerchandisingPlanning.spTXTDataLoad_Measure_hs_Inv_Ch_Tfr_Unit_SingleFiscalWeek.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus |
| MerchandisingPlanning | [spTXTDataLoad_Measure_hs Inv Ch Tfr Unit_SingleFiscalWeek_Value_Validation](MerchandisingPlanning.spTXTDataLoad_Measure_hs_Inv_Ch_Tfr_Unit_SingleFiscalWeek_Value_Validation.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateValidation, MerchandisingPlanning.TXTDataLoad_ValidationEmailDetailLog |
| MerchandisingPlanning | [spTXTDataLoad_Measure_hs Inv Ch Tfr Value_SingleFiscalWeek](MerchandisingPlanning.spTXTDataLoad_Measure_hs_Inv_Ch_Tfr_Value_SingleFiscalWeek.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus |
| MerchandisingPlanning | [spTXTDataLoad_Measure_hs Inv Ch Tfr Value_SingleFiscalWeek_Value_Validation](MerchandisingPlanning.spTXTDataLoad_Measure_hs_Inv_Ch_Tfr_Value_SingleFiscalWeek_Value_Validation.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateValidation, MerchandisingPlanning.TXTDataLoad_ValidationEmailDetailLog |
| MerchandisingPlanning | [spTXTDataLoad_Measure_hs Inv EOP Cost Value_SingleFiscalWeek](MerchandisingPlanning.spTXTDataLoad_Measure_hs_Inv_EOP_Cost_Value_SingleFiscalWeek.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus |
| MerchandisingPlanning | [spTXTDataLoad_Measure_hs Inv EOP Cost Value_SingleFiscalWeek_Value_Validation](MerchandisingPlanning.spTXTDataLoad_Measure_hs_Inv_EOP_Cost_Value_SingleFiscalWeek_Value_Validation.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateValidation, MerchandisingPlanning.TXTDataLoad_ValidationEmailDetailLog |
| MerchandisingPlanning | [spTXTDataLoad_Measure_hs Inv EOP Unit_SingleFiscalWeek](MerchandisingPlanning.spTXTDataLoad_Measure_hs_Inv_EOP_Unit_SingleFiscalWeek.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus |
| MerchandisingPlanning | [spTXTDataLoad_Measure_hs Inv EOP Unit_SingleFiscalWeek_Value_Validation](MerchandisingPlanning.spTXTDataLoad_Measure_hs_Inv_EOP_Unit_SingleFiscalWeek_Value_Validation.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateValidation, MerchandisingPlanning.TXTDataLoad_ValidationEmailDetailLog |
| MerchandisingPlanning | [spTXTDataLoad_Measure_hs Inv EOP Value_SingleFiscalWeek](MerchandisingPlanning.spTXTDataLoad_Measure_hs_Inv_EOP_Value_SingleFiscalWeek.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus |
| MerchandisingPlanning | [spTXTDataLoad_Measure_hs Inv EOP Value_SingleFiscalWeek_Validation](MerchandisingPlanning.spTXTDataLoad_Measure_hs_Inv_EOP_Value_SingleFiscalWeek_Validation.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateValidation, MerchandisingPlanning.TXTDataLoad_ValidationEmailDetailLog |
| MerchandisingPlanning | [spTXTDataLoad_Measure_hs Markdown Perm Value_SingleFiscalWeek](MerchandisingPlanning.spTXTDataLoad_Measure_hs_Markdown_Perm_Value_SingleFiscalWeek.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus |
| MerchandisingPlanning | [spTXTDataLoad_Measure_hs Markdown Perm Value_SingleFiscalWeek_Validation](MerchandisingPlanning.spTXTDataLoad_Measure_hs_Markdown_Perm_Value_SingleFiscalWeek_Validation.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateValidation, MerchandisingPlanning.TXTDataLoad_ValidationEmailDetailLog |
| MerchandisingPlanning | [spTXTDataLoad_Measure_hs Markdown POS Value_SingleFiscalWeek](MerchandisingPlanning.spTXTDataLoad_Measure_hs_Markdown_POS_Value_SingleFiscalWeek.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus |
| MerchandisingPlanning | [spTXTDataLoad_Measure_hs Markdown POS Value_SingleFiscalWeek_Validation](MerchandisingPlanning.spTXTDataLoad_Measure_hs_Markdown_POS_Value_SingleFiscalWeek_Validation.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateValidation, MerchandisingPlanning.TXTDataLoad_ValidationEmailDetailLog |
| MerchandisingPlanning | [spTXTDataLoad_Measure_hs On Order Cost Value_SingleFiscalWeek](MerchandisingPlanning.spTXTDataLoad_Measure_hs_On_Order_Cost_Value_SingleFiscalWeek.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus_V2 |
| MerchandisingPlanning | [spTXTDataLoad_Measure_hs On Order Cost Value_SingleFiscalWeek_V2](MerchandisingPlanning.spTXTDataLoad_Measure_hs_On_Order_Cost_Value_SingleFiscalWeek_V2.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus_V2 |
| MerchandisingPlanning | [spTXTDataLoad_Measure_hs On Order Cost Value_SingleFiscalWeek_Validation](MerchandisingPlanning.spTXTDataLoad_Measure_hs_On_Order_Cost_Value_SingleFiscalWeek_Validation.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateValidation, MerchandisingPlanning.TXTDataLoad_ValidationEmailDetailLog |
| MerchandisingPlanning | [spTXTDataLoad_Measure_hs On Order Unit_SingleFiscalWeek](MerchandisingPlanning.spTXTDataLoad_Measure_hs_On_Order_Unit_SingleFiscalWeek.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus_V2 |
| MerchandisingPlanning | [spTXTDataLoad_Measure_hs On Order Unit_SingleFiscalWeek_V2](MerchandisingPlanning.spTXTDataLoad_Measure_hs_On_Order_Unit_SingleFiscalWeek_V2.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus_V2, MerchandisingPlanning.vwTXT_CalculatedTime |
| -- Description: | [Loads On Order data to TXT in preparation of the TXT Weekly Dataload.](--_Description_Loads_On_Order_data_to_TXT_in_preparation_of_the_TXT_Weekly_Dataload..md) |  |
| MerchandisingPlanning | [spTXTDataLoad_Measure_hs On Order Unit_SingleFiscalWeek_Validation](MerchandisingPlanning.spTXTDataLoad_Measure_hs_On_Order_Unit_SingleFiscalWeek_Validation.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateValidation, MerchandisingPlanning.TXTDataLoad_ValidationEmailDetailLog |
| MerchandisingPlanning | [spTXTDataLoad_Measure_hs On Order Value_SingleFiscalWeek](MerchandisingPlanning.spTXTDataLoad_Measure_hs_On_Order_Value_SingleFiscalWeek.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus_V2 |
| MerchandisingPlanning | [spTXTDataLoad_Measure_hs On Order Value_SingleFiscalWeek_V2](MerchandisingPlanning.spTXTDataLoad_Measure_hs_On_Order_Value_SingleFiscalWeek_V2.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus_V2, MerchandisingPlanning.vwTXT_CalculatedTime |
| -- Description: | [Loads On Order data to TXT in preparation of the TXT Weekly Dataload.](--_Description_Loads_On_Order_data_to_TXT_in_preparation_of_the_TXT_Weekly_Dataload..md) |  |
| MerchandisingPlanning | [spTXTDataLoad_Measure_hs On Order Value_SingleFiscalWeek_Validation](MerchandisingPlanning.spTXTDataLoad_Measure_hs_On_Order_Value_SingleFiscalWeek_Validation.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateValidation, MerchandisingPlanning.TXTDataLoad_ValidationEmailDetailLog |
| MerchandisingPlanning | [spTXTDataLoad_Measure_hs Receipts Cost Value_SingleFiscalWeek](MerchandisingPlanning.spTXTDataLoad_Measure_hs_Receipts_Cost_Value_SingleFiscalWeek.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus |
| MerchandisingPlanning | [spTXTDataLoad_Measure_hs Receipts Cost Value_SingleFiscalWeek_Validation](MerchandisingPlanning.spTXTDataLoad_Measure_hs_Receipts_Cost_Value_SingleFiscalWeek_Validation.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateValidation, MerchandisingPlanning.TXTDataLoad_ValidationEmailDetailLog |
| MerchandisingPlanning | [spTXTDataLoad_Measure_hs Receipts Unit_SingleFiscalWeek](MerchandisingPlanning.spTXTDataLoad_Measure_hs_Receipts_Unit_SingleFiscalWeek.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus |
| MerchandisingPlanning | [spTXTDataLoad_Measure_hs Receipts Unit_SingleFiscalWeek_Validation](MerchandisingPlanning.spTXTDataLoad_Measure_hs_Receipts_Unit_SingleFiscalWeek_Validation.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateValidation, MerchandisingPlanning.TXTDataLoad_ValidationEmailDetailLog |
| MerchandisingPlanning | [spTXTDataLoad_Measure_hs Receipts Value_SingleFiscalWeek](MerchandisingPlanning.spTXTDataLoad_Measure_hs_Receipts_Value_SingleFiscalWeek.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus |
| MerchandisingPlanning | [spTXTDataLoad_Measure_hs Receipts Value_SingleFiscalWeek_Validation](MerchandisingPlanning.spTXTDataLoad_Measure_hs_Receipts_Value_SingleFiscalWeek_Validation.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateValidation, MerchandisingPlanning.TXTDataLoad_ValidationEmailDetailLog |
| MerchandisingPlanning | [spTXTDataLoad_Measure_hs Sales Cost Value Base_SingleFiscalWeek](MerchandisingPlanning.spTXTDataLoad_Measure_hs_Sales_Cost_Value_Base_SingleFiscalWeek.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus |
| MerchandisingPlanning | [spTXTDataLoad_Measure_hs Sales Cost Value Base_SingleFiscalWeek_Validation](MerchandisingPlanning.spTXTDataLoad_Measure_hs_Sales_Cost_Value_Base_SingleFiscalWeek_Validation.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateValidation, MerchandisingPlanning.TXTDataLoad_ValidationEmailDetailLog |
| MerchandisingPlanning | [spTXTDataLoad_Measure_hs Sales Unit_SingleFiscalWeek](MerchandisingPlanning.spTXTDataLoad_Measure_hs_Sales_Unit_SingleFiscalWeek.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus |
| MerchandisingPlanning | [spTXTDataLoad_Measure_hs Sales Unit_SingleFiscalWeek_Validation](MerchandisingPlanning.spTXTDataLoad_Measure_hs_Sales_Unit_SingleFiscalWeek_Validation.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateValidation, MerchandisingPlanning.TXTDataLoad_ValidationEmailDetailLog |
| MerchandisingPlanning | [spTXTDataLoad_Measure_hs Sales Value Base_SingleFiscalWeek](MerchandisingPlanning.spTXTDataLoad_Measure_hs_Sales_Value_Base_SingleFiscalWeek.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus |
| MerchandisingPlanning | [spTXTDataLoad_Measure_hs Sales Value Base_SingleFiscalWeek_Validation](MerchandisingPlanning.spTXTDataLoad_Measure_hs_Sales_Value_Base_SingleFiscalWeek_Validation.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateValidation, MerchandisingPlanning.TXTDataLoad_ValidationEmailDetailLog |
| MerchandisingPlanning | [spTXTDataLoad_Measure_hs Sales Value Local_SingleFiscalWeek](MerchandisingPlanning.spTXTDataLoad_Measure_hs_Sales_Value_Local_SingleFiscalWeek.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus |
| MerchandisingPlanning | [spTXTDataLoad_Measure_hs Sales Value Local_SingleFiscalWeek_Validation](MerchandisingPlanning.spTXTDataLoad_Measure_hs_Sales_Value_Local_SingleFiscalWeek_Validation.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateValidation, MerchandisingPlanning.TXTDataLoad_ValidationEmailDetailLog |
| MerchandisingPlanning | [spTXTDataLoad_Measure_hs Shrink Cost Value_SingleFiscalWeek](MerchandisingPlanning.spTXTDataLoad_Measure_hs_Shrink_Cost_Value_SingleFiscalWeek.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus |
| MerchandisingPlanning | [spTXTDataLoad_Measure_hs Shrink Cost Value_SingleFiscalWeek_Validation](MerchandisingPlanning.spTXTDataLoad_Measure_hs_Shrink_Cost_Value_SingleFiscalWeek_Validation.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateValidation, MerchandisingPlanning.TXTDataLoad_ValidationEmailDetailLog |
| MerchandisingPlanning | [spTXTDataLoad_Measure_hs Shrink Unit_SingleFiscalWeek](MerchandisingPlanning.spTXTDataLoad_Measure_hs_Shrink_Unit_SingleFiscalWeek.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus |
| MerchandisingPlanning | [spTXTDataLoad_Measure_hs Shrink Unit_SingleFiscalWeek_Validation](MerchandisingPlanning.spTXTDataLoad_Measure_hs_Shrink_Unit_SingleFiscalWeek_Validation.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateValidation, MerchandisingPlanning.TXTDataLoad_ValidationEmailDetailLog |
| MerchandisingPlanning | [spTXTDataLoad_Measure_hs Shrink Value_SingleFiscalWeek](MerchandisingPlanning.spTXTDataLoad_Measure_hs_Shrink_Value_SingleFiscalWeek.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus |
| MerchandisingPlanning | [spTXTDataLoad_Measure_hs Shrink Value_SingleFiscalWeek_Validation](MerchandisingPlanning.spTXTDataLoad_Measure_hs_Shrink_Value_SingleFiscalWeek_Validation.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateValidation, MerchandisingPlanning.TXTDataLoad_ValidationEmailDetailLog |
| MerchandisingPlanning | [spTXTDataLoad_Measure_hs Store Count_SingleFiscalWeek](MerchandisingPlanning.spTXTDataLoad_Measure_hs_Store_Count_SingleFiscalWeek.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus |
| MerchandisingPlanning | [spTXTDataLoad_Measure_hs Store Count_SingleFiscalWeek_V2](MerchandisingPlanning.spTXTDataLoad_Measure_hs_Store_Count_SingleFiscalWeek_V2.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus_V2 |
| MerchandisingPlanning | [spTXTDataLoad_Measure_hs Store Count_SingleFiscalWeek_Validation](MerchandisingPlanning.spTXTDataLoad_Measure_hs_Store_Count_SingleFiscalWeek_Validation.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateValidation, MerchandisingPlanning.TXTDataLoad_ValidationEmailDetailLog |
| MerchandisingPlanning | [spTXTDataLoad_Measure_hs Store Status_SingleFiscalWeek](MerchandisingPlanning.spTXTDataLoad_Measure_hs_Store_Status_SingleFiscalWeek.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus |
| MerchandisingPlanning | [spTXTDataLoad_Measure_hs Store Status_SingleFiscalWeek_V2](MerchandisingPlanning.spTXTDataLoad_Measure_hs_Store_Status_SingleFiscalWeek_V2.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateBatchStatus_V2 |
| MerchandisingPlanning | [spTXTDataLoad_Measure_hs Store Status_SingleFiscalWeek_Validation](MerchandisingPlanning.spTXTDataLoad_Measure_hs_Store_Status_SingleFiscalWeek_Validation.md) | MerchandisingPlanning.spTXTDataLoad_ETLBatchDetailLog_UpdateValidation, MerchandisingPlanning.TXTDataLoad_ValidationEmailDetailLog |
