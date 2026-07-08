# dbo.sv_deposit_category

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.sv_deposit_category"]
    code_description(["code_description"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| code_description |

## View Code

```sql
create view dbo.sv_deposit_category

AS


SELECT code, code_display_descr FROM code_description
WHERE code_type = 16
```

