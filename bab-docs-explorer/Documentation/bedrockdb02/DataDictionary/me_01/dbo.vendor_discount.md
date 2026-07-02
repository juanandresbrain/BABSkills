# dbo.vendor_discount

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| vendor_discount_id | decimal | 9 | 0 | YES |  |  |
| vendor_id | decimal | 9 | 0 |  |  |  |
| discount_id | smallint | 2 | 0 |  |  |  |
| bookmark | nvarchar | 20 | 0 |  |  |  |
| leading_key | nvarchar | 20 | 1 |  |  |  |
| use_percent_for_discount_flag | bit | 1 | 0 |  |  |  |
| base_calculation_on | smallint | 2 | 1 |  |  |  |
| reflect_discount_in_cost_flag | bit | 1 | 0 |  |  |  |
| discount_value | decimal | 9 | 0 |  |  |  |
| subject_to_terms_flag | bit | 1 | 0 |  |  |  |
| gl_account_id | decimal | 9 | 1 |  |  |  |

