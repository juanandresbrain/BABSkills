# dbo.wprep_all_style_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.wprep_all_style_$sp"]
    dbo_get_job_params__sp(["dbo.get_job_params_$sp"]) --> SP
    dbo_get_last_range_end__sp(["dbo.get_last_range_end_$sp"]) --> SP
    dbo_get_max_wrk_ib_allocation_id__sp(["dbo.get_max_wrk_ib_allocation_id_$sp"]) --> SP
    dbo_job_error_handler__sp(["dbo.job_error_handler_$sp"]) --> SP
    dbo_job_header(["dbo.job_header"]) --> SP
    dbo_job_progress_handler__sp(["dbo.job_progress_handler_$sp"]) --> SP
    dbo_return_debug_flag__sp(["dbo.return_debug_flag_$sp"]) --> SP
    dbo_wrk_ib_allocation(["dbo.wrk_ib_allocation"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.get_job_params_$sp |
| dbo.get_last_range_end_$sp |
| dbo.get_max_wrk_ib_allocation_id_$sp |
| dbo.job_error_handler_$sp |
| dbo.job_header |
| dbo.job_progress_handler_$sp |
| dbo.return_debug_flag_$sp |
| dbo.wrk_ib_allocation |

## Stored Procedure Code

```sql

```

