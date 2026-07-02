# dbo.hist_style_loc_li

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_id | decimal | 9 | 0 | YES |  |  |
| location_id | smallint | 2 | 0 | YES |  |  |
| perm_md_retail | decimal | 9 | 0 |  |  |  |
| perm_mu_retail | decimal | 9 | 0 |  |  |  |
| perm_mdc_retail | decimal | 9 | 0 |  |  |  |
| perm_muc_retail | decimal | 9 | 0 |  |  |  |
| promo_pc_total_retail | decimal | 9 | 0 |  |  |  |
| received_units | int | 4 | 0 |  |  |  |
| received_retail | decimal | 9 | 0 |  |  |  |
| received_cost | decimal | 9 | 0 |  |  |  |
| return_to_vendor_units | int | 4 | 0 |  |  |  |
| return_to_vendor_retail | decimal | 9 | 0 |  |  |  |
| return_to_vendor_cost | decimal | 9 | 0 |  |  |  |
| distributions_units | int | 4 | 0 |  |  |  |
| distributions_retail | decimal | 9 | 0 |  |  |  |
| distributions_cost | decimal | 9 | 0 |  |  |  |
| transfer_in_units | int | 4 | 0 |  |  |  |
| transfer_in_retail | decimal | 9 | 0 |  |  |  |
| transfer_in_cost | decimal | 9 | 0 |  |  |  |
| transfer_out_units | int | 4 | 0 |  |  |  |
| transfer_out_retail | decimal | 9 | 0 |  |  |  |
| transfer_out_cost | decimal | 9 | 0 |  |  |  |
| sales_total_units | int | 4 | 0 |  |  |  |
| sales_total_retail | decimal | 9 | 0 |  |  |  |
| sales_total_cost | decimal | 9 | 0 |  |  |  |
| return_units | int | 4 | 0 |  |  |  |
| return_retail | decimal | 9 | 0 |  |  |  |
| return_cost | decimal | 9 | 0 |  |  |  |
| shrink_actual_units | int | 4 | 0 |  |  |  |
| shrink_actual_retail | decimal | 9 | 0 |  |  |  |
| shrink_actual_cost | decimal | 9 | 0 |  |  |  |
| adjustments_total_units | int | 4 | 0 |  |  |  |
| adjustments_total_retail | decimal | 9 | 0 |  |  |  |
| adjustments_total_cost | decimal | 9 | 0 |  |  |  |
| cost_factors_total_cost | decimal | 9 | 0 |  |  |  |
| discounts_total_cost | decimal | 9 | 0 |  |  |  |
| sales_total_sellcurr_retail | decimal | 9 | 0 |  |  |  |
| return_sellcurr_retail | decimal | 9 | 0 |  |  |  |
| perm_md_sellcurr_retail | decimal | 9 | 0 |  |  |  |
| perm_mu_sellcurr_retail | decimal | 9 | 0 |  |  |  |
| perm_mdc_sellcurr_retail | decimal | 9 | 0 |  |  |  |
| perm_muc_sellcurr_retail | decimal | 9 | 0 |  |  |  |
| promo_pc_total_sellcurr_retail | decimal | 9 | 0 |  |  |  |
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
| received_retail_local | decimal | 9 | 1 |  |  |  |
| received_retail_te_local | decimal | 9 | 1 |  |  |  |
| received_cost_local | decimal | 9 | 1 |  |  |  |
| return_to_vendor_retail_local | decimal | 9 | 1 |  |  |  |
| return_to_vendor_retail_te_local | decimal | 9 | 1 |  |  |  |
| return_to_vendor_cost_local | decimal | 9 | 1 |  |  |  |
| distributions_retail_local | decimal | 9 | 1 |  |  |  |
| distributions_retail_te_local | decimal | 9 | 1 |  |  |  |
| distributions_cost_local | decimal | 9 | 1 |  |  |  |
| transfer_in_retail_local | decimal | 9 | 1 |  |  |  |
| transfer_in_retail_te_local | decimal | 9 | 1 |  |  |  |
| transfer_in_cost_local | decimal | 9 | 1 |  |  |  |
| transfer_out_retail_local | decimal | 9 | 1 |  |  |  |
| transfer_out_retail_te_local | decimal | 9 | 1 |  |  |  |
| transfer_out_cost_local | decimal | 9 | 1 |  |  |  |
| sales_total_cost_local | decimal | 9 | 1 |  |  |  |
| return_cost_local | decimal | 9 | 1 |  |  |  |
| shrink_actual_retail_local | decimal | 9 | 1 |  |  |  |
| shrink_actual_retail_te_local | decimal | 9 | 1 |  |  |  |
| shrink_actual_cost_local | decimal | 9 | 1 |  |  |  |
| adjustments_total_retail_local | decimal | 9 | 1 |  |  |  |
| adjustments_total_retail_te_local | decimal | 9 | 1 |  |  |  |
| adjustments_total_cost_local | decimal | 9 | 1 |  |  |  |
| cost_factors_total_cost_local | decimal | 9 | 1 |  |  |  |
| discounts_total_cost_local | decimal | 9 | 1 |  |  |  |
| shipped_units | int | 4 | 1 |  |  |  |
| shipped_cost | decimal | 9 | 1 |  |  |  |
| shipped_cost_local | decimal | 9 | 1 |  |  |  |
| shipped_retail | decimal | 9 | 1 |  |  |  |
| shipped_retail_te | decimal | 9 | 1 |  |  |  |
| shipped_retail_local | decimal | 9 | 1 |  |  |  |
| shipped_retail_te_local | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.hk_style_delete_hist_$sp](../../StoredProcedures/ma_01/dbo.hk_style_delete_hist_$sp.md)
- [ma_01: dbo.nsb_style_analysis_$sp](../../StoredProcedures/ma_01/dbo.nsb_style_analysis_$sp.md)
- [ma_01: dbo.post_hist_style_$sp](../../StoredProcedures/ma_01/dbo.post_hist_style_$sp.md)
- [ma_01: dbo.rpt_style_analysis_$sp](../../StoredProcedures/ma_01/dbo.rpt_style_analysis_$sp.md)
- [ma_01: dbo.startup_style_loc_li_$sp](../../StoredProcedures/ma_01/dbo.startup_style_loc_li_$sp.md)

