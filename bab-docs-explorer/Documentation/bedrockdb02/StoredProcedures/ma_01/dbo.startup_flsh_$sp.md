# dbo.startup_flsh_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.startup_flsh_$sp"]
    dbo_startup_error_handler__sp(["dbo.startup_error_handler_$sp"]) --> SP
    dbo_startup_flsh_group_loc_da__sp(["dbo.startup_flsh_group_loc_da_$sp"]) --> SP
    dbo_startup_flsh_loc_da__sp(["dbo.startup_flsh_loc_da_$sp"]) --> SP
    dbo_startup_flsh_style_loc_da__sp(["dbo.startup_flsh_style_loc_da_$sp"]) --> SP
    dbo_startup_multi_currency_main_log(["dbo.startup_multi_currency_main_log"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.startup_error_handler_$sp |
| dbo.startup_flsh_group_loc_da_$sp |
| dbo.startup_flsh_loc_da_$sp |
| dbo.startup_flsh_style_loc_da_$sp |
| dbo.startup_multi_currency_main_log |

## Stored Procedure Code

```sql

```

