# dbo.post_wrk_ib_allocation_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.post_wrk_ib_allocation_$sp"]
    dbo_job_error_handler__sp(["dbo.job_error_handler_$sp"]) --> SP
    dbo_job_header(["dbo.job_header"]) --> SP
    dbo_job_progress_handler__sp(["dbo.job_progress_handler_$sp"]) --> SP
    dbo_return_debug_flag__sp(["dbo.return_debug_flag_$sp"]) --> SP
    dbo_syn_ib_allocation(["dbo.syn_ib_allocation"]) --> SP
    dbo_syn_sku(["dbo.syn_sku"]) --> SP
    dbo_syn_style_color(["dbo.syn_style_color"]) --> SP
    dbo_syn_style_group(["dbo.syn_style_group"]) --> SP
    dbo_syn_style_size(["dbo.syn_style_size"]) --> SP
    dbo_wrk_ib_all_style_alt_group(["dbo.wrk_ib_all_style_alt_group"]) --> SP
    dbo_wrk_ib_allocation(["dbo.wrk_ib_allocation"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.job_error_handler_$sp |
| dbo.job_header |
| dbo.job_progress_handler_$sp |
| dbo.return_debug_flag_$sp |
| dbo.syn_ib_allocation |
| dbo.syn_sku |
| dbo.syn_style_color |
| dbo.syn_style_group |
| dbo.syn_style_size |
| dbo.wrk_ib_all_style_alt_group |
| dbo.wrk_ib_allocation |

## Stored Procedure Code

```sql

```

