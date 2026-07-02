# dbo.OpenSegmentedChunk

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.OpenSegmentedChunk"]
    dbo_ChunkSegmentMapping(["dbo.ChunkSegmentMapping"]) --> SP
    dbo_SegmentedChunk(["dbo.SegmentedChunk"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ChunkSegmentMapping |
| dbo.SegmentedChunk |

## Stored Procedure Code

```sql

```

