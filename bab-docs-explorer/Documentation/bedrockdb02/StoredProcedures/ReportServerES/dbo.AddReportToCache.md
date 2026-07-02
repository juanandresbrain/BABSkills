# dbo.AddReportToCache

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.AddReportToCache"]
    dbo_CachePolicy(["dbo.CachePolicy"]) --> SP
    dbo_EnforceCacheLimits(["dbo.EnforceCacheLimits"]) --> SP
    dbo_ExecutionCache(["dbo.ExecutionCache"]) --> SP
    dbo_ReportSchedule(["dbo.ReportSchedule"]) --> SP
    dbo_Schedule(["dbo.Schedule"]) --> SP
    dbo_SnapshotData(["dbo.SnapshotData"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.CachePolicy |
| dbo.EnforceCacheLimits |
| dbo.ExecutionCache |
| dbo.ReportSchedule |
| dbo.Schedule |
| dbo.SnapshotData |

## Stored Procedure Code

```sql

```

