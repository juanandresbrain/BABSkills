# dbo.DC_INS_ITM_ADDL_INFO

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DC_INS_ITM_ADDL_INFO"]
    dbo_DC_ITEM(["dbo.DC_ITEM"]) --> SP
    dbo_ITEM_ADDL_INFO(["dbo.ITEM_ADDL_INFO"]) --> SP
    dbo_TMP_ITEM(["dbo.TMP_ITEM"]) --> SP
    dbo_TMP_ITEM_ADDL_INFO(["dbo.TMP_ITEM_ADDL_INFO"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DC_ITEM |
| dbo.ITEM_ADDL_INFO |
| dbo.TMP_ITEM |
| dbo.TMP_ITEM_ADDL_INFO |

## Stored Procedure Code

```sql

```

