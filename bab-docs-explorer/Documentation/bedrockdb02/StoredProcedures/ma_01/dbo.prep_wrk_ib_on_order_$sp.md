# dbo.prep_wrk_ib_on_order_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.prep_wrk_ib_on_order_$sp"]
    dbo_get_job_params__sp(["dbo.get_job_params_$sp"]) --> SP
    dbo_get_last_range_end__sp(["dbo.get_last_range_end_$sp"]) --> SP
    dbo_get_max_ib_on_order_id__sp(["dbo.get_max_ib_on_order_id_$sp"]) --> SP
    dbo_is_tax_exclusive__sp(["dbo.is_tax_exclusive_$sp"]) --> SP
    dbo_job_error_handler__sp(["dbo.job_error_handler_$sp"]) --> SP
    dbo_job_header(["dbo.job_header"]) --> SP
    dbo_job_progress_handler__sp(["dbo.job_progress_handler_$sp"]) --> SP
    dbo_posting_parameter(["dbo.posting_parameter"]) --> SP
    dbo_return_debug_flag__sp(["dbo.return_debug_flag_$sp"]) --> SP
    dbo_syn_oo_populate_notax_retails__sp(["dbo.syn_oo_populate_notax_retails_$sp"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.get_job_params_$sp |
| dbo.get_last_range_end_$sp |
| dbo.get_max_ib_on_order_id_$sp |
| dbo.is_tax_exclusive_$sp |
| dbo.job_error_handler_$sp |
| dbo.job_header |
| dbo.job_progress_handler_$sp |
| dbo.posting_parameter |
| dbo.return_debug_flag_$sp |
| dbo.syn_oo_populate_notax_retails_$sp |

## Stored Procedure Code

```sql

```

