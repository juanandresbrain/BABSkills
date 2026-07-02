# dbo.SetSnapshotChunksVersion

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.SetSnapshotChunksVersion"]
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
CREATE PROCEDURE [dbo].[SetSnapshotChunksVersion]
@SnapshotDataID as uniqueidentifier,
@IsPermanentSnapshot as bit,
@Version as smallint
AS
declare @affectedRows int
set @affectedRows = 0
if @IsPermanentSnapshot = 1
BEGIN
   if @Version > 0
   BEGIN
      UPDATE ChunkData
      SET Version = @Version
      WHERE SnapshotDataID = @SnapshotDataID

      SELECT @affectedRows = @affectedRows + @@rowcount

      UPDATE SegmentedChunk
      SET Version = @Version
      WHERE SnapshotDataId = @SnapshotDataID

      SELECT @affectedRows = @affectedRows + @@rowcount
   END ELSE BEGIN
      UPDATE ChunkData
      SET Version = Version
      WHERE SnapshotDataID = @SnapshotDataID

      SELECT @affectedRows = @affectedRows + @@rowcount

      UPDATE SegmentedChunk
      SET Version = Version
      WHERE SnapshotDataId = @SnapshotDataID

      SELECT @affectedRows = @affectedRows + @@rowcount
   END
END ELSE BEGIN
   if @Version > 0
   BEGIN
      UPDATE [ReportServerBIRPT02TempDB].dbo.ChunkData
      SET Version = @Version
      WHERE SnapshotDataID = @SnapshotDataID

      SELECT @affectedRows = @affectedRows + @@rowcount

      UPDATE [ReportServerBIRPT02TempDB].dbo.SegmentedChunk
      SET Version = @Version
      WHERE SnapshotDataId = @SnapshotDataID

      SELECT @affectedRows = @affectedRows + @@rowcount
   END ELSE BEGIN
      UPDATE [ReportServerBIRPT02TempDB].dbo.ChunkData
      SET Version = Version
      WHERE SnapshotDataID = @SnapshotDataID

      SELECT @affectedRows = @affectedRows + @@rowcount

      UPDATE [ReportServerBIRPT02TempDB].dbo.SegmentedChunk
      SET Version = Version
      WHERE SnapshotDataId = @SnapshotDataID

      SELECT @affectedRows = @affectedRows + @@rowcount
   END
END
SELECT @affectedRows
```

