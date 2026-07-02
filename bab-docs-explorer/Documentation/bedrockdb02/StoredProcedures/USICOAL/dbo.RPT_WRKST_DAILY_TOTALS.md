# dbo.RPT_WRKST_DAILY_TOTALS

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.RPT_WRKST_DAILY_TOTALS"]
    dbo_PMT_ACCT_LN_ITEM(["dbo.PMT_ACCT_LN_ITEM"]) --> SP
    dbo_RETAIL_TRANSACTION(["dbo.RETAIL_TRANSACTION"]) --> SP
    dbo_SALE_RTRN_LN_ITEM(["dbo.SALE_RTRN_LN_ITEM"]) --> SP
    dbo_WORKSTATION(["dbo.WORKSTATION"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.PMT_ACCT_LN_ITEM |
| dbo.RETAIL_TRANSACTION |
| dbo.SALE_RTRN_LN_ITEM |
| dbo.WORKSTATION |

## Stored Procedure Code

```sql

```

