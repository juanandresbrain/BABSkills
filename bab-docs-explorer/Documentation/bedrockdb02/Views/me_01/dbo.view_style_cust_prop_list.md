# dbo.view_style_cust_prop_list

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_style_cust_prop_list"]
    dbo_custom_property(["dbo.custom_property"]) --> VIEW
    dbo_entity_custom_property(["dbo.entity_custom_property"]) --> VIEW
    dbo_style(["dbo.style"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.custom_property |
| dbo.entity_custom_property |
| dbo.style |

## View Code

```sql
create view dbo.view_style_cust_prop_list AS
SELECT DISTINCT
  a.style_id,  
  e.custom_property_value,   
  e.custom_property_id, 
  b.cust_prop_code,
  b.cust_prop_label
FROM entity_custom_property e
RIGHT OUTER JOIN style a 
ON a.style_id =e.parent_id and e.parent_type =1
LEFT  OUTER JOIN custom_property b 
ON e.custom_property_id = b.custom_property_id
```

