# dbo.post_hist_cmp_sku_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.post_hist_cmp_sku_$sp"]
    dbo_a(["dbo.a"]) --> SP
    dbo_calendar_merch_week(["dbo.calendar_merch_week"]) --> SP
    dbo_hist_cmp_sku_chn_li(["dbo.hist_cmp_sku_chn_li"]) --> SP
    dbo_hist_cmp_sku_chn_pd(["dbo.hist_cmp_sku_chn_pd"]) --> SP
    dbo_hist_cmp_sku_chn_wk(["dbo.hist_cmp_sku_chn_wk"]) --> SP
    dbo_hist_cmp_sku_chn_yr(["dbo.hist_cmp_sku_chn_yr"]) --> SP
    dbo_hist_cmp_sku_loc_li(["dbo.hist_cmp_sku_loc_li"]) --> SP
    dbo_hist_cmp_sku_loc_pd(["dbo.hist_cmp_sku_loc_pd"]) --> SP
    dbo_hist_cmp_sku_loc_wk(["dbo.hist_cmp_sku_loc_wk"]) --> SP
    dbo_hist_cmp_sku_loc_yr(["dbo.hist_cmp_sku_loc_yr"]) --> SP
    dbo_post_cmp_work_sku(["dbo.post_cmp_work_sku"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.a |
| dbo.calendar_merch_week |
| dbo.hist_cmp_sku_chn_li |
| dbo.hist_cmp_sku_chn_pd |
| dbo.hist_cmp_sku_chn_wk |
| dbo.hist_cmp_sku_chn_yr |
| dbo.hist_cmp_sku_loc_li |
| dbo.hist_cmp_sku_loc_pd |
| dbo.hist_cmp_sku_loc_wk |
| dbo.hist_cmp_sku_loc_yr |
| dbo.post_cmp_work_sku |

## Stored Procedure Code

```sql

```

