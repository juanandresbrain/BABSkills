# dbo.awt_user_import_class_vw

**Database:** auditworks_work  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.awt_user_import_class_vw"]
    awt_user_import_class(["awt_user_import_class"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| awt_user_import_class |

## View Code

```sql
create view dbo.awt_user_import_class_vw
  (import_id, entry_type, class_code, class_description ,department_code)
as select import_id, entry_type, class_code, class_description ,department_code
from awt_user_import_class
```

