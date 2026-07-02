# dbo.NSB_SP_LP_VOID_ITEMS

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.NSB_SP_LP_VOID_ITEMS"]
    dbo_DEPARTMENT(["dbo.DEPARTMENT"]) --> SP
    dbo_EMPLOYEE(["dbo.EMPLOYEE"]) --> SP
    dbo_OPERATOR(["dbo.OPERATOR"]) --> SP
    dbo_RETAIL_TRANSACTION(["dbo.RETAIL_TRANSACTION"]) --> SP
    dbo_RPT_SELECT_OBJECT(["dbo.RPT_SELECT_OBJECT"]) --> SP
    dbo_SALE_RTRN_LN_ITEM(["dbo.SALE_RTRN_LN_ITEM"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DEPARTMENT |
| dbo.EMPLOYEE |
| dbo.OPERATOR |
| dbo.RETAIL_TRANSACTION |
| dbo.RPT_SELECT_OBJECT |
| dbo.SALE_RTRN_LN_ITEM |

## Stored Procedure Code

```sql

```

