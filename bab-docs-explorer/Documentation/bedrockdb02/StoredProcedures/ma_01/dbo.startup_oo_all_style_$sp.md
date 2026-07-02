# dbo.startup_oo_all_style_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.startup_oo_all_style_$sp"]
    dbo_calendar_date(["dbo.calendar_date"]) --> SP
    dbo_calendar_merch_week(["dbo.calendar_merch_week"]) --> SP
    dbo_multi_currency_location_cost_wk(["dbo.multi_currency_location_cost_wk"]) --> SP
    dbo_multi_currency_location_retail_wk(["dbo.multi_currency_location_retail_wk"]) --> SP
    dbo_oo_all_style_currency_rate(["dbo.oo_all_style_currency_rate"]) --> SP
    dbo_oo_all_style_loc_li(["dbo.oo_all_style_loc_li"]) --> SP
    dbo_oo_all_style_loc_pd(["dbo.oo_all_style_loc_pd"]) --> SP
    dbo_oo_all_style_loc_wk(["dbo.oo_all_style_loc_wk"]) --> SP
    dbo_oo_all_style_loc_yr(["dbo.oo_all_style_loc_yr"]) --> SP
    dbo_startup_multi_currency_style_log(["dbo.startup_multi_currency_style_log"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar_date |
| dbo.calendar_merch_week |
| dbo.multi_currency_location_cost_wk |
| dbo.multi_currency_location_retail_wk |
| dbo.oo_all_style_currency_rate |
| dbo.oo_all_style_loc_li |
| dbo.oo_all_style_loc_pd |
| dbo.oo_all_style_loc_wk |
| dbo.oo_all_style_loc_yr |
| dbo.startup_multi_currency_style_log |

## Stored Procedure Code

```sql

```

