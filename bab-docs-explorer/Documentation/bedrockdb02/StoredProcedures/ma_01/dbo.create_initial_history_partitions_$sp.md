# dbo.create_initial_history_partitions_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.create_initial_history_partitions_$sp"]
    dbo_calendar_merch_week(["dbo.calendar_merch_week"]) --> SP
    dbo_hist_oh_group_chn_pd(["dbo.hist_oh_group_chn_pd"]) --> SP
    dbo_hist_oh_group_chn_wk(["dbo.hist_oh_group_chn_wk"]) --> SP
    dbo_hist_oh_group_chn_yr(["dbo.hist_oh_group_chn_yr"]) --> SP
    dbo_user_partition(["dbo.user_partition"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar_merch_week |
| dbo.hist_oh_group_chn_pd |
| dbo.hist_oh_group_chn_wk |
| dbo.hist_oh_group_chn_yr |
| dbo.user_partition |

## Stored Procedure Code

```sql

```

