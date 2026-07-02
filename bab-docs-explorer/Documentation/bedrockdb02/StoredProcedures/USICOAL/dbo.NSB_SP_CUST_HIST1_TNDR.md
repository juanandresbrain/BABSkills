# dbo.NSB_SP_CUST_HIST1_TNDR

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.NSB_SP_CUST_HIST1_TNDR"]
    dbo_RETAIL_TRANSACTION(["dbo.RETAIL_TRANSACTION"]) --> SP
    dbo_TENDER(["dbo.TENDER"]) --> SP
    dbo_TENDER_LINE_ITEM(["dbo.TENDER_LINE_ITEM"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.RETAIL_TRANSACTION |
| dbo.TENDER |
| dbo.TENDER_LINE_ITEM |

## Stored Procedure Code

```sql
/* Report Id = 1030*/
```

