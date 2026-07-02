# dbo.TempChunkExists

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.TempChunkExists"]
    dbo_SegmentedChunk(["dbo.SegmentedChunk"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.SegmentedChunk |

## Stored Procedure Code

```sql
CREATE PROC [dbo].[TempChunkExists]
    @ChunkId uniqueidentifier
AS
BEGIN
    SELECT COUNT(1) FROM [ReportServerBIRPT02TempDB].dbo.SegmentedChunk
    WHERE ChunkId = @ChunkId
END
```

