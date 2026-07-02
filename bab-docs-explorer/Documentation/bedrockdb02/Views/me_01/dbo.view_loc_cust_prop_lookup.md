# dbo.view_loc_cust_prop_lookup

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_loc_cust_prop_lookup"]
    dbo_custom_property(["dbo.custom_property"]) --> VIEW
    dbo_entity_custom_property(["dbo.entity_custom_property"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.custom_property |
| dbo.entity_custom_property |

## View Code

```sql
create view dbo.view_loc_cust_prop_lookup as
select distinct a.custom_property_id, a.cust_prop_code , 
a.cust_prop_label, a.entity_type , b.custom_property_value
from custom_property a, entity_custom_property b 
where a.entity_type =2
and a.custom_property_id = b.custom_property_id
```

