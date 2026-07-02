# dbo.dl_hist_styleclr

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| dl_hist_styleclr_id | bigint | 8 | 0 | YES |  |  |
| record_no | bigint | 8 | 0 |  |  |  |
| style_code | nvarchar | 40 | 0 |  |  |  |
| color_code | nvarchar | 6 | 0 |  |  |  |
| merch_year_wk | int | 4 | 0 |  |  |  |
| location_code | nvarchar | 40 | 0 |  |  |  |
| perm_md_retail | decimal | 9 | 0 |  |  |  |
| perm_mu_retail | decimal | 9 | 0 |  |  |  |
| perm_mdc_retail | decimal | 9 | 0 |  |  |  |
| perm_muc_retail | decimal | 9 | 0 |  |  |  |
| promo_pc_total_retail | decimal | 9 | 0 |  |  |  |
| received_units | int | 4 | 0 |  |  |  |
| received_retail | decimal | 9 | 0 |  |  |  |
| return_to_vendor_units | int | 4 | 0 |  |  |  |
| return_to_vendor_retail | decimal | 9 | 0 |  |  |  |
| distributions_units | int | 4 | 0 |  |  |  |
| distributions_retail | decimal | 9 | 0 |  |  |  |
| transfer_in_units | int | 4 | 0 |  |  |  |
| transfer_in_retail | decimal | 9 | 0 |  |  |  |
| transfer_out_units | int | 4 | 0 |  |  |  |
| transfer_out_retail | decimal | 9 | 0 |  |  |  |
| sales_total_units | int | 4 | 0 |  |  |  |
| sales_total_retail | decimal | 9 | 0 |  |  |  |
| sales_total_cost | decimal | 9 | 0 |  |  |  |
| return_units | int | 4 | 0 |  |  |  |
| return_retail | decimal | 9 | 0 |  |  |  |
| return_cost | decimal | 9 | 0 |  |  |  |
| shrink_actual_units | int | 4 | 0 |  |  |  |
| shrink_actual_retail | decimal | 9 | 0 |  |  |  |
| adjustments_total_units | int | 4 | 0 |  |  |  |
| adjustments_total_retail | decimal | 9 | 0 |  |  |  |
| perm_md_sellcurr_retail | decimal | 9 | 0 |  |  |  |
| perm_mu_sellcurr_retail | decimal | 9 | 0 |  |  |  |
| perm_mdc_sellcurr_retail | decimal | 9 | 0 |  |  |  |
| perm_muc_sellcurr_retail | decimal | 9 | 0 |  |  |  |
| promo_pc_total_sellcurr_retail | decimal | 9 | 0 |  |  |  |
| sales_total_sellcurr_retail | decimal | 9 | 0 |  |  |  |
| return_sellcurr_retail | decimal | 9 | 0 |  |  |  |
| exchange_rate_diff_retail | decimal | 9 | 0 |  |  |  |
| perm_md_retail_te | decimal | 9 | 0 |  |  |  |
| perm_mu_retail_te | decimal | 9 | 0 |  |  |  |
| perm_mdc_retail_te | decimal | 9 | 0 |  |  |  |
| perm_muc_retail_te | decimal | 9 | 0 |  |  |  |
| promo_pc_total_retail_te | decimal | 9 | 0 |  |  |  |
| received_retail_te | decimal | 9 | 0 |  |  |  |
| return_to_vendor_retail_te | decimal | 9 | 0 |  |  |  |
| distributions_retail_te | decimal | 9 | 0 |  |  |  |
| transfer_in_retail_te | decimal | 9 | 0 |  |  |  |
| transfer_out_retail_te | decimal | 9 | 0 |  |  |  |
| sales_total_retail_te | decimal | 9 | 0 |  |  |  |
| return_retail_te | decimal | 9 | 0 |  |  |  |
| shrink_actual_retail_te | decimal | 9 | 0 |  |  |  |
| adjustments_total_retail_te | decimal | 9 | 0 |  |  |  |
| sales_total_sellcurr_retail_te | decimal | 9 | 0 |  |  |  |
| return_sellcurr_retail_te | decimal | 9 | 0 |  |  |  |
| perm_md_sellcurr_retail_te | decimal | 9 | 0 |  |  |  |
| perm_mu_sellcurr_retail_te | decimal | 9 | 0 |  |  |  |
| perm_mdc_sellcurr_retail_te | decimal | 9 | 0 |  |  |  |
| perm_muc_sellcurr_retail_te | decimal | 9 | 0 |  |  |  |
| promo_pc_total_sellcurr_ret_te | decimal | 9 | 0 |  |  |  |
| valid_flag | bit | 1 | 0 |  |  |  |
| duplicate_flag | bit | 1 | 0 |  |  |  |
| style_code_fk_invalid_flag | bit | 1 | 0 |  |  |  |
| color_code_fk_invalid_flag | bit | 1 | 0 |  |  |  |
| style_color_fk_invalid_flag | bit | 1 | 0 |  |  |  |
| merch_year_wk_fk_invalid_flag | bit | 1 | 0 |  |  |  |
| location_code_fk_invalid_flag | bit | 1 | 0 |  |  |  |
| hist_past_cutoff_week | tinyint | 1 | 0 |  |  |  |
| already_on_file_flag | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.dl_hist_styleclr_vld_$sp](../../StoredProcedures/ma_01/dbo.dl_hist_styleclr_vld_$sp.md)
- [ma_01: dbo.dl_hist_task_imp_ld_prep_$sp](../../StoredProcedures/ma_01/dbo.dl_hist_task_imp_ld_prep_$sp.md)
- [ma_01: dbo.dl_hist_task_imp_trunc_$sp](../../StoredProcedures/ma_01/dbo.dl_hist_task_imp_trunc_$sp.md)

