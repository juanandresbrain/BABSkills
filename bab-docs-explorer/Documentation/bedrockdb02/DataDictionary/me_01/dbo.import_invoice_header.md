# dbo.import_invoice_header

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| import_invoice_header_id | decimal | 9 | 0 | YES |  |  |
| action_code | nchar | 2 | 0 |  |  |  |
| vendor_code | nvarchar | 40 | 0 |  |  |  |
| transaction_type | tinyint | 1 | 0 |  |  |  |
| ref_invoice_no | nvarchar | 44 | 1 |  |  |  |
| payment_status_code | tinyint | 1 | 1 |  |  |  |
| invoice_date | smalldatetime | 4 | 0 |  |  |  |
| terms | nvarchar | 30 | 1 |  |  |  |
| due_date | smalldatetime | 4 | 1 |  |  |  |
| discount_date | smalldatetime | 4 | 1 |  |  |  |
| exchange_rate | float | 8 | 1 |  |  |  |
| currency | nvarchar | 6 | 1 |  |  |  |
| remit_to_vendor | nvarchar | 40 | 1 |  |  |  |
| payment_reference_number | nvarchar | 60 | 1 |  |  |  |
| invoice_no | nvarchar | 44 | 0 |  |  |  |

