# dbo.jumpmind_sls_order_price_mod

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| order_id | varchar | 8000 | 1 |  |  |  |
| line_sequence_number | int | 4 | 1 |  |  |  |
| mod_line_sequence_number | int | 4 | 1 |  |  |  |
| username | varchar | 8000 | 1 |  |  |  |
| reason_code | varchar | 8000 | 1 |  |  |  |
| mod_by_percentage | decimal | 17 | 1 |  |  |  |
| mod_by_amount | decimal | 17 | 1 |  |  |  |
| rounding_amount | decimal | 17 | 1 |  |  |  |
| calc_method | varchar | 8000 | 1 |  |  |  |
| iso_currency_code | varchar | 8000 | 1 |  |  |  |
| price_mod_type_code | varchar | 8000 | 1 |  |  |  |
| price_mod_source_type_code | varchar | 8000 | 1 |  |  |  |
| voided | int | 4 | 1 |  |  |  |
| create_time | datetime2 | 8 | 1 |  |  |  |
| create_by | varchar | 8000 | 1 |  |  |  |
| last_update_time | datetime2 | 8 | 1 |  |  |  |
| last_update_by | varchar | 8000 | 1 |  |  |  |
