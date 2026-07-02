# dbo.import_po_receipt_msg

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| import_po_receipt_msg_id | decimal | 9 | 0 | YES |  |  |
| import_po_receipt_id | decimal | 9 | 0 |  |  |  |
| action | nvarchar | 2 | 0 |  |  |  |
| message_type_description | nvarchar | 40 | 0 |  |  |  |
| message_text | nvarchar | 510 | 0 |  |  |  |

