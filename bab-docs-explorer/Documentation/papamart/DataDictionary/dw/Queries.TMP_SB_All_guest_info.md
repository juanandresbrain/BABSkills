# Queries.TMP_SB_All_guest_info

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| customer_no | numeric | 13 | 0 |  |  |  |
| customer_id | int | 4 | 0 |  |  |  |
| address_id | smallint | 2 | 0 |  |  |  |
| country_code | nchar | 6 | 0 |  |  |  |
| address_match_key | nchar | 50 | 0 |  |  |  |
| address_type_code | nchar | 8 | 0 |  |  |  |
| mail_indicator | tinyint | 1 | 0 |  |  |  |
| carrier_route | nchar | 8 | 1 |  |  |  |
| address_ncoa_date | smalldatetime | 4 | 1 |  |  |  |
| address_1 | nvarchar | 80 | 1 |  |  |  |
| address_2 | nvarchar | 80 | 1 |  |  |  |
| address_3 | nvarchar | 80 | 1 |  |  |  |
| address_4 | nvarchar | 80 | 1 |  |  |  |
| address_5 | nvarchar | 80 | 1 |  |  |  |
| address_6 | nvarchar | 80 | 1 |  |  |  |
| post_code | nvarchar | 40 | 1 |  |  |  |
| date_last_modified | datetime | 8 | 0 |  |  |  |
| address_error | nvarchar | 20 | 1 |  |  |  |
| address_longitude | float | 8 | 1 |  |  |  |
| address_latitude | float | 8 | 1 |  |  |  |
| timestamp | timestamp | 8 | 1 |  |  |  |
| create_store_no | int | 4 | 1 |  |  |  |
| modify_store_no | int | 4 | 1 |  |  |  |
| create_user_id | int | 4 | 0 |  |  |  |
| create_date | datetime | 8 | 0 |  |  |  |
| modify_user_id | int | 4 | 0 |  |  |  |
| create_source_id | tinyint | 1 | 0 |  |  |  |
| create_comment | nvarchar | 510 | 1 |  |  |  |
| modify_source_id | tinyint | 1 | 0 |  |  |  |
| modify_comment | nvarchar | 510 | 1 |  |  |  |
| posted_date | datetime | 8 | 0 |  |  |  |
| old_customer_id | int | 4 | 1 |  |  |  |
| temp_old_cust_no | numeric | 13 | 1 |  |  |  |
