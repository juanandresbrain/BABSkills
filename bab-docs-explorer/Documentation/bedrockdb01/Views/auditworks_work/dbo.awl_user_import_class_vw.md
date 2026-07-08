# dbo.awl_user_import_class_vw

**Database:** auditworks_work  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.awl_user_import_class_vw"]
    awl_user_import_class(["awl_user_import_class"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| awl_user_import_class |

## View Code

```sql
create view dbo.awl_user_import_class_vw
  (import_id, entry_type, class_code, class_description ,department_code)
as select import_id, entry_type, class_code, class_description ,department_code
from awl_user_import_class
```

