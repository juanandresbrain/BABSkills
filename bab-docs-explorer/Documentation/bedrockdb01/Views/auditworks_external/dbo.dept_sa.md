# dbo.dept_sa

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.dept_sa"]
    user_department(["user_department"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| user_department |

## View Code

```sql
create view dbo.dept_sa AS
    SELECT upc_lookup_division, department_code, department_description, resource_id
FROM user_department
```

