# dbo.post_oo_unc_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.post_oo_unc_$sp"]
    dbo_calendar_date(["dbo.calendar_date"]) --> SP
    dbo_calendar_merch_period(["dbo.calendar_merch_period"]) --> SP
    dbo_calendar_merch_week(["dbo.calendar_merch_week"]) --> SP
    dbo_country(["dbo.country"]) --> SP
    dbo_hierarchy_group(["dbo.hierarchy_group"]) --> SP
    dbo_jurisdiction(["dbo.jurisdiction"]) --> SP
    dbo_location(["dbo.location"]) --> SP
    dbo_oo_unc_group_chn_li(["dbo.oo_unc_group_chn_li"]) --> SP
    dbo_oo_unc_group_chn_pd(["dbo.oo_unc_group_chn_pd"]) --> SP
    dbo_oo_unc_group_chn_wk(["dbo.oo_unc_group_chn_wk"]) --> SP
    dbo_oo_unc_group_chn_yr(["dbo.oo_unc_group_chn_yr"]) --> SP
    dbo_oo_unc_group_loc_li(["dbo.oo_unc_group_loc_li"]) --> SP
    dbo_oo_unc_group_loc_pd(["dbo.oo_unc_group_loc_pd"]) --> SP
    dbo_oo_unc_group_loc_wk(["dbo.oo_unc_group_loc_wk"]) --> SP
    dbo_oo_unc_group_loc_yr(["dbo.oo_unc_group_loc_yr"]) --> SP
    dbo_syn_currency_conversion(["dbo.syn_currency_conversion"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar_date |
| dbo.calendar_merch_period |
| dbo.calendar_merch_week |
| dbo.country |
| dbo.hierarchy_group |
| dbo.jurisdiction |
| dbo.location |
| dbo.oo_unc_group_chn_li |
| dbo.oo_unc_group_chn_pd |
| dbo.oo_unc_group_chn_wk |
| dbo.oo_unc_group_chn_yr |
| dbo.oo_unc_group_loc_li |
| dbo.oo_unc_group_loc_pd |
| dbo.oo_unc_group_loc_wk |
| dbo.oo_unc_group_loc_yr |
| dbo.syn_currency_conversion |

## Stored Procedure Code

```sql

```

