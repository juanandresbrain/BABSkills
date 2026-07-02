# dbo.SetSnapshotProcessingFlags

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.SetSnapshotProcessingFlags"]
    dbo_SnapshotData(["dbo.SnapshotData"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.SnapshotData |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[SetSnapshotProcessingFlags]
@SnapshotDataID as uniqueidentifier,
@IsPermanentSnapshot as bit,
@ProcessingFlags int
AS

if @IsPermanentSnapshot = 1
BEGIN
    UPDATE SnapshotData
    SET ProcessingFlags = @ProcessingFlags
    WHERE SnapshotDataID = @SnapshotDataID
END ELSE BEGIN
    UPDATE [ReportServerBIRPT02TempDB].dbo.SnapshotData
    SET ProcessingFlags = @ProcessingFlags
    WHERE SnapshotDataID = @SnapshotDataID
END
```

