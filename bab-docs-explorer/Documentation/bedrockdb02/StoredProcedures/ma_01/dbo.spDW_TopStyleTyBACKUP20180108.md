# dbo.spDW_TopStyleTyBACKUP20180108

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spDW_TopStyleTyBACKUP20180108"]
    dbo_date_dim(["dbo.date_dim"]) --> SP
    dbo_hierarchy_group(["dbo.hierarchy_group"]) --> SP
    dbo_hist_oh_style_loc_wk(["dbo.hist_oh_style_loc_wk"]) --> SP
    dbo_hist_style_loc_wk(["dbo.hist_style_loc_wk"]) --> SP
    dbo_hist_style_loc_yr(["dbo.hist_style_loc_yr"]) --> SP
    dbo_jurisdiction(["dbo.jurisdiction"]) --> SP
    dbo_location(["dbo.location"]) --> SP
    dbo_oo_all_style_loc_pd(["dbo.oo_all_style_loc_pd"]) --> SP
    dbo_style(["dbo.style"]) --> SP
    dbo_style_parent(["dbo.style_parent"]) --> SP
    dbo_view_oh_style_loctype_wk(["dbo.view_oh_style_loctype_wk"]) --> SP
    dbo_view_style_attribute_outer(["dbo.view_style_attribute_outer"]) --> SP
    dbo_view_style_cust_prop_outer(["dbo.view_style_cust_prop_outer"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.date_dim |
| dbo.hierarchy_group |
| dbo.hist_oh_style_loc_wk |
| dbo.hist_style_loc_wk |
| dbo.hist_style_loc_yr |
| dbo.jurisdiction |
| dbo.location |
| dbo.oo_all_style_loc_pd |
| dbo.style |
| dbo.style_parent |
| dbo.view_oh_style_loctype_wk |
| dbo.view_style_attribute_outer |
| dbo.view_style_cust_prop_outer |

## Stored Procedure Code

```sql

```

