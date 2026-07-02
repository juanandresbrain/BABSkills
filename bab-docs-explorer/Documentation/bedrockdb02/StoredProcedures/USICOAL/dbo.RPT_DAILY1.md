# dbo.RPT_DAILY1

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.RPT_DAILY1"]
    dbo_DEPARTMENT(["dbo.DEPARTMENT"]) --> SP
    dbo_DOC_TRN_TYPE(["dbo.DOC_TRN_TYPE"]) --> SP
    dbo_ITEM_DISCOUNT(["dbo.ITEM_DISCOUNT"]) --> SP
    dbo_ITEM_TAX_AUTH(["dbo.ITEM_TAX_AUTH"]) --> SP
    dbo_PRICE_OVERRIDE(["dbo.PRICE_OVERRIDE"]) --> SP
    dbo_RETAIL_TRANSACTION(["dbo.RETAIL_TRANSACTION"]) --> SP
    dbo_RETAIL_TRN_DOCUMENT(["dbo.RETAIL_TRN_DOCUMENT"]) --> SP
    dbo_SALE_RTRN_LN_ITEM(["dbo.SALE_RTRN_LN_ITEM"]) --> SP
    dbo_TENDER_LINE_ITEM(["dbo.TENDER_LINE_ITEM"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DEPARTMENT |
| dbo.DOC_TRN_TYPE |
| dbo.ITEM_DISCOUNT |
| dbo.ITEM_TAX_AUTH |
| dbo.PRICE_OVERRIDE |
| dbo.RETAIL_TRANSACTION |
| dbo.RETAIL_TRN_DOCUMENT |
| dbo.SALE_RTRN_LN_ITEM |
| dbo.TENDER_LINE_ITEM |

## Stored Procedure Code

```sql

```

