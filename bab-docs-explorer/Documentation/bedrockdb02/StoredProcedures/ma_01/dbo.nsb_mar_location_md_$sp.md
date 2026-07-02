# dbo.nsb_mar_location_md_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.nsb_mar_location_md_$sp"]
    dbo_calendar_merch_week(["dbo.calendar_merch_week"]) --> SP
    dbo_hierarchy_group(["dbo.hierarchy_group"]) --> SP
    dbo_hierarchy_level(["dbo.hierarchy_level"]) --> SP
    dbo_hist_cmp_group_loc_wk(["dbo.hist_cmp_group_loc_wk"]) --> SP
    dbo_hist_group_loc_wk(["dbo.hist_group_loc_wk"]) --> SP
    dbo_hist_oh_group_loc_wk(["dbo.hist_oh_group_loc_wk"]) --> SP
    dbo_history_component(["dbo.history_component"]) --> SP
    dbo_location(["dbo.location"]) --> SP
    dbo_merch_group_parent(["dbo.merch_group_parent"]) --> SP
    dbo_oo_all_group_loc_wk(["dbo.oo_all_group_loc_wk"]) --> SP
    dbo_parameter_plan_elements(["dbo.parameter_plan_elements"]) --> SP
    dbo_plan_group_loc_wk(["dbo.plan_group_loc_wk"]) --> SP
    dbo_price_status(["dbo.price_status"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar_merch_week |
| dbo.hierarchy_group |
| dbo.hierarchy_level |
| dbo.hist_cmp_group_loc_wk |
| dbo.hist_group_loc_wk |
| dbo.hist_oh_group_loc_wk |
| dbo.history_component |
| dbo.location |
| dbo.merch_group_parent |
| dbo.oo_all_group_loc_wk |
| dbo.parameter_plan_elements |
| dbo.plan_group_loc_wk |
| dbo.price_status |

## Stored Procedure Code

```sql

```

