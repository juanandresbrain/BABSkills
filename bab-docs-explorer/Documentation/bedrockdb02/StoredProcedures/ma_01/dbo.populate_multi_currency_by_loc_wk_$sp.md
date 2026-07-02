# dbo.populate_multi_currency_by_loc_wk_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.populate_multi_currency_by_loc_wk_$sp"]
    dbo_a(["dbo.a"]) --> SP
    dbo_calendar_date(["dbo.calendar_date"]) --> SP
    dbo_calendar_merch_week(["dbo.calendar_merch_week"]) --> SP
    dbo_m(["dbo.m"]) --> SP
    dbo_multi_currency_location_cost_wk(["dbo.multi_currency_location_cost_wk"]) --> SP
    dbo_multi_currency_location_retail_wk(["dbo.multi_currency_location_retail_wk"]) --> SP
    dbo_syn_multi_currency_location(["dbo.syn_multi_currency_location"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.a |
| dbo.calendar_date |
| dbo.calendar_merch_week |
| dbo.m |
| dbo.multi_currency_location_cost_wk |
| dbo.multi_currency_location_retail_wk |
| dbo.syn_multi_currency_location |

## Stored Procedure Code

```sql

```

