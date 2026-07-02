# dbo.GetDataSetForExecution

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.GetDataSetForExecution"]
    dbo_CachePolicy(["dbo.CachePolicy"]) --> SP
    dbo_Catalog(["dbo.Catalog"]) --> SP
    dbo_ExecutionCache(["dbo.ExecutionCache"]) --> SP
    dbo_SnapshotData(["dbo.SnapshotData"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.CachePolicy |
| dbo.Catalog |
| dbo.ExecutionCache |
| dbo.SnapshotData |

## Stored Procedure Code

```sql

```

