# dbo.hist_styleclr_chn_yr

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_id | decimal | 9 | 0 | YES |  |  |
| color_id | smallint | 2 | 0 | YES |  |  |
| merch_year | smallint | 2 | 0 | YES |  |  |
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
| shipped_units | int | 4 | 1 |  |  |  |
| shipped_retail | decimal | 9 | 1 |  |  |  |
| shipped_retail_te | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.hk_style_delete_hist_$sp](../../StoredProcedures/ma_01/dbo.hk_style_delete_hist_$sp.md)
- [ma_01: dbo.post_hist_style_color_$sp](../../StoredProcedures/ma_01/dbo.post_hist_style_color_$sp.md)
- [ma_01: dbo.post_hist_styleclr_$sp](../../StoredProcedures/ma_01/dbo.post_hist_styleclr_$sp.md)

