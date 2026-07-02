# dbo.wpost_iv_hist_group_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.wpost_iv_hist_group_$sp"]
    dbo_calendar_date(["dbo.calendar_date"]) --> SP
    dbo_job_error_handler__sp(["dbo.job_error_handler_$sp"]) --> SP
    dbo_job_header(["dbo.job_header"]) --> SP
    dbo_job_progress_handler__sp(["dbo.job_progress_handler_$sp"]) --> SP
    dbo_return_debug_flag__sp(["dbo.return_debug_flag_$sp"]) --> SP
    dbo_wrk_group_loc_wk(["dbo.wrk_group_loc_wk"]) --> SP
    dbo_wrk_ib_inventory(["dbo.wrk_ib_inventory"]) --> SP
    dbo_wrk_ib_iv_style_alt_group(["dbo.wrk_ib_iv_style_alt_group"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar_date |
| dbo.job_error_handler_$sp |
| dbo.job_header |
| dbo.job_progress_handler_$sp |
| dbo.return_debug_flag_$sp |
| dbo.wrk_group_loc_wk |
| dbo.wrk_ib_inventory |
| dbo.wrk_ib_iv_style_alt_group |

## Stored Procedure Code

```sql

```

