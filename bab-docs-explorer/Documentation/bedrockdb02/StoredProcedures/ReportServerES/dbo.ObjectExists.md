# dbo.ObjectExists

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.ObjectExists"]
    dbo_ExtendedCatalog(["dbo.ExtendedCatalog"]) --> SP
    dbo_GetUserID(["dbo.GetUserID"]) --> SP
    dbo_SecData(["dbo.SecData"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ExtendedCatalog |
| dbo.GetUserID |
| dbo.SecData |

## Stored Procedure Code

```sql

```

