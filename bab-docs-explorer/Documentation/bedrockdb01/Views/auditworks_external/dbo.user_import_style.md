# dbo.user_import_style

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.user_import_style"]
    dbo_ext_user_import_style(["dbo.ext_user_import_style"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ext_user_import_style |

## View Code

```sql
CREATE VIEW dbo.user_import_style AS
 SELECT entry_type, 
        style_reference_id, 
        style_long_description,
        class_code, 
        cost, 
        subclass_code, 
        import_id, 
        upc_lookup_division,
        style_short_description,
        style_code, 
        tax_item_group_id 
   FROM auditworks_work.dbo.ext_user_import_style
```

