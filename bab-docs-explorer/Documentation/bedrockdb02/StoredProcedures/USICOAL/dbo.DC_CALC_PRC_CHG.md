# dbo.DC_CALC_PRC_CHG

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DC_CALC_PRC_CHG"]
    dbo_DC_PRC_CHG_ITEM(["dbo.DC_PRC_CHG_ITEM"]) --> SP
    dbo_ITEM(["dbo.ITEM"]) --> SP
    dbo_PRICE_CHANGE(["dbo.PRICE_CHANGE"]) --> SP
    dbo_STORE_ITEM(["dbo.STORE_ITEM"]) --> SP
    dbo_TMP_PRC_CHANGE(["dbo.TMP_PRC_CHANGE"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DC_PRC_CHG_ITEM |
| dbo.ITEM |
| dbo.PRICE_CHANGE |
| dbo.STORE_ITEM |
| dbo.TMP_PRC_CHANGE |

## Stored Procedure Code

```sql

```

