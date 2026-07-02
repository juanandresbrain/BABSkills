# dbo.startup_oh_style_loc_pd_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.startup_oh_style_loc_pd_$sp"]
    dbo_calendar_merch_period(["dbo.calendar_merch_period"]) --> SP
    dbo_calendar_merch_week(["dbo.calendar_merch_week"]) --> SP
    dbo_dummy_hist_oh_style_loc_pd(["dbo.dummy_hist_oh_style_loc_pd"]) --> SP
    dbo_hist_oh_style_loc_pd(["dbo.hist_oh_style_loc_pd"]) --> SP
    dbo_hist_oh_style_loc_wk(["dbo.hist_oh_style_loc_wk"]) --> SP
    dbo_merch_year_pd_pf(["dbo.merch_year_pd_pf"]) --> SP
    dbo_startup_multi_currency_style_log(["dbo.startup_multi_currency_style_log"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar_merch_period |
| dbo.calendar_merch_week |
| dbo.dummy_hist_oh_style_loc_pd |
| dbo.hist_oh_style_loc_pd |
| dbo.hist_oh_style_loc_wk |
| dbo.merch_year_pd_pf |
| dbo.startup_multi_currency_style_log |

## Stored Procedure Code

```sql

```

