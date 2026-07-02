# dbo.CreateEditSession

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.CreateEditSession"]
    dbo_GetUserID(["dbo.GetUserID"]) --> SP
    dbo_SnapshotData(["dbo.SnapshotData"]) --> SP
    dbo_TempCatalog(["dbo.TempCatalog"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.GetUserID |
| dbo.SnapshotData |
| dbo.TempCatalog |

## Stored Procedure Code

```sql

```

