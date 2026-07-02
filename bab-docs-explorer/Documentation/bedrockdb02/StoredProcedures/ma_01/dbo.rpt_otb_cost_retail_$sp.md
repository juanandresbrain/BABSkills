# dbo.rpt_otb_cost_retail_$sp

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.rpt_otb_cost_retail_$sp"]
    dbo_location_parent(["dbo.location_parent"]) --> SP
    dbo_merch_group_parent(["dbo.merch_group_parent"]) --> SP
    dbo_oo_all_group_loc_pd(["dbo.oo_all_group_loc_pd"]) --> SP
    dbo_oo_unc_group_loc_pd(["dbo.oo_unc_group_loc_pd"]) --> SP
    dbo_plan_element(["dbo.plan_element"]) --> SP
    dbo_plan_group_loc_pd(["dbo.plan_group_loc_pd"]) --> SP
    dbo_plan_version(["dbo.plan_version"]) --> SP
    dbo_view_calendar_merch_pd_rel(["dbo.view_calendar_merch_pd_rel"]) --> SP
    dbo_view_otb_proj_bop_inv(["dbo.view_otb_proj_bop_inv"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.location_parent |
| dbo.merch_group_parent |
| dbo.oo_all_group_loc_pd |
| dbo.oo_unc_group_loc_pd |
| dbo.plan_element |
| dbo.plan_group_loc_pd |
| dbo.plan_version |
| dbo.view_calendar_merch_pd_rel |
| dbo.view_otb_proj_bop_inv |

## Stored Procedure Code

```sql

```

