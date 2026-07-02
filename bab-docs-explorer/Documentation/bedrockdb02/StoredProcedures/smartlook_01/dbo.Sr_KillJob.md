# dbo.Sr_KillJob

**Database:** smartlook_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Sr_KillJob"]
    dbo_Sr_History(["dbo.Sr_History"]) --> SP
    dbo_Sr_Job(["dbo.Sr_Job"]) --> SP
    dbo_Sr_Server(["dbo.Sr_Server"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Sr_History |
| dbo.Sr_Job |
| dbo.Sr_Server |

## Stored Procedure Code

```sql

```

