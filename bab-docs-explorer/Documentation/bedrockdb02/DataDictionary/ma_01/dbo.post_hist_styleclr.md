# dbo.post_hist_styleclr

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_id | decimal | 9 | 0 |  |  |  |
| color_id | smallint | 2 | 0 |  |  |  |
| merch_year_wk | int | 4 | 0 |  |  |  |
| location_id | smallint | 2 | 0 |  |  |  |
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
| sales_total_sellcurr_retail | decimal | 9 | 0 |  |  |  |
| return_sellcurr_retail | decimal | 9 | 0 |  |  |  |
| perm_md_sellcurr_retail | decimal | 9 | 0 |  |  |  |
| perm_mu_sellcurr_retail | decimal | 9 | 0 |  |  |  |
| perm_mdc_sellcurr_retail | decimal | 9 | 0 |  |  |  |
| perm_muc_sellcurr_retail | decimal | 9 | 0 |  |  |  |
| promo_pc_total_sellcurr_retail | decimal | 9 | 0 |  |  |  |
| exchange_rate_diff_retail | decimal | 9 | 0 |  |  |  |
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

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerification](../../StoredProcedures/me_01/dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerification.md)
- [me_01: dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJC2](../../StoredProcedures/me_01/dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJC2.md)
- [me_01: dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJC2V2](../../StoredProcedures/me_01/dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJC2V2.md)
- [me_01: dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJCtest](../../StoredProcedures/me_01/dbo.spMerchandisingReportInfobaseVsMerchantViewDailyVerificationJCtest.md)
- [ma_01: dbo.post_hist_oh_cmp_styleclr_$sp](../../StoredProcedures/ma_01/dbo.post_hist_oh_cmp_styleclr_$sp.md)
- [ma_01: dbo.post_hist_styleclr_$sp](../../StoredProcedures/ma_01/dbo.post_hist_styleclr_$sp.md)

