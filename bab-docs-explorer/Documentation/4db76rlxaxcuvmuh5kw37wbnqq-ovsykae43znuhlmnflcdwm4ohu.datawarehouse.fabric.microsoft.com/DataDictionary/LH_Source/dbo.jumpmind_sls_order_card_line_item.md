# dbo.jumpmind_sls_order_card_line_item

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| order_id | varchar | 8000 | 1 |  |  |  |
| line_sequence_number | int | 4 | 1 |  |  |  |
| brand | varchar | 8000 | 1 |  |  |  |
| card_name | varchar | 8000 | 1 |  |  |  |
| code | varchar | 8000 | 1 |  |  |  |
| type_code | varchar | 8000 | 1 |  |  |  |
| payment_provider_code | varchar | 8000 | 1 |  |  |  |
| masked_card_number | varchar | 8000 | 1 |  |  |  |
| entry_mode | varchar | 8000 | 1 |  |  |  |
| service_code | varchar | 8000 | 1 |  |  |  |
| expiration_date | varchar | 8000 | 1 |  |  |  |
| card_number | varchar | 8000 | 1 |  |  |  |
| gift_card_action_code | varchar | 8000 | 1 |  |  |  |
| ref_line_sequence_number | int | 4 | 1 |  |  |  |
| create_time | datetime2 | 8 | 1 |  |  |  |
| create_by | varchar | 8000 | 1 |  |  |  |
| last_update_time | datetime2 | 8 | 1 |  |  |  |
| last_update_by | varchar | 8000 | 1 |  |  |  |
