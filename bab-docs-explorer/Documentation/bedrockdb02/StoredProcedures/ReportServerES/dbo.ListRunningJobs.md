# dbo.ListRunningJobs

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.ListRunningJobs"]
    dbo_RunningJobs(["dbo.RunningJobs"]) --> SP
    dbo_Users(["dbo.Users"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.RunningJobs |
| dbo.Users |

## Stored Procedure Code

```sql

```

