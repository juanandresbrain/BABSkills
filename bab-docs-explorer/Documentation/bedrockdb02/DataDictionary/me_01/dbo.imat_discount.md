# dbo.imat_discount

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| imat_discount_id | decimal | 9 | 0 | YES |  |  |
| imat_header_id | decimal | 9 | 0 |  |  |  |
| discount_applicability_group | int | 4 | 0 |  |  |  |
| item_specific_discount_flag | bit | 1 | 0 |  |  |  |
| sequence_number | int | 4 | 0 |  |  |  |
| calculation_method | tinyint | 1 | 0 |  |  |  |
| discount_value | decimal | 9 | 0 |  |  |  |
| base_calculation_on | tinyint | 1 | 0 |  |  |  |
| reflect_in_discount_cost_flag | bit | 1 | 0 |  |  |  |
| reflect_in_net_cost_flag | bit | 1 | 0 |  |  |  |
| subject_to_terms_flag | bit | 1 | 0 |  |  |  |
| discount_id | smallint | 2 | 0 |  |  |  |

