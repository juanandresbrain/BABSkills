# dbo.hk_style_delete_hist_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.hk_style_delete_hist_$sp"]
    dbo_hist_sku_chn_li(["dbo.hist_sku_chn_li"]) --> SP
    dbo_hist_sku_chn_pd(["dbo.hist_sku_chn_pd"]) --> SP
    dbo_hist_sku_chn_wk(["dbo.hist_sku_chn_wk"]) --> SP
    dbo_hist_sku_chn_yr(["dbo.hist_sku_chn_yr"]) --> SP
    dbo_hist_sku_loc_li(["dbo.hist_sku_loc_li"]) --> SP
    dbo_hist_sku_loc_pd(["dbo.hist_sku_loc_pd"]) --> SP
    dbo_hist_sku_loc_wk(["dbo.hist_sku_loc_wk"]) --> SP
    dbo_hist_sku_loc_yr(["dbo.hist_sku_loc_yr"]) --> SP
    dbo_hist_style_chn_li(["dbo.hist_style_chn_li"]) --> SP
    dbo_hist_style_chn_pd(["dbo.hist_style_chn_pd"]) --> SP
    dbo_hist_style_chn_wk(["dbo.hist_style_chn_wk"]) --> SP
    dbo_hist_style_chn_yr(["dbo.hist_style_chn_yr"]) --> SP
    dbo_hist_style_loc_li(["dbo.hist_style_loc_li"]) --> SP
    dbo_hist_style_loc_pd(["dbo.hist_style_loc_pd"]) --> SP
    dbo_hist_style_loc_wk(["dbo.hist_style_loc_wk"]) --> SP
    dbo_hist_style_loc_yr(["dbo.hist_style_loc_yr"]) --> SP
    dbo_hist_styleclr_chn_li(["dbo.hist_styleclr_chn_li"]) --> SP
    dbo_hist_styleclr_chn_pd(["dbo.hist_styleclr_chn_pd"]) --> SP
    dbo_hist_styleclr_chn_wk(["dbo.hist_styleclr_chn_wk"]) --> SP
    dbo_hist_styleclr_chn_yr(["dbo.hist_styleclr_chn_yr"]) --> SP
    dbo_hist_styleclr_loc_li(["dbo.hist_styleclr_loc_li"]) --> SP
    dbo_hist_styleclr_loc_pd(["dbo.hist_styleclr_loc_pd"]) --> SP
    dbo_hist_styleclr_loc_wk(["dbo.hist_styleclr_loc_wk"]) --> SP
    dbo_hist_styleclr_loc_yr(["dbo.hist_styleclr_loc_yr"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.hist_sku_chn_li |
| dbo.hist_sku_chn_pd |
| dbo.hist_sku_chn_wk |
| dbo.hist_sku_chn_yr |
| dbo.hist_sku_loc_li |
| dbo.hist_sku_loc_pd |
| dbo.hist_sku_loc_wk |
| dbo.hist_sku_loc_yr |
| dbo.hist_style_chn_li |
| dbo.hist_style_chn_pd |
| dbo.hist_style_chn_wk |
| dbo.hist_style_chn_yr |
| dbo.hist_style_loc_li |
| dbo.hist_style_loc_pd |
| dbo.hist_style_loc_wk |
| dbo.hist_style_loc_yr |
| dbo.hist_styleclr_chn_li |
| dbo.hist_styleclr_chn_pd |
| dbo.hist_styleclr_chn_wk |
| dbo.hist_styleclr_chn_yr |
| dbo.hist_styleclr_loc_li |
| dbo.hist_styleclr_loc_pd |
| dbo.hist_styleclr_loc_wk |
| dbo.hist_styleclr_loc_yr |

## Stored Procedure Code

```sql

```

