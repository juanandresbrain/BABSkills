# dbo.startup_flsh_group_loc_da_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.startup_flsh_group_loc_da_$sp"]
    dbo_calendar_date(["dbo.calendar_date"]) --> SP
    dbo_country(["dbo.country"]) --> SP
    dbo_flsh_group_loc_rate_by_date(["dbo.flsh_group_loc_rate_by_date"]) --> SP
    dbo_hist_flsh_group_loc_da(["dbo.hist_flsh_group_loc_da"]) --> SP
    dbo_jurisdiction(["dbo.jurisdiction"]) --> SP
    dbo_location(["dbo.location"]) --> SP
    dbo_startup_multi_currency_group_log(["dbo.startup_multi_currency_group_log"]) --> SP
    dbo_syn_currency_conversion(["dbo.syn_currency_conversion"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar_date |
| dbo.country |
| dbo.flsh_group_loc_rate_by_date |
| dbo.hist_flsh_group_loc_da |
| dbo.jurisdiction |
| dbo.location |
| dbo.startup_multi_currency_group_log |
| dbo.syn_currency_conversion |

## Stored Procedure Code

```sql

```

