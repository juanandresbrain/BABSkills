# dbo.DC_PRC_CHG_STR_ITM

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DC_PRC_CHG_STR_ITM"]
    dbo_DC_STORE_ITEM(["dbo.DC_STORE_ITEM"]) --> SP
    dbo_ITEM(["dbo.ITEM"]) --> SP
    dbo_STORE_ITEM(["dbo.STORE_ITEM"]) --> SP
    dbo_TMP_PRC_CHANGE(["dbo.TMP_PRC_CHANGE"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DC_STORE_ITEM |
| dbo.ITEM |
| dbo.STORE_ITEM |
| dbo.TMP_PRC_CHANGE |

## Stored Procedure Code

```sql

```

