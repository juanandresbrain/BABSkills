# dbo.imat_tax

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imat_tax_id | decimal | 9 | 0 | YES |  |  |
| imat_header_id | decimal | 9 | 0 |  |  |  |
| parent_id | decimal | 9 | 0 |  |  |  |
| parent_type | tinyint | 1 | 0 |  |  |  |
| tax_type_id | smallint | 2 | 1 |  |  |  |
| tax_rate_id | smallint | 2 | 1 |  |  |  |
| surtax_type_id | smallint | 2 | 1 |  |  |  |
| surtax_rate_id | smallint | 2 | 1 |  |  |  |
| tax_rate | decimal | 5 | 0 |  |  |  |
| taxable_amount | decimal | 9 | 0 |  |  |  |
| tax_amount | decimal | 9 | 0 |  |  |  |

