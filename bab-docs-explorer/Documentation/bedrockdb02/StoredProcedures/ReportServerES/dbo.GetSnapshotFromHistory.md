# dbo.GetSnapshotFromHistory

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.GetSnapshotFromHistory"]
    dbo_Catalog(["dbo.Catalog"]) --> SP
    dbo_History(["dbo.History"]) --> SP
    dbo_SecData(["dbo.SecData"]) --> SP
    dbo_SnapshotData(["dbo.SnapshotData"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Catalog |
| dbo.History |
| dbo.SecData |
| dbo.SnapshotData |

## Stored Procedure Code

```sql

```

