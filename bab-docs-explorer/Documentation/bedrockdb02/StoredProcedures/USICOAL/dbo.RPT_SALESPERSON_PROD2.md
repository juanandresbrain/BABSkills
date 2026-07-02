# dbo.RPT_SALESPERSON_PROD2

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.RPT_SALESPERSON_PROD2"]
    dbo_EMPLOYEE(["dbo.EMPLOYEE"]) --> SP
    dbo_ITEM_DISCOUNT(["dbo.ITEM_DISCOUNT"]) --> SP
    dbo_OPERATOR(["dbo.OPERATOR"]) --> SP
    dbo_PRICE_OVERRIDE(["dbo.PRICE_OVERRIDE"]) --> SP
    dbo_RETAIL_TRANSACTION(["dbo.RETAIL_TRANSACTION"]) --> SP
    dbo_SALE_RTRN_LN_ITEM(["dbo.SALE_RTRN_LN_ITEM"]) --> SP
    dbo_SPIFF(["dbo.SPIFF"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.EMPLOYEE |
| dbo.ITEM_DISCOUNT |
| dbo.OPERATOR |
| dbo.PRICE_OVERRIDE |
| dbo.RETAIL_TRANSACTION |
| dbo.SALE_RTRN_LN_ITEM |
| dbo.SPIFF |

## Stored Procedure Code

```sql

```

