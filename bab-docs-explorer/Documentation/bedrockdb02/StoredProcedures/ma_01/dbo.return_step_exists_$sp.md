# dbo.return_step_exists_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.return_step_exists_$sp"]
    dbo_job_detail(["dbo.job_detail"]) --> SP
    dbo_job_error_handler__sp(["dbo.job_error_handler_$sp"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.job_detail |
| dbo.job_error_handler_$sp |

## Stored Procedure Code

```sql
create proc [dbo].[return_step_exists_$sp]
```

