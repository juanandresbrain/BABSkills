# dbo.cleanup_wrk_ib_cost_factor_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.cleanup_wrk_ib_cost_factor_$sp"]
    dbo_job_error_handler__sp(["dbo.job_error_handler_$sp"]) --> SP
    dbo_job_header(["dbo.job_header"]) --> SP
    dbo_job_progress_handler__sp(["dbo.job_progress_handler_$sp"]) --> SP
    dbo_return_debug_flag__sp(["dbo.return_debug_flag_$sp"]) --> SP
    dbo_wrk_ib_cfd_style_alt_group(["dbo.wrk_ib_cfd_style_alt_group"]) --> SP
    dbo_wrk_ib_cost_factor_discount(["dbo.wrk_ib_cost_factor_discount"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.job_error_handler_$sp |
| dbo.job_header |
| dbo.job_progress_handler_$sp |
| dbo.return_debug_flag_$sp |
| dbo.wrk_ib_cfd_style_alt_group |
| dbo.wrk_ib_cost_factor_discount |

## Stored Procedure Code

```sql

```

