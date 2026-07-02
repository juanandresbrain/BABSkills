# dbo.RPT_EMPL_PROD_EXCL_TAX3

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.RPT_EMPL_PROD_EXCL_TAX3"]
    dbo_EMPLOYEE(["dbo.EMPLOYEE"]) --> SP
    dbo_ITEM_DISCOUNT(["dbo.ITEM_DISCOUNT"]) --> SP
    dbo_ITEM_TAX_AUTH(["dbo.ITEM_TAX_AUTH"]) --> SP
    dbo_OPERATOR(["dbo.OPERATOR"]) --> SP
    dbo_PRICE_OVERRIDE(["dbo.PRICE_OVERRIDE"]) --> SP
    dbo_RETAIL_TRANSACTION(["dbo.RETAIL_TRANSACTION"]) --> SP
    dbo_RPT_SELECT_OBJECT(["dbo.RPT_SELECT_OBJECT"]) --> SP
    dbo_SALE_RTRN_LN_ITEM(["dbo.SALE_RTRN_LN_ITEM"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.EMPLOYEE |
| dbo.ITEM_DISCOUNT |
| dbo.ITEM_TAX_AUTH |
| dbo.OPERATOR |
| dbo.PRICE_OVERRIDE |
| dbo.RETAIL_TRANSACTION |
| dbo.RPT_SELECT_OBJECT |
| dbo.SALE_RTRN_LN_ITEM |

## Stored Procedure Code

```sql

```

