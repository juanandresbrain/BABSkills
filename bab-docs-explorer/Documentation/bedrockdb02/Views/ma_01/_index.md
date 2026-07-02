# Views: ma_01

| Schema | View | Table Dependencies |
|---|---|---|
| dbo | [ib_future_inv_reserve_total](dbo.ib_future_inv_reserve_total.md) | dbo.syn_ib_future_inventory_reserve_total, dbo.syn_sku, dbo.syn_style_color, dbo.syn_style_group, dbo.syn_style_size |
| dbo | [view_calendar_merch_pd_rel](dbo.view_calendar_merch_pd_rel.md) | dbo.calendar_merch_period |
| dbo | [view_calendar_merch_pd_wk_rel](dbo.view_calendar_merch_pd_wk_rel.md) | dbo.calendar_merch_period, dbo.calendar_merch_week |
| dbo | [view_calendar_merch_week_rel](dbo.view_calendar_merch_week_rel.md) | dbo.calendar_merch_week |
| dbo | [view_color_group](dbo.view_color_group.md) | dbo.color, dbo.color_group, dbo.color_group_item |
| dbo | [view_dl_hist_group](dbo.view_dl_hist_group.md) | dbo.dl_hist_group |
| dbo | [view_dl_hist_oh_group](dbo.view_dl_hist_oh_group.md) | dbo.dl_hist_oh_group |
| dbo | [view_dl_hist_oh_sku](dbo.view_dl_hist_oh_sku.md) | dbo.dl_hist_oh_sku |
| dbo | [view_dl_hist_oh_style](dbo.view_dl_hist_oh_style.md) | dbo.dl_hist_oh_style |
| dbo | [view_dl_hist_oh_styleclr](dbo.view_dl_hist_oh_styleclr.md) | dbo.dl_hist_oh_styleclr |
| dbo | [view_dl_hist_sku](dbo.view_dl_hist_sku.md) | dbo.dl_hist_sku |
| dbo | [view_dl_hist_style](dbo.view_dl_hist_style.md) | dbo.dl_hist_style |
| dbo | [view_dl_hist_styleclr](dbo.view_dl_hist_styleclr.md) | dbo.dl_hist_styleclr |
| dbo | [view_fcast_group_loc_pd](dbo.view_fcast_group_loc_pd.md) | dbo.calendar_merch_week, dbo.color, dbo.forecast, dbo.forecast_detail, dbo.forecast_sale, dbo.sku, dbo.style, dbo.style_color, dbo.style_group |
| dbo | [view_fcast_group_loc_wk](dbo.view_fcast_group_loc_wk.md) | dbo.calendar_merch_week, dbo.color, dbo.forecast, dbo.forecast_detail, dbo.forecast_sale, dbo.sku, dbo.style, dbo.style_color, dbo.style_group |
| dbo | [view_fcast_sku_loc_pd](dbo.view_fcast_sku_loc_pd.md) | dbo.calendar_merch_week, dbo.forecast, dbo.forecast_detail, dbo.forecast_sale, dbo.sku |
| dbo | [view_fcast_sku_loc_wk](dbo.view_fcast_sku_loc_wk.md) | dbo.calendar_merch_week, dbo.forecast, dbo.forecast_detail, dbo.forecast_sale, dbo.sku |
| dbo | [view_fcast_style_loc_pd](dbo.view_fcast_style_loc_pd.md) | dbo.calendar_merch_week, dbo.forecast, dbo.forecast_detail, dbo.forecast_sale, dbo.style |
| dbo | [view_fcast_style_loc_wk](dbo.view_fcast_style_loc_wk.md) | dbo.calendar_merch_week, dbo.forecast, dbo.forecast_detail, dbo.forecast_sale, dbo.style |
| dbo | [view_fcast_styleclr_loc_pd](dbo.view_fcast_styleclr_loc_pd.md) | dbo.calendar_merch_week, dbo.color, dbo.forecast, dbo.forecast_detail, dbo.forecast_sale, dbo.style, dbo.style_color |
| dbo | [view_fcast_styleclr_loc_wk](dbo.view_fcast_styleclr_loc_wk.md) | dbo.calendar_merch_week, dbo.color, dbo.forecast, dbo.forecast_detail, dbo.forecast_sale, dbo.style, dbo.style_color |
| dbo | [view_hierarchy_attribute_inner](dbo.view_hierarchy_attribute_inner.md) | dbo.entity_attribute_set, dbo.merch_group_parent |
| dbo | [view_hierarchy_attribute_outer](dbo.view_hierarchy_attribute_outer.md) | dbo.attribute, dbo.attribute_set, dbo.entity_attribute_set, dbo.merch_group_parent |
| dbo | [view_hist_cmp_group_loc_li](dbo.view_hist_cmp_group_loc_li.md) | dbo.hierarchy_group, dbo.hist_cmp_group_loc_li |
| dbo | [view_hist_cmp_group_loc_pd](dbo.view_hist_cmp_group_loc_pd.md) | dbo.hierarchy_group, dbo.hist_cmp_group_loc_pd |
| dbo | [view_hist_cmp_group_loc_wk](dbo.view_hist_cmp_group_loc_wk.md) | dbo.hierarchy_group, dbo.hist_cmp_group_loc_wk |
| dbo | [view_hist_cmp_group_loc_yr](dbo.view_hist_cmp_group_loc_yr.md) | dbo.hierarchy_group, dbo.hist_cmp_group_loc_yr |
| dbo | [view_hist_cmp_sku_chn_li](dbo.view_hist_cmp_sku_chn_li.md) | dbo.hist_cmp_sku_chn_li, dbo.style_color |
| dbo | [view_hist_cmp_sku_chn_pd](dbo.view_hist_cmp_sku_chn_pd.md) | dbo.hist_cmp_sku_chn_pd, dbo.style_color |
| dbo | [view_hist_cmp_sku_chn_wk](dbo.view_hist_cmp_sku_chn_wk.md) | dbo.hist_cmp_sku_chn_wk, dbo.style_color |
| dbo | [view_hist_cmp_sku_chn_yr](dbo.view_hist_cmp_sku_chn_yr.md) | dbo.hist_cmp_sku_chn_yr, dbo.style_color |
| dbo | [view_hist_cmp_sku_loc_li](dbo.view_hist_cmp_sku_loc_li.md) | dbo.hist_cmp_sku_loc_li, dbo.style_color |
| dbo | [view_hist_cmp_sku_loc_pd](dbo.view_hist_cmp_sku_loc_pd.md) | dbo.hist_cmp_sku_loc_pd, dbo.style_color |
| dbo | [view_hist_cmp_sku_loc_wk](dbo.view_hist_cmp_sku_loc_wk.md) | dbo.hist_cmp_sku_loc_wk, dbo.style_color |
| dbo | [view_hist_cmp_sku_loc_yr](dbo.view_hist_cmp_sku_loc_yr.md) | dbo.hist_cmp_sku_loc_yr, dbo.style_color |
| dbo | [view_hist_cmp_styleclr_chn_li](dbo.view_hist_cmp_styleclr_chn_li.md) | dbo.hierarchy_group, dbo.hist_cmp_styleclr_chn_li, dbo.style_color, dbo.style_group |
| dbo | [view_hist_cmp_styleclr_chn_pd](dbo.view_hist_cmp_styleclr_chn_pd.md) | dbo.hierarchy_group, dbo.hist_cmp_styleclr_chn_pd, dbo.style_color, dbo.style_group |
| dbo | [view_hist_cmp_styleclr_chn_wk](dbo.view_hist_cmp_styleclr_chn_wk.md) | dbo.hierarchy_group, dbo.hist_cmp_styleclr_chn_wk, dbo.style_color, dbo.style_group |
| dbo | [view_hist_cmp_styleclr_chn_yr](dbo.view_hist_cmp_styleclr_chn_yr.md) | dbo.hierarchy_group, dbo.hist_cmp_styleclr_chn_yr, dbo.style_color, dbo.style_group |
| dbo | [view_hist_cmp_styleclr_loc_li](dbo.view_hist_cmp_styleclr_loc_li.md) | dbo.hierarchy_group, dbo.hist_cmp_styleclr_loc_li, dbo.style_color, dbo.style_group |
| dbo | [view_hist_cmp_styleclr_loc_pd](dbo.view_hist_cmp_styleclr_loc_pd.md) | dbo.hierarchy_group, dbo.hist_cmp_styleclr_loc_pd, dbo.style_color, dbo.style_group |
| dbo | [view_hist_cmp_styleclr_loc_wk](dbo.view_hist_cmp_styleclr_loc_wk.md) | dbo.hierarchy_group, dbo.hist_cmp_styleclr_loc_wk, dbo.style_color, dbo.style_group |
| dbo | [view_hist_cmp_styleclr_loc_yr](dbo.view_hist_cmp_styleclr_loc_yr.md) | dbo.hierarchy_group, dbo.hist_cmp_styleclr_loc_yr, dbo.style_color, dbo.style_group |
| dbo | [view_hist_flsh_group_loc_da](dbo.view_hist_flsh_group_loc_da.md) | dbo.hierarchy_group, dbo.hist_flsh_group_loc_da |
| dbo | [view_hist_group_loc_li](dbo.view_hist_group_loc_li.md) | dbo.hierarchy_group, dbo.hist_group_loc_li |
| dbo | [view_hist_group_loc_pd](dbo.view_hist_group_loc_pd.md) | dbo.hierarchy_group, dbo.hist_group_loc_pd |
| dbo | [view_hist_group_loc_wk](dbo.view_hist_group_loc_wk.md) | dbo.hierarchy_group, dbo.hist_group_loc_wk |
| dbo | [view_hist_group_loc_yr](dbo.view_hist_group_loc_yr.md) | dbo.hierarchy_group, dbo.hist_group_loc_yr |
| dbo | [view_hist_oh_group_loc_li](dbo.view_hist_oh_group_loc_li.md) | dbo.hierarchy_group, dbo.hist_oh_group_loc_li |
| dbo | [view_hist_oh_group_loc_pd](dbo.view_hist_oh_group_loc_pd.md) | dbo.hierarchy_group, dbo.hist_oh_group_loc_pd |
| dbo | [view_hist_oh_group_loc_wk](dbo.view_hist_oh_group_loc_wk.md) | dbo.hierarchy_group, dbo.hist_oh_group_loc_wk |
| dbo | [view_hist_oh_group_loc_yr](dbo.view_hist_oh_group_loc_yr.md) | dbo.hierarchy_group, dbo.hist_oh_group_loc_yr |
| dbo | [view_hist_oh_sku_chn_li](dbo.view_hist_oh_sku_chn_li.md) | dbo.hist_oh_sku_chn_li, dbo.style_color |
| dbo | [view_hist_oh_sku_chn_pd](dbo.view_hist_oh_sku_chn_pd.md) | dbo.hist_oh_sku_chn_pd, dbo.style_color |
| dbo | [view_hist_oh_sku_chn_wk](dbo.view_hist_oh_sku_chn_wk.md) | dbo.hist_oh_sku_chn_wk, dbo.style_color |
| dbo | [view_hist_oh_sku_chn_yr](dbo.view_hist_oh_sku_chn_yr.md) | dbo.hist_oh_sku_chn_yr, dbo.style_color |
| dbo | [view_hist_oh_sku_loc_li](dbo.view_hist_oh_sku_loc_li.md) | dbo.hist_oh_sku_loc_li, dbo.style_color |
| dbo | [view_hist_oh_sku_loc_pd](dbo.view_hist_oh_sku_loc_pd.md) | dbo.hist_oh_sku_loc_pd, dbo.style_color |
| dbo | [view_hist_oh_sku_loc_wk](dbo.view_hist_oh_sku_loc_wk.md) | dbo.hist_oh_sku_loc_wk, dbo.style_color |
| dbo | [view_hist_oh_sku_loc_yr](dbo.view_hist_oh_sku_loc_yr.md) | dbo.hist_oh_sku_loc_yr, dbo.style_color |
| dbo | [view_hist_oh_styleclr_chn_li](dbo.view_hist_oh_styleclr_chn_li.md) | dbo.hierarchy_group, dbo.hist_oh_styleclr_chn_li, dbo.style_color, dbo.style_group |
| dbo | [view_hist_oh_styleclr_chn_pd](dbo.view_hist_oh_styleclr_chn_pd.md) | dbo.hierarchy_group, dbo.hist_oh_styleclr_chn_pd, dbo.style_color, dbo.style_group |
| dbo | [view_hist_oh_styleclr_chn_wk](dbo.view_hist_oh_styleclr_chn_wk.md) | dbo.hierarchy_group, dbo.hist_oh_styleclr_chn_wk, dbo.style_color, dbo.style_group |
| dbo | [view_hist_oh_styleclr_chn_yr](dbo.view_hist_oh_styleclr_chn_yr.md) | dbo.hierarchy_group, dbo.hist_oh_styleclr_chn_yr, dbo.style_color, dbo.style_group |
| dbo | [view_hist_oh_styleclr_loc_li](dbo.view_hist_oh_styleclr_loc_li.md) | dbo.hierarchy_group, dbo.hist_oh_styleclr_loc_li, dbo.style_color, dbo.style_group |
| dbo | [view_hist_oh_styleclr_loc_pd](dbo.view_hist_oh_styleclr_loc_pd.md) | dbo.hierarchy_group, dbo.hist_oh_styleclr_loc_pd, dbo.style_color, dbo.style_group |
| dbo | [view_hist_oh_styleclr_loc_wk](dbo.view_hist_oh_styleclr_loc_wk.md) | dbo.hierarchy_group, dbo.hist_oh_styleclr_loc_wk, dbo.style_color, dbo.style_group |
| dbo | [view_hist_oh_styleclr_loc_yr](dbo.view_hist_oh_styleclr_loc_yr.md) | dbo.hierarchy_group, dbo.hist_oh_styleclr_loc_yr, dbo.style_color, dbo.style_group |
| dbo | [view_hist_sku_chn_li](dbo.view_hist_sku_chn_li.md) | dbo.hist_sku_chn_li, dbo.style_color |
| dbo | [view_hist_sku_chn_pd](dbo.view_hist_sku_chn_pd.md) | dbo.hist_sku_chn_pd, dbo.style_color |
| dbo | [view_hist_sku_chn_wk](dbo.view_hist_sku_chn_wk.md) | dbo.hist_sku_chn_wk, dbo.style_color |
| dbo | [view_hist_sku_chn_yr](dbo.view_hist_sku_chn_yr.md) | dbo.hist_sku_chn_yr, dbo.style_color |
| dbo | [view_hist_sku_loc_li](dbo.view_hist_sku_loc_li.md) | dbo.hist_sku_loc_li, dbo.style_color |
| dbo | [view_hist_sku_loc_pd](dbo.view_hist_sku_loc_pd.md) | dbo.hist_sku_loc_pd, dbo.style_color |
| dbo | [view_hist_sku_loc_wk](dbo.view_hist_sku_loc_wk.md) | dbo.hist_sku_loc_wk, dbo.style_color |
| dbo | [view_hist_sku_loc_yr](dbo.view_hist_sku_loc_yr.md) | dbo.hist_sku_loc_yr, dbo.style_color |
| dbo | [view_hist_style_loc_li](dbo.view_hist_style_loc_li.md) | dbo.hist_style_loc_li, dbo.location |
| dbo | [view_hist_style_loc_pd](dbo.view_hist_style_loc_pd.md) | dbo.hist_style_loc_pd, dbo.location |
| dbo | [view_hist_style_loc_wk](dbo.view_hist_style_loc_wk.md) | dbo.hist_style_loc_wk, dbo.location |
| dbo | [view_hist_style_loc_yr](dbo.view_hist_style_loc_yr.md) | dbo.hist_style_loc_yr, dbo.location |
| dbo | [view_hist_styleclr_chn_li](dbo.view_hist_styleclr_chn_li.md) | dbo.hierarchy_group, dbo.hist_styleclr_chn_li, dbo.style_color, dbo.style_group |
| dbo | [view_hist_styleclr_chn_pd](dbo.view_hist_styleclr_chn_pd.md) | dbo.hierarchy_group, dbo.hist_styleclr_chn_pd, dbo.style_color, dbo.style_group |
| dbo | [view_hist_styleclr_chn_wk](dbo.view_hist_styleclr_chn_wk.md) | dbo.hierarchy_group, dbo.hist_styleclr_chn_wk, dbo.style_color, dbo.style_group |
| dbo | [view_hist_styleclr_chn_yr](dbo.view_hist_styleclr_chn_yr.md) | dbo.hierarchy_group, dbo.hist_styleclr_chn_yr, dbo.style_color, dbo.style_group |
| dbo | [view_hist_styleclr_loc_li](dbo.view_hist_styleclr_loc_li.md) | dbo.hierarchy_group, dbo.hist_styleclr_loc_li, dbo.style_color, dbo.style_group |
| dbo | [view_hist_styleclr_loc_pd](dbo.view_hist_styleclr_loc_pd.md) | dbo.hierarchy_group, dbo.hist_styleclr_loc_pd, dbo.style_color, dbo.style_group |
| dbo | [view_hist_styleclr_loc_wk](dbo.view_hist_styleclr_loc_wk.md) | dbo.hierarchy_group, dbo.hist_styleclr_loc_wk, dbo.style_color, dbo.style_group |
| dbo | [view_hist_styleclr_loc_yr](dbo.view_hist_styleclr_loc_yr.md) | dbo.hierarchy_group, dbo.hist_styleclr_loc_yr, dbo.style_color, dbo.style_group |
| dbo | [view_ib_activity_date](dbo.view_ib_activity_date.md) | dbo.ib_activity_date, dbo.location, dbo.style_color |
| dbo | [view_loc_hierarchy_lookup](dbo.view_loc_hierarchy_lookup.md) | dbo.hierarchy, dbo.hierarchy_level |
| dbo | [view_location_attribute_outer](dbo.view_location_attribute_outer.md) | dbo.attribute, dbo.attribute_set, dbo.entity_attribute_set, dbo.location |
| dbo | [view_location_cust_prop_outer](dbo.view_location_cust_prop_outer.md) | dbo.custom_property, dbo.entity_custom_property, dbo.location |
| dbo | [view_location_employee](dbo.view_location_employee.md) | dbo.view_location_employee |
| dbo | [view_location_group_employee](dbo.view_location_group_employee.md) | dbo.view_location_group_employee |
| dbo | [view_location_parent_outer](dbo.view_location_parent_outer.md) | dbo.hierarchy_group, dbo.hierarchy_level, dbo.location, dbo.location_parent |
| dbo | [view_ma_att_ent_loc_grp_item](dbo.view_ma_att_ent_loc_grp_item.md) | dbo.attribute, dbo.attribute_set, dbo.entity_loc_group_item |
| dbo | [view_ma_ssnl_prfl_loc_grp_item](dbo.view_ma_ssnl_prfl_loc_grp_item.md) | dbo.entity_loc_group, dbo.seasonal_profile_group, dbo.ssnl_prfl_loc_grp_item |
| dbo | [view_merch_group_employee](dbo.view_merch_group_employee.md) | dbo.view_merch_group_employee |
| dbo | [view_min_max_profile](dbo.view_min_max_profile.md) | dbo.min_max_profile, dbo.sku |
| dbo | [view_oh_group_loctype_li](dbo.view_oh_group_loctype_li.md) | dbo.hist_oh_group_loc_li, dbo.location |
| dbo | [view_oh_group_loctype_pd](dbo.view_oh_group_loctype_pd.md) | dbo.hist_oh_group_loc_pd, dbo.location |
| dbo | [view_oh_group_loctype_wk](dbo.view_oh_group_loctype_wk.md) | dbo.hist_oh_group_loc_wk, dbo.location |
| dbo | [view_oh_group_loctype_yr](dbo.view_oh_group_loctype_yr.md) | dbo.hist_oh_group_loc_yr, dbo.location |
| dbo | [view_oh_sku_loctype_li](dbo.view_oh_sku_loctype_li.md) | dbo.hist_oh_sku_loc_li, dbo.location |
| dbo | [view_oh_sku_loctype_pd](dbo.view_oh_sku_loctype_pd.md) | dbo.hist_oh_sku_loc_pd, dbo.location |
| dbo | [view_oh_sku_loctype_wk](dbo.view_oh_sku_loctype_wk.md) | dbo.hist_oh_sku_loc_wk, dbo.location |
| dbo | [view_oh_sku_loctype_yr](dbo.view_oh_sku_loctype_yr.md) | dbo.hist_oh_sku_loc_yr, dbo.location |
| dbo | [view_oh_style_loctype_li](dbo.view_oh_style_loctype_li.md) | dbo.hist_oh_style_loc_li, dbo.location |
| dbo | [view_oh_style_loctype_pd](dbo.view_oh_style_loctype_pd.md) | dbo.hist_oh_style_loc_pd, dbo.location |
| dbo | [view_oh_style_loctype_wk](dbo.view_oh_style_loctype_wk.md) | dbo.hist_oh_style_loc_wk, dbo.location |
| dbo | [view_oh_style_loctype_yr](dbo.view_oh_style_loctype_yr.md) | dbo.hist_oh_style_loc_yr, dbo.location |
| dbo | [view_oh_styleclr_loctype_li](dbo.view_oh_styleclr_loctype_li.md) | dbo.hist_oh_styleclr_loc_li, dbo.location, dbo.style_color |
| dbo | [view_oh_styleclr_loctype_pd](dbo.view_oh_styleclr_loctype_pd.md) | dbo.hist_oh_styleclr_loc_pd, dbo.location, dbo.style_color |
| dbo | [view_oh_styleclr_loctype_wk](dbo.view_oh_styleclr_loctype_wk.md) | dbo.hist_oh_styleclr_loc_wk, dbo.location, dbo.style_color |
| dbo | [view_oh_styleclr_loctype_yr](dbo.view_oh_styleclr_loctype_yr.md) | dbo.hist_oh_styleclr_loc_yr, dbo.location, dbo.style_color |
| dbo | [view_oo_all_group_loc_li](dbo.view_oo_all_group_loc_li.md) | dbo.hierarchy_group, dbo.oo_all_group_loc_li |
| dbo | [view_oo_all_group_loc_pd](dbo.view_oo_all_group_loc_pd.md) | dbo.hierarchy_group, dbo.oo_all_group_loc_pd |
| dbo | [view_oo_all_group_loc_wk](dbo.view_oo_all_group_loc_wk.md) | dbo.hierarchy_group, dbo.oo_all_group_loc_wk |
| dbo | [view_oo_all_group_loc_yr](dbo.view_oo_all_group_loc_yr.md) | dbo.hierarchy_group, dbo.oo_all_group_loc_yr |
| dbo | [view_oo_all_sku_chn_li](dbo.view_oo_all_sku_chn_li.md) | dbo.oo_all_sku_chn_li, dbo.style_color |
| dbo | [view_oo_all_sku_chn_pd](dbo.view_oo_all_sku_chn_pd.md) | dbo.oo_all_sku_chn_pd, dbo.style_color |
| dbo | [view_oo_all_sku_chn_wk](dbo.view_oo_all_sku_chn_wk.md) | dbo.oo_all_sku_chn_wk, dbo.style_color |
| dbo | [view_oo_all_sku_chn_yr](dbo.view_oo_all_sku_chn_yr.md) | dbo.oo_all_sku_chn_yr, dbo.style_color |
| dbo | [view_oo_all_sku_loc_li](dbo.view_oo_all_sku_loc_li.md) | dbo.oo_all_sku_loc_li, dbo.style_color |
| dbo | [view_oo_all_sku_loc_pd](dbo.view_oo_all_sku_loc_pd.md) | dbo.oo_all_sku_loc_pd, dbo.style_color |
| dbo | [view_oo_all_sku_loc_wk](dbo.view_oo_all_sku_loc_wk.md) | dbo.oo_all_sku_loc_wk, dbo.style_color |
| dbo | [view_oo_all_sku_loc_yr](dbo.view_oo_all_sku_loc_yr.md) | dbo.oo_all_sku_loc_yr, dbo.style_color |
| dbo | [view_oo_all_styleclr_chn_li](dbo.view_oo_all_styleclr_chn_li.md) | dbo.hierarchy_group, dbo.oo_all_styleclr_chn_li, dbo.style_color, dbo.style_group |
| dbo | [view_oo_all_styleclr_chn_pd](dbo.view_oo_all_styleclr_chn_pd.md) | dbo.hierarchy_group, dbo.oo_all_styleclr_chn_pd, dbo.style_color, dbo.style_group |
| dbo | [view_oo_all_styleclr_chn_wk](dbo.view_oo_all_styleclr_chn_wk.md) | dbo.hierarchy_group, dbo.oo_all_styleclr_chn_wk, dbo.style_color, dbo.style_group |
| dbo | [view_oo_all_styleclr_chn_yr](dbo.view_oo_all_styleclr_chn_yr.md) | dbo.hierarchy_group, dbo.oo_all_styleclr_chn_yr, dbo.style_color, dbo.style_group |
| dbo | [view_oo_all_styleclr_loc_li](dbo.view_oo_all_styleclr_loc_li.md) | dbo.hierarchy_group, dbo.oo_all_styleclr_loc_li, dbo.style_color, dbo.style_group |
| dbo | [view_oo_all_styleclr_loc_pd](dbo.view_oo_all_styleclr_loc_pd.md) | dbo.hierarchy_group, dbo.oo_all_styleclr_loc_pd, dbo.style_color, dbo.style_group |
| dbo | [view_oo_all_styleclr_loc_wk](dbo.view_oo_all_styleclr_loc_wk.md) | dbo.hierarchy_group, dbo.oo_all_styleclr_loc_wk, dbo.style_color, dbo.style_group |
| dbo | [view_oo_all_styleclr_loc_yr](dbo.view_oo_all_styleclr_loc_yr.md) | dbo.hierarchy_group, dbo.oo_all_styleclr_loc_yr, dbo.style_color, dbo.style_group |
| dbo | [view_oo_plan_exp](dbo.view_oo_plan_exp.md) | dbo.oo_all_group_loc_wk, dbo.oo_unc_group_loc_wk |
| dbo | [view_otb_bop_loc_proj_reds](dbo.view_otb_bop_loc_proj_reds.md) | dbo.plan_element, dbo.plan_group_loc_wk, dbo.plan_version, dbo.post_parameter, dbo.view_calendar_merch_pd_rel, dbo.view_calendar_merch_pd_wk_rel |
| dbo | [view_otb_hist](dbo.view_otb_hist.md) | dbo.hist_group_chn_wk, dbo.post_parameter |
| dbo | [view_otb_loc_hist](dbo.view_otb_loc_hist.md) | dbo.hist_group_loc_wk, dbo.post_parameter |
| dbo | [view_otb_loc_oh_bow](dbo.view_otb_loc_oh_bow.md) | dbo.hist_oh_group_loc_wk, dbo.post_parameter, dbo.view_calendar_merch_week_rel |
| dbo | [view_otb_loc_on_order](dbo.view_otb_loc_on_order.md) | dbo.oo_all_group_loc_pd, dbo.view_calendar_merch_pd_rel |
| dbo | [view_otb_loc_on_order_unc](dbo.view_otb_loc_on_order_unc.md) | dbo.oo_all_group_loc_pd, dbo.view_calendar_merch_pd_rel |
| dbo | [view_otb_loc_proj_additions](dbo.view_otb_loc_proj_additions.md) | dbo.plan_element, dbo.plan_group_loc_pd, dbo.plan_version |
| dbo | [view_otb_loc_proj_reductions](dbo.view_otb_loc_proj_reductions.md) | dbo.plan_element, dbo.plan_group_loc_wk, dbo.plan_version, dbo.post_parameter, dbo.view_calendar_merch_pd_rel, dbo.view_calendar_merch_pd_wk_rel, dbo.view_otb_loc_proj_additions |
| dbo | [view_otb_oh_bow](dbo.view_otb_oh_bow.md) | dbo.hist_oh_group_chn_wk, dbo.post_parameter, dbo.view_calendar_merch_week_rel |
| dbo | [view_otb_on_order](dbo.view_otb_on_order.md) | dbo.oo_all_group_loc_pd, dbo.view_calendar_merch_pd_rel |
| dbo | [view_otb_proj_additions](dbo.view_otb_proj_additions.md) | dbo.plan_element, dbo.plan_group_loc_pd, dbo.plan_version |
| dbo | [view_otb_proj_bop_inv](dbo.view_otb_proj_bop_inv.md) | dbo.location_parent, dbo.merch_group_parent, dbo.plan_group_loc_pd, dbo.plan_version, dbo.post_parameter, dbo.view_otb_bop_loc_proj_reds, dbo.view_otb_loc_hist, dbo.view_otb_loc_oh_bow, dbo.view_otb_loc_on_order, dbo.view_otb_loc_on_order_unc |
| dbo | [view_otb_proj_reductions](dbo.view_otb_proj_reductions.md) | dbo.plan_element, dbo.plan_group_chn_wk, dbo.plan_version, dbo.post_parameter, dbo.view_calendar_merch_pd_rel, dbo.view_calendar_merch_pd_wk_rel, dbo.view_otb_proj_additions |
| dbo | [view_period_label](dbo.view_period_label.md) | dbo.period_label |
| dbo | [view_plan_group_loc_pd](dbo.view_plan_group_loc_pd.md) | dbo.oo_all_group_loc_pd, dbo.oo_unc_group_loc_pd, dbo.plan_element, dbo.plan_group_loc_pd, dbo.plan_version, dbo.post_parameter, dbo.view_calendar_merch_pd_rel, dbo.view_otb_loc_hist, dbo.view_otb_loc_oh_bow, dbo.view_otb_loc_on_order, dbo.view_otb_loc_proj_reductions |
| dbo | [view_plan_ver_element](dbo.view_plan_ver_element.md) | dbo.plan_element, dbo.plan_version |
| dbo | [view_pricing_group_styleclr](dbo.view_pricing_group_styleclr.md) | dbo.pricing_group_location, dbo.style_color |
| dbo | [view_sku_seasonal_profile](dbo.view_sku_seasonal_profile.md) | dbo.color, dbo.seasonal_profile_item, dbo.size_master, dbo.sku, dbo.style, dbo.style_color, dbo.style_size |
| dbo | [view_style_attribute_outer](dbo.view_style_attribute_outer.md) | dbo.attribute, dbo.attribute_set, dbo.entity_attribute_set, dbo.style |
| dbo | [view_style_calendar_outer](dbo.view_style_calendar_outer.md) | dbo.calendar, dbo.style |
| dbo | [view_style_cust_prop_outer](dbo.view_style_cust_prop_outer.md) | dbo.custom_property, dbo.entity_custom_property, dbo.style |
| dbo | [view_style_custom_property](dbo.view_style_custom_property.md) | dbo.entity_custom_property |
| dbo | [view_style_employee](dbo.view_style_employee.md) | dbo.view_style_employee |
| dbo | [view_styleclr_attribute_inner](dbo.view_styleclr_attribute_inner.md) | dbo.attribute_set, dbo.entity_attribute_set, dbo.style_color |
| dbo | [view_styleclr_attribute_outer](dbo.view_styleclr_attribute_outer.md) | dbo.attribute, dbo.attribute_set, dbo.entity_attribute_set, dbo.style_color |
| dbo | [view_styleclr_seasonal_profile](dbo.view_styleclr_seasonal_profile.md) | dbo.color, dbo.seasonal_profile_item, dbo.style, dbo.style_color |
| dbo | [view_upc_first](dbo.view_upc_first.md) | dbo.sku, dbo.upc |
| dbo | [view_upc_first_style](dbo.view_upc_first_style.md) | dbo.sku, dbo.upc |
| dbo | [view_upc_first_styleclr](dbo.view_upc_first_styleclr.md) | dbo.sku, dbo.upc |
| dbo | [view_upc_inhouse_outer](dbo.view_upc_inhouse_outer.md) | dbo.sku, dbo.upc |
| dbo | [view_upc_vendor_outer](dbo.view_upc_vendor_outer.md) | dbo.sku, dbo.upc |
| dbo | [view_vendor_attribute_inner](dbo.view_vendor_attribute_inner.md) | dbo.attribute_set, dbo.entity_attribute_set, dbo.vendor |
| dbo | [view_vendor_attribute_outer](dbo.view_vendor_attribute_outer.md) | dbo.attribute, dbo.attribute_set, dbo.entity_attribute_set, dbo.vendor |
| dbo | [view_wholesale_inv_sku_outer](dbo.view_wholesale_inv_sku_outer.md) | dbo.color, dbo.size_master, dbo.sku, dbo.style, dbo.style_color, dbo.style_size, dbo.style_vendor, dbo.syn_view_wholesale_inventory_sku, dbo.vendor |
| dbo | [view_wholesale_inv_styclr_out](dbo.view_wholesale_inv_styclr_out.md) | dbo.color, dbo.style, dbo.style_color, dbo.style_vendor, dbo.syn_view_wholesale_inventory_sku, dbo.vendor |
| dbo | [view_wholesale_inv_style_outer](dbo.view_wholesale_inv_style_outer.md) | dbo.style, dbo.style_vendor, dbo.syn_view_wholesale_inventory_sku, dbo.vendor |
| dbo | [vwDW_DailySales_StyleColor_DOMO](dbo.vwDW_DailySales_StyleColor_DOMO.md) | dbo.date_dim, dbo.hist_flsh_style_loc_da, dbo.product_dim, dbo.xref_location_store |
| dbo | [vwDW_dim_InventoryStatus](dbo.vwDW_dim_InventoryStatus.md) | dbo.inventory_status |
| dbo | [vwDW_MerchPartitionData_biapp01](dbo.vwDW_MerchPartitionData_biapp01.md) | dbo.date_dim, dbo.hist_oh_styleclr_loc_wk, dbo.hist_styleclr_loc_wk |
| dbo | [vwDW_MerchPartitionData_biapp01_New](dbo.vwDW_MerchPartitionData_biapp01_New.md) | dbo.date_dim, dbo.hist_oh_styleclr_loc_wk, dbo.hist_styleclr_loc_wk |
| dbo | [vwDW_WeeklyAlloc_StyleColor_biapp01](dbo.vwDW_WeeklyAlloc_StyleColor_biapp01.md) | dbo.oo_all_style_loc_wk, dbo.product_dim, dbo.xref_date_merch_wk, dbo.xref_location_store |
| dbo | [vwDW_WeeklyAlloc_StyleColor_biapp01_v2](dbo.vwDW_WeeklyAlloc_StyleColor_biapp01_v2.md) | dbo.oo_all_style_loc_wk, dbo.product_dim, dbo.style, dbo.xref_date_merch_wk, dbo.xref_location_store |
| dbo | [vwDW_WeeklyAlloc_StyleColor_biapp01_v3](dbo.vwDW_WeeklyAlloc_StyleColor_biapp01_v3.md) | dbo.oo_all_style_loc_wk, dbo.product_dim, dbo.style, dbo.xref_date_merch_wk, dbo.xref_location_store |
| dbo | [vwDW_WeeklyAlloc_StyleColor_biapp01_v4](dbo.vwDW_WeeklyAlloc_StyleColor_biapp01_v4.md) | dbo.oo_all_style_loc_wk, dbo.product_dim, dbo.style, dbo.xref_date_merch_wk, dbo.xref_location_store |
| dbo | [vwDW_WeeklyOnHand_StyleColor](dbo.vwDW_WeeklyOnHand_StyleColor.md) | dbo.date_dim, dbo.hist_oh_styleclr_loc_wk, dbo.location, dbo.oo_all_styleclr_loc_wk, dbo.product_dim, dbo.sku, dbo.style, dbo.style_retail, dbo.upc, dbo.vwDW_Store |
| dbo | [vwDW_WeeklyOnHand_StyleColor_biapp01](dbo.vwDW_WeeklyOnHand_StyleColor_biapp01.md) | dbo.hist_oh_style_loc_wk, dbo.location, dbo.oo_all_style_loc_wk, dbo.product_dim, dbo.style_retail, dbo.xref_Cost_Rates, dbo.xref_date_merch_wk, dbo.xref_location_store |
| dbo | [vwDW_WeeklyOnHand_StyleColor_biapp01_v2](dbo.vwDW_WeeklyOnHand_StyleColor_biapp01_v2.md) | dbo.hist_oh_style_loc_wk, dbo.location, dbo.oo_all_style_loc_wk, dbo.product_dim, dbo.style, dbo.style_retail, dbo.xref_Cost_Rates, dbo.xref_date_merch_wk, dbo.xref_location_store |
| dbo | [vwDW_WeeklyOnHand_StyleColor_biapp01_v3](dbo.vwDW_WeeklyOnHand_StyleColor_biapp01_v3.md) | dbo.hist_oh_style_loc_wk, dbo.location, dbo.oo_all_style_loc_wk, dbo.product_dim, dbo.style, dbo.style_retail, dbo.xref_Cost_Rates, dbo.xref_date_merch_wk, dbo.xref_location_store |
| dbo | [vwDW_WeeklyOnHand_StyleColor_biapp01_v4](dbo.vwDW_WeeklyOnHand_StyleColor_biapp01_v4.md) | dbo.hist_oh_style_loc_wk, dbo.location, dbo.oo_all_style_loc_wk, dbo.product_dim, dbo.style, dbo.style_retail, dbo.xref_Cost_Rates, dbo.xref_date_merch_wk, dbo.xref_location_store |
| dbo | [vwDW_WeeklyOnHand_StyleColor_DOMO](dbo.vwDW_WeeklyOnHand_StyleColor_DOMO.md) | dbo.hist_oh_style_loc_wk, dbo.location, dbo.oo_all_style_loc_wk, dbo.product_dim, dbo.style_retail, dbo.xref_Cost_Rates, dbo.xref_date_merch_wk, dbo.xref_location_store |
| dbo | [vwDW_WeeklyOnHand_StyleColor_new](dbo.vwDW_WeeklyOnHand_StyleColor_new.md) | dbo.date_dim, dbo.hist_oh_styleclr_loc_wk, dbo.location, dbo.oo_all_styleclr_loc_wk, dbo.product_dim, dbo.sku, dbo.style, dbo.style_color, dbo.style_retail, dbo.upc, dbo.vwDW_Store |
| dbo | [vwDW_WeeklyOnHand_StyleColor_prod](dbo.vwDW_WeeklyOnHand_StyleColor_prod.md) | dbo.date_dim, dbo.hist_oh_styleclr_loc_wk, dbo.location, dbo.oo_all_styleclr_loc_wk, dbo.product_dim, dbo.sku, dbo.style, dbo.style_retail, dbo.upc, dbo.vwDW_Store |
| dbo | [vwDW_WeeklyOnHand_StyleColor_v2](dbo.vwDW_WeeklyOnHand_StyleColor_v2.md) | dbo.date_dim, dbo.hist_oh_styleclr_loc_wk, dbo.location, dbo.oo_all_styleclr_loc_wk, dbo.product_dim, dbo.sku, dbo.style, dbo.style_retail, dbo.upc, dbo.vwDW_Store |
| dbo | [vwDW_WeeklyOnOrder_StyleColor](dbo.vwDW_WeeklyOnOrder_StyleColor.md) | dbo.date_dim, dbo.location, dbo.oo_all_styleclr_loc_wk, dbo.product_dim, dbo.sku, dbo.style, dbo.style_retail, dbo.upc, dbo.vwDW_Store |
| dbo | [vwDW_WeeklyOnOrder_StyleColor_biapp01](dbo.vwDW_WeeklyOnOrder_StyleColor_biapp01.md) | dbo.oo_all_style_loc_wk, dbo.product_dim, dbo.style_retail, dbo.xref_Cost_Rates, dbo.xref_date_merch_wk, dbo.xref_location_store, dbo.xref_style_product |
| dbo | [vwDW_WeeklyOnOrder_StyleColor_biapp01_v2](dbo.vwDW_WeeklyOnOrder_StyleColor_biapp01_v2.md) | dbo.oo_all_style_loc_wk, dbo.product_dim, dbo.style, dbo.style_retail, dbo.xref_Cost_Rates, dbo.xref_date_merch_wk, dbo.xref_location_store, dbo.xref_style_product |
| dbo | [vwDW_WeeklyOnOrder_StyleColor_biapp01_v3](dbo.vwDW_WeeklyOnOrder_StyleColor_biapp01_v3.md) | dbo.oo_all_style_loc_wk, dbo.product_dim, dbo.style, dbo.style_retail, dbo.xref_Cost_Rates, dbo.xref_date_merch_wk, dbo.xref_location_store, dbo.xref_style_product |
| dbo | [vwDW_WeeklyOnOrder_StyleColor_biapp01_v4](dbo.vwDW_WeeklyOnOrder_StyleColor_biapp01_v4.md) | dbo.oo_all_style_loc_wk, dbo.product_dim, dbo.style, dbo.style_retail, dbo.xref_Cost_Rates, dbo.xref_date_merch_wk, dbo.xref_location_store, dbo.xref_style_product |
| dbo | [vwDW_WeeklyOnOrder_StyleColor_DOMO](dbo.vwDW_WeeklyOnOrder_StyleColor_DOMO.md) | dbo.oo_all_style_loc_wk, dbo.product_dim, dbo.style_retail, dbo.xref_Cost_Rates, dbo.xref_date_merch_wk, dbo.xref_location_store, dbo.xref_style_product |
| dbo | [vwDW_WeeklyOnOrder_StyleColor_new](dbo.vwDW_WeeklyOnOrder_StyleColor_new.md) | dbo.date_dim, dbo.location, dbo.oo_all_styleclr_loc_wk, dbo.product_dim, dbo.sku, dbo.style, dbo.style_color, dbo.style_retail, dbo.upc, dbo.vwDW_Store |
| dbo | [vwDW_WeeklySales_StyleColor](dbo.vwDW_WeeklySales_StyleColor.md) | dbo.date_dim, dbo.hist_styleclr_loc_wk, dbo.location, dbo.product_dim, dbo.sku, dbo.style, dbo.upc, dbo.vwDW_Store |
| dbo | [vwDW_WeeklySales_StyleColor_biapp01](dbo.vwDW_WeeklySales_StyleColor_biapp01.md) | dbo.hist_style_loc_wk, dbo.product_dim, dbo.xref_Cost_Rates, dbo.xref_date_merch_wk, dbo.xref_GBP_EUR_Rates, dbo.xref_location_store |
| dbo | [vwDW_WeeklySales_StyleColor_biapp01_v2](dbo.vwDW_WeeklySales_StyleColor_biapp01_v2.md) | dbo.hist_style_loc_wk, dbo.product_dim, dbo.style, dbo.xref_Cost_Rates, dbo.xref_date_merch_wk, dbo.xref_GBP_EUR_Rates, dbo.xref_location_store |
| dbo | [vwDW_WeeklySales_StyleColor_biapp01_v3](dbo.vwDW_WeeklySales_StyleColor_biapp01_v3.md) | dbo.hist_style_loc_wk, dbo.product_dim, dbo.store_dim, dbo.style, dbo.xref_Cost_Rates, dbo.xref_date_merch_wk, dbo.xref_GBP_EUR_Rates, dbo.xref_location_store |
| dbo | [vwDW_WeeklySales_StyleColor_biapp01_v4](dbo.vwDW_WeeklySales_StyleColor_biapp01_v4.md) | dbo.hist_style_loc_wk, dbo.product_dim, dbo.store_dim, dbo.style, dbo.xref_Cost_Rates, dbo.xref_date_merch_wk, dbo.xref_GBP_EUR_Rates, dbo.xref_location_store |
| dbo | [vwDW_WeeklySales_StyleColor_DOMO](dbo.vwDW_WeeklySales_StyleColor_DOMO.md) | dbo.hist_style_loc_wk, dbo.product_dim, dbo.xref_Cost_Rates, dbo.xref_date_merch_wk, dbo.xref_GBP_EUR_Rates, dbo.xref_location_store |
| dbo | [vwDW_WeeklySales_StyleColor_new](dbo.vwDW_WeeklySales_StyleColor_new.md) | dbo.date_dim, dbo.hist_styleclr_loc_wk, dbo.location, dbo.product_dim, dbo.sku, dbo.style, dbo.style_color, dbo.upc, dbo.vwDW_Store |
| dbo | [vwFranch_ExtractStyles](dbo.vwFranch_ExtractStyles.md) | dbo.attribute, dbo.attribute_set, dbo.calendar_year, dbo.color, dbo.entity_attribute_set, dbo.hierarchy_group, dbo.ib_activity_date, dbo.season, dbo.style, dbo.style_color, dbo.style_group, dbo.style_vendor, dbo.vendor, dbo.vwDW_ProductPrimaryJurisdiction |
| dbo | [vwTXT_Fields](dbo.vwTXT_Fields.md) | dbo.calendar_date, dbo.hist_style_chn_pd, dbo.style |
| MerchandisingPlanning | [vwTXT_CalculatedTime](MerchandisingPlanning.vwTXT_CalculatedTime.md) | dbo.calendar_date, dbo.calendar_period, dbo.calendar_week, dbo.calendar_year |
