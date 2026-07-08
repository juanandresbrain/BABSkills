# dbo.sv_glc_desc

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.sv_glc_desc"]
    code_description(["code_description"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| code_description |

## View Code

```sql
create view dbo.sv_glc_desc
as
select glc_type = code,  glc_desc=code_display_descr
from code_description
where code_type = 33
```

