# dbo.view_style_custom_property

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_style_custom_property"]
    dbo_entity_custom_property(["dbo.entity_custom_property"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.entity_custom_property |

## View Code

```sql
create view dbo.view_style_custom_property as
select
	entity_custom_property_id,
	custom_property_id,
	parent_type,
	parent_id,
	custom_property_value ,
	binary_checksum (custom_property_value) custom_property_value_id
from entity_custom_property
where parent_type=1
```

