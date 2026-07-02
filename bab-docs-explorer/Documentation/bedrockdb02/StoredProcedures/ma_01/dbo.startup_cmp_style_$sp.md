# dbo.startup_cmp_style_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.startup_cmp_style_$sp"]
    dbo_startup_cmp_style_loc_li__sp(["dbo.startup_cmp_style_loc_li_$sp"]) --> SP
    dbo_startup_cmp_style_loc_pd__sp(["dbo.startup_cmp_style_loc_pd_$sp"]) --> SP
    dbo_startup_cmp_style_loc_wk__sp(["dbo.startup_cmp_style_loc_wk_$sp"]) --> SP
    dbo_startup_cmp_style_loc_yr__sp(["dbo.startup_cmp_style_loc_yr_$sp"]) --> SP
    dbo_startup_error_handler__sp(["dbo.startup_error_handler_$sp"]) --> SP
    dbo_startup_multi_currency_main_log(["dbo.startup_multi_currency_main_log"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.startup_cmp_style_loc_li_$sp |
| dbo.startup_cmp_style_loc_pd_$sp |
| dbo.startup_cmp_style_loc_wk_$sp |
| dbo.startup_cmp_style_loc_yr_$sp |
| dbo.startup_error_handler_$sp |
| dbo.startup_multi_currency_main_log |

## Stored Procedure Code

```sql

```

