# dbo.AddHistoryRecord

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.AddHistoryRecord"]
    dbo_History(["dbo.History"]) --> SP
    dbo_SnapshotData(["dbo.SnapshotData"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.History |
| dbo.SnapshotData |

## Stored Procedure Code

```sql

```

