# dbo.DC_DEL_PRC_CHG

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DC_DEL_PRC_CHG"]
    dbo_PRICE_CHANGE(["dbo.PRICE_CHANGE"]) --> SP
    dbo_PRICE_CHANGE_ITEM(["dbo.PRICE_CHANGE_ITEM"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.PRICE_CHANGE |
| dbo.PRICE_CHANGE_ITEM |

## Stored Procedure Code

```sql

```

