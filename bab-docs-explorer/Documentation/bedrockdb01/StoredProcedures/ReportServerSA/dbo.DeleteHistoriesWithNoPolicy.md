# dbo.DeleteHistoriesWithNoPolicy

**Database:** ReportServerSA  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.DeleteHistoriesWithNoPolicy"]
    Catalog(["Catalog"]) --> SP
    History(["History"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Catalog |
| History |

## Stored Procedure Code

```sql
-- delete all snapshots for all reports that inherit system History policy
CREATE PROCEDURE [dbo].[DeleteHistoriesWithNoPolicy]
AS
SET NOCOUNT OFF
DELETE
FROM History
WHERE HistoryID in
   (SELECT HistoryID
    FROM History JOIN Catalog on ItemID = ReportID
    WHERE SnapshotLimit is null
   )
```

