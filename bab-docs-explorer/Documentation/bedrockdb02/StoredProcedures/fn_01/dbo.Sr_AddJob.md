# dbo.Sr_AddJob

**Database:** fn_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Sr_AddJob"]
    dbo_Sr_Job(["dbo.Sr_Job"]) --> SP
    dbo_Sv_GetNextID(["dbo.Sv_GetNextID"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Sr_Job |
| dbo.Sv_GetNextID |

## Stored Procedure Code

```sql

```

