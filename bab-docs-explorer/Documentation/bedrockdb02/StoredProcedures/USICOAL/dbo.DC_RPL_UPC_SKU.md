# dbo.DC_RPL_UPC_SKU

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DC_RPL_UPC_SKU"]
    dbo_ITEM(["dbo.ITEM"]) --> SP
    dbo_POS_IDENTITY(["dbo.POS_IDENTITY"]) --> SP
    dbo_TMP_POS_ID_PLU_CODE(["dbo.TMP_POS_ID_PLU_CODE"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ITEM |
| dbo.POS_IDENTITY |
| dbo.TMP_POS_ID_PLU_CODE |

## Stored Procedure Code

```sql

```

