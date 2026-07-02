# dbo.view_oo_all_group_loc_pd

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_oo_all_group_loc_pd"]
    dbo_hierarchy_group(["dbo.hierarchy_group"]) --> VIEW
    dbo_oo_all_group_loc_pd(["dbo.oo_all_group_loc_pd"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.hierarchy_group |
| dbo.oo_all_group_loc_pd |

## View Code

```sql
create view dbo.view_oo_all_group_loc_pd

as
   select  merch_year_pd, location_id,
   sum(on_order_units) on_order_units, 
   sum(on_order_retail) on_order_retail, 
   sum(on_order_cost) on_order_cost,
   sum(allocation_units) allocation_units,
   sum(on_order_retail_local) on_order_retail_local,
   sum(on_order_retail_te_local) on_order_retail_te_local,
   sum(on_order_cost_local) on_order_cost_local
   from oo_all_group_loc_pd h , hierarchy_group hg
   where h.hierarchy_group_id = hg.hierarchy_group_id and
   hg.hierarchy_id =1
   group by merch_year_pd, location_id
```

