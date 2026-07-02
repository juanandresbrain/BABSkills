# dbo.RemoveSegmentedMapping

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.RemoveSegmentedMapping"]
    dbo_ChunkSegmentMapping(["dbo.ChunkSegmentMapping"]) --> SP
    dbo_SegmentedChunk(["dbo.SegmentedChunk"]) --> SP
    dbo_SnapshotData(["dbo.SnapshotData"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ChunkSegmentMapping |
| dbo.SegmentedChunk |
| dbo.SnapshotData |

## Stored Procedure Code

```sql

```

