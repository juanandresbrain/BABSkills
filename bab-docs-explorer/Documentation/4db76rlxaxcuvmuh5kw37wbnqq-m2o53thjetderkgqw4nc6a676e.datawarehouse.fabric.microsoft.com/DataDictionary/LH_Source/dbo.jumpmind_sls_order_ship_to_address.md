# dbo.jumpmind_sls_order_ship_to_address

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| order_id | varchar | 8000 | 1 |  |  |  |
| sequence_number | int | 4 | 1 |  |  |  |
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
| primary_address_flag | int | 4 | 1 |  |  |  |
| latitude | varchar | 8000 | 1 |  |  |  |
| longitude | varchar | 8000 | 1 |  |  |  |
| create_time | datetime2 | 8 | 1 |  |  |  |
| create_by | varchar | 8000 | 1 |  |  |  |
| last_update_time | datetime2 | 8 | 1 |  |  |  |
| last_update_by | varchar | 8000 | 1 |  |  |  |
| first_name | varchar | 8000 | 1 |  |  |  |
| last_name | varchar | 8000 | 1 |  |  |  |
| phone | varchar | 8000 | 1 |  |  |  |
| email | varchar | 8000 | 1 |  |  |  |
| suggestion_accepted_flag | int | 4 | 1 |  |  |  |
| unit_number | varchar | 8000 | 1 |  |  |  |
| unit_type | varchar | 8000 | 1 |  |  |  |
