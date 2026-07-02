# dbo.reclass_oh_post_adjust_cmp_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.reclass_oh_post_adjust_cmp_$sp"]
    dbo_calendar_merch_week(["dbo.calendar_merch_week"]) --> SP
    dbo_hist_cmp_group_chn_li(["dbo.hist_cmp_group_chn_li"]) --> SP
    dbo_hist_cmp_group_chn_pd(["dbo.hist_cmp_group_chn_pd"]) --> SP
    dbo_hist_cmp_group_chn_wk(["dbo.hist_cmp_group_chn_wk"]) --> SP
    dbo_hist_cmp_group_chn_yr(["dbo.hist_cmp_group_chn_yr"]) --> SP
    dbo_hist_cmp_group_loc_li(["dbo.hist_cmp_group_loc_li"]) --> SP
    dbo_hist_cmp_group_loc_pd(["dbo.hist_cmp_group_loc_pd"]) --> SP
    dbo_hist_cmp_group_loc_wk(["dbo.hist_cmp_group_loc_wk"]) --> SP
    dbo_hist_cmp_group_loc_yr(["dbo.hist_cmp_group_loc_yr"]) --> SP
    dbo_post_parameter(["dbo.post_parameter"]) --> SP
    dbo_rc_oh_style_chn_curr(["dbo.rc_oh_style_chn_curr"]) --> SP
    dbo_rc_oh_style_chn_wk(["dbo.rc_oh_style_chn_wk"]) --> SP
    dbo_rc_oh_style_loc_curr(["dbo.rc_oh_style_loc_curr"]) --> SP
    dbo_rc_oh_style_loc_wk(["dbo.rc_oh_style_loc_wk"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar_merch_week |
| dbo.hist_cmp_group_chn_li |
| dbo.hist_cmp_group_chn_pd |
| dbo.hist_cmp_group_chn_wk |
| dbo.hist_cmp_group_chn_yr |
| dbo.hist_cmp_group_loc_li |
| dbo.hist_cmp_group_loc_pd |
| dbo.hist_cmp_group_loc_wk |
| dbo.hist_cmp_group_loc_yr |
| dbo.post_parameter |
| dbo.rc_oh_style_chn_curr |
| dbo.rc_oh_style_chn_wk |
| dbo.rc_oh_style_loc_curr |
| dbo.rc_oh_style_loc_wk |

## Stored Procedure Code

```sql

```

