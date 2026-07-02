# dbo.rpt_merchandise_allocation_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.rpt_merchandise_allocation_$sp"]
    dbo_hist_group_loc_wk(["dbo.hist_group_loc_wk"]) --> SP
    dbo_hist_oh_group_loc_li(["dbo.hist_oh_group_loc_li"]) --> SP
    dbo_post_parameter(["dbo.post_parameter"]) --> SP
    dbo_view_calendar_merch_week_rel(["dbo.view_calendar_merch_week_rel"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.hist_group_loc_wk |
| dbo.hist_oh_group_loc_li |
| dbo.post_parameter |
| dbo.view_calendar_merch_week_rel |

## Stored Procedure Code

```sql

```

