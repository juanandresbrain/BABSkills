# dbo.sv_style_class

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.sv_style_class"]
    class_sa(["class_sa"]) --> VIEW
    style_sa(["style_sa"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| class_sa |
| style_sa |

## View Code

```sql
create view dbo.sv_style_class
as
select s.style_reference_id, s.style_long_description, s.class_code,
       c.class_description
from  style_sa s, class_sa c
where s.class_code = c.class_code
```

