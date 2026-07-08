# dbo.sv_user_department

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.sv_user_department"]
    lg_dept_sa(["lg_dept_sa"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| lg_dept_sa |

## View Code

```sql
create view dbo.sv_user_department

as
SELECT department_code, department_description FROM lg_dept_sa
```

