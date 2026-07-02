# dbo.IsSegmentedChunk

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.IsSegmentedChunk"]
    dbo_ChunkData(["dbo.ChunkData"]) --> SP
    dbo_SegmentedChunk(["dbo.SegmentedChunk"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ChunkData |
| dbo.SegmentedChunk |

## Stored Procedure Code

```sql

```

