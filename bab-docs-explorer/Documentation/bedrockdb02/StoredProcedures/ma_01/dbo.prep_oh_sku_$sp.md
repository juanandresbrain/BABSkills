# dbo.prep_oh_sku_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.prep_oh_sku_$sp"]
    dbo_get_job_params__sp(["dbo.get_job_params_$sp"]) --> SP
    dbo_get_last_range_end_phase2__sp(["dbo.get_last_range_end_phase2_$sp"]) --> SP
    dbo_job_error_handler__sp(["dbo.job_error_handler_$sp"]) --> SP
    dbo_job_header(["dbo.job_header"]) --> SP
    dbo_job_progress_handler__sp(["dbo.job_progress_handler_$sp"]) --> SP
    dbo_return_debug_flag__sp(["dbo.return_debug_flag_$sp"]) --> SP
    dbo_wrk_oh_sku_loc_wk(["dbo.wrk_oh_sku_loc_wk"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.get_job_params_$sp |
| dbo.get_last_range_end_phase2_$sp |
| dbo.job_error_handler_$sp |
| dbo.job_header |
| dbo.job_progress_handler_$sp |
| dbo.return_debug_flag_$sp |
| dbo.wrk_oh_sku_loc_wk |

## Stored Procedure Code

```sql

```

