# dbo.ma_01_hist_styleclr_loc_wk

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_id | decimal | 9 | 1 |  |  |  |
| color_id | int | 4 | 1 |  |  |  |
| merch_year_wk | int | 4 | 1 |  |  |  |
| location_id | int | 4 | 1 |  |  |  |
| perm_md_retail | decimal | 9 | 1 |  |  |  |
| perm_mu_retail | decimal | 9 | 1 |  |  |  |
| perm_mdc_retail | decimal | 9 | 1 |  |  |  |
| perm_muc_retail | decimal | 9 | 1 |  |  |  |
| promo_pc_total_retail | decimal | 9 | 1 |  |  |  |
| received_units | int | 4 | 1 |  |  |  |
| received_retail | decimal | 9 | 1 |  |  |  |
| return_to_vendor_units | int | 4 | 1 |  |  |  |
| return_to_vendor_retail | decimal | 9 | 1 |  |  |  |
| distributions_units | int | 4 | 1 |  |  |  |
| distributions_retail | decimal | 9 | 1 |  |  |  |
| transfer_in_units | int | 4 | 1 |  |  |  |
| transfer_in_retail | decimal | 9 | 1 |  |  |  |
| transfer_out_units | int | 4 | 1 |  |  |  |
| transfer_out_retail | decimal | 9 | 1 |  |  |  |
| sales_total_units | int | 4 | 1 |  |  |  |
| sales_total_retail | decimal | 9 | 1 |  |  |  |
| sales_total_cost | decimal | 9 | 1 |  |  |  |
| return_units | int | 4 | 1 |  |  |  |
| return_retail | decimal | 9 | 1 |  |  |  |
| return_cost | decimal | 9 | 1 |  |  |  |
| shrink_actual_units | int | 4 | 1 |  |  |  |
| shrink_actual_retail | decimal | 9 | 1 |  |  |  |
| adjustments_total_units | int | 4 | 1 |  |  |  |
| adjustments_total_retail | decimal | 9 | 1 |  |  |  |
| sales_total_sellcurr_retail | decimal | 9 | 1 |  |  |  |
| return_sellcurr_retail | decimal | 9 | 1 |  |  |  |
| perm_md_sellcurr_retail | decimal | 9 | 1 |  |  |  |
| perm_mu_sellcurr_retail | decimal | 9 | 1 |  |  |  |
| perm_mdc_sellcurr_retail | decimal | 9 | 1 |  |  |  |
| perm_muc_sellcurr_retail | decimal | 9 | 1 |  |  |  |
| promo_pc_total_sellcurr_retail | decimal | 9 | 1 |  |  |  |
| exchange_rate_diff_retail | decimal | 9 | 1 |  |  |  |
| perm_md_retail_te | decimal | 9 | 1 |  |  |  |
| perm_mu_retail_te | decimal | 9 | 1 |  |  |  |
| perm_mdc_retail_te | decimal | 9 | 1 |  |  |  |
| perm_muc_retail_te | decimal | 9 | 1 |  |  |  |
| promo_pc_total_retail_te | decimal | 9 | 1 |  |  |  |
| received_retail_te | decimal | 9 | 1 |  |  |  |
| return_to_vendor_retail_te | decimal | 9 | 1 |  |  |  |
| distributions_retail_te | decimal | 9 | 1 |  |  |  |
| transfer_in_retail_te | decimal | 9 | 1 |  |  |  |
| transfer_out_retail_te | decimal | 9 | 1 |  |  |  |
| sales_total_retail_te | decimal | 9 | 1 |  |  |  |
| return_retail_te | decimal | 9 | 1 |  |  |  |
| shrink_actual_retail_te | decimal | 9 | 1 |  |  |  |
| adjustments_total_retail_te | decimal | 9 | 1 |  |  |  |
| sales_total_sellcurr_retail_te | decimal | 9 | 1 |  |  |  |
| return_sellcurr_retail_te | decimal | 9 | 1 |  |  |  |
| perm_md_sellcurr_retail_te | decimal | 9 | 1 |  |  |  |
| perm_mu_sellcurr_retail_te | decimal | 9 | 1 |  |  |  |
| perm_mdc_sellcurr_retail_te | decimal | 9 | 1 |  |  |  |
| perm_muc_sellcurr_retail_te | decimal | 9 | 1 |  |  |  |
| promo_pc_total_sellcurr_ret_te | decimal | 9 | 1 |  |  |  |
| received_retail_local | decimal | 9 | 1 |  |  |  |
| received_retail_te_local | decimal | 9 | 1 |  |  |  |
| return_to_vendor_retail_local | decimal | 9 | 1 |  |  |  |
| return_to_vendor_retail_te_local | decimal | 9 | 1 |  |  |  |
| distributions_retail_local | decimal | 9 | 1 |  |  |  |
| distributions_retail_te_local | decimal | 9 | 1 |  |  |  |
| transfer_in_retail_local | decimal | 9 | 1 |  |  |  |
| transfer_in_retail_te_local | decimal | 9 | 1 |  |  |  |
| transfer_out_retail_local | decimal | 9 | 1 |  |  |  |
| transfer_out_retail_te_local | decimal | 9 | 1 |  |  |  |
| sales_total_cost_local | decimal | 9 | 1 |  |  |  |
| return_cost_local | decimal | 9 | 1 |  |  |  |
| shrink_actual_retail_local | decimal | 9 | 1 |  |  |  |
| shrink_actual_retail_te_local | decimal | 9 | 1 |  |  |  |
| adjustments_total_retail_local | decimal | 9 | 1 |  |  |  |
| adjustments_total_retail_te_local | decimal | 9 | 1 |  |  |  |
| shipped_units | int | 4 | 1 |  |  |  |
| shipped_retail | decimal | 9 | 1 |  |  |  |
| shipped_retail_te | decimal | 9 | 1 |  |  |  |
| shipped_retail_local | decimal | 9 | 1 |  |  |  |
| shipped_retail_te_local | decimal | 9 | 1 |  |  |  |
