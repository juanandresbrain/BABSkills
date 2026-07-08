# dbo.ecp_commission_code

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.ecp_commission_code"]
    alpha_code_description(["alpha_code_description"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| alpha_code_description |

## View Code

```sql
create view dbo.ecp_commission_code
as
  SELECT *
  FROM alpha_code_description
  where code_type in (11, 13, 14, 15)
        OR (code_type = 0 and code in ('11', '13', '14', '15'))
```

