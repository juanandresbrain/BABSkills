# dbo.NSB_SP_VOID_TRN2

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.NSB_SP_VOID_TRN2"]
    dbo_EMPLOYEE(["dbo.EMPLOYEE"]) --> SP
    dbo_OPERATOR(["dbo.OPERATOR"]) --> SP
    dbo_RETAIL_TRANSACTION(["dbo.RETAIL_TRANSACTION"]) --> SP
    dbo_RPT_SELECT_OBJECT(["dbo.RPT_SELECT_OBJECT"]) --> SP
    dbo_VOID_TRANSACTION(["dbo.VOID_TRANSACTION"]) --> SP
    dbo_WORKSTATION(["dbo.WORKSTATION"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.EMPLOYEE |
| dbo.OPERATOR |
| dbo.RETAIL_TRANSACTION |
| dbo.RPT_SELECT_OBJECT |
| dbo.VOID_TRANSACTION |
| dbo.WORKSTATION |

## Stored Procedure Code

```sql
/*Report Id = 1161*/
```

