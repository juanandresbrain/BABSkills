# dbo.post_flash_style_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.post_flash_style_$sp"]
    dbo_hist_flsh_style_chn_da(["dbo.hist_flsh_style_chn_da"]) --> SP
    dbo_hist_flsh_style_loc_da(["dbo.hist_flsh_style_loc_da"]) --> SP
    dbo_job_detail(["dbo.job_detail"]) --> SP
    dbo_job_error_handler__sp(["dbo.job_error_handler_$sp"]) --> SP
    dbo_job_header(["dbo.job_header"]) --> SP
    dbo_job_progress_handler__sp(["dbo.job_progress_handler_$sp"]) --> SP
    dbo_return_debug_flag__sp(["dbo.return_debug_flag_$sp"]) --> SP
    dbo_return_step_exists__sp(["dbo.return_step_exists_$sp"]) --> SP
    dbo_wrk_flsh_style_loc_da(["dbo.wrk_flsh_style_loc_da"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.hist_flsh_style_chn_da |
| dbo.hist_flsh_style_loc_da |
| dbo.job_detail |
| dbo.job_error_handler_$sp |
| dbo.job_header |
| dbo.job_progress_handler_$sp |
| dbo.return_debug_flag_$sp |
| dbo.return_step_exists_$sp |
| dbo.wrk_flsh_style_loc_da |

## Stored Procedure Code

```sql

```

