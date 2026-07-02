# dbo.startup_oh_group_loc_li_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.startup_oh_group_loc_li_$sp"]
    dbo_hist_oh_group_loc_li(["dbo.hist_oh_group_loc_li"]) --> SP
    dbo_hist_oh_group_loc_yr(["dbo.hist_oh_group_loc_yr"]) --> SP
    dbo_startup_multi_currency_group_log(["dbo.startup_multi_currency_group_log"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.hist_oh_group_loc_li |
| dbo.hist_oh_group_loc_yr |
| dbo.startup_multi_currency_group_log |

## Stored Procedure Code

```sql

```

