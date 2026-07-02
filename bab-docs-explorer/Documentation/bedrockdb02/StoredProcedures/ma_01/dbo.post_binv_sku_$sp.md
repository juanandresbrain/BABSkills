# dbo.post_binv_sku_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.post_binv_sku_$sp"]
    dbo_a(["dbo.a"]) --> SP
    dbo_calendar(["dbo.calendar"]) --> SP
    dbo_calendar_merch_period(["dbo.calendar_merch_period"]) --> SP
    dbo_calendar_merch_week(["dbo.calendar_merch_week"]) --> SP
    dbo_hist_oh_sku_chn_li(["dbo.hist_oh_sku_chn_li"]) --> SP
    dbo_hist_oh_sku_chn_pd(["dbo.hist_oh_sku_chn_pd"]) --> SP
    dbo_hist_oh_sku_chn_wk(["dbo.hist_oh_sku_chn_wk"]) --> SP
    dbo_hist_oh_sku_chn_yr(["dbo.hist_oh_sku_chn_yr"]) --> SP
    dbo_hist_oh_sku_loc_li(["dbo.hist_oh_sku_loc_li"]) --> SP
    dbo_hist_oh_sku_loc_pd(["dbo.hist_oh_sku_loc_pd"]) --> SP
    dbo_hist_oh_sku_loc_wk(["dbo.hist_oh_sku_loc_wk"]) --> SP
    dbo_hist_oh_sku_loc_yr(["dbo.hist_oh_sku_loc_yr"]) --> SP
    dbo_post_binv_sku_adj(["dbo.post_binv_sku_adj"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.a |
| dbo.calendar |
| dbo.calendar_merch_period |
| dbo.calendar_merch_week |
| dbo.hist_oh_sku_chn_li |
| dbo.hist_oh_sku_chn_pd |
| dbo.hist_oh_sku_chn_wk |
| dbo.hist_oh_sku_chn_yr |
| dbo.hist_oh_sku_loc_li |
| dbo.hist_oh_sku_loc_pd |
| dbo.hist_oh_sku_loc_wk |
| dbo.hist_oh_sku_loc_yr |
| dbo.post_binv_sku_adj |

## Stored Procedure Code

```sql

```

