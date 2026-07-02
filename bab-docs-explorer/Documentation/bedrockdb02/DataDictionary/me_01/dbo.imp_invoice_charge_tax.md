# dbo.imp_invoice_charge_tax

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imp_invoice_charge_tax_id | decimal | 9 | 0 | YES |  |  |
| import_invoice_header_id | decimal | 9 | 0 |  |  |  |
| import_invoice_charges_id | decimal | 9 | 0 |  |  |  |
| action_code | nvarchar | 2 | 0 |  |  |  |
| invoice_no | nvarchar | 44 | 0 |  |  |  |
| gl_distribution_type | smallint | 2 | 0 |  |  |  |
| charge_code | nvarchar | 30 | 1 |  |  |  |
| tax_type_code | nvarchar | 10 | 0 |  |  |  |
| tax_rate_code | nvarchar | 12 | 0 |  |  |  |

