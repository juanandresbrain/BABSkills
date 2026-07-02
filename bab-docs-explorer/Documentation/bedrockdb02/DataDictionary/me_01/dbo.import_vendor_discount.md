# dbo.import_vendor_discount

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| import_vendor_discount_id | decimal | 9 | 0 | YES |  |  |
| entity_type | nvarchar | 4 | 0 |  |  |  |
| action_type | nchar | 2 | 0 |  |  |  |
| vendor_code | nvarchar | 40 | 0 |  |  |  |
| discount_code | nvarchar | 16 | 0 |  |  |  |
| use_percent_for_discount_flag | nchar | 2 | 1 |  |  |  |
| base_calculation_on | smallint | 2 | 1 |  |  |  |
| reflect_discount_in_cost_flag | nchar | 2 | 1 |  |  |  |
| discount_value | decimal | 9 | 1 |  |  |  |
| import_replication_queue_id | decimal | 9 | 1 |  |  |  |
| gl_account_no | nvarchar | 60 | 1 |  |  |  |
| subject_to_terms_flag | nchar | 2 | 1 |  |  |  |

