# dbo.startup_group_loc_yr_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.startup_group_loc_yr_$sp"]
    dbo_calendar_merch_period(["dbo.calendar_merch_period"]) --> SP
    dbo_dummy_hist_group_loc_yr(["dbo.dummy_hist_group_loc_yr"]) --> SP
    dbo_hist_group_loc_pd(["dbo.hist_group_loc_pd"]) --> SP
    dbo_hist_group_loc_yr(["dbo.hist_group_loc_yr"]) --> SP
    dbo_merch_year_pf(["dbo.merch_year_pf"]) --> SP
    dbo_startup_multi_currency_group_log(["dbo.startup_multi_currency_group_log"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar_merch_period |
| dbo.dummy_hist_group_loc_yr |
| dbo.hist_group_loc_pd |
| dbo.hist_group_loc_yr |
| dbo.merch_year_pf |
| dbo.startup_multi_currency_group_log |

## Stored Procedure Code

```sql

```

