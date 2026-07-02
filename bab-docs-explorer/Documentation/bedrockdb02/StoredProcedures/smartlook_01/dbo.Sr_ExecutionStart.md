# dbo.Sr_ExecutionStart

**Database:** smartlook_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Sr_ExecutionStart"]
    dbo_Sr_History(["dbo.Sr_History"]) --> SP
    dbo_Sr_Job(["dbo.Sr_Job"]) --> SP
    dbo_Sr_Server(["dbo.Sr_Server"]) --> SP
    dbo_Sv_GetNextID(["dbo.Sv_GetNextID"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Sr_History |
| dbo.Sr_Job |
| dbo.Sr_Server |
| dbo.Sv_GetNextID |

## Stored Procedure Code

```sql

```

