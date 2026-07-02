# dbo.RPT_STORE_DAILY_DOCS

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.RPT_STORE_DAILY_DOCS"]
    dbo_DOC_TRN_TYPE(["dbo.DOC_TRN_TYPE"]) --> SP
    dbo_RETAIL_TRANSACTION(["dbo.RETAIL_TRANSACTION"]) --> SP
    dbo_RETAIL_TRN_DOCUMENT(["dbo.RETAIL_TRN_DOCUMENT"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DOC_TRN_TYPE |
| dbo.RETAIL_TRANSACTION |
| dbo.RETAIL_TRN_DOCUMENT |

## Stored Procedure Code

```sql

```

