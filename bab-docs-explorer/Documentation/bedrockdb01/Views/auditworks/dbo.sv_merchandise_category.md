# dbo.sv_merchandise_category

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.sv_merchandise_category"]
    code_description(["code_description"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| code_description |

## View Code

```sql
create view dbo.sv_merchandise_category
as

SELECT code, code_display_descr FROM code_description
WHERE code_type = 24
```

