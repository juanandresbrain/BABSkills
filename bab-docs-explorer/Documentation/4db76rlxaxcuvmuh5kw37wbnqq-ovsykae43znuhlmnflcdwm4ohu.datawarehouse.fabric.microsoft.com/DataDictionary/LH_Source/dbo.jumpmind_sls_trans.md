# dbo.jumpmind_sls_trans

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| device_id | varchar | 8000 | 1 |  |  |  |
| business_date | varchar | 8000 | 1 |  |  |  |
| sequence_number | bigint | 8 | 1 |  |  |  |
| trans_type | varchar | 8000 | 1 |  |  |  |
| trans_status | varchar | 8000 | 1 |  |  |  |
| business_unit_id | varchar | 8000 | 1 |  |  |  |
| username | varchar | 8000 | 1 |  |  |  |
| begin_time | datetime2 | 8 | 1 |  |  |  |
| end_time | datetime2 | 8 | 1 |  |  |  |
| local_offset | int | 4 | 1 |  |  |  |
| client_offset | int | 4 | 1 |  |  |  |
| keyed_offline | int | 4 | 1 |  |  |  |
| override_user_id | varchar | 8000 | 1 |  |  |  |
| barcode | varchar | 8000 | 1 |  |  |  |
| training_mode | int | 4 | 1 |  |  |  |
| session_id | varchar | 8000 | 1 |  |  |  |
| trans_pin | varchar | 8000 | 1 |  |  |  |
| till_id | varchar | 8000 | 1 |  |  |  |
| app_id | varchar | 8000 | 1 |  |  |  |
| app_version | int | 4 | 1 |  |  |  |
| create_time | datetime2 | 8 | 1 |  |  |  |
| create_by | varchar | 8000 | 1 |  |  |  |
| last_update_time | datetime2 | 8 | 1 |  |  |  |
| last_update_by | varchar | 8000 | 1 |  |  |  |
| suspended_trans_data | varchar | 8000 | 1 |  |  |  |
| bank_bag_number | varchar | 8000 | 1 |  |  |  |
