# dbo.DC_UPD_POS_RULE

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DC_UPD_POS_RULE"]
    dbo_DC_ITEM(["dbo.DC_ITEM"]) --> SP
    dbo_ITEM_POS_SELL_RULE(["dbo.ITEM_POS_SELL_RULE"]) --> SP
    dbo_SPIFF_DEFINITION(["dbo.SPIFF_DEFINITION"]) --> SP
    dbo_TMP_ITEM(["dbo.TMP_ITEM"]) --> SP
    dbo_TMP_ITEM_POS_SELL_RULE(["dbo.TMP_ITEM_POS_SELL_RULE"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DC_ITEM |
| dbo.ITEM_POS_SELL_RULE |
| dbo.SPIFF_DEFINITION |
| dbo.TMP_ITEM |
| dbo.TMP_ITEM_POS_SELL_RULE |

## Stored Procedure Code

```sql

```

