# dbo.post_oo_style_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.post_oo_style_$sp"]
    dbo_calendar_merch_week(["dbo.calendar_merch_week"]) --> SP
    dbo_job_detail(["dbo.job_detail"]) --> SP
    dbo_job_error_handler__sp(["dbo.job_error_handler_$sp"]) --> SP
    dbo_job_header(["dbo.job_header"]) --> SP
    dbo_job_progress_handler__sp(["dbo.job_progress_handler_$sp"]) --> SP
    dbo_oo_all_style_chn_li(["dbo.oo_all_style_chn_li"]) --> SP
    dbo_oo_all_style_chn_pd(["dbo.oo_all_style_chn_pd"]) --> SP
    dbo_oo_all_style_chn_wk(["dbo.oo_all_style_chn_wk"]) --> SP
    dbo_oo_all_style_chn_yr(["dbo.oo_all_style_chn_yr"]) --> SP
    dbo_oo_all_style_loc_li(["dbo.oo_all_style_loc_li"]) --> SP
    dbo_oo_all_style_loc_pd(["dbo.oo_all_style_loc_pd"]) --> SP
    dbo_oo_all_style_loc_wk(["dbo.oo_all_style_loc_wk"]) --> SP
    dbo_oo_all_style_loc_yr(["dbo.oo_all_style_loc_yr"]) --> SP
    dbo_return_debug_flag__sp(["dbo.return_debug_flag_$sp"]) --> SP
    dbo_return_step_exists__sp(["dbo.return_step_exists_$sp"]) --> SP
    dbo_wrk_oo_all_style_loc_wk(["dbo.wrk_oo_all_style_loc_wk"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar_merch_week |
| dbo.job_detail |
| dbo.job_error_handler_$sp |
| dbo.job_header |
| dbo.job_progress_handler_$sp |
| dbo.oo_all_style_chn_li |
| dbo.oo_all_style_chn_pd |
| dbo.oo_all_style_chn_wk |
| dbo.oo_all_style_chn_yr |
| dbo.oo_all_style_loc_li |
| dbo.oo_all_style_loc_pd |
| dbo.oo_all_style_loc_wk |
| dbo.oo_all_style_loc_yr |
| dbo.return_debug_flag_$sp |
| dbo.return_step_exists_$sp |
| dbo.wrk_oo_all_style_loc_wk |

## Stored Procedure Code

```sql

```

