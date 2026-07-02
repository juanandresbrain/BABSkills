# dbo.view_style_attribute_wl

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_style_attribute_wl"]
    dbo_attribute(["dbo.attribute"]) --> VIEW
    dbo_attribute_set(["dbo.attribute_set"]) --> VIEW
    dbo_entity_attribute_set(["dbo.entity_attribute_set"]) --> VIEW
    dbo_style(["dbo.style"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.attribute |
| dbo.attribute_set |
| dbo.entity_attribute_set |
| dbo.style |

## View Code

```sql
create view dbo.view_style_attribute_wl 
AS
SELECT 	DISTINCT
	s.style_id,
	eas.attribute_set_id,
	eas.attribute_id,
	a.attribute_code, 
	a.attribute_label,
	ats.attribute_set_code,
	ats.attribute_set_label
FROM	style s
LEFT OUTER JOIN entity_attribute_set eas ON (s.style_id = eas.parent_id AND eas.parent_type = 1)
LEFT OUTER JOIN attribute a ON (eas.attribute_id = a.attribute_id)
LEFT OUTER JOIN attribute_set ats ON (eas.attribute_set_id = ats.attribute_set_id)
```

