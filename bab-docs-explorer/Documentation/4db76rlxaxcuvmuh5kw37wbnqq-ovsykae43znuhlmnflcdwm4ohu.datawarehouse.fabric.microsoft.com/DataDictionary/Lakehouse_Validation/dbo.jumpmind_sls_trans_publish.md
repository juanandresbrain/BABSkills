# dbo.jumpmind_sls_trans_publish

**Database:** Lakehouse_Validation  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| device_id | varchar | 8000 | 1 |  |  |  |
| business_date | varchar | 8000 | 1 |  |  |  |
| sequence_number | bigint | 8 | 1 |  |  |  |
| order_id | varchar | 8000 | 1 |  |  |  |
| message_type_code | varchar | 8000 | 1 |  |  |  |
| trans_type | varchar | 8000 | 1 |  |  |  |
| trans_status | varchar | 8000 | 1 |  |  |  |
| business_unit_id | varchar | 8000 | 1 |  |  |  |
| app_version | int | 4 | 1 |  |  |  |
| create_time | datetime2 | 8 | 1 |  |  |  |
| create_by | varchar | 8000 | 1 |  |  |  |
| last_update_time | datetime2 | 8 | 1 |  |  |  |
| last_update_by | varchar | 8000 | 1 |  |  |  |
| timezone_offset | varchar | 8000 | 1 |  |  |  |
