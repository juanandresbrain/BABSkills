# dbo.sv_user_department

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.sv_user_department"]
    dept_sa(["dept_sa"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dept_sa |

## View Code

```sql
create view dbo.sv_user_department

as
SELECT department_code, department_description FROM dept_sa
```

