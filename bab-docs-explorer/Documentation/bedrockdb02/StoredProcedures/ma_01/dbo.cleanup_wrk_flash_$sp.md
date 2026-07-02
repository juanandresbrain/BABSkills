# dbo.cleanup_wrk_flash_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.cleanup_wrk_flash_$sp"]
    dbo_job_error_handler__sp(["dbo.job_error_handler_$sp"]) --> SP
    dbo_job_progress_handler__sp(["dbo.job_progress_handler_$sp"]) --> SP
    dbo_return_debug_flag__sp(["dbo.return_debug_flag_$sp"]) --> SP
    dbo_wrk_flsh_group_loc_da(["dbo.wrk_flsh_group_loc_da"]) --> SP
    dbo_wrk_flsh_style_loc_da(["dbo.wrk_flsh_style_loc_da"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.job_error_handler_$sp |
| dbo.job_progress_handler_$sp |
| dbo.return_debug_flag_$sp |
| dbo.wrk_flsh_group_loc_da |
| dbo.wrk_flsh_style_loc_da |

## Stored Procedure Code

```sql

```

