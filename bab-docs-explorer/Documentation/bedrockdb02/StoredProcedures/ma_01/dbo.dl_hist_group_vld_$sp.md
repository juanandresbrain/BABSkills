# dbo.dl_hist_group_vld_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.dl_hist_group_vld_$sp"]
    dbo_calendar_merch_week(["dbo.calendar_merch_week"]) --> SP
    dbo_dl_hist_group(["dbo.dl_hist_group"]) --> SP
    dbo_dl_hist_task(["dbo.dl_hist_task"]) --> SP
    dbo_hierarchy(["dbo.hierarchy"]) --> SP
    dbo_hierarchy_group(["dbo.hierarchy_group"]) --> SP
    dbo_hierarchy_level(["dbo.hierarchy_level"]) --> SP
    dbo_hist_group_loc_wk(["dbo.hist_group_loc_wk"]) --> SP
    dbo_location(["dbo.location"]) --> SP
    dbo_post_parameter(["dbo.post_parameter"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar_merch_week |
| dbo.dl_hist_group |
| dbo.dl_hist_task |
| dbo.hierarchy |
| dbo.hierarchy_group |
| dbo.hierarchy_level |
| dbo.hist_group_loc_wk |
| dbo.location |
| dbo.post_parameter |

## Stored Procedure Code

```sql

```

