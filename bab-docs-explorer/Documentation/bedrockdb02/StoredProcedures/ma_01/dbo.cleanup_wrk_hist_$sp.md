# dbo.cleanup_wrk_hist_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.cleanup_wrk_hist_$sp"]
    dbo_job_error_handler__sp(["dbo.job_error_handler_$sp"]) --> SP
    dbo_job_progress_handler__sp(["dbo.job_progress_handler_$sp"]) --> SP
    dbo_return_debug_flag__sp(["dbo.return_debug_flag_$sp"]) --> SP
    dbo_wrk_group_loc_wk(["dbo.wrk_group_loc_wk"]) --> SP
    dbo_wrk_sku_loc_wk(["dbo.wrk_sku_loc_wk"]) --> SP
    dbo_wrk_style_loc_wk(["dbo.wrk_style_loc_wk"]) --> SP
    dbo_wrk_styleclr_loc_wk(["dbo.wrk_styleclr_loc_wk"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.job_error_handler_$sp |
| dbo.job_progress_handler_$sp |
| dbo.return_debug_flag_$sp |
| dbo.wrk_group_loc_wk |
| dbo.wrk_sku_loc_wk |
| dbo.wrk_style_loc_wk |
| dbo.wrk_styleclr_loc_wk |

## Stored Procedure Code

```sql

```

