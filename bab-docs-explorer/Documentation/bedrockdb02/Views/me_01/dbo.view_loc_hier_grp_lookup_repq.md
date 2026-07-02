# dbo.view_loc_hier_grp_lookup_repq

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_loc_hier_grp_lookup_repq"]
    dbo_hierarchy(["dbo.hierarchy"]) --> VIEW
    dbo_hierarchy_group(["dbo.hierarchy_group"]) --> VIEW
    dbo_hierarchy_level(["dbo.hierarchy_level"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.hierarchy |
| dbo.hierarchy_group |
| dbo.hierarchy_level |

## View Code

```sql
create view dbo.view_loc_hier_grp_lookup_repq 







AS
SELECT hierarchy_level_label + N' - ' + hierarchy_group_label 'hierarchy_group_label', hierarchy_group_code
FROM hierarchy h
INNER JOIN hierarchy_level hl ON (h.hierarchy_id = hl.hierarchy_id)
INNER JOIN hierarchy_group hg ON (hg.hierarchy_id = h.hierarchy_id AND hg.hierarchy_level_id = hl.hierarchy_level_id)
WHERE h.hierarchy_type = 2
AND h.alternate_flag = 0
AND h.active_flag = 1
AND hg.active_flag = 1
GROUP BY hierarchy_level_label, hierarchy_group_label, hierarchy_group_code
```

