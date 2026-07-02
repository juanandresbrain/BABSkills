# dbo.UpdateSnapshotReferences

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.UpdateSnapshotReferences"]
    dbo_Catalog(["dbo.Catalog"]) --> SP
    dbo_ExecutionCache(["dbo.ExecutionCache"]) --> SP
    dbo_History(["dbo.History"]) --> SP
    dbo_SnapshotData(["dbo.SnapshotData"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Catalog |
| dbo.ExecutionCache |
| dbo.History |
| dbo.SnapshotData |

## Stored Procedure Code

```sql

```

