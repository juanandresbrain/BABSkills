# dbo.startup_oo_all_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.startup_oo_all_$sp"]
    dbo_startup_error_handler__sp(["dbo.startup_error_handler_$sp"]) --> SP
    dbo_startup_multi_currency_main_log(["dbo.startup_multi_currency_main_log"]) --> SP
    dbo_startup_oo_all_group__sp(["dbo.startup_oo_all_group_$sp"]) --> SP
    dbo_startup_oo_all_style__sp(["dbo.startup_oo_all_style_$sp"]) --> SP
    dbo_startup_oo_all_styleclr__sp(["dbo.startup_oo_all_styleclr_$sp"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.startup_error_handler_$sp |
| dbo.startup_multi_currency_main_log |
| dbo.startup_oo_all_group_$sp |
| dbo.startup_oo_all_style_$sp |
| dbo.startup_oo_all_styleclr_$sp |

## Stored Procedure Code

```sql

```

