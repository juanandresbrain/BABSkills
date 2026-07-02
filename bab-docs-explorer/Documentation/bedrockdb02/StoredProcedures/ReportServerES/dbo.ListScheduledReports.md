# dbo.ListScheduledReports

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.ListScheduledReports"]
    dbo_Catalog(["dbo.Catalog"]) --> SP
    dbo_ReportSchedule(["dbo.ReportSchedule"]) --> SP
    dbo_Schedule(["dbo.Schedule"]) --> SP
    dbo_SecData(["dbo.SecData"]) --> SP
    dbo_Subscriptions(["dbo.Subscriptions"]) --> SP
    dbo_Users(["dbo.Users"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Catalog |
| dbo.ReportSchedule |
| dbo.Schedule |
| dbo.SecData |
| dbo.Subscriptions |
| dbo.Users |

## Stored Procedure Code

```sql

```

