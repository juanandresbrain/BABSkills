# dbo.import_invoice_charges

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| import_invoice_charges_id | decimal | 9 | 0 | YES |  |  |
| import_invoice_header_id | decimal | 9 | 0 |  |  |  |
| action_code | nchar | 2 | 0 |  |  |  |
| gl_distribution_type | smallint | 2 | 0 |  |  |  |
| charge_code | nvarchar | 30 | 1 |  |  |  |
| discount_applicability_group | int | 4 | 0 |  |  |  |
| gross_amount_foreign | decimal | 9 | 1 |  |  |  |
| net_amount_foreign | decimal | 9 | 1 |  |  |  |
| invoice_no | nvarchar | 44 | 0 |  |  |  |
| tax_type_code | nvarchar | 10 | 1 |  |  |  |

