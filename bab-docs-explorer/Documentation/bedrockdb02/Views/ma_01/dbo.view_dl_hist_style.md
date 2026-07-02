# dbo.view_dl_hist_style

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_dl_hist_style"]
    dbo_dl_hist_style(["dbo.dl_hist_style"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.dl_hist_style |

## View Code

```sql
create view dbo.view_dl_hist_style AS
SELECT dl_hist_style_id,
   record_no,   
   style_code,
   merch_year_wk,
   location_code,
   perm_md_retail,
   perm_mu_retail,
   perm_mdc_retail,
   perm_muc_retail,
   promo_pc_total_retail,
   received_units,
   received_retail,
   received_cost,
   return_to_vendor_units,
   return_to_vendor_retail,
   return_to_vendor_cost,
   distributions_units,
   distributions_retail,
   distributions_cost,
   transfer_in_units,
   transfer_in_retail,
   transfer_in_cost,
   transfer_out_units,
   transfer_out_retail,
   transfer_out_cost,
   sales_total_units,
   sales_total_retail,
   sales_total_cost,
   return_units,
   return_retail,
   return_cost,
   shrink_actual_units,
   shrink_actual_retail,
   shrink_actual_cost,
   adjustments_total_units,
   adjustments_total_retail,
   adjustments_total_cost,
   cost_factors_total_cost,
   discounts_total_cost,
   perm_md_sellcurr_retail,
   perm_mu_sellcurr_retail,
   perm_mdc_sellcurr_retail,
   perm_muc_sellcurr_retail,   
   promo_pc_total_sellcurr_retail,   
   sales_total_sellcurr_retail,   
   return_sellcurr_retail,
   exchange_rate_diff_retail,
   perm_md_retail_te,
   perm_mu_retail_te,
   perm_mdc_retail_te,
   perm_muc_retail_te,
   promo_pc_total_retail_te,
   received_retail_te,
   return_to_vendor_retail_te,
   distributions_retail_te,
   transfer_in_retail_te,
   transfer_out_retail_te,
   sales_total_retail_te,
   return_retail_te,
   shrink_actual_retail_te,
   adjustments_total_retail_te,
   sales_total_sellcurr_retail_te,
   return_sellcurr_retail_te,
   perm_md_sellcurr_retail_te,
   perm_mu_sellcurr_retail_te,
   perm_mdc_sellcurr_retail_te,
   perm_muc_sellcurr_retail_te,
   promo_pc_total_sellcurr_ret_te
FROM dl_hist_style
```

