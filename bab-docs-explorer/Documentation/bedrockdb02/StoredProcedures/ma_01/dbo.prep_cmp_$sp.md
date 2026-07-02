# dbo.prep_cmp_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.prep_cmp_$sp"]
    dbo_job_error_handler__sp(["dbo.job_error_handler_$sp"]) --> SP
    dbo_job_progress_handler__sp(["dbo.job_progress_handler_$sp"]) --> SP
    dbo_posting_parameter(["dbo.posting_parameter"]) --> SP
    dbo_prep_cmp_group__sp(["dbo.prep_cmp_group_$sp"]) --> SP
    dbo_prep_cmp_sku__sp(["dbo.prep_cmp_sku_$sp"]) --> SP
    dbo_prep_cmp_style__sp(["dbo.prep_cmp_style_$sp"]) --> SP
    dbo_prep_cmp_style_color__sp(["dbo.prep_cmp_style_color_$sp"]) --> SP
    dbo_return_debug_flag__sp(["dbo.return_debug_flag_$sp"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.job_error_handler_$sp |
| dbo.job_progress_handler_$sp |
| dbo.posting_parameter |
| dbo.prep_cmp_group_$sp |
| dbo.prep_cmp_sku_$sp |
| dbo.prep_cmp_style_$sp |
| dbo.prep_cmp_style_color_$sp |
| dbo.return_debug_flag_$sp |

## Stored Procedure Code

```sql

```

