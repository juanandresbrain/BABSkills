# dbo.import_invoice_ref

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| import_invoice_ref_id | decimal | 9 | 0 | YES |  |  |
| import_invoice_header_id | decimal | 9 | 0 | YES |  |  |
| action_code | nchar | 2 | 0 |  |  |  |
| reference_type | tinyint | 1 | 0 |  |  |  |
| reference_number | nvarchar | 40 | 0 |  |  |  |
| location_code | nvarchar | 40 | 1 |  |  |  |
| invoice_no | nvarchar | 44 | 0 |  |  |  |

