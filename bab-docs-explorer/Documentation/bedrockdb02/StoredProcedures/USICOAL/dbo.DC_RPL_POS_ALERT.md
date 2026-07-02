# dbo.DC_RPL_POS_ALERT

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DC_RPL_POS_ALERT"]
    dbo_ITEM(["dbo.ITEM"]) --> SP
    dbo_ITEM_ALERT(["dbo.ITEM_ALERT"]) --> SP
    dbo_TMP_POS_ITEM_ALERT(["dbo.TMP_POS_ITEM_ALERT"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ITEM |
| dbo.ITEM_ALERT |
| dbo.TMP_POS_ITEM_ALERT |

## Stored Procedure Code

```sql

```

