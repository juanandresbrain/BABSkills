# dbo.sv_customer_role

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.sv_customer_role"]
    code_description(["code_description"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| code_description |

## View Code

```sql
create view dbo.sv_customer_role

AS
select customer_role = code, customer_role_descr = code_display_descr
from code_description
where code_type = 7
```

