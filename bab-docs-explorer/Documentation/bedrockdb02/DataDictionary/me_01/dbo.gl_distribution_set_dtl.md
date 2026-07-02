# dbo.gl_distribution_set_dtl

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| gl_distribution_set_dtl_id | int | 4 | 0 | YES |  |  |
| gl_distribution_set_id | int | 4 | 0 |  |  |  |
| gl_distribution_type_id | int | 4 | 0 |  |  |  |
| gl_account_id | decimal | 9 | 0 |  |  |  |
| discount_applicability_group | smallint | 2 | 0 |  |  |  |
| gl_effect | smallint | 2 | 0 |  |  |  |
| store_allocation_method | smallint | 2 | 0 |  |  |  |
| style_allocation_method | smallint | 2 | 0 |  |  |  |
| tax_type_id | smallint | 2 | 1 |  |  |  |

