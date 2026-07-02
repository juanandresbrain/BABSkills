# dbo.RPT_DAILY_TAX_RATES1

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.RPT_DAILY_TAX_RATES1"]
    dbo_STORE(["dbo.STORE"]) --> SP
    dbo_STORE_TEXT_VARIABLE(["dbo.STORE_TEXT_VARIABLE"]) --> SP
    dbo_TAX_GRP_ZONE_AUTH(["dbo.TAX_GRP_ZONE_AUTH"]) --> SP
    dbo_TAX_RULE(["dbo.TAX_RULE"]) --> SP
    dbo_VALUE_ADDED_TAX(["dbo.VALUE_ADDED_TAX"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.STORE |
| dbo.STORE_TEXT_VARIABLE |
| dbo.TAX_GRP_ZONE_AUTH |
| dbo.TAX_RULE |
| dbo.VALUE_ADDED_TAX |

## Stored Procedure Code

```sql

```

