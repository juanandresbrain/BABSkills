# dbo.validate_wrk_ib_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.validate_wrk_ib_$sp"]
    dbo_job_error_handler__sp(["dbo.job_error_handler_$sp"]) --> SP
    dbo_job_progress_handler__sp(["dbo.job_progress_handler_$sp"]) --> SP
    dbo_posting_parameter(["dbo.posting_parameter"]) --> SP
    dbo_return_debug_flag__sp(["dbo.return_debug_flag_$sp"]) --> SP
    dbo_validate_wrk_ib_allocation__sp(["dbo.validate_wrk_ib_allocation_$sp"]) --> SP
    dbo_validate_wrk_ib_cost_fact__sp(["dbo.validate_wrk_ib_cost_fact_$sp"]) --> SP
    dbo_validate_wrk_ib_inventory__sp(["dbo.validate_wrk_ib_inventory_$sp"]) --> SP
    dbo_validate_wrk_ib_on_order__sp(["dbo.validate_wrk_ib_on_order_$sp"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.job_error_handler_$sp |
| dbo.job_progress_handler_$sp |
| dbo.posting_parameter |
| dbo.return_debug_flag_$sp |
| dbo.validate_wrk_ib_allocation_$sp |
| dbo.validate_wrk_ib_cost_fact_$sp |
| dbo.validate_wrk_ib_inventory_$sp |
| dbo.validate_wrk_ib_on_order_$sp |

## Stored Procedure Code

```sql

```

