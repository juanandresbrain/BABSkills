# dbo.jumpmind_sls_order_promo_code_line_item

**Database:** Lakehouse_Validation  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| order_id | varchar | 8000 | 1 |  |  |  |
| line_sequence_number | int | 4 | 1 |  |  |  |
| voided | int | 4 | 1 |  |  |  |
| override_user_id | varchar | 8000 | 1 |  |  |  |
| entry_method_code | varchar | 8000 | 1 |  |  |  |
| reward_promo_code_id | varchar | 8000 | 1 |  |  |  |
| promo_code_id | varchar | 8000 | 1 |  |  |  |
| loyalty_number | varchar | 8000 | 1 |  |  |  |
| loyalty_promotion_flag | int | 4 | 1 |  |  |  |
| origin_promotion_id | varchar | 8000 | 1 |  |  |  |
| reward_promotion_id | varchar | 8000 | 1 |  |  |  |
| code | varchar | 8000 | 1 |  |  |  |
| description | varchar | 8000 | 1 |  |  |  |
| event_type_code | varchar | 8000 | 1 |  |  |  |
| effective_start_time | datetime2 | 8 | 1 |  |  |  |
| effective_end_time | datetime2 | 8 | 1 |  |  |  |
| print_on_receipt_flag | int | 4 | 1 |  |  |  |
| create_time | datetime2 | 8 | 1 |  |  |  |
| create_by | varchar | 8000 | 1 |  |  |  |
| last_update_time | datetime2 | 8 | 1 |  |  |  |
| last_update_by | varchar | 8000 | 1 |  |  |  |
