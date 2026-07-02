# dbo.view_hist_cmp_styleclr_chn_li

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_hist_cmp_styleclr_chn_li"]
    dbo_hierarchy_group(["dbo.hierarchy_group"]) --> VIEW
    dbo_hist_cmp_styleclr_chn_li(["dbo.hist_cmp_styleclr_chn_li"]) --> VIEW
    dbo_style_color(["dbo.style_color"]) --> VIEW
    dbo_style_group(["dbo.style_group"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.hierarchy_group |
| dbo.hist_cmp_styleclr_chn_li |
| dbo.style_color |
| dbo.style_group |

## View Code

```sql
create view dbo.view_hist_cmp_styleclr_chn_li AS
SELECT b.style_color_id, a.style_id, a.color_id, a.component_type_code, a.history_component_id, a.component_units, a.component_retail, a.component_cost, c.hierarchy_group_id
FROM hist_cmp_styleclr_chn_li a, style_color b, hierarchy_group c, style_group d
WHERE a.style_id = b.style_id   and a.color_id = b.color_id
and
b.style_id = d.style_id
and d.hierarchy_group_id = c.hierarchy_group_id
and d.main_group_flag = 1
and c.hierarchy_id =1
```

