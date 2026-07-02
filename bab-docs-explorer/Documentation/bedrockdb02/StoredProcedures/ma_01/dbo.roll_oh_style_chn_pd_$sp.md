# dbo.roll_oh_style_chn_pd_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.roll_oh_style_chn_pd_$sp"]
    dbo_calendar_merch_period(["dbo.calendar_merch_period"]) --> SP
    dbo_hist_oh_style_chn_pd(["dbo.hist_oh_style_chn_pd"]) --> SP
    dbo_job_error_handler__sp(["dbo.job_error_handler_$sp"]) --> SP
    dbo_job_header(["dbo.job_header"]) --> SP
    dbo_job_params(["dbo.job_params"]) --> SP
    dbo_job_progress_handler__sp(["dbo.job_progress_handler_$sp"]) --> SP
    dbo_merch_year_pd_pf(["dbo.merch_year_pd_pf"]) --> SP
    dbo_return_debug_flag__sp(["dbo.return_debug_flag_$sp"]) --> SP
    dbo_wrk_roll_oh_style_chn_pd(["dbo.wrk_roll_oh_style_chn_pd"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar_merch_period |
| dbo.hist_oh_style_chn_pd |
| dbo.job_error_handler_$sp |
| dbo.job_header |
| dbo.job_params |
| dbo.job_progress_handler_$sp |
| dbo.merch_year_pd_pf |
| dbo.return_debug_flag_$sp |
| dbo.wrk_roll_oh_style_chn_pd |

## Stored Procedure Code

```sql

```

