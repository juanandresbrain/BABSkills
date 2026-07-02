# MerchandisingPlanning.spTXTDataLoad_AsyncExecute

**Database:** TXTStaging  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["MerchandisingPlanning.spTXTDataLoad_AsyncExecute"]
    dbo_sp_add_job(["dbo.sp_add_job"]) --> SP
    dbo_sp_add_jobserver(["dbo.sp_add_jobserver"]) --> SP
    dbo_sp_add_jobstep(["dbo.sp_add_jobstep"]) --> SP
    dbo_sp_start_job(["dbo.sp_start_job"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sp_add_job |
| dbo.sp_add_jobserver |
| dbo.sp_add_jobstep |
| dbo.sp_start_job |

## Stored Procedure Code

```sql

```

