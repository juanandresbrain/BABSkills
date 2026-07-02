# dbo.reclass_hist_oh_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.reclass_hist_oh_$sp"]
    dbo_calendar_merch_week(["dbo.calendar_merch_week"]) --> SP
    dbo_hist_oh_group_chn_li(["dbo.hist_oh_group_chn_li"]) --> SP
    dbo_hist_oh_group_chn_pd(["dbo.hist_oh_group_chn_pd"]) --> SP
    dbo_hist_oh_group_chn_wk(["dbo.hist_oh_group_chn_wk"]) --> SP
    dbo_hist_oh_group_chn_yr(["dbo.hist_oh_group_chn_yr"]) --> SP
    dbo_hist_oh_group_loc_li(["dbo.hist_oh_group_loc_li"]) --> SP
    dbo_hist_oh_group_loc_pd(["dbo.hist_oh_group_loc_pd"]) --> SP
    dbo_hist_oh_group_loc_wk(["dbo.hist_oh_group_loc_wk"]) --> SP
    dbo_hist_oh_group_loc_yr(["dbo.hist_oh_group_loc_yr"]) --> SP
    dbo_hist_oh_style_loc_wk(["dbo.hist_oh_style_loc_wk"]) --> SP
    dbo_history_component(["dbo.history_component"]) --> SP
    dbo_p(["dbo.p"]) --> SP
    dbo_post_parameter(["dbo.post_parameter"]) --> SP
    dbo_rc_oh_style_chn_li(["dbo.rc_oh_style_chn_li"]) --> SP
    dbo_rc_oh_style_chn_pd(["dbo.rc_oh_style_chn_pd"]) --> SP
    dbo_rc_oh_style_chn_wk(["dbo.rc_oh_style_chn_wk"]) --> SP
    dbo_rc_oh_style_chn_yr(["dbo.rc_oh_style_chn_yr"]) --> SP
    dbo_rc_oh_style_loc_li(["dbo.rc_oh_style_loc_li"]) --> SP
    dbo_rc_oh_style_loc_pd(["dbo.rc_oh_style_loc_pd"]) --> SP
    dbo_rc_oh_style_loc_wk(["dbo.rc_oh_style_loc_wk"]) --> SP
    dbo_rc_oh_style_loc_yr(["dbo.rc_oh_style_loc_yr"]) --> SP
    dbo_reclass_oh_post_adjust_cmp__sp(["dbo.reclass_oh_post_adjust_cmp_$sp"]) --> SP
    dbo_style_reclass_detail(["dbo.style_reclass_detail"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar_merch_week |
| dbo.hist_oh_group_chn_li |
| dbo.hist_oh_group_chn_pd |
| dbo.hist_oh_group_chn_wk |
| dbo.hist_oh_group_chn_yr |
| dbo.hist_oh_group_loc_li |
| dbo.hist_oh_group_loc_pd |
| dbo.hist_oh_group_loc_wk |
| dbo.hist_oh_group_loc_yr |
| dbo.hist_oh_style_loc_wk |
| dbo.history_component |
| dbo.p |
| dbo.post_parameter |
| dbo.rc_oh_style_chn_li |
| dbo.rc_oh_style_chn_pd |
| dbo.rc_oh_style_chn_wk |
| dbo.rc_oh_style_chn_yr |
| dbo.rc_oh_style_loc_li |
| dbo.rc_oh_style_loc_pd |
| dbo.rc_oh_style_loc_wk |
| dbo.rc_oh_style_loc_yr |
| dbo.reclass_oh_post_adjust_cmp_$sp |
| dbo.style_reclass_detail |

## Stored Procedure Code

```sql

```

