# dbo.DC_MOVE_UPC_SKU

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DC_MOVE_UPC_SKU"]
    dbo_POS_ID_PLU_CODE(["dbo.POS_ID_PLU_CODE"]) --> SP
    dbo_TMP_POS_ID_PLU_CODE(["dbo.TMP_POS_ID_PLU_CODE"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.POS_ID_PLU_CODE |
| dbo.TMP_POS_ID_PLU_CODE |

## Stored Procedure Code

```sql

```

