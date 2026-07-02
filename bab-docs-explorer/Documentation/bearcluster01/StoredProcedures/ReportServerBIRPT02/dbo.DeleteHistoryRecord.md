# dbo.DeleteHistoryRecord

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DeleteHistoryRecord"]
    dbo_History(["dbo.History"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.History |

## Stored Procedure Code

```sql
-- delete one historical snapshot
CREATE PROCEDURE [dbo].[DeleteHistoryRecord]
@ReportID uniqueidentifier,
@SnapshotDate DateTime
AS
SET NOCOUNT OFF
DELETE
FROM History
WHERE ReportID = @ReportID AND SnapshotDate = @SnapshotDate
```

