# dbo.CleanExpiredJobs

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.CleanExpiredJobs"]
    dbo_RunningJobs(["dbo.RunningJobs"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.RunningJobs |

## Stored Procedure Code

```sql

```

