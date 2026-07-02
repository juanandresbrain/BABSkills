# dbo.wpost_oh_sku_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.wpost_oh_sku_$sp"]
    dbo_calendar_date(["dbo.calendar_date"]) --> SP
    dbo_calendar_merch_week(["dbo.calendar_merch_week"]) --> SP
    dbo_get_last_range_end__sp(["dbo.get_last_range_end_$sp"]) --> SP
    dbo_job_error_handler__sp(["dbo.job_error_handler_$sp"]) --> SP
    dbo_job_header(["dbo.job_header"]) --> SP
    dbo_job_progress_handler__sp(["dbo.job_progress_handler_$sp"]) --> SP
    dbo_return_debug_flag__sp(["dbo.return_debug_flag_$sp"]) --> SP
    dbo_wrk_ib_inventory(["dbo.wrk_ib_inventory"]) --> SP
    dbo_wrk_oh_sku_loc_wk(["dbo.wrk_oh_sku_loc_wk"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar_date |
| dbo.calendar_merch_week |
| dbo.get_last_range_end_$sp |
| dbo.job_error_handler_$sp |
| dbo.job_header |
| dbo.job_progress_handler_$sp |
| dbo.return_debug_flag_$sp |
| dbo.wrk_ib_inventory |
| dbo.wrk_oh_sku_loc_wk |

## Stored Procedure Code

```sql

```

