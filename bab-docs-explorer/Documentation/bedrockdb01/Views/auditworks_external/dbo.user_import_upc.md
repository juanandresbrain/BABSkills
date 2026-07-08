# dbo.user_import_upc

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.user_import_upc"]
    dbo_ext_user_import_upc(["dbo.ext_user_import_upc"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ext_user_import_upc |

## View Code

```sql
CREATE VIEW dbo.user_import_upc AS
 SELECT entry_type, 
   	upc_no, 
   	sku_id, 
   	pos_identifier, 
       	pos_identifier_type, 
       	style_reference_id, 
       	import_id, 
       	upc_lookup_division,
       	color_code, 
       	color_short_description, 
       	prim_size_label, 
       	sec_size_label,
        size_master_id, 
        tax_item_group_id 
   FROM auditworks_work.dbo.ext_user_import_upc
```

