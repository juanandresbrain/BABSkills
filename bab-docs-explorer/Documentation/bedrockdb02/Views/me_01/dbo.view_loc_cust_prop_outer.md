# dbo.view_loc_cust_prop_outer

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_loc_cust_prop_outer"]
    dbo_custom_property(["dbo.custom_property"]) --> VIEW
    dbo_entity_custom_property(["dbo.entity_custom_property"]) --> VIEW
    dbo_location(["dbo.location"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.custom_property |
| dbo.entity_custom_property |
| dbo.location |

## View Code

```sql
create view dbo.view_loc_cust_prop_outer AS
SELECT g.location_id,f.custom_property_value,
{fn IFNULL(g.custom_property_id ,-1)} custom_property_id, g.cust_prop_code, g.cust_prop_label
FROM  (  SELECT DISTINCT a.location_id,  
                         e.custom_property_value,
                         e.custom_property_id
         FROM entity_custom_property  e RIGHT JOIN location a 
         ON a.location_id =e.parent_id 
         LEFT JOIN  custom_property b
         ON e.custom_property_id = b.custom_property_id ) f
         RIGHT JOIN  
      (  SELECT DISTINCT a.location_id, 
                         NULL custom_property_value,
                         e.custom_property_id,
                         e.cust_prop_code,
                         e.cust_prop_label
         FROM custom_property e, location a
         WHERE e.entity_type=2 ) g
ON f.location_id = g.location_id
AND  (f.custom_property_id = g.custom_property_id 
OR    f.custom_property_id is NULL)
```

