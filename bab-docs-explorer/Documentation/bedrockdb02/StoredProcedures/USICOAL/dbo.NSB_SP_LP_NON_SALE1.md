# dbo.NSB_SP_LP_NON_SALE1

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.NSB_SP_LP_NON_SALE1"]
    dbo_EMPLOYEE(["dbo.EMPLOYEE"]) --> SP
    dbo_NO_SALE_RSN_CODE(["dbo.NO_SALE_RSN_CODE"]) --> SP
    dbo_NO_SALE_TRN(["dbo.NO_SALE_TRN"]) --> SP
    dbo_OPERATOR(["dbo.OPERATOR"]) --> SP
    dbo_PAIDIO_TRANSACTION(["dbo.PAIDIO_TRANSACTION"]) --> SP
    dbo_RETAIL_TRANSACTION(["dbo.RETAIL_TRANSACTION"]) --> SP
    dbo_RPT_SELECT_OBJECT(["dbo.RPT_SELECT_OBJECT"]) --> SP
    dbo_TENDER_CONTROL_TRN(["dbo.TENDER_CONTROL_TRN"]) --> SP
    dbo_TNDR_CTRL_TRN_TNDR(["dbo.TNDR_CTRL_TRN_TNDR"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.EMPLOYEE |
| dbo.NO_SALE_RSN_CODE |
| dbo.NO_SALE_TRN |
| dbo.OPERATOR |
| dbo.PAIDIO_TRANSACTION |
| dbo.RETAIL_TRANSACTION |
| dbo.RPT_SELECT_OBJECT |
| dbo.TENDER_CONTROL_TRN |
| dbo.TNDR_CTRL_TRN_TNDR |

## Stored Procedure Code

```sql

```

