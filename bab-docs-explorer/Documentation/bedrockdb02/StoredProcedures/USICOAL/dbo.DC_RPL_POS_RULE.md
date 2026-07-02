# dbo.DC_RPL_POS_RULE

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DC_RPL_POS_RULE"]
    dbo_DC_ITEM(["dbo.DC_ITEM"]) --> SP
    dbo_SPIFF_DEFINITION(["dbo.SPIFF_DEFINITION"]) --> SP
    dbo_TMP_ITEM_POS_SELL_RULE(["dbo.TMP_ITEM_POS_SELL_RULE"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DC_ITEM |
| dbo.SPIFF_DEFINITION |
| dbo.TMP_ITEM_POS_SELL_RULE |

## Stored Procedure Code

```sql

```

