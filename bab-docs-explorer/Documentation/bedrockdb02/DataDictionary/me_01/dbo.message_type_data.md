# dbo.message_type_data

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| message_type_id | decimal | 9 | 0 | YES |  |  |
| message_type_description | nvarchar | 40 | 0 |  |  |  |
| exclusive_flag | bit | 1 | 0 |  |  |  |
| max_length | smallint | 2 | 0 |  |  |  |
| transaction_type | smallint | 2 | 1 |  |  |  |
| edi_support_flag | bit | 1 | 0 |  |  |  |
| print_message_for_vendor_flag | bit | 1 | 0 |  |  |  |
| print_on_po_receipt_flag | bit | 1 | 0 |  |  |  |
| user_defined_flag | bit | 1 | 0 |  |  |  |
| active_flag | bit | 1 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |

