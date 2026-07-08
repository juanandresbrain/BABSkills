# dbo.TempChunkExists

**Database:** ReportServerESell  
**Server:** bedrockdb01  

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
	SELECT COUNT(1) FROM [ReportServerESellTempDB].dbo.SegmentedChunk
	WHERE ChunkId = @ChunkId
END
```

