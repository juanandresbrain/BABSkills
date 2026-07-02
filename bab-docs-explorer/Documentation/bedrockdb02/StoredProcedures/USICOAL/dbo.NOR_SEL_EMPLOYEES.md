# dbo.NOR_SEL_EMPLOYEES

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.NOR_SEL_EMPLOYEES"]
    dbo_EMPLOYEE(["dbo.EMPLOYEE"]) --> SP
    dbo_EMPLOYEE_JOB_TYPE(["dbo.EMPLOYEE_JOB_TYPE"]) --> SP
    dbo_JOB_TYPE(["dbo.JOB_TYPE"]) --> SP
    dbo_OPERATOR(["dbo.OPERATOR"]) --> SP
    dbo_RETAIL_TRANSACTION(["dbo.RETAIL_TRANSACTION"]) --> SP
    dbo_RETAIL_TRN_DOCUMENT(["dbo.RETAIL_TRN_DOCUMENT"]) --> SP
    dbo_SALE_RTRN_LN_ITEM(["dbo.SALE_RTRN_LN_ITEM"]) --> SP
    dbo_SPIFF(["dbo.SPIFF"]) --> SP
    dbo_STORE_EVENT(["dbo.STORE_EVENT"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.EMPLOYEE |
| dbo.EMPLOYEE_JOB_TYPE |
| dbo.JOB_TYPE |
| dbo.OPERATOR |
| dbo.RETAIL_TRANSACTION |
| dbo.RETAIL_TRN_DOCUMENT |
| dbo.SALE_RTRN_LN_ITEM |
| dbo.SPIFF |
| dbo.STORE_EVENT |

## Stored Procedure Code

```sql

```

