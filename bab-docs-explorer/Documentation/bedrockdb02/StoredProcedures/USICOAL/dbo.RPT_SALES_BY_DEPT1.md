# dbo.RPT_SALES_BY_DEPT1

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.RPT_SALES_BY_DEPT1"]
    dbo_DEPARTMENT(["dbo.DEPARTMENT"]) --> SP
    dbo_DEPT_GROUP(["dbo.DEPT_GROUP"]) --> SP
    dbo_PRICE_OVERRIDE(["dbo.PRICE_OVERRIDE"]) --> SP
    dbo_RETAIL_TRANSACTION(["dbo.RETAIL_TRANSACTION"]) --> SP
    dbo_SALE_RTRN_LN_ITEM(["dbo.SALE_RTRN_LN_ITEM"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DEPARTMENT |
| dbo.DEPT_GROUP |
| dbo.PRICE_OVERRIDE |
| dbo.RETAIL_TRANSACTION |
| dbo.SALE_RTRN_LN_ITEM |

## Stored Procedure Code

```sql

```

