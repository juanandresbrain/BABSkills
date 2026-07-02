# dbo.import_invoice_message

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| import_invoice_message_id | decimal | 9 | 0 | YES |  |  |
| import_invoice_header_id | decimal | 9 | 0 | YES |  |  |
| action_code | nchar | 2 | 0 |  |  |  |
| message_type | nvarchar | 40 | 0 |  |  |  |
| message | nvarchar | 510 | 0 |  |  |  |
| invoice_no | nvarchar | 44 | 0 |  |  |  |

