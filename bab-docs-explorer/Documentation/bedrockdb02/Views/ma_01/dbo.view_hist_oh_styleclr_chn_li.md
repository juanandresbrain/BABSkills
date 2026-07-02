# dbo.view_hist_oh_styleclr_chn_li

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_hist_oh_styleclr_chn_li"]
    dbo_hierarchy_group(["dbo.hierarchy_group"]) --> VIEW
    dbo_hist_oh_styleclr_chn_li(["dbo.hist_oh_styleclr_chn_li"]) --> VIEW
    dbo_style_color(["dbo.style_color"]) --> VIEW
    dbo_style_group(["dbo.style_group"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.hierarchy_group |
| dbo.hist_oh_styleclr_chn_li |
| dbo.style_color |
| dbo.style_group |

## View Code

```sql
create view dbo.view_hist_oh_styleclr_chn_li 

AS
SELECT b.style_color_id, a.style_id, a.color_id, a.inventory_status_id, a.price_status_id, a.on_hand_units, a.on_hand_retail, a.on_hand_retail_te, c.hierarchy_group_id
FROM hist_oh_styleclr_chn_li a, style_color b, hierarchy_group c, style_group d
WHERE a.style_id = b.style_id   and a.color_id = b.color_id
and
b.style_id = d.style_id
and d.hierarchy_group_id = c.hierarchy_group_id
and d.main_group_flag = 1
and c.hierarchy_id =1
```

