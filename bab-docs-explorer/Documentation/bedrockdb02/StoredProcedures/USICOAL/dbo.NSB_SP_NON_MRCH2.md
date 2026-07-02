# dbo.NSB_SP_NON_MRCH2

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.NSB_SP_NON_MRCH2"]
    dbo_EMPLOYEE(["dbo.EMPLOYEE"]) --> SP
    dbo_ITEM(["dbo.ITEM"]) --> SP
    dbo_OPERATOR(["dbo.OPERATOR"]) --> SP
    dbo_RETAIL_TRANSACTION(["dbo.RETAIL_TRANSACTION"]) --> SP
    dbo_SALE_RTRN_LN_ITEM(["dbo.SALE_RTRN_LN_ITEM"]) --> SP
    dbo_SPIFF(["dbo.SPIFF"]) --> SP
    dbo_WORKSTATION(["dbo.WORKSTATION"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.EMPLOYEE |
| dbo.ITEM |
| dbo.OPERATOR |
| dbo.RETAIL_TRANSACTION |
| dbo.SALE_RTRN_LN_ITEM |
| dbo.SPIFF |
| dbo.WORKSTATION |

## Stored Procedure Code

```sql

```

