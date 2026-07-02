# dbo.RPT_SALES_PLAN1

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.RPT_SALES_PLAN1"]
    dbo_FISCAL_DAY(["dbo.FISCAL_DAY"]) --> SP
    dbo_RETAIL_TRANSACTION(["dbo.RETAIL_TRANSACTION"]) --> SP
    dbo_SALE_RTRN_LN_ITEM(["dbo.SALE_RTRN_LN_ITEM"]) --> SP
    dbo_STORE_GOAL(["dbo.STORE_GOAL"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.FISCAL_DAY |
| dbo.RETAIL_TRANSACTION |
| dbo.SALE_RTRN_LN_ITEM |
| dbo.STORE_GOAL |

## Stored Procedure Code

```sql

```

