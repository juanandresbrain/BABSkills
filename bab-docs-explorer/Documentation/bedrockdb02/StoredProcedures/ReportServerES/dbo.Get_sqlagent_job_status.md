# dbo.Get_sqlagent_job_status

**Database:** ReportServerES  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Get_sqlagent_job_status"]
    dbo_sp_verify_job_identifiers(["dbo.sp_verify_job_identifiers"]) --> SP
    dbo_sysjobs(["dbo.sysjobs"]) --> SP
    dbo_xp_sqlagent_enum_jobs(["dbo.xp_sqlagent_enum_jobs"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sp_verify_job_identifiers |
| dbo.sysjobs |
| dbo.xp_sqlagent_enum_jobs |

## Stored Procedure Code

```sql

```

