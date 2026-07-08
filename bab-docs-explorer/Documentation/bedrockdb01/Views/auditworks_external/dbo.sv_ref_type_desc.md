# dbo.sv_ref_type_desc

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.sv_ref_type_desc"]
    code_description(["code_description"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| code_description |

## View Code

```sql
create view dbo.sv_ref_type_desc
as
select reference_type=code, ref_type_desc=code_display_descr
from code_description
where code_type=22
```

