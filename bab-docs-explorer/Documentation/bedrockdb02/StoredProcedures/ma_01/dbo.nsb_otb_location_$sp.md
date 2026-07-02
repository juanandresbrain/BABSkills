# dbo.nsb_otb_location_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.nsb_otb_location_$sp"]
    dbo_calendar_merch_period(["dbo.calendar_merch_period"]) --> SP
    dbo_calendar_merch_week(["dbo.calendar_merch_week"]) --> SP
    dbo_hierarchy_group(["dbo.hierarchy_group"]) --> SP
    dbo_hierarchy_level(["dbo.hierarchy_level"]) --> SP
    dbo_hist_group_loc_pd(["dbo.hist_group_loc_pd"]) --> SP
    dbo_hist_oh_group_loc_pd(["dbo.hist_oh_group_loc_pd"]) --> SP
    dbo_location(["dbo.location"]) --> SP
    dbo_location_parent(["dbo.location_parent"]) --> SP
    dbo_merch_group_parent(["dbo.merch_group_parent"]) --> SP
    dbo_oo_all_group_loc_pd(["dbo.oo_all_group_loc_pd"]) --> SP
    dbo_parameter_plan_elements(["dbo.parameter_plan_elements"]) --> SP
    dbo_plan_group_loc_pd(["dbo.plan_group_loc_pd"]) --> SP
    dbo_post_parameter(["dbo.post_parameter"]) --> SP
    dbo_view_calendar_merch_pd_rel(["dbo.view_calendar_merch_pd_rel"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar_merch_period |
| dbo.calendar_merch_week |
| dbo.hierarchy_group |
| dbo.hierarchy_level |
| dbo.hist_group_loc_pd |
| dbo.hist_oh_group_loc_pd |
| dbo.location |
| dbo.location_parent |
| dbo.merch_group_parent |
| dbo.oo_all_group_loc_pd |
| dbo.parameter_plan_elements |
| dbo.plan_group_loc_pd |
| dbo.post_parameter |
| dbo.view_calendar_merch_pd_rel |

## Stored Procedure Code

```sql

```

