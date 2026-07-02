# dbo.post_oh_work_sku_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.post_oh_work_sku_$sp"]
    dbo_calendar(["dbo.calendar"]) --> SP
    dbo_calendar_merch_period(["dbo.calendar_merch_period"]) --> SP
    dbo_calendar_merch_week(["dbo.calendar_merch_week"]) --> SP
    dbo_post_hist_oh_sku(["dbo.post_hist_oh_sku"]) --> SP
    dbo_post_oh_work_sku_li(["dbo.post_oh_work_sku_li"]) --> SP
    dbo_post_oh_work_sku_pd(["dbo.post_oh_work_sku_pd"]) --> SP
    dbo_post_oh_work_sku_wk(["dbo.post_oh_work_sku_wk"]) --> SP
    dbo_post_oh_work_sku_yr(["dbo.post_oh_work_sku_yr"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar |
| dbo.calendar_merch_period |
| dbo.calendar_merch_week |
| dbo.post_hist_oh_sku |
| dbo.post_oh_work_sku_li |
| dbo.post_oh_work_sku_pd |
| dbo.post_oh_work_sku_wk |
| dbo.post_oh_work_sku_yr |

## Stored Procedure Code

```sql

```

