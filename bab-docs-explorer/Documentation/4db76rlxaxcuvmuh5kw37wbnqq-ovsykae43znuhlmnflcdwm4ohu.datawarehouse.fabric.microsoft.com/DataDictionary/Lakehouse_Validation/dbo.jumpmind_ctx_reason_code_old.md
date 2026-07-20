# dbo.jumpmind_ctx_reason_code_old

**Database:** Lakehouse_Validation  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| reason_code_group_id | varchar | 8000 | 0 |  |  |  |
| reason_code_id | varchar | 8000 | 0 |  |  |  |
| display_value | varchar | 8000 | 1 |  |  |  |
| display_order | int | 4 | 1 |  |  |  |
| display_default | smallint | 2 | 1 |  |  |  |
| disposition_group_id | varchar | 8000 | 1 |  |  |  |
| create_time | datetime2 | 8 | 0 |  |  |  |
| create_by | varchar | 8000 | 0 |  |  |  |
| last_update_time | datetime2 | 8 | 1 |  |  |  |
| last_update_by | varchar | 8000 | 0 |  |  |  |
| tag_country | varchar | 8000 | 0 |  |  |  |
| tag_state | varchar | 8000 | 0 |  |  |  |
| tag_store_number | varchar | 8000 | 0 |  |  |  |
| tag_store_type | varchar | 8000 | 0 |  |  |  |
| tag_device_type | varchar | 8000 | 0 |  |  |  |
| tag_app_id | varchar | 8000 | 0 |  |  |  |
| tag_business_unit_id | varchar | 8000 | 0 |  |  |  |
| tag_brand | varchar | 8000 | 0 |  |  |  |
| tag_device_id | varchar | 8000 | 0 |  |  |  |
