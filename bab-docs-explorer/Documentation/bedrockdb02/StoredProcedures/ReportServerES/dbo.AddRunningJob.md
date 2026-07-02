# dbo.AddRunningJob

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.AddRunningJob"]
    dbo_GetUserID(["dbo.GetUserID"]) --> SP
    dbo_RunningJobs(["dbo.RunningJobs"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.GetUserID |
| dbo.RunningJobs |

## Stored Procedure Code

```sql

```

