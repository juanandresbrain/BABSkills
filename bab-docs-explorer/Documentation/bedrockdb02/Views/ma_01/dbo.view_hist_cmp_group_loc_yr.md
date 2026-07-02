# dbo.view_hist_cmp_group_loc_yr

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_hist_cmp_group_loc_yr"]
    dbo_hierarchy_group(["dbo.hierarchy_group"]) --> VIEW
    dbo_hist_cmp_group_loc_yr(["dbo.hist_cmp_group_loc_yr"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.hierarchy_group |
| dbo.hist_cmp_group_loc_yr |

## View Code

```sql
create view dbo.view_hist_cmp_group_loc_yr



as
select merch_year, location_id, component_type_code, history_component_id,
sum(component_units)component_units, 
sum(component_retail)component_retail, 
sum(component_cost)component_cost,
sum(component_sellcurr_retail) component_sellcurr_retail,
sum(component_retail_te) component_retail_te,
sum(component_sellcurr_retail_te) component_sellcurr_retail_te,
sum(component_cost_local) component_cost_local
from hist_cmp_group_loc_yr h , hierarchy_group hg
where h.hierarchy_group_id = hg.hierarchy_group_id and
hg.hierarchy_id =1
group by
merch_year,location_id, component_type_code, history_component_id
```

