# dbo.FindObjectsNonRecursive

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.FindObjectsNonRecursive"]
    dbo_Catalog(["dbo.Catalog"]) --> SP
    dbo_SecData(["dbo.SecData"]) --> SP
    dbo_Users(["dbo.Users"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Catalog |
| dbo.SecData |
| dbo.Users |

## Stored Procedure Code

```sql

```

