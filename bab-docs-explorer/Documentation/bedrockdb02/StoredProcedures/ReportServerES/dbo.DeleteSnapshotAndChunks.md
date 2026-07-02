# dbo.DeleteSnapshotAndChunks

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DeleteSnapshotAndChunks"]
    dbo_ChunkData(["dbo.ChunkData"]) --> SP
    dbo_SegmentedChunk(["dbo.SegmentedChunk"]) --> SP
    dbo_SnapshotData(["dbo.SnapshotData"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ChunkData |
| dbo.SegmentedChunk |
| dbo.SnapshotData |

## Stored Procedure Code

```sql

```

