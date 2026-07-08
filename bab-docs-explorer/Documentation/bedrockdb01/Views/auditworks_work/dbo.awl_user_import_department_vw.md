# dbo.awl_user_import_department_vw

**Database:** auditworks_work  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.awl_user_import_department_vw"]
    awl_user_import_department(["awl_user_import_department"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| awl_user_import_department |

## View Code

```sql
create view dbo.awl_user_import_department_vw 
    (entry_type, department_code, department_description, import_id)
AS SELECT entry_type, department_code, department_description, import_id
FROM awl_user_import_department
```

