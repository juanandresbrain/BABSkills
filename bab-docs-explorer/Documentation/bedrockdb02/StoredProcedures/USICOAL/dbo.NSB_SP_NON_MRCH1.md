# dbo.NSB_SP_NON_MRCH1

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.NSB_SP_NON_MRCH1"]
    dbo_ITEM(["dbo.ITEM"]) --> SP
    dbo_RETAIL_TRANSACTION(["dbo.RETAIL_TRANSACTION"]) --> SP
    dbo_SALE_RTRN_LN_ITEM(["dbo.SALE_RTRN_LN_ITEM"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ITEM |
| dbo.RETAIL_TRANSACTION |
| dbo.SALE_RTRN_LN_ITEM |

## Stored Procedure Code

```sql
/* Report Id = 1090
```

