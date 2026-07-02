# dbo.imat_subledger

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imat_subledger_id | decimal | 9 | 0 | YES |  |  |
| imat_header_id | decimal | 9 | 0 |  |  |  |
| gl_posting_date | smalldatetime | 4 | 0 |  |  |  |
| entry_type | int | 4 | 0 |  |  |  |
| discount_applicability_group | smallint | 2 | 0 |  |  |  |
| gross_amount | decimal | 9 | 0 |  |  |  |
| net_amount | decimal | 9 | 0 |  |  |  |
| gl_effect | int | 4 | 0 |  |  |  |
| posting_status | int | 4 | 0 |  |  |  |
| gl_account_id | decimal | 9 | 0 |  |  |  |
| gl_distribution_type_id | int | 4 | 0 |  |  |  |
| source_gl_account_no | nvarchar | 60 | 0 |  |  |  |
| non_terms_net_amount | decimal | 9 | 0 |  |  |  |
| gross_amount_foreign | decimal | 9 | 0 |  |  |  |
| net_amount_foreign | decimal | 9 | 0 |  |  |  |
| non_terms_net_amount_foreign | decimal | 9 | 0 |  |  |  |
| tax_type_id | smallint | 2 | 1 |  |  |  |
| tax_amount | decimal | 9 | 0 |  |  |  |
| tax_amount_foreign | decimal | 9 | 0 |  |  |  |

