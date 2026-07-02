# dbo.rpt_style_listing_class_vendor_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.rpt_style_listing_class_vendor_$sp"]
    dbo_hist_cmp_style_chn_wk(["dbo.hist_cmp_style_chn_wk"]) --> SP
    dbo_hist_oh_style_chn_li(["dbo.hist_oh_style_chn_li"]) --> SP
    dbo_hist_oh_style_loc_wk(["dbo.hist_oh_style_loc_wk"]) --> SP
    dbo_hist_style_chn_li(["dbo.hist_style_chn_li"]) --> SP
    dbo_hist_style_chn_wk(["dbo.hist_style_chn_wk"]) --> SP
    dbo_location(["dbo.location"]) --> SP
    dbo_oo_all_style_chn_li(["dbo.oo_all_style_chn_li"]) --> SP
    dbo_post_parameter(["dbo.post_parameter"]) --> SP
    dbo_view_calendar_merch_week_rel(["dbo.view_calendar_merch_week_rel"]) --> SP
    dbo_view_ib_activity_date(["dbo.view_ib_activity_date"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.hist_cmp_style_chn_wk |
| dbo.hist_oh_style_chn_li |
| dbo.hist_oh_style_loc_wk |
| dbo.hist_style_chn_li |
| dbo.hist_style_chn_wk |
| dbo.location |
| dbo.oo_all_style_chn_li |
| dbo.post_parameter |
| dbo.view_calendar_merch_week_rel |
| dbo.view_ib_activity_date |

## Stored Procedure Code

```sql

```

