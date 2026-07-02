# dbo.import_invoice_discount

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| import_invoice_discount_id | decimal | 9 | 0 | YES |  |  |
| import_invoice_header_id | decimal | 9 | 0 | YES |  |  |
| action_code | nchar | 2 | 0 |  |  |  |
| discount_applicability_group | int | 4 | 0 |  |  |  |
| sequence_number | int | 4 | 0 |  |  |  |
| discount_type | nvarchar | 40 | 0 |  |  |  |
| amount_type | tinyint | 1 | 0 |  |  |  |
| value_amount | decimal | 9 | 1 |  |  |  |
| value_percent | decimal | 5 | 1 |  |  |  |
| base_calculation_on | tinyint | 1 | 0 |  |  |  |
| reflect_in_discount_cost_flag | nchar | 2 | 0 |  |  |  |
| reflect_in_net_cost_flag | nchar | 2 | 0 |  |  |  |
| subject_to_terms_flag | nchar | 2 | 0 |  |  |  |
| invoice_no | nvarchar | 44 | 0 |  |  |  |

