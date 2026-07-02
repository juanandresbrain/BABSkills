# dbo.DC_INS_ITM_KYWRD

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DC_INS_ITM_KYWRD"]
    dbo_DC_ITEM(["dbo.DC_ITEM"]) --> SP
    dbo_ITEM_KEYWORD(["dbo.ITEM_KEYWORD"]) --> SP
    dbo_TMP_ITEM(["dbo.TMP_ITEM"]) --> SP
    dbo_TMP_ITEM_KEYWORD(["dbo.TMP_ITEM_KEYWORD"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DC_ITEM |
| dbo.ITEM_KEYWORD |
| dbo.TMP_ITEM |
| dbo.TMP_ITEM_KEYWORD |

## Stored Procedure Code

```sql

```

