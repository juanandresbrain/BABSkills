# dbo.CreateTimeBasedSubscriptionSchedule

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.CreateTimeBasedSubscriptionSchedule"]
    dbo_AddReportSchedule(["dbo.AddReportSchedule"]) --> SP
    dbo_Catalog(["dbo.Catalog"]) --> SP
    dbo_CreateTask(["dbo.CreateTask"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.AddReportSchedule |
| dbo.Catalog |
| dbo.CreateTask |

## Stored Procedure Code

```sql

```

