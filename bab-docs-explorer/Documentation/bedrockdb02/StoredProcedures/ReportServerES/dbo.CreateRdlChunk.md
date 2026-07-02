# dbo.CreateRdlChunk

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.CreateRdlChunk"]
    dbo_Catalog(["dbo.Catalog"]) --> SP
    dbo_CreateChunkSegment(["dbo.CreateChunkSegment"]) --> SP
    dbo_CreateSegmentedChunk(["dbo.CreateSegmentedChunk"]) --> SP
    dbo_SegmentedChunk(["dbo.SegmentedChunk"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Catalog |
| dbo.CreateChunkSegment |
| dbo.CreateSegmentedChunk |
| dbo.SegmentedChunk |

## Stored Procedure Code

```sql

```

