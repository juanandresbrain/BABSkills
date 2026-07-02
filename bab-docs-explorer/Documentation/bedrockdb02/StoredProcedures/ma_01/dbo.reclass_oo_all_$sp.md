# dbo.reclass_oo_all_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.reclass_oo_all_$sp"]
    dbo_calendar_merch_week(["dbo.calendar_merch_week"]) --> SP
    dbo_oo_all_group_chn_li(["dbo.oo_all_group_chn_li"]) --> SP
    dbo_oo_all_group_chn_pd(["dbo.oo_all_group_chn_pd"]) --> SP
    dbo_oo_all_group_chn_wk(["dbo.oo_all_group_chn_wk"]) --> SP
    dbo_oo_all_group_chn_yr(["dbo.oo_all_group_chn_yr"]) --> SP
    dbo_oo_all_group_loc_li(["dbo.oo_all_group_loc_li"]) --> SP
    dbo_oo_all_group_loc_pd(["dbo.oo_all_group_loc_pd"]) --> SP
    dbo_oo_all_group_loc_wk(["dbo.oo_all_group_loc_wk"]) --> SP
    dbo_oo_all_group_loc_yr(["dbo.oo_all_group_loc_yr"]) --> SP
    dbo_oo_all_style_chn_wk(["dbo.oo_all_style_chn_wk"]) --> SP
    dbo_oo_all_style_loc_wk(["dbo.oo_all_style_loc_wk"]) --> SP
    dbo_style_reclass_detail(["dbo.style_reclass_detail"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar_merch_week |
| dbo.oo_all_group_chn_li |
| dbo.oo_all_group_chn_pd |
| dbo.oo_all_group_chn_wk |
| dbo.oo_all_group_chn_yr |
| dbo.oo_all_group_loc_li |
| dbo.oo_all_group_loc_pd |
| dbo.oo_all_group_loc_wk |
| dbo.oo_all_group_loc_yr |
| dbo.oo_all_style_chn_wk |
| dbo.oo_all_style_loc_wk |
| dbo.style_reclass_detail |

## Stored Procedure Code

```sql

```

