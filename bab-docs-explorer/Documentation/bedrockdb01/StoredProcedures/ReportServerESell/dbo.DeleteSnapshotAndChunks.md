# dbo.DeleteSnapshotAndChunks

**Database:** ReportServerESell  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DeleteSnapshotAndChunks"]
    ChunkData(["ChunkData"]) --> SP
    dbo_ChunkData(["dbo.ChunkData"]) --> SP
    SegmentedChunk(["SegmentedChunk"]) --> SP
    dbo_SegmentedChunk(["dbo.SegmentedChunk"]) --> SP
    SnapshotData(["SnapshotData"]) --> SP
    dbo_SnapshotData(["dbo.SnapshotData"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| ChunkData |
| dbo.ChunkData |
| SegmentedChunk |
| dbo.SegmentedChunk |
| SnapshotData |
| dbo.SnapshotData |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[DeleteSnapshotAndChunks]
@SnapshotID uniqueidentifier,
@IsPermanentSnapshot bit
AS

-- Delete from Snapshot, ChunkData and SegmentedChunk table.
-- Shared segments are not deleted.
-- TODO: currently this is being called from a bunch of places that handles exceptions.
-- We should try to delete the segments in some of all of those cases as well.
IF @IsPermanentSnapshot != 0 BEGIN

    DELETE ChunkData
    WHERE ChunkData.SnapshotDataID = @SnapshotID
    
    DELETE SegmentedChunk
    WHERE SegmentedChunk.SnapshotDataId = @SnapshotID
    
    DELETE SnapshotData
    WHERE SnapshotData.SnapshotDataID = @SnapshotID
   
END ELSE BEGIN

    DELETE [ReportServerESellTempDB].dbo.ChunkData
    WHERE SnapshotDataID = @SnapshotID
       
    DELETE [ReportServerESellTempDB].dbo.SegmentedChunk
    WHERE SnapshotDataId = @SnapshotID

    DELETE [ReportServerESellTempDB].dbo.SnapshotData
    WHERE SnapshotDataID = @SnapshotID

END
```

