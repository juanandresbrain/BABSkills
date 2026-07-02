# dbo.GetExecutionOptions

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.GetExecutionOptions"]
    dbo_Catalog(["dbo.Catalog"]) --> SP
    dbo_ReportSchedule(["dbo.ReportSchedule"]) --> SP
    dbo_Schedule(["dbo.Schedule"]) --> SP
    dbo_Users(["dbo.Users"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Catalog |
| dbo.ReportSchedule |
| dbo.Schedule |
| dbo.Users |

## Stored Procedure Code

```sql

```

