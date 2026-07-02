# dbo.is_tax_exclusive_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.is_tax_exclusive_$sp"]
    dbo_job_error_handler__sp(["dbo.job_error_handler_$sp"]) --> SP
    dbo_job_progress_handler__sp(["dbo.job_progress_handler_$sp"]) --> SP
    dbo_return_debug_flag__sp(["dbo.return_debug_flag_$sp"]) --> SP
    dbo_syn_jurisdiction_tax(["dbo.syn_jurisdiction_tax"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.job_error_handler_$sp |
| dbo.job_progress_handler_$sp |
| dbo.return_debug_flag_$sp |
| dbo.syn_jurisdiction_tax |

## Stored Procedure Code

```sql

```

