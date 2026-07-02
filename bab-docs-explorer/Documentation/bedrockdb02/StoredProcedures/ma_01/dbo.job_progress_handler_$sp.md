# dbo.job_progress_handler_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.job_progress_handler_$sp"]
    dbo_job_debug(["dbo.job_debug"]) --> SP
    dbo_job_error_handler__sp(["dbo.job_error_handler_$sp"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.job_debug |
| dbo.job_error_handler_$sp |

## Stored Procedure Code

```sql

```

