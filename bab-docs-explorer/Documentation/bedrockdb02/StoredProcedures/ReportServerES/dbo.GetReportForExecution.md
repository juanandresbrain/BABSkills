# dbo.GetReportForExecution

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.GetReportForExecution"]
    dbo_CachePolicy(["dbo.CachePolicy"]) --> SP
    dbo_Catalog(["dbo.Catalog"]) --> SP
    dbo_ExecutionCache(["dbo.ExecutionCache"]) --> SP
    dbo_ExtendedCatalog(["dbo.ExtendedCatalog"]) --> SP
    dbo_GetUserID(["dbo.GetUserID"]) --> SP
    dbo_ReportSchedule(["dbo.ReportSchedule"]) --> SP
    dbo_Schedule(["dbo.Schedule"]) --> SP
    dbo_SecData(["dbo.SecData"]) --> SP
    dbo_SnapshotData(["dbo.SnapshotData"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.CachePolicy |
| dbo.Catalog |
| dbo.ExecutionCache |
| dbo.ExtendedCatalog |
| dbo.GetUserID |
| dbo.ReportSchedule |
| dbo.Schedule |
| dbo.SecData |
| dbo.SnapshotData |

## Stored Procedure Code

```sql

```

