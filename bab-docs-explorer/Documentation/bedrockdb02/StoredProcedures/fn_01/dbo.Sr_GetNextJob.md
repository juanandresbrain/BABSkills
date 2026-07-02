# dbo.Sr_GetNextJob

**Database:** fn_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Sr_GetNextJob"]
    dbo_Sr_Job(["dbo.Sr_Job"]) --> SP
    dbo_Sr_Machine(["dbo.Sr_Machine"]) --> SP
    dbo_Sr_Server(["dbo.Sr_Server"]) --> SP
    dbo_Work_Job(["dbo.Work_Job"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Sr_Job |
| dbo.Sr_Machine |
| dbo.Sr_Server |
| dbo.Work_Job |

## Stored Procedure Code

```sql

```

