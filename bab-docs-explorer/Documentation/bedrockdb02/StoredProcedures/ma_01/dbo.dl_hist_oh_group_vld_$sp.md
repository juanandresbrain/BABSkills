# dbo.dl_hist_oh_group_vld_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.dl_hist_oh_group_vld_$sp"]
    dbo_calendar_merch_week(["dbo.calendar_merch_week"]) --> SP
    dbo_dl_hist_oh_group(["dbo.dl_hist_oh_group"]) --> SP
    dbo_dl_hist_task(["dbo.dl_hist_task"]) --> SP
    dbo_hierarchy(["dbo.hierarchy"]) --> SP
    dbo_hierarchy_group(["dbo.hierarchy_group"]) --> SP
    dbo_hierarchy_level(["dbo.hierarchy_level"]) --> SP
    dbo_hist_oh_group_loc_wk(["dbo.hist_oh_group_loc_wk"]) --> SP
    dbo_inventory_status(["dbo.inventory_status"]) --> SP
    dbo_location(["dbo.location"]) --> SP
    dbo_post_parameter(["dbo.post_parameter"]) --> SP
    dbo_price_status(["dbo.price_status"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar_merch_week |
| dbo.dl_hist_oh_group |
| dbo.dl_hist_task |
| dbo.hierarchy |
| dbo.hierarchy_group |
| dbo.hierarchy_level |
| dbo.hist_oh_group_loc_wk |
| dbo.inventory_status |
| dbo.location |
| dbo.post_parameter |
| dbo.price_status |

## Stored Procedure Code

```sql

```

