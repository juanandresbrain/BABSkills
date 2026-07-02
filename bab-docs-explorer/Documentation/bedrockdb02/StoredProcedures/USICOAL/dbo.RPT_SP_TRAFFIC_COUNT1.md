# dbo.RPT_SP_TRAFFIC_COUNT1

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.RPT_SP_TRAFFIC_COUNT1"]
    dbo_RETAIL_TRANSACTION(["dbo.RETAIL_TRANSACTION"]) --> SP
    dbo_SALE_RTRN_LN_ITEM(["dbo.SALE_RTRN_LN_ITEM"]) --> SP
    dbo_TRAFFIC_COUNT(["dbo.TRAFFIC_COUNT"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.RETAIL_TRANSACTION |
| dbo.SALE_RTRN_LN_ITEM |
| dbo.TRAFFIC_COUNT |

## Stored Procedure Code

```sql

```

