# dbo.view_vendor_review_attribute_o

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_vendor_review_attribute_o"]
    dbo_attribute(["dbo.attribute"]) --> VIEW
    dbo_attribute_set(["dbo.attribute_set"]) --> VIEW
    dbo_vendor_review_attr_set(["dbo.vendor_review_attr_set"]) --> VIEW
    dbo_vendor_review_parameter(["dbo.vendor_review_parameter"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.attribute |
| dbo.attribute_set |
| dbo.vendor_review_attr_set |
| dbo.vendor_review_parameter |

## View Code

```sql
create view dbo.view_vendor_review_attribute_o  AS
SELECT g.vendor_review_parameter_id,{fn IFNULL(f.attribute_set_id,-1)}attribute_set_id,f.attribute_set_code, f.attribute_set_label,g.attribute_id,
g.attribute_code,g.attribute_label
FROM
  (  SELECT DISTINCT a.vendor_review_parameter_id,  
                     b.attribute_set_id,
                     b.attribute_set_code, 
                     b.attribute_set_label,   
                     b.attribute_id 
     FROM vendor_review_attr_set e RIGHT JOIN vendor_review_parameter a 
       on a.vendor_review_parameter_id =e.vendor_review_parameter_id
     LEFT JOIN  attribute_set b
       on e.attribute_set_id = b.attribute_set_id ) f  
     RIGHT JOIN
  (  SELECT DISTINCT  
                a.vendor_review_parameter_id, 
                NULL attribute_set_code,
                e.attribute_code,
                e.attribute_label,
                e.attribute_id 
     FROM attribute e ,vendor_review_parameter a
     WHERE e.parent_type=229) g
on  f.vendor_review_parameter_id = g.vendor_review_parameter_id
AND   (f.attribute_id = g.attribute_id
OR     f.attribute_id is NULL)
```

