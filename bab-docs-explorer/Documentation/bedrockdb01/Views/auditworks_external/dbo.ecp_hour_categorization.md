# dbo.ecp_hour_categorization

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.ecp_hour_categorization"]
    alpha_code_description(["alpha_code_description"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| alpha_code_description |

## View Code

```sql
create view dbo.ecp_hour_categorization
as
  SELECT code_type,
       code,
       code_status,
       code_display_descr1,
       code_display_descr2,
       system_code,
       resource_id,
       active_flag
  FROM alpha_code_description
  where code_type in (27, 28, 29)
        OR (code_type = 0 and code in ('27', '28', '29'))
```

