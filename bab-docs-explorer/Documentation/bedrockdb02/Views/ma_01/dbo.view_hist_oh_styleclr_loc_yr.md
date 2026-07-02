# dbo.view_hist_oh_styleclr_loc_yr

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_hist_oh_styleclr_loc_yr"]
    dbo_hierarchy_group(["dbo.hierarchy_group"]) --> VIEW
    dbo_hist_oh_styleclr_loc_yr(["dbo.hist_oh_styleclr_loc_yr"]) --> VIEW
    dbo_style_color(["dbo.style_color"]) --> VIEW
    dbo_style_group(["dbo.style_group"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.hierarchy_group |
| dbo.hist_oh_styleclr_loc_yr |
| dbo.style_color |
| dbo.style_group |

## View Code

```sql
create view dbo.view_hist_oh_styleclr_loc_yr 

AS
SELECT b.style_color_id, a.style_id, a.color_id, a.merch_year, a.location_id, a.inventory_status_id, a.price_status_id, a.on_hand_units, a.on_hand_retail, a.on_hand_retail_te, a.on_hand_retail_local, a.on_hand_retail_te_local, c.hierarchy_group_id
FROM hist_oh_styleclr_loc_yr a, style_color b, hierarchy_group c, style_group d
WHERE a.style_id = b.style_id   and a.color_id = b.color_id
and
b.style_id = d.style_id
and d.hierarchy_group_id = c.hierarchy_group_id
and d.main_group_flag = 1
and c.hierarchy_id =1
```

