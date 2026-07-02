# dbo.RPL_ADD_DISTR_SCHED

**Database:** USICOAL  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.RPL_ADD_DISTR_SCHED"]
    dbo_sp_add_jobschedule(["dbo.sp_add_jobschedule"]) --> SP
    dbo_syscategories(["dbo.syscategories"]) --> SP
    dbo_sysjobs(["dbo.sysjobs"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sp_add_jobschedule |
| dbo.syscategories |
| dbo.sysjobs |

## Stored Procedure Code

```sql

```

