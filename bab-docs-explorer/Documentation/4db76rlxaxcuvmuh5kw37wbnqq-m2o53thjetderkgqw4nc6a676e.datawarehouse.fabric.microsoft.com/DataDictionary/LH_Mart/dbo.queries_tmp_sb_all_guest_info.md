# dbo.queries_tmp_sb_all_guest_info

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| customer_no | decimal | 13 | 1 |  |  |  |
| customer_id | int | 4 | 1 |  |  |  |
| address_id | int | 4 | 1 |  |  |  |
| country_code | varchar | 8000 | 1 |  |  |  |
| address_match_key | varchar | 8000 | 1 |  |  |  |
| address_type_code | varchar | 8000 | 1 |  |  |  |
| mail_indicator | int | 4 | 1 |  |  |  |
| carrier_route | varchar | 8000 | 1 |  |  |  |
| address_ncoa_date | datetime2 | 8 | 1 |  |  |  |
| address_1 | varchar | 8000 | 1 |  |  |  |
| address_2 | varchar | 8000 | 1 |  |  |  |
| address_3 | varchar | 8000 | 1 |  |  |  |
| address_4 | varchar | 8000 | 1 |  |  |  |
| address_5 | varchar | 8000 | 1 |  |  |  |
| address_6 | varchar | 8000 | 1 |  |  |  |
| post_code | varchar | 8000 | 1 |  |  |  |
| date_last_modified | datetime2 | 8 | 1 |  |  |  |
| address_error | varchar | 8000 | 1 |  |  |  |
| address_longitude | float | 8 | 1 |  |  |  |
| address_latitude | float | 8 | 1 |  |  |  |
| timestamp | varbinary | 8000 | 1 |  |  |  |
| create_store_no | int | 4 | 1 |  |  |  |
| modify_store_no | int | 4 | 1 |  |  |  |
| create_user_id | int | 4 | 1 |  |  |  |
| create_date | datetime2 | 8 | 1 |  |  |  |
| modify_user_id | int | 4 | 1 |  |  |  |
| create_source_id | int | 4 | 1 |  |  |  |
| create_comment | varchar | 8000 | 1 |  |  |  |
| modify_source_id | int | 4 | 1 |  |  |  |
| modify_comment | varchar | 8000 | 1 |  |  |  |
| posted_date | datetime2 | 8 | 1 |  |  |  |
| old_customer_id | int | 4 | 1 |  |  |  |
| temp_old_cust_no | decimal | 13 | 1 |  |  |  |
