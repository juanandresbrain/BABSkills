# dbo.rpt_style_analysis_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.rpt_style_analysis_$sp"]
    dbo_calendar_date(["dbo.calendar_date"]) --> SP
    dbo_calendar_merch_week(["dbo.calendar_merch_week"]) --> SP
    dbo_hierarchy_group(["dbo.hierarchy_group"]) --> SP
    dbo_hist_oh_style_loc_li(["dbo.hist_oh_style_loc_li"]) --> SP
    dbo_hist_oh_style_loc_wk(["dbo.hist_oh_style_loc_wk"]) --> SP
    dbo_hist_style_loc_li(["dbo.hist_style_loc_li"]) --> SP
    dbo_hist_style_loc_wk(["dbo.hist_style_loc_wk"]) --> SP
    dbo_ib_activity_date(["dbo.ib_activity_date"]) --> SP
    dbo_location(["dbo.location"]) --> SP
    dbo_location_status(["dbo.location_status"]) --> SP
    dbo_oo_all_style_chn_wk(["dbo.oo_all_style_chn_wk"]) --> SP
    dbo_oo_all_style_loc_li(["dbo.oo_all_style_loc_li"]) --> SP
    dbo_post_parameter(["dbo.post_parameter"]) --> SP
    dbo_price_status(["dbo.price_status"]) --> SP
    dbo_style(["dbo.style"]) --> SP
    dbo_style_parent(["dbo.style_parent"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar_date |
| dbo.calendar_merch_week |
| dbo.hierarchy_group |
| dbo.hist_oh_style_loc_li |
| dbo.hist_oh_style_loc_wk |
| dbo.hist_style_loc_li |
| dbo.hist_style_loc_wk |
| dbo.ib_activity_date |
| dbo.location |
| dbo.location_status |
| dbo.oo_all_style_chn_wk |
| dbo.oo_all_style_loc_li |
| dbo.post_parameter |
| dbo.price_status |
| dbo.style |
| dbo.style_parent |

## Stored Procedure Code

```sql

```

