# dbo.awt_user_import_style_vw

**Database:** auditworks_work  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.awt_user_import_style_vw"]
    awt_user_import_style(["awt_user_import_style"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| awt_user_import_style |

## View Code

```sql
create view dbo.awt_user_import_style_vw
      (entry_type, style_reference_id, style_long_description,
       class_code, cost, subclass_code, import_id)
AS SELECT entry_type, style_reference_id, style_long_description,
         class_code, cost, subclass_code, import_id
FROM awt_user_import_style
```

