# dbo.calendar_merch_period

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| calendar_period_id | decimal | 9 | 0 | YES |  |  |
| calendar_id | smallint | 2 | 0 |  |  |  |
| merch_year | smallint | 2 | 0 |  |  |  |
| merch_period | tinyint | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.get_last_pd_$fn](../../StoredProcedures/ma_01/dbo.get_last_pd_$fn.md)
- [ma_01: dbo.get_last_x_pds_$fn](../../StoredProcedures/ma_01/dbo.get_last_x_pds_$fn.md)
- [ma_01: dbo.get_last_x_pds_ly_$fn](../../StoredProcedures/ma_01/dbo.get_last_x_pds_ly_$fn.md)
- [ma_01: dbo.get_last_x_yrs_$fn](../../StoredProcedures/ma_01/dbo.get_last_x_yrs_$fn.md)
- [ma_01: dbo.get_next_x_pds_$fn](../../StoredProcedures/ma_01/dbo.get_next_x_pds_$fn.md)
- [ma_01: dbo.get_next_x_yrs_$fn](../../StoredProcedures/ma_01/dbo.get_next_x_yrs_$fn.md)
- [ma_01: dbo.get_prev_last_x_pds_$fn](../../StoredProcedures/ma_01/dbo.get_prev_last_x_pds_$fn.md)
- [ma_01: dbo.get_prev_last_x_pds_ly_$fn](../../StoredProcedures/ma_01/dbo.get_prev_last_x_pds_ly_$fn.md)
- [ma_01: dbo.get_prev_last_x_yrs_$fn](../../StoredProcedures/ma_01/dbo.get_prev_last_x_yrs_$fn.md)
- [ma_01: dbo.get_prev_pd_$fn](../../StoredProcedures/ma_01/dbo.get_prev_pd_$fn.md)
- [ma_01: dbo.nsb_otb_chain_$sp](../../StoredProcedures/ma_01/dbo.nsb_otb_chain_$sp.md)
- [ma_01: dbo.nsb_otb_location_$sp](../../StoredProcedures/ma_01/dbo.nsb_otb_location_$sp.md)
- [ma_01: dbo.nsb_par_chain_$sp](../../StoredProcedures/ma_01/dbo.nsb_par_chain_$sp.md)
- [ma_01: dbo.nsb_par_chain_rim_$sp](../../StoredProcedures/ma_01/dbo.nsb_par_chain_rim_$sp.md)
- [ma_01: dbo.nsb_par_location_$sp](../../StoredProcedures/ma_01/dbo.nsb_par_location_$sp.md)
- [ma_01: dbo.populate_multi_currency_by_loc_pd_$sp](../../StoredProcedures/ma_01/dbo.populate_multi_currency_by_loc_pd_$sp.md)
- [ma_01: dbo.post_binv_group_$sp](../../StoredProcedures/ma_01/dbo.post_binv_group_$sp.md)
- [ma_01: dbo.post_binv_sku_$sp](../../StoredProcedures/ma_01/dbo.post_binv_sku_$sp.md)
- [ma_01: dbo.post_binv_style_$sp](../../StoredProcedures/ma_01/dbo.post_binv_style_$sp.md)
- [ma_01: dbo.post_binv_styleclr_$sp](../../StoredProcedures/ma_01/dbo.post_binv_styleclr_$sp.md)
- [ma_01: dbo.post_hist_group_rim_$sp](../../StoredProcedures/ma_01/dbo.post_hist_group_rim_$sp.md)
- [ma_01: dbo.post_oh_work_group_$sp](../../StoredProcedures/ma_01/dbo.post_oh_work_group_$sp.md)
- [ma_01: dbo.post_oh_work_sku_$sp](../../StoredProcedures/ma_01/dbo.post_oh_work_sku_$sp.md)
- [ma_01: dbo.post_oh_work_style_$sp](../../StoredProcedures/ma_01/dbo.post_oh_work_style_$sp.md)
- [ma_01: dbo.post_oh_work_styleclr_$sp](../../StoredProcedures/ma_01/dbo.post_oh_work_styleclr_$sp.md)
- [ma_01: dbo.post_oo_unc_$sp](../../StoredProcedures/ma_01/dbo.post_oo_unc_$sp.md)
- [ma_01: dbo.roll_oh_group_chn_pd_$sp](../../StoredProcedures/ma_01/dbo.roll_oh_group_chn_pd_$sp.md)
- [ma_01: dbo.roll_oh_group_loc_pd_$sp](../../StoredProcedures/ma_01/dbo.roll_oh_group_loc_pd_$sp.md)
- [ma_01: dbo.roll_oh_sku_chn_pd_$sp](../../StoredProcedures/ma_01/dbo.roll_oh_sku_chn_pd_$sp.md)
- [ma_01: dbo.roll_oh_sku_loc_pd_$sp](../../StoredProcedures/ma_01/dbo.roll_oh_sku_loc_pd_$sp.md)
- [ma_01: dbo.roll_oh_style_chn_pd_$sp](../../StoredProcedures/ma_01/dbo.roll_oh_style_chn_pd_$sp.md)
- [ma_01: dbo.roll_oh_style_color_chn_pd_$sp](../../StoredProcedures/ma_01/dbo.roll_oh_style_color_chn_pd_$sp.md)
- [ma_01: dbo.roll_oh_style_color_loc_pd_$sp](../../StoredProcedures/ma_01/dbo.roll_oh_style_color_loc_pd_$sp.md)
- [ma_01: dbo.roll_oh_style_loc_pd_$sp](../../StoredProcedures/ma_01/dbo.roll_oh_style_loc_pd_$sp.md)
- [ma_01: dbo.rpt_otb_chain_$sp](../../StoredProcedures/ma_01/dbo.rpt_otb_chain_$sp.md)
- [ma_01: dbo.rpt_otb_location_$sp](../../StoredProcedures/ma_01/dbo.rpt_otb_location_$sp.md)
- [ma_01: dbo.rpt_par_chain_$sp](../../StoredProcedures/ma_01/dbo.rpt_par_chain_$sp.md)
- [ma_01: dbo.rpt_par_chain_rim_$sp](../../StoredProcedures/ma_01/dbo.rpt_par_chain_rim_$sp.md)
- [ma_01: dbo.rpt_par_location_home_$sp](../../StoredProcedures/ma_01/dbo.rpt_par_location_home_$sp.md)
- [ma_01: dbo.rpt_par_location_local_$sp](../../StoredProcedures/ma_01/dbo.rpt_par_location_local_$sp.md)
- [ma_01: dbo.startup_cmp_group_loc_pd_$sp](../../StoredProcedures/ma_01/dbo.startup_cmp_group_loc_pd_$sp.md)
- [ma_01: dbo.startup_cmp_group_loc_yr_$sp](../../StoredProcedures/ma_01/dbo.startup_cmp_group_loc_yr_$sp.md)
- [ma_01: dbo.startup_cmp_style_loc_pd_$sp](../../StoredProcedures/ma_01/dbo.startup_cmp_style_loc_pd_$sp.md)
- [ma_01: dbo.startup_cmp_style_loc_yr_$sp](../../StoredProcedures/ma_01/dbo.startup_cmp_style_loc_yr_$sp.md)
- [ma_01: dbo.startup_cmp_styleclr_loc_pd_$sp](../../StoredProcedures/ma_01/dbo.startup_cmp_styleclr_loc_pd_$sp.md)
- [ma_01: dbo.startup_cmp_styleclr_loc_yr_$sp](../../StoredProcedures/ma_01/dbo.startup_cmp_styleclr_loc_yr_$sp.md)
- [ma_01: dbo.startup_group_loc_pd_$sp](../../StoredProcedures/ma_01/dbo.startup_group_loc_pd_$sp.md)
- [ma_01: dbo.startup_group_loc_yr_$sp](../../StoredProcedures/ma_01/dbo.startup_group_loc_yr_$sp.md)
- [ma_01: dbo.startup_hist_rim_oh_group_$sp](../../StoredProcedures/ma_01/dbo.startup_hist_rim_oh_group_$sp.md)
- [ma_01: dbo.startup_oh_group_loc_pd_$sp](../../StoredProcedures/ma_01/dbo.startup_oh_group_loc_pd_$sp.md)
- [ma_01: dbo.startup_oh_group_loc_yr_$sp](../../StoredProcedures/ma_01/dbo.startup_oh_group_loc_yr_$sp.md)
- [ma_01: dbo.startup_oh_style_loc_pd_$sp](../../StoredProcedures/ma_01/dbo.startup_oh_style_loc_pd_$sp.md)
- [ma_01: dbo.startup_oh_style_loc_yr_$sp](../../StoredProcedures/ma_01/dbo.startup_oh_style_loc_yr_$sp.md)
- [ma_01: dbo.startup_oh_styleclr_loc_pd_$sp](../../StoredProcedures/ma_01/dbo.startup_oh_styleclr_loc_pd_$sp.md)
- [ma_01: dbo.startup_oh_styleclr_loc_yr_$sp](../../StoredProcedures/ma_01/dbo.startup_oh_styleclr_loc_yr_$sp.md)
- [ma_01: dbo.startup_style_loc_pd_$sp](../../StoredProcedures/ma_01/dbo.startup_style_loc_pd_$sp.md)
- [ma_01: dbo.startup_style_loc_yr_$sp](../../StoredProcedures/ma_01/dbo.startup_style_loc_yr_$sp.md)
- [ma_01: dbo.startup_styleclr_loc_pd_$sp](../../StoredProcedures/ma_01/dbo.startup_styleclr_loc_pd_$sp.md)
- [ma_01: dbo.startup_styleclr_loc_yr_$sp](../../StoredProcedures/ma_01/dbo.startup_styleclr_loc_yr_$sp.md)
- [ma_01: dbo.summarize_hist_cmp_group_$sp](../../StoredProcedures/ma_01/dbo.summarize_hist_cmp_group_$sp.md)
- [ma_01: dbo.summarize_hist_cmp_sku_$sp](../../StoredProcedures/ma_01/dbo.summarize_hist_cmp_sku_$sp.md)
- [ma_01: dbo.summarize_hist_cmp_style_$sp](../../StoredProcedures/ma_01/dbo.summarize_hist_cmp_style_$sp.md)
- [ma_01: dbo.summarize_hist_cmp_styleclr_$sp](../../StoredProcedures/ma_01/dbo.summarize_hist_cmp_styleclr_$sp.md)

