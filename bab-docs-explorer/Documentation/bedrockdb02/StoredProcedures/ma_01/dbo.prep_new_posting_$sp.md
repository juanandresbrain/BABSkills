# dbo.prep_new_posting_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.prep_new_posting_$sp"]
    dbo_add_partitions__sp(["dbo.add_partitions_$sp"]) --> SP
    dbo_cleanup_wrk_ib_allocation__sp(["dbo.cleanup_wrk_ib_allocation_$sp"]) --> SP
    dbo_cleanup_wrk_ib_cost_factor__sp(["dbo.cleanup_wrk_ib_cost_factor_$sp"]) --> SP
    dbo_cleanup_wrk_ib_inventory__sp(["dbo.cleanup_wrk_ib_inventory_$sp"]) --> SP
    dbo_cleanup_wrk_ib_on_order__sp(["dbo.cleanup_wrk_ib_on_order_$sp"]) --> SP
    dbo_job_error_handler__sp(["dbo.job_error_handler_$sp"]) --> SP
    dbo_job_header(["dbo.job_header"]) --> SP
    dbo_job_progress_handler__sp(["dbo.job_progress_handler_$sp"]) --> SP
    dbo_posting_parameter(["dbo.posting_parameter"]) --> SP
    dbo_return_debug_flag__sp(["dbo.return_debug_flag_$sp"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.add_partitions_$sp |
| dbo.cleanup_wrk_ib_allocation_$sp |
| dbo.cleanup_wrk_ib_cost_factor_$sp |
| dbo.cleanup_wrk_ib_inventory_$sp |
| dbo.cleanup_wrk_ib_on_order_$sp |
| dbo.job_error_handler_$sp |
| dbo.job_header |
| dbo.job_progress_handler_$sp |
| dbo.posting_parameter |
| dbo.return_debug_flag_$sp |

## Stored Procedure Code

```sql

```

