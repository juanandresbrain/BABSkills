# dbo.CleanBrokenSnapshots

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.CleanBrokenSnapshots"]
    dbo_ChunkData(["dbo.ChunkData"]) --> SP
    dbo_SnapshotData(["dbo.SnapshotData"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ChunkData |
| dbo.SnapshotData |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[CleanBrokenSnapshots]
@Machine nvarchar(512),
@SnapshotsCleaned int OUTPUT,
@ChunksCleaned int OUTPUT,
@TempSnapshotID uniqueidentifier OUTPUT
AS
    SET DEADLOCK_PRIORITY LOW
    DECLARE @now AS datetime
    SELECT @now = GETDATE()

    CREATE TABLE #tempSnapshot (SnapshotDataID uniqueidentifier)
    INSERT INTO #tempSnapshot SELECT TOP 1 SnapshotDataID
    FROM SnapshotData  WITH (NOLOCK)
    where SnapshotData.PermanentRefcount <= 0
    AND ExpirationDate < @now
    SET @SnapshotsCleaned = @@ROWCOUNT

    DELETE ChunkData FROM ChunkData INNER JOIN #tempSnapshot
    ON ChunkData.SnapshotDataID = #tempSnapshot.SnapshotDataID
    SET @ChunksCleaned = @@ROWCOUNT

    DELETE SnapshotData FROM SnapshotData INNER JOIN #tempSnapshot
    ON SnapshotData.SnapshotDataID = #tempSnapshot.SnapshotDataID

    TRUNCATE TABLE #tempSnapshot

    INSERT INTO #tempSnapshot SELECT TOP 1 SnapshotDataID
    FROM [ReportServerBIRPT02TempDB].dbo.SnapshotData  WITH (NOLOCK)
    where [ReportServerBIRPT02TempDB].dbo.SnapshotData.PermanentRefcount <= 0
    AND [ReportServerBIRPT02TempDB].dbo.SnapshotData.ExpirationDate < @now
    AND [ReportServerBIRPT02TempDB].dbo.SnapshotData.Machine = @Machine
    SET @SnapshotsCleaned = @SnapshotsCleaned + @@ROWCOUNT

    SELECT @TempSnapshotID = (SELECT SnapshotDataID FROM #tempSnapshot)

    DELETE [ReportServerBIRPT02TempDB].dbo.ChunkData FROM [ReportServerBIRPT02TempDB].dbo.ChunkData INNER JOIN #tempSnapshot
    ON [ReportServerBIRPT02TempDB].dbo.ChunkData.SnapshotDataID = #tempSnapshot.SnapshotDataID
    SET @ChunksCleaned = @ChunksCleaned + @@ROWCOUNT

    DELETE [ReportServerBIRPT02TempDB].dbo.SnapshotData FROM [ReportServerBIRPT02TempDB].dbo.SnapshotData INNER JOIN #tempSnapshot
    ON [ReportServerBIRPT02TempDB].dbo.SnapshotData.SnapshotDataID = #tempSnapshot.SnapshotDataID
```

