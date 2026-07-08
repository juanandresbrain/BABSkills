# dbo.user_import_style

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.user_import_style"]
    awl_user_import_style(["awl_user_import_style"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| awl_user_import_style |

## View Code

```sql
create view dbo.user_import_style (entry_type, style_reference_id, style_long_description,
         class_code, cost, subclass_code, import_id, upc_lookup_division, style_short_description,
         style_code, tax_item_group_id)
AS SELECT entry_type, style_reference_id, style_long_description,
         class_code, cost, subclass_code, import_id, upc_lookup_division,style_short_description,
         style_code, tax_item_group_id 
FROM auditworks_work..awl_user_import_style
```

