# dbo.prep_roll_oh_color_loc_pd_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.prep_roll_oh_color_loc_pd_$sp"]
    dbo_get_current_period__sp(["dbo.get_current_period_$sp"]) --> SP
    dbo_get_last_range_end__sp(["dbo.get_last_range_end_$sp"]) --> SP
    dbo_job_error_handler__sp(["dbo.job_error_handler_$sp"]) --> SP
    dbo_job_header(["dbo.job_header"]) --> SP
    dbo_job_progress_handler__sp(["dbo.job_progress_handler_$sp"]) --> SP
    dbo_return_debug_flag__sp(["dbo.return_debug_flag_$sp"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.get_current_period_$sp |
| dbo.get_last_range_end_$sp |
| dbo.job_error_handler_$sp |
| dbo.job_header |
| dbo.job_progress_handler_$sp |
| dbo.return_debug_flag_$sp |

## Stored Procedure Code

```sql

```

