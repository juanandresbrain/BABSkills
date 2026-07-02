# dbo.view_oo_all_styleclr_loc_wk

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_oo_all_styleclr_loc_wk"]
    dbo_hierarchy_group(["dbo.hierarchy_group"]) --> VIEW
    dbo_oo_all_styleclr_loc_wk(["dbo.oo_all_styleclr_loc_wk"]) --> VIEW
    dbo_style_color(["dbo.style_color"]) --> VIEW
    dbo_style_group(["dbo.style_group"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.hierarchy_group |
| dbo.oo_all_styleclr_loc_wk |
| dbo.style_color |
| dbo.style_group |

## View Code

```sql
create view dbo.view_oo_all_styleclr_loc_wk 

AS
SELECT b.style_color_id, a.style_id, a.color_id, a.merch_year_wk, a.location_id, a.on_order_units, a.on_order_retail, a.on_order_retail_te, a.on_order_retail_local, a.on_order_retail_te_local, a.allocation_units, c.hierarchy_group_id
FROM oo_all_styleclr_loc_wk a, style_color b, hierarchy_group c, style_group d
WHERE a.style_id = b.style_id   and a.color_id = b.color_id
and
b.style_id = d.style_id
and d.hierarchy_group_id = c.hierarchy_group_id
and d.main_group_flag = 1
and c.hierarchy_id =1
```

