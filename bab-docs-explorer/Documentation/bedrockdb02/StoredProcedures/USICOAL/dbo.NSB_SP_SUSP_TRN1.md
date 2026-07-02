# dbo.NSB_SP_SUSP_TRN1

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.NSB_SP_SUSP_TRN1"]
    dbo_EMPLOYEE(["dbo.EMPLOYEE"]) --> SP
    dbo_OPERATOR(["dbo.OPERATOR"]) --> SP
    dbo_RETAIL_TRANSACTION(["dbo.RETAIL_TRANSACTION"]) --> SP
    dbo_RPT_SELECT_OBJECT(["dbo.RPT_SELECT_OBJECT"]) --> SP
    dbo_SUSP_TRN_RSN_CODE(["dbo.SUSP_TRN_RSN_CODE"]) --> SP
    dbo_SUSPENDED_TRN(["dbo.SUSPENDED_TRN"]) --> SP
    dbo_WORKSTATION(["dbo.WORKSTATION"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.EMPLOYEE |
| dbo.OPERATOR |
| dbo.RETAIL_TRANSACTION |
| dbo.RPT_SELECT_OBJECT |
| dbo.SUSP_TRN_RSN_CODE |
| dbo.SUSPENDED_TRN |
| dbo.WORKSTATION |

## Stored Procedure Code

```sql
/*Report Id = 1140
```

