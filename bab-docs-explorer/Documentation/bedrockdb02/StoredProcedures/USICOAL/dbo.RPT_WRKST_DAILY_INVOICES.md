# dbo.RPT_WRKST_DAILY_INVOICES

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.RPT_WRKST_DAILY_INVOICES"]
    dbo_DOC_TRN_TYPE(["dbo.DOC_TRN_TYPE"]) --> SP
    dbo_PMT_ACCT_LN_ITEM(["dbo.PMT_ACCT_LN_ITEM"]) --> SP
    dbo_RETAIL_TRANSACTION(["dbo.RETAIL_TRANSACTION"]) --> SP
    dbo_RETAIL_TRN_DOCUMENT(["dbo.RETAIL_TRN_DOCUMENT"]) --> SP
    dbo_SALE_RTRN_LN_ITEM(["dbo.SALE_RTRN_LN_ITEM"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DOC_TRN_TYPE |
| dbo.PMT_ACCT_LN_ITEM |
| dbo.RETAIL_TRANSACTION |
| dbo.RETAIL_TRN_DOCUMENT |
| dbo.SALE_RTRN_LN_ITEM |

## Stored Procedure Code

```sql

```

