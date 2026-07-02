# dbo.validate_wrk_ib_inventory_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.validate_wrk_ib_inventory_$sp"]
    dbo_get_current_week__sp(["dbo.get_current_week_$sp"]) --> SP
    dbo_job_error_handler__sp(["dbo.job_error_handler_$sp"]) --> SP
    dbo_job_header(["dbo.job_header"]) --> SP
    dbo_job_info(["dbo.job_info"]) --> SP
    dbo_job_progress_handler__sp(["dbo.job_progress_handler_$sp"]) --> SP
    dbo_post_parameter(["dbo.post_parameter"]) --> SP
    dbo_return_debug_flag__sp(["dbo.return_debug_flag_$sp"]) --> SP
    dbo_wrk_ib_inventory(["dbo.wrk_ib_inventory"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.get_current_week_$sp |
| dbo.job_error_handler_$sp |
| dbo.job_header |
| dbo.job_info |
| dbo.job_progress_handler_$sp |
| dbo.post_parameter |
| dbo.return_debug_flag_$sp |
| dbo.wrk_ib_inventory |

## Stored Procedure Code

```sql

```

