# dbo.DeleteHistoryRecord

**Database:** ReportServerSA  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DeleteHistoryRecord"]
    History(["History"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| History |

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

