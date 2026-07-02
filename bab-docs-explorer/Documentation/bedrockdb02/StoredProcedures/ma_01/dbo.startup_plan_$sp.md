# dbo.startup_plan_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.startup_plan_$sp"]
    dbo_startup_error_handler__sp(["dbo.startup_error_handler_$sp"]) --> SP
    dbo_startup_multi_currency_main_log(["dbo.startup_multi_currency_main_log"]) --> SP
    dbo_startup_plan_group_chn__sp(["dbo.startup_plan_group_chn_$sp"]) --> SP
    dbo_startup_plan_group_loc_pd__sp(["dbo.startup_plan_group_loc_pd_$sp"]) --> SP
    dbo_startup_plan_group_loc_wk__sp(["dbo.startup_plan_group_loc_wk_$sp"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.startup_error_handler_$sp |
| dbo.startup_multi_currency_main_log |
| dbo.startup_plan_group_chn_$sp |
| dbo.startup_plan_group_loc_pd_$sp |
| dbo.startup_plan_group_loc_wk_$sp |

## Stored Procedure Code

```sql

```

