# dbo.wpost_cf_cmp_group_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.wpost_cf_cmp_group_$sp"]
    dbo_calendar_date(["dbo.calendar_date"]) --> SP
    dbo_component_xref(["dbo.component_xref"]) --> SP
    dbo_history_component(["dbo.history_component"]) --> SP
    dbo_job_error_handler__sp(["dbo.job_error_handler_$sp"]) --> SP
    dbo_job_header(["dbo.job_header"]) --> SP
    dbo_job_progress_handler__sp(["dbo.job_progress_handler_$sp"]) --> SP
    dbo_return_debug_flag__sp(["dbo.return_debug_flag_$sp"]) --> SP
    dbo_wrk_cmp_group_loc_wk(["dbo.wrk_cmp_group_loc_wk"]) --> SP
    dbo_wrk_ib_cfd_style_alt_group(["dbo.wrk_ib_cfd_style_alt_group"]) --> SP
    dbo_wrk_ib_cost_factor_discount(["dbo.wrk_ib_cost_factor_discount"]) --> SP
    dbo_wrk_ib_iv_style_alt_group(["dbo.wrk_ib_iv_style_alt_group"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar_date |
| dbo.component_xref |
| dbo.history_component |
| dbo.job_error_handler_$sp |
| dbo.job_header |
| dbo.job_progress_handler_$sp |
| dbo.return_debug_flag_$sp |
| dbo.wrk_cmp_group_loc_wk |
| dbo.wrk_ib_cfd_style_alt_group |
| dbo.wrk_ib_cost_factor_discount |
| dbo.wrk_ib_iv_style_alt_group |

## Stored Procedure Code

```sql

```

