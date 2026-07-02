# dbo.view_dist_sku_scale_o

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_dist_sku_scale_o"]
    dbo_color(["dbo.color"]) --> VIEW
    dbo_dist_sku_scale(["dbo.dist_sku_scale"]) --> VIEW
    dbo_distribution(["dbo.distribution"]) --> VIEW
    dbo_hierarchy_group(["dbo.hierarchy_group"]) --> VIEW
    dbo_size_master(["dbo.size_master"]) --> VIEW
    dbo_sku(["dbo.sku"]) --> VIEW
    dbo_style(["dbo.style"]) --> VIEW
    dbo_style_color(["dbo.style_color"]) --> VIEW
    dbo_style_group(["dbo.style_group"]) --> VIEW
    dbo_style_size(["dbo.style_size"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.color |
| dbo.dist_sku_scale |
| dbo.distribution |
| dbo.hierarchy_group |
| dbo.size_master |
| dbo.sku |
| dbo.style |
| dbo.style_color |
| dbo.style_group |
| dbo.style_size |

## View Code

```sql
CREATE view dbo.view_dist_sku_scale_o 
as
select distinct  d.distribution_id ,  ds.sku_id, ds.scale_qty,
 h.hierarchy_group_id,h.hierarchy_group_code,
h.hierarchy_group_short_label, h.hierarchy_group_label, s.style_id, s.style_code,c.color_id, c.color_code,
 c.color_long_description ,c.color_short_description , s.long_desc , s.short_desc,  sm.size_code, sm.prim_size_label,
sm.sec_size_label, sm.prim_seq_no, sm.sec_seq_no
from   dist_sku_scale ds
right outer join distribution d
on  ds.distribution_id = d.distribution_id
left JOIN sku sk
on ds.sku_id =sk.sku_id
LEFT JOIN style_color sc
on sk.style_color_id =sc.style_color_id
LEFT JOIN style s
on sk.style_id = s.style_id
LEFT JOIN color c 
on sc.color_id = c.color_id
LEFT JOIN style_size  ss
on sk.style_size_id = ss.style_size_id
LEFT JOIN style_group sg
on s.style_id =sg.style_id
and  sg.main_group_flag =1
LEFT JOIN size_master sm
on ss.size_master_id = sm.size_master_id
LEFT JOIN  hierarchy_group h
on sg.hierarchy_group_id = h.hierarchy_group_id
```

