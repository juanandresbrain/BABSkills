# dbo.DeleteHistoryRecordByHistoryId

**Database:** ReportServerBIRPT02  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DeleteHistoryRecordByHistoryId"]
    dbo_History(["dbo.History"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.History |

## Stored Procedure Code

```sql
-- delete one historical snapshot by history id
CREATE PROCEDURE [dbo].[DeleteHistoryRecordByHistoryId]
@ReportID uniqueidentifier,
@HistoryId uniqueidentifier
AS
SET NOCOUNT OFF
DELETE
FROM History
WHERE ReportID = @ReportID AND HistoryId = @HistoryId
```

