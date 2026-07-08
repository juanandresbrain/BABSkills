# dbo.user_import_class

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.user_import_class"]
    dbo_ext_user_import_class(["dbo.ext_user_import_class"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ext_user_import_class |

## View Code

```sql
CREATE VIEW dbo.user_import_class AS
 SELECT import_id, 
        entry_type, 
        class_code, 
        class_description,
        department_code,
        upc_lookup_division, 
        class_short_description, 
        tax_item_group_id 
   FROM auditworks_work.dbo.ext_user_import_class
```

