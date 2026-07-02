# dbo.CreateNewSnapshotVersion

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.CreateNewSnapshotVersion"]
    dbo_CopyChunks(["dbo.CopyChunks"]) --> SP
    dbo_SnapshotData(["dbo.SnapshotData"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.CopyChunks |
| dbo.SnapshotData |

## Stored Procedure Code

```sql

```

