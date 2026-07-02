# dbo.view_po_message_o

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_po_message_o"]
    dbo_message_type(["dbo.message_type"]) --> VIEW
    dbo_po(["dbo.po"]) --> VIEW
    dbo_po_message(["dbo.po_message"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.message_type |
| dbo.po |
| dbo.po_message |

## View Code

```sql
create view dbo.view_po_message_o 
AS
SELECT	DISTINCT
		po.po_id,
		pm.message_type_id,
		pm.message AS po_msg,
		mt.message_type_description AS po_msg_type
FROM	po
		LEFT OUTER JOIN po_message pm 
		ON (po.po_id = pm.po_id)
		LEFT OUTER JOIN message_type mt 
		ON (pm.message_type_id = mt.message_type_id)
```

