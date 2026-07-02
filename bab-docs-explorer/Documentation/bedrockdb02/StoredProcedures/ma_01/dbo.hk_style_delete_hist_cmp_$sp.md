# dbo.hk_style_delete_hist_cmp_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.hk_style_delete_hist_cmp_$sp"]
    dbo_hist_cmp_sku_chn_li(["dbo.hist_cmp_sku_chn_li"]) --> SP
    dbo_hist_cmp_sku_chn_pd(["dbo.hist_cmp_sku_chn_pd"]) --> SP
    dbo_hist_cmp_sku_chn_wk(["dbo.hist_cmp_sku_chn_wk"]) --> SP
    dbo_hist_cmp_sku_chn_yr(["dbo.hist_cmp_sku_chn_yr"]) --> SP
    dbo_hist_cmp_sku_loc_li(["dbo.hist_cmp_sku_loc_li"]) --> SP
    dbo_hist_cmp_sku_loc_pd(["dbo.hist_cmp_sku_loc_pd"]) --> SP
    dbo_hist_cmp_sku_loc_wk(["dbo.hist_cmp_sku_loc_wk"]) --> SP
    dbo_hist_cmp_sku_loc_yr(["dbo.hist_cmp_sku_loc_yr"]) --> SP
    dbo_hist_cmp_style_chn_li(["dbo.hist_cmp_style_chn_li"]) --> SP
    dbo_hist_cmp_style_chn_pd(["dbo.hist_cmp_style_chn_pd"]) --> SP
    dbo_hist_cmp_style_chn_wk(["dbo.hist_cmp_style_chn_wk"]) --> SP
    dbo_hist_cmp_style_chn_yr(["dbo.hist_cmp_style_chn_yr"]) --> SP
    dbo_hist_cmp_style_loc_li(["dbo.hist_cmp_style_loc_li"]) --> SP
    dbo_hist_cmp_style_loc_pd(["dbo.hist_cmp_style_loc_pd"]) --> SP
    dbo_hist_cmp_style_loc_wk(["dbo.hist_cmp_style_loc_wk"]) --> SP
    dbo_hist_cmp_style_loc_yr(["dbo.hist_cmp_style_loc_yr"]) --> SP
    dbo_hist_cmp_styleclr_chn_li(["dbo.hist_cmp_styleclr_chn_li"]) --> SP
    dbo_hist_cmp_styleclr_chn_pd(["dbo.hist_cmp_styleclr_chn_pd"]) --> SP
    dbo_hist_cmp_styleclr_chn_wk(["dbo.hist_cmp_styleclr_chn_wk"]) --> SP
    dbo_hist_cmp_styleclr_chn_yr(["dbo.hist_cmp_styleclr_chn_yr"]) --> SP
    dbo_hist_cmp_styleclr_loc_li(["dbo.hist_cmp_styleclr_loc_li"]) --> SP
    dbo_hist_cmp_styleclr_loc_pd(["dbo.hist_cmp_styleclr_loc_pd"]) --> SP
    dbo_hist_cmp_styleclr_loc_wk(["dbo.hist_cmp_styleclr_loc_wk"]) --> SP
    dbo_hist_cmp_styleclr_loc_yr(["dbo.hist_cmp_styleclr_loc_yr"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.hist_cmp_sku_chn_li |
| dbo.hist_cmp_sku_chn_pd |
| dbo.hist_cmp_sku_chn_wk |
| dbo.hist_cmp_sku_chn_yr |
| dbo.hist_cmp_sku_loc_li |
| dbo.hist_cmp_sku_loc_pd |
| dbo.hist_cmp_sku_loc_wk |
| dbo.hist_cmp_sku_loc_yr |
| dbo.hist_cmp_style_chn_li |
| dbo.hist_cmp_style_chn_pd |
| dbo.hist_cmp_style_chn_wk |
| dbo.hist_cmp_style_chn_yr |
| dbo.hist_cmp_style_loc_li |
| dbo.hist_cmp_style_loc_pd |
| dbo.hist_cmp_style_loc_wk |
| dbo.hist_cmp_style_loc_yr |
| dbo.hist_cmp_styleclr_chn_li |
| dbo.hist_cmp_styleclr_chn_pd |
| dbo.hist_cmp_styleclr_chn_wk |
| dbo.hist_cmp_styleclr_chn_yr |
| dbo.hist_cmp_styleclr_loc_li |
| dbo.hist_cmp_styleclr_loc_pd |
| dbo.hist_cmp_styleclr_loc_wk |
| dbo.hist_cmp_styleclr_loc_yr |

## Stored Procedure Code

```sql

```

