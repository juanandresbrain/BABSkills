# dbo.CreateTask

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.CreateTask"]
    dbo_GetUserID(["dbo.GetUserID"]) --> SP
    dbo_Schedule(["dbo.Schedule"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.GetUserID |
| dbo.Schedule |

## Stored Procedure Code

```sql

```

