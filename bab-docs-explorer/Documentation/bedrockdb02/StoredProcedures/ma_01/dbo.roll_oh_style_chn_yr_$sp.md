# dbo.roll_oh_style_chn_yr_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.roll_oh_style_chn_yr_$sp"]
    dbo_calendar(["dbo.calendar"]) --> SP
    dbo_hist_oh_style_chn_yr(["dbo.hist_oh_style_chn_yr"]) --> SP
    dbo_job_error_handler__sp(["dbo.job_error_handler_$sp"]) --> SP
    dbo_job_header(["dbo.job_header"]) --> SP
    dbo_job_params(["dbo.job_params"]) --> SP
    dbo_job_progress_handler__sp(["dbo.job_progress_handler_$sp"]) --> SP
    dbo_merch_year_pf(["dbo.merch_year_pf"]) --> SP
    dbo_return_debug_flag__sp(["dbo.return_debug_flag_$sp"]) --> SP
    dbo_wrk_roll_oh_style_chn_yr(["dbo.wrk_roll_oh_style_chn_yr"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar |
| dbo.hist_oh_style_chn_yr |
| dbo.job_error_handler_$sp |
| dbo.job_header |
| dbo.job_params |
| dbo.job_progress_handler_$sp |
| dbo.merch_year_pf |
| dbo.return_debug_flag_$sp |
| dbo.wrk_roll_oh_style_chn_yr |

## Stored Procedure Code

```sql

```

