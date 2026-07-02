# dbo.get_this_yr_beg_prd_$fn

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.get_this_yr_beg_prd_$fn"]
    dbo_calendar(["dbo.calendar"]) --> SP
    dbo_calendar_merch_week(["dbo.calendar_merch_week"]) --> SP
    dbo_post_parameter(["dbo.post_parameter"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar |
| dbo.calendar_merch_week |
| dbo.post_parameter |

## Stored Procedure Code

```sql

```

