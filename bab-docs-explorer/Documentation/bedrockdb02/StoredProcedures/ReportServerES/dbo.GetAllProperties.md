# dbo.GetAllProperties

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.GetAllProperties"]
    dbo_ExtendedCatalog(["dbo.ExtendedCatalog"]) --> SP
    dbo_GetUserID(["dbo.GetUserID"]) --> SP
    dbo_SecData(["dbo.SecData"]) --> SP
    dbo_Users(["dbo.Users"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ExtendedCatalog |
| dbo.GetUserID |
| dbo.SecData |
| dbo.Users |

## Stored Procedure Code

```sql

```

