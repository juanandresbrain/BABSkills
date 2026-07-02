# dbo.ListHistory

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.ListHistory"]
    dbo_ChunkData(["dbo.ChunkData"]) --> SP
    dbo_ChunkSegmentMapping(["dbo.ChunkSegmentMapping"]) --> SP
    dbo_History(["dbo.History"]) --> SP
    dbo_Segment(["dbo.Segment"]) --> SP
    dbo_SegmentedChunk(["dbo.SegmentedChunk"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ChunkData |
| dbo.ChunkSegmentMapping |
| dbo.History |
| dbo.Segment |
| dbo.SegmentedChunk |

## Stored Procedure Code

```sql

```

