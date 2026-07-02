# dbo.DC_UPD_ITM_ALERT

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DC_UPD_ITM_ALERT"]
    dbo_DC_ITEM(["dbo.DC_ITEM"]) --> SP
    dbo_ITEM_ALERT(["dbo.ITEM_ALERT"]) --> SP
    dbo_TMP_ITEM(["dbo.TMP_ITEM"]) --> SP
    dbo_TMP_ITEM_ALERT(["dbo.TMP_ITEM_ALERT"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DC_ITEM |
| dbo.ITEM_ALERT |
| dbo.TMP_ITEM |
| dbo.TMP_ITEM_ALERT |

## Stored Procedure Code

```sql

```

