# dbo.startup_style_loc_wk_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.startup_style_loc_wk_$sp"]
    dbo_calendar_date(["dbo.calendar_date"]) --> SP
    dbo_calendar_merch_week(["dbo.calendar_merch_week"]) --> SP
    dbo_dummy_hist_style_loc_wk(["dbo.dummy_hist_style_loc_wk"]) --> SP
    dbo_hist_style_loc_wk(["dbo.hist_style_loc_wk"]) --> SP
    dbo_merch_year_wk_pf(["dbo.merch_year_wk_pf"]) --> SP
    dbo_multi_currency_location_cost_wk(["dbo.multi_currency_location_cost_wk"]) --> SP
    dbo_multi_currency_location_retail_wk(["dbo.multi_currency_location_retail_wk"]) --> SP
    dbo_startup_multi_currency_style_log(["dbo.startup_multi_currency_style_log"]) --> SP
    dbo_style_currency_rate(["dbo.style_currency_rate"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar_date |
| dbo.calendar_merch_week |
| dbo.dummy_hist_style_loc_wk |
| dbo.hist_style_loc_wk |
| dbo.merch_year_wk_pf |
| dbo.multi_currency_location_cost_wk |
| dbo.multi_currency_location_retail_wk |
| dbo.startup_multi_currency_style_log |
| dbo.style_currency_rate |

## Stored Procedure Code

```sql

```

