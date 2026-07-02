# dbo.view_style_cust_prop_list_cs

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_style_cust_prop_list_cs"]
    dbo_custom_property(["dbo.custom_property"]) --> VIEW
    dbo_view_entity_custm_property_cs(["dbo.view_entity_custm_property_cs"]) --> VIEW
    dbo_view_style_cs(["dbo.view_style_cs"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.custom_property |
| dbo.view_entity_custm_property_cs |
| dbo.view_style_cs |

## View Code

```sql
create view dbo.view_style_cust_prop_list_cs AS
SELECT DISTINCT
  a.style_id,  
  e.custom_property_value,   
  e.custom_property_id, 
  b.cust_prop_code,
  b.cust_prop_label
FROM view_entity_custm_property_cs e
RIGHT OUTER JOIN view_style_cs a ON a.style_id =e.parent_id and e.parent_type =1
LEFT  OUTER JOIN custom_property b ON e.custom_property_id = b.custom_property_id
```

