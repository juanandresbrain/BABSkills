# dbo.NSB_SP_KPI1

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.NSB_SP_KPI1"]
    dbo_ITEM_DISCOUNT(["dbo.ITEM_DISCOUNT"]) --> SP
    dbo_PRICE_OVERRIDE(["dbo.PRICE_OVERRIDE"]) --> SP
    dbo_RETAIL_TRANSACTION(["dbo.RETAIL_TRANSACTION"]) --> SP
    dbo_SALE_RTRN_LN_ITEM(["dbo.SALE_RTRN_LN_ITEM"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ITEM_DISCOUNT |
| dbo.PRICE_OVERRIDE |
| dbo.RETAIL_TRANSACTION |
| dbo.SALE_RTRN_LN_ITEM |

## Stored Procedure Code

```sql

```

