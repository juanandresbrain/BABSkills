# dbo.view_style_attribute_outer

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_style_attribute_outer"]
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
create view dbo.view_style_attribute_outer AS
SELECT g.style_id,{fn IFNULL(f.attribute_set_id,-1)}attribute_set_id,
f.attribute_set_code, f.attribute_set_label,g.attribute_id, g.attribute_code, g.attribute_label
FROM
  (  SELECT DISTINCT a.style_id,  
                     b.attribute_set_id,
                     b.attribute_set_code, 
                     b.attribute_set_label,   
                     e.attribute_id 
     FROM entity_attribute_set e RIGHT JOIN style a 
       on a.style_id =e.parent_id and e.parent_type =1
     LEFT JOIN  attribute_set b
       on e.attribute_set_id = b.attribute_set_id ) f  
     RIGHT JOIN
  (  SELECT DISTINCT  
                a.style_id, 
                NULL attribute_set_code,
                e.attribute_id,
                e.attribute_code,
                e.attribute_label 
     FROM attribute e ,style a
     WHERE e.parent_type=1) g
on  f.style_id = g.style_id
AND   (f.attribute_id = g.attribute_id
OR     f.attribute_id is NULL)
```

