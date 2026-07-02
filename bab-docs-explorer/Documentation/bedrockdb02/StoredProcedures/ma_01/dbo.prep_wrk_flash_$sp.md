# dbo.prep_wrk_flash_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.prep_wrk_flash_$sp"]
    dbo_job_error_handler__sp(["dbo.job_error_handler_$sp"]) --> SP
    dbo_job_progress_handler__sp(["dbo.job_progress_handler_$sp"]) --> SP
    dbo_posting_parameter(["dbo.posting_parameter"]) --> SP
    dbo_return_debug_flag__sp(["dbo.return_debug_flag_$sp"]) --> SP
    dbo_wprep_flash_group__sp(["dbo.wprep_flash_group_$sp"]) --> SP
    dbo_wprep_flash_style__sp(["dbo.wprep_flash_style_$sp"]) --> SP
    dbo_wrk_flsh_group_loc_da(["dbo.wrk_flsh_group_loc_da"]) --> SP
    dbo_wrk_flsh_style_loc_da(["dbo.wrk_flsh_style_loc_da"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.job_error_handler_$sp |
| dbo.job_progress_handler_$sp |
| dbo.posting_parameter |
| dbo.return_debug_flag_$sp |
| dbo.wprep_flash_group_$sp |
| dbo.wprep_flash_style_$sp |
| dbo.wrk_flsh_group_loc_da |
| dbo.wrk_flsh_style_loc_da |

## Stored Procedure Code

```sql

```

