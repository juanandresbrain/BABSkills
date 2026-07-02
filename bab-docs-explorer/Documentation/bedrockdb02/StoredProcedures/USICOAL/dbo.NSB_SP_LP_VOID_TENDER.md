# dbo.NSB_SP_LP_VOID_TENDER

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.NSB_SP_LP_VOID_TENDER"]
    dbo_EMPLOYEE(["dbo.EMPLOYEE"]) --> SP
    dbo_OPERATOR(["dbo.OPERATOR"]) --> SP
    dbo_RETAIL_TRANSACTION(["dbo.RETAIL_TRANSACTION"]) --> SP
    dbo_RPT_SELECT_OBJECT(["dbo.RPT_SELECT_OBJECT"]) --> SP
    dbo_TENDER(["dbo.TENDER"]) --> SP
    dbo_TENDER_LINE_ITEM(["dbo.TENDER_LINE_ITEM"]) --> SP
    dbo_WORKSTATION(["dbo.WORKSTATION"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.EMPLOYEE |
| dbo.OPERATOR |
| dbo.RETAIL_TRANSACTION |
| dbo.RPT_SELECT_OBJECT |
| dbo.TENDER |
| dbo.TENDER_LINE_ITEM |
| dbo.WORKSTATION |

## Stored Procedure Code

```sql

```

