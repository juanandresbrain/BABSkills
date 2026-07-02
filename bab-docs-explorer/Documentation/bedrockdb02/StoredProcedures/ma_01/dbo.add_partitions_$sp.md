# dbo.add_partitions_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.add_partitions_$sp"]
    dbo_calendar_merch_week(["dbo.calendar_merch_week"]) --> SP
    dbo_get_current_period__sp(["dbo.get_current_period_$sp"]) --> SP
    dbo_get_current_week__sp(["dbo.get_current_week_$sp"]) --> SP
    dbo_get_current_year__sp(["dbo.get_current_year_$sp"]) --> SP
    dbo_job_error_handler__sp(["dbo.job_error_handler_$sp"]) --> SP
    dbo_job_progress_handler__sp(["dbo.job_progress_handler_$sp"]) --> SP
    dbo_return_debug_flag__sp(["dbo.return_debug_flag_$sp"]) --> SP
    dbo_user_partition(["dbo.user_partition"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar_merch_week |
| dbo.get_current_period_$sp |
| dbo.get_current_week_$sp |
| dbo.get_current_year_$sp |
| dbo.job_error_handler_$sp |
| dbo.job_progress_handler_$sp |
| dbo.return_debug_flag_$sp |
| dbo.user_partition |

## Stored Procedure Code

```sql

```

