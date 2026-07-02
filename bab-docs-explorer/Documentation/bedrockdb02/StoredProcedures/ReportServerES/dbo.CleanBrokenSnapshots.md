# dbo.CleanBrokenSnapshots

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.CleanBrokenSnapshots"]
    dbo_ChunkData(["dbo.ChunkData"]) --> SP
    dbo_SnapshotData(["dbo.SnapshotData"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ChunkData |
| dbo.SnapshotData |

## Stored Procedure Code

```sql

```

