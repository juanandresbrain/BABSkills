# dbo.summarize_hist_cmp_sku_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.summarize_hist_cmp_sku_$sp"]
    dbo_calendar_merch_period(["dbo.calendar_merch_period"]) --> SP
    dbo_calendar_merch_week(["dbo.calendar_merch_week"]) --> SP
    dbo_hist_cmp_sku_chn_li(["dbo.hist_cmp_sku_chn_li"]) --> SP
    dbo_hist_cmp_sku_chn_pd(["dbo.hist_cmp_sku_chn_pd"]) --> SP
    dbo_hist_cmp_sku_chn_wk(["dbo.hist_cmp_sku_chn_wk"]) --> SP
    dbo_hist_cmp_sku_chn_yr(["dbo.hist_cmp_sku_chn_yr"]) --> SP
    dbo_hist_cmp_sku_loc_li(["dbo.hist_cmp_sku_loc_li"]) --> SP
    dbo_hist_cmp_sku_loc_pd(["dbo.hist_cmp_sku_loc_pd"]) --> SP
    dbo_hist_cmp_sku_loc_wk(["dbo.hist_cmp_sku_loc_wk"]) --> SP
    dbo_hist_cmp_sku_loc_yr(["dbo.hist_cmp_sku_loc_yr"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar_merch_period |
| dbo.calendar_merch_week |
| dbo.hist_cmp_sku_chn_li |
| dbo.hist_cmp_sku_chn_pd |
| dbo.hist_cmp_sku_chn_wk |
| dbo.hist_cmp_sku_chn_yr |
| dbo.hist_cmp_sku_loc_li |
| dbo.hist_cmp_sku_loc_pd |
| dbo.hist_cmp_sku_loc_wk |
| dbo.hist_cmp_sku_loc_yr |

## Stored Procedure Code

```sql

```

