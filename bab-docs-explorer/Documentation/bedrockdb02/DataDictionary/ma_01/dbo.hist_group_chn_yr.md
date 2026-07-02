# dbo.hist_group_chn_yr

**Database:** ma_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| hierarchy_group_id | int | 4 | 0 | YES |  |  |
| merch_year | smallint | 2 | 0 | YES |  |  |
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
| shrink_provision_units | int | 4 | 0 |  |  |  |
| shrink_provision_retail | decimal | 9 | 0 |  |  |  |
| shrink_provision_cost | decimal | 9 | 0 |  |  |  |
| adjustments_total_units | int | 4 | 0 |  |  |  |
| adjustments_total_retail | decimal | 9 | 0 |  |  |  |
| adjustments_total_cost | decimal | 9 | 0 |  |  |  |
| cost_factors_total_cost | decimal | 9 | 0 |  |  |  |
| discounts_total_cost | decimal | 9 | 0 |  |  |  |
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
| inventory_reductions_cost | decimal | 9 | 1 |  |  |  |
| shrink_total_cost | decimal | 9 | 1 |  |  |  |
| markdown_cost | decimal | 9 | 1 |  |  |  |
| markdown_promo_cost | decimal | 9 | 1 |  |  |  |
| rim_additions_cost | decimal | 9 | 1 |  |  |  |
| distribution_net_retail | decimal | 9 | 1 |  |  |  |
| purchase_net_retail | decimal | 9 | 1 |  |  |  |
| transfer_net_retail | decimal | 9 | 1 |  |  |  |
| markups_retail | decimal | 9 | 1 |  |  |  |
| shipped_units | int | 4 | 1 |  |  |  |
| shipped_cost | decimal | 9 | 1 |  |  |  |
| shipped_retail | decimal | 9 | 1 |  |  |  |
| shipped_retail_te | decimal | 9 | 1 |  |  |  |

## Referenced By Stored Procedures

- [ma_01: dbo.post_hist_group_$sp](../../StoredProcedures/ma_01/dbo.post_hist_group_$sp.md)
- [ma_01: dbo.post_hist_group_rim_$sp](../../StoredProcedures/ma_01/dbo.post_hist_group_rim_$sp.md)
- [ma_01: dbo.reclass_hist_$sp](../../StoredProcedures/ma_01/dbo.reclass_hist_$sp.md)

