# dbo.hist_currency_exchange_rate_pd_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.hist_currency_exchange_rate_pd_$sp"]
    dbo_calendar_date(["dbo.calendar_date"]) --> SP
    dbo_imp_cd_rim_oh_group_home(["dbo.imp_cd_rim_oh_group_home"]) --> SP
    dbo_imp_cd_rim_oh_group_local(["dbo.imp_cd_rim_oh_group_local"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar_date |
| dbo.imp_cd_rim_oh_group_home |
| dbo.imp_cd_rim_oh_group_local |

## Stored Procedure Code

```sql

```

