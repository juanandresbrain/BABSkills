# dbo.RPT_WRKST_SALES_BY_VAT_RATE

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.RPT_WRKST_SALES_BY_VAT_RATE"]
    dbo_ITEM_TAX_AUTH(["dbo.ITEM_TAX_AUTH"]) --> SP
    dbo_RETAIL_TRANSACTION(["dbo.RETAIL_TRANSACTION"]) --> SP
    dbo_SALE_RTRN_LN_ITEM(["dbo.SALE_RTRN_LN_ITEM"]) --> SP
    dbo_STORE(["dbo.STORE"]) --> SP
    dbo_TAX_GRP_ZONE_AUTH(["dbo.TAX_GRP_ZONE_AUTH"]) --> SP
    dbo_TAX_RULE(["dbo.TAX_RULE"]) --> SP
    dbo_VALUE_ADDED_TAX(["dbo.VALUE_ADDED_TAX"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ITEM_TAX_AUTH |
| dbo.RETAIL_TRANSACTION |
| dbo.SALE_RTRN_LN_ITEM |
| dbo.STORE |
| dbo.TAX_GRP_ZONE_AUTH |
| dbo.TAX_RULE |
| dbo.VALUE_ADDED_TAX |

## Stored Procedure Code

```sql

```

