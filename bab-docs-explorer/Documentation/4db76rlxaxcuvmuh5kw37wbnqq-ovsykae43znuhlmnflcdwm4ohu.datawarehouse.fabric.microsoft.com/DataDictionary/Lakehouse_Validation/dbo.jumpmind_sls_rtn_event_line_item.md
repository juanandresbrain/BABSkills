# dbo.jumpmind_sls_rtn_event_line_item

**Database:** Lakehouse_Validation  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| device_id | varchar | 8000 | 1 |  |  |  |
| business_date | varchar | 8000 | 1 |  |  |  |
| sequence_number | bigint | 8 | 1 |  |  |  |
| line_sequence_number | int | 4 | 1 |  |  |  |
| rtn_event_type_code | varchar | 8000 | 1 |  |  |  |
| rtn_rejection_code | varchar | 8000 | 1 |  |  |  |
| pos_item_id | varchar | 8000 | 1 |  |  |  |
| item_id | varchar | 8000 | 1 |  |  |  |
| entry_mode_code | varchar | 8000 | 1 |  |  |  |
| orig_line_sequence_number | int | 4 | 1 |  |  |  |
| orig_sequence_number | bigint | 8 | 1 |  |  |  |
| orig_business_date | varchar | 8000 | 1 |  |  |  |
| orig_device_id | varchar | 8000 | 1 |  |  |  |
| orig_order_id | varchar | 8000 | 1 |  |  |  |
| rtn_policy_id | varchar | 8000 | 1 |  |  |  |
| voided | int | 4 | 1 |  |  |  |
| override_user_id | varchar | 8000 | 1 |  |  |  |
| entry_method_code | varchar | 8000 | 1 |  |  |  |
| create_time | datetime2 | 8 | 1 |  |  |  |
| create_by | varchar | 8000 | 1 |  |  |  |
| last_update_time | datetime2 | 8 | 1 |  |  |  |
| last_update_by | varchar | 8000 | 1 |  |  |  |
