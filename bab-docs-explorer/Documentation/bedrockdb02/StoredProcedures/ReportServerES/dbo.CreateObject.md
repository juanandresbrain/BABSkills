# dbo.CreateObject

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.CreateObject"]
    dbo_Catalog(["dbo.Catalog"]) --> SP
    dbo_GetUserID(["dbo.GetUserID"]) --> SP
    dbo_SnapshotData(["dbo.SnapshotData"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Catalog |
| dbo.GetUserID |
| dbo.SnapshotData |

## Stored Procedure Code

```sql

```

