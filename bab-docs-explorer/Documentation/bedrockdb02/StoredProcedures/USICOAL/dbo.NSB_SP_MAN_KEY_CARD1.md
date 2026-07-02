# dbo.NSB_SP_MAN_KEY_CARD1

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.NSB_SP_MAN_KEY_CARD1"]
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
/* Report Id = 1060*/
```

