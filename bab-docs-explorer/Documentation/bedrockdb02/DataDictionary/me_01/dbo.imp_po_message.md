# dbo.imp_po_message

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imp_po_message_id | decimal | 9 | 0 |  |  |  |
| imp_po_id | decimal | 9 | 0 |  |  |  |
| action_type | nchar | 2 | 1 |  |  |  |
| po_no | nvarchar | 40 | 1 |  |  |  |
| message_type | nvarchar | 40 | 1 |  |  |  |
| message | nvarchar | 510 | 0 |  |  |  |
| parent_type | smallint | 2 | 0 |  |  |  |
| parent_document_no | smallint | 2 | 1 |  |  |  |

