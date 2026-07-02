# dbo.RPT_MRCH_SUM_EXCL_TAX1

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.RPT_MRCH_SUM_EXCL_TAX1"]
    dbo_DEPARTMENT(["dbo.DEPARTMENT"]) --> SP
    dbo_DEPT_GROUP(["dbo.DEPT_GROUP"]) --> SP
    dbo_ITEM(["dbo.ITEM"]) --> SP
    dbo_ITEM_DISCOUNT(["dbo.ITEM_DISCOUNT"]) --> SP
    dbo_ITEM_TAX_AUTH(["dbo.ITEM_TAX_AUTH"]) --> SP
    dbo_PRICE_OVERRIDE(["dbo.PRICE_OVERRIDE"]) --> SP
    dbo_RETAIL_TRANSACTION(["dbo.RETAIL_TRANSACTION"]) --> SP
    dbo_RPT_SELECT_OBJECT(["dbo.RPT_SELECT_OBJECT"]) --> SP
    dbo_SALE_RTRN_LN_ITEM(["dbo.SALE_RTRN_LN_ITEM"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.DEPARTMENT |
| dbo.DEPT_GROUP |
| dbo.ITEM |
| dbo.ITEM_DISCOUNT |
| dbo.ITEM_TAX_AUTH |
| dbo.PRICE_OVERRIDE |
| dbo.RETAIL_TRANSACTION |
| dbo.RPT_SELECT_OBJECT |
| dbo.SALE_RTRN_LN_ITEM |

## Stored Procedure Code

```sql

```

