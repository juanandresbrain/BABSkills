# dbo.SetSnapshotProcessingFlags

**Database:** ReportServerSA  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.SetSnapshotProcessingFlags"]
    SnapshotData(["SnapshotData"]) --> SP
    dbo_SnapshotData(["dbo.SnapshotData"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| SnapshotData |
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
	UPDATE [ReportServerSATempDB].dbo.SnapshotData
	SET ProcessingFlags = @ProcessingFlags
	WHERE SnapshotDataID = @SnapshotDataID
END
```

