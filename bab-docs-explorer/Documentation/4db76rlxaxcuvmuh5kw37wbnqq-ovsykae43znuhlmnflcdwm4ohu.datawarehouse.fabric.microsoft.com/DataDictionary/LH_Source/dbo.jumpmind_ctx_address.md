# dbo.jumpmind_ctx_address

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| business_unit_id | varchar | 8000 | 0 |  |  |  |
| sequence_number | int | 4 | 0 |  |  |  |
| address_type | varchar | 8000 | 1 |  |  |  |
| attention | varchar | 8000 | 1 |  |  |  |
| line1 | varchar | 8000 | 1 |  |  |  |
| line2 | varchar | 8000 | 1 |  |  |  |
| line3 | varchar | 8000 | 1 |  |  |  |
| line4 | varchar | 8000 | 1 |  |  |  |
| city | varchar | 8000 | 1 |  |  |  |
| state_id | varchar | 8000 | 1 |  |  |  |
| country_id | varchar | 8000 | 1 |  |  |  |
| postal_code | varchar | 8000 | 1 |  |  |  |
| primary_address_flag | smallint | 2 | 1 |  |  |  |
| latitude | varchar | 8000 | 1 |  |  |  |
| longitude | varchar | 8000 | 1 |  |  |  |
| create_time | datetime2 | 8 | 0 |  |  |  |
| create_by | varchar | 8000 | 0 |  |  |  |
| last_update_time | datetime2 | 8 | 1 |  |  |  |
| last_update_by | varchar | 8000 | 0 |  |  |  |
| unit_number | varchar | 8000 | 1 |  |  |  |
| unit_type | varchar | 8000 | 1 |  |  |  |
