# dbo.awt_user_import_upc_vw

**Database:** auditworks_work  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.awt_user_import_upc_vw"]
    awt_user_import_upc(["awt_user_import_upc"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| awt_user_import_upc |

## View Code

```sql
create view dbo.awt_user_import_upc_vw 
       (entry_type, upc_no, sku_id, pos_identifier, 
       pos_identifier_type, style_reference_id, import_id)
AS
SELECT entry_type, upc_no, sku_id, pos_identifier, 
       pos_identifier_type, style_reference_id, import_id
FROM awt_user_import_upc
```

