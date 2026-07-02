# dbo.RPT_TOP_SELL_BY_QTY1

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.RPT_TOP_SELL_BY_QTY1"]
    dbo_COLOR(["dbo.COLOR"]) --> SP
    dbo_DEPARTMENT(["dbo.DEPARTMENT"]) --> SP
    dbo_DEPT_GROUP(["dbo.DEPT_GROUP"]) --> SP
    dbo_RETAIL_TRANSACTION(["dbo.RETAIL_TRANSACTION"]) --> SP
    dbo_SALE_RTRN_LN_ITEM(["dbo.SALE_RTRN_LN_ITEM"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.COLOR |
| dbo.DEPARTMENT |
| dbo.DEPT_GROUP |
| dbo.RETAIL_TRANSACTION |
| dbo.SALE_RTRN_LN_ITEM |

## Stored Procedure Code

```sql

```

