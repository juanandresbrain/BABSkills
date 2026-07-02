# dbo.post_oh_sku_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.post_oh_sku_$sp"]
    dbo_calendar_merch_week(["dbo.calendar_merch_week"]) --> SP
    dbo_hist_oh_sku_chn_li(["dbo.hist_oh_sku_chn_li"]) --> SP
    dbo_hist_oh_sku_chn_pd(["dbo.hist_oh_sku_chn_pd"]) --> SP
    dbo_hist_oh_sku_chn_wk(["dbo.hist_oh_sku_chn_wk"]) --> SP
    dbo_hist_oh_sku_chn_yr(["dbo.hist_oh_sku_chn_yr"]) --> SP
    dbo_hist_oh_sku_loc_li(["dbo.hist_oh_sku_loc_li"]) --> SP
    dbo_hist_oh_sku_loc_pd(["dbo.hist_oh_sku_loc_pd"]) --> SP
    dbo_hist_oh_sku_loc_wk(["dbo.hist_oh_sku_loc_wk"]) --> SP
    dbo_hist_oh_sku_loc_yr(["dbo.hist_oh_sku_loc_yr"]) --> SP
    dbo_job_detail(["dbo.job_detail"]) --> SP
    dbo_job_error_handler__sp(["dbo.job_error_handler_$sp"]) --> SP
    dbo_job_header(["dbo.job_header"]) --> SP
    dbo_job_progress_handler__sp(["dbo.job_progress_handler_$sp"]) --> SP
    dbo_return_debug_flag__sp(["dbo.return_debug_flag_$sp"]) --> SP
    dbo_return_step_exists__sp(["dbo.return_step_exists_$sp"]) --> SP
    dbo_wrk_oh_sku_loc_wk(["dbo.wrk_oh_sku_loc_wk"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar_merch_week |
| dbo.hist_oh_sku_chn_li |
| dbo.hist_oh_sku_chn_pd |
| dbo.hist_oh_sku_chn_wk |
| dbo.hist_oh_sku_chn_yr |
| dbo.hist_oh_sku_loc_li |
| dbo.hist_oh_sku_loc_pd |
| dbo.hist_oh_sku_loc_wk |
| dbo.hist_oh_sku_loc_yr |
| dbo.job_detail |
| dbo.job_error_handler_$sp |
| dbo.job_header |
| dbo.job_progress_handler_$sp |
| dbo.return_debug_flag_$sp |
| dbo.return_step_exists_$sp |
| dbo.wrk_oh_sku_loc_wk |

## Stored Procedure Code

```sql

```

