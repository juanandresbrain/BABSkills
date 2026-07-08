# dbo.sv_store_closed_reason

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.sv_store_closed_reason"]
    code_description(["code_description"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| code_description |

## View Code

```sql
create view dbo.sv_store_closed_reason

AS

SELECT code, code_display_descr FROM code_description
WHERE code_type = 32
```

