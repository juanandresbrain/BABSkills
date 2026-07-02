# dbo.job_params

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| job_type | int | 4 | 0 | YES |  |  |
| job_batch_size | decimal | 9 | 0 |  |  |  |
| range_batch_size | decimal | 9 | 0 |  |  |  |
| debug_flag | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.create_jobs_sales_posting_$sp](../../StoredProcedures/me_01/dbo.create_jobs_sales_posting_$sp.md)
- [me_01: dbo.import_asn_$sp](../../StoredProcedures/me_01/dbo.import_asn_$sp.md)
- [me_01: dbo.import_pc_$sp](../../StoredProcedures/me_01/dbo.import_pc_$sp.md)
- [me_01: dbo.populate_im_sale_from_file_$sp](../../StoredProcedures/me_01/dbo.populate_im_sale_from_file_$sp.md)
- [me_01: dbo.populate_im_sale_from_SA_$sp](../../StoredProcedures/me_01/dbo.populate_im_sale_from_SA_$sp.md)
- [me_01: dbo.return_debug_flag_$sp](../../StoredProcedures/me_01/dbo.return_debug_flag_$sp.md)
- [ma_01: dbo.get_job_params_$sp](../../StoredProcedures/ma_01/dbo.get_job_params_$sp.md)
- [ma_01: dbo.return_debug_flag_$sp](../../StoredProcedures/ma_01/dbo.return_debug_flag_$sp.md)
- [ma_01: dbo.roll_oh_group_chn_pd_$sp](../../StoredProcedures/ma_01/dbo.roll_oh_group_chn_pd_$sp.md)
- [ma_01: dbo.roll_oh_group_chn_wk_$sp](../../StoredProcedures/ma_01/dbo.roll_oh_group_chn_wk_$sp.md)
- [ma_01: dbo.roll_oh_group_chn_yr_$sp](../../StoredProcedures/ma_01/dbo.roll_oh_group_chn_yr_$sp.md)
- [ma_01: dbo.roll_oh_group_loc_pd_$sp](../../StoredProcedures/ma_01/dbo.roll_oh_group_loc_pd_$sp.md)
- [ma_01: dbo.roll_oh_group_loc_wk_$sp](../../StoredProcedures/ma_01/dbo.roll_oh_group_loc_wk_$sp.md)
- [ma_01: dbo.roll_oh_group_loc_yr_$sp](../../StoredProcedures/ma_01/dbo.roll_oh_group_loc_yr_$sp.md)
- [ma_01: dbo.roll_oh_sku_chn_pd_$sp](../../StoredProcedures/ma_01/dbo.roll_oh_sku_chn_pd_$sp.md)
- [ma_01: dbo.roll_oh_sku_chn_wk_$sp](../../StoredProcedures/ma_01/dbo.roll_oh_sku_chn_wk_$sp.md)
- [ma_01: dbo.roll_oh_sku_chn_yr_$sp](../../StoredProcedures/ma_01/dbo.roll_oh_sku_chn_yr_$sp.md)
- [ma_01: dbo.roll_oh_sku_loc_pd_$sp](../../StoredProcedures/ma_01/dbo.roll_oh_sku_loc_pd_$sp.md)
- [ma_01: dbo.roll_oh_sku_loc_wk_$sp](../../StoredProcedures/ma_01/dbo.roll_oh_sku_loc_wk_$sp.md)
- [ma_01: dbo.roll_oh_sku_loc_yr_$sp](../../StoredProcedures/ma_01/dbo.roll_oh_sku_loc_yr_$sp.md)
- [ma_01: dbo.roll_oh_style_chn_pd_$sp](../../StoredProcedures/ma_01/dbo.roll_oh_style_chn_pd_$sp.md)
- [ma_01: dbo.roll_oh_style_chn_wk_$sp](../../StoredProcedures/ma_01/dbo.roll_oh_style_chn_wk_$sp.md)
- [ma_01: dbo.roll_oh_style_chn_yr_$sp](../../StoredProcedures/ma_01/dbo.roll_oh_style_chn_yr_$sp.md)
- [ma_01: dbo.roll_oh_style_color_chn_pd_$sp](../../StoredProcedures/ma_01/dbo.roll_oh_style_color_chn_pd_$sp.md)
- [ma_01: dbo.roll_oh_style_color_chn_wk_$sp](../../StoredProcedures/ma_01/dbo.roll_oh_style_color_chn_wk_$sp.md)
- [ma_01: dbo.roll_oh_style_color_chn_yr_$sp](../../StoredProcedures/ma_01/dbo.roll_oh_style_color_chn_yr_$sp.md)
- [ma_01: dbo.roll_oh_style_color_loc_pd_$sp](../../StoredProcedures/ma_01/dbo.roll_oh_style_color_loc_pd_$sp.md)
- [ma_01: dbo.roll_oh_style_color_loc_wk_$sp](../../StoredProcedures/ma_01/dbo.roll_oh_style_color_loc_wk_$sp.md)
- [ma_01: dbo.roll_oh_style_color_loc_yr_$sp](../../StoredProcedures/ma_01/dbo.roll_oh_style_color_loc_yr_$sp.md)
- [ma_01: dbo.roll_oh_style_loc_pd_$sp](../../StoredProcedures/ma_01/dbo.roll_oh_style_loc_pd_$sp.md)
- [ma_01: dbo.roll_oh_style_loc_wk_$sp](../../StoredProcedures/ma_01/dbo.roll_oh_style_loc_wk_$sp.md)
- [ma_01: dbo.roll_oh_style_loc_yr_$sp](../../StoredProcedures/ma_01/dbo.roll_oh_style_loc_yr_$sp.md)

