# dbo.prep_wrk_cmp_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.prep_wrk_cmp_$sp"]
    dbo_job_error_handler__sp(["dbo.job_error_handler_$sp"]) --> SP
    dbo_job_progress_handler__sp(["dbo.job_progress_handler_$sp"]) --> SP
    dbo_posting_parameter(["dbo.posting_parameter"]) --> SP
    dbo_return_debug_flag__sp(["dbo.return_debug_flag_$sp"]) --> SP
    dbo_wprep_cf_cmp_group__sp(["dbo.wprep_cf_cmp_group_$sp"]) --> SP
    dbo_wprep_cf_cmp_style__sp(["dbo.wprep_cf_cmp_style_$sp"]) --> SP
    dbo_wprep_cf_cmp_style_color__sp(["dbo.wprep_cf_cmp_style_color_$sp"]) --> SP
    dbo_wprep_cmp_sku__sp(["dbo.wprep_cmp_sku_$sp"]) --> SP
    dbo_wprep_iv_cmp_group__sp(["dbo.wprep_iv_cmp_group_$sp"]) --> SP
    dbo_wprep_iv_cmp_style__sp(["dbo.wprep_iv_cmp_style_$sp"]) --> SP
    dbo_wprep_iv_cmp_style_color__sp(["dbo.wprep_iv_cmp_style_color_$sp"]) --> SP
    dbo_wrk_cmp_group_loc_wk(["dbo.wrk_cmp_group_loc_wk"]) --> SP
    dbo_wrk_cmp_sku_loc_wk(["dbo.wrk_cmp_sku_loc_wk"]) --> SP
    dbo_wrk_cmp_style_loc_wk(["dbo.wrk_cmp_style_loc_wk"]) --> SP
    dbo_wrk_cmp_styleclr_loc_wk(["dbo.wrk_cmp_styleclr_loc_wk"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.job_error_handler_$sp |
| dbo.job_progress_handler_$sp |
| dbo.posting_parameter |
| dbo.return_debug_flag_$sp |
| dbo.wprep_cf_cmp_group_$sp |
| dbo.wprep_cf_cmp_style_$sp |
| dbo.wprep_cf_cmp_style_color_$sp |
| dbo.wprep_cmp_sku_$sp |
| dbo.wprep_iv_cmp_group_$sp |
| dbo.wprep_iv_cmp_style_$sp |
| dbo.wprep_iv_cmp_style_color_$sp |
| dbo.wrk_cmp_group_loc_wk |
| dbo.wrk_cmp_sku_loc_wk |
| dbo.wrk_cmp_style_loc_wk |
| dbo.wrk_cmp_styleclr_loc_wk |

## Stored Procedure Code

```sql

```

