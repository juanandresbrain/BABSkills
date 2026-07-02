# dbo.reclass_hist_cmp_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.reclass_hist_cmp_$sp"]
    dbo_calendar_merch_week(["dbo.calendar_merch_week"]) --> SP
    dbo_hist_cmp_group_chn_li(["dbo.hist_cmp_group_chn_li"]) --> SP
    dbo_hist_cmp_group_chn_pd(["dbo.hist_cmp_group_chn_pd"]) --> SP
    dbo_hist_cmp_group_chn_wk(["dbo.hist_cmp_group_chn_wk"]) --> SP
    dbo_hist_cmp_group_chn_yr(["dbo.hist_cmp_group_chn_yr"]) --> SP
    dbo_hist_cmp_group_loc_li(["dbo.hist_cmp_group_loc_li"]) --> SP
    dbo_hist_cmp_group_loc_pd(["dbo.hist_cmp_group_loc_pd"]) --> SP
    dbo_hist_cmp_group_loc_wk(["dbo.hist_cmp_group_loc_wk"]) --> SP
    dbo_hist_cmp_group_loc_yr(["dbo.hist_cmp_group_loc_yr"]) --> SP
    dbo_hist_cmp_style_loc_wk(["dbo.hist_cmp_style_loc_wk"]) --> SP
    dbo_rc_cmp_style_chn_li(["dbo.rc_cmp_style_chn_li"]) --> SP
    dbo_rc_cmp_style_chn_pd(["dbo.rc_cmp_style_chn_pd"]) --> SP
    dbo_rc_cmp_style_chn_wk(["dbo.rc_cmp_style_chn_wk"]) --> SP
    dbo_rc_cmp_style_chn_yr(["dbo.rc_cmp_style_chn_yr"]) --> SP
    dbo_rc_cmp_style_loc_li(["dbo.rc_cmp_style_loc_li"]) --> SP
    dbo_rc_cmp_style_loc_pd(["dbo.rc_cmp_style_loc_pd"]) --> SP
    dbo_rc_cmp_style_loc_wk(["dbo.rc_cmp_style_loc_wk"]) --> SP
    dbo_rc_cmp_style_loc_yr(["dbo.rc_cmp_style_loc_yr"]) --> SP
    dbo_style_reclass_detail(["dbo.style_reclass_detail"]) --> SP
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
| dbo.hist_cmp_style_loc_wk |
| dbo.rc_cmp_style_chn_li |
| dbo.rc_cmp_style_chn_pd |
| dbo.rc_cmp_style_chn_wk |
| dbo.rc_cmp_style_chn_yr |
| dbo.rc_cmp_style_loc_li |
| dbo.rc_cmp_style_loc_pd |
| dbo.rc_cmp_style_loc_wk |
| dbo.rc_cmp_style_loc_yr |
| dbo.style_reclass_detail |

## Stored Procedure Code

```sql

```

