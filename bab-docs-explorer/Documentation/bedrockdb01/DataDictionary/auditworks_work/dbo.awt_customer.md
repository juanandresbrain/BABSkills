# dbo.awt_customer

**Database:** auditworks_work  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_no | int | 4 | 0 |  |  |  |
| register_no | int | 4 | 0 |  |  |  |
| entry_date_time | datetime | 8 | 0 |  |  |  |
| transaction_series | char | 1 | 0 |  |  |  |
| transaction_no | int | 4 | 0 |  |  |  |
| from_line_id | numeric | 5 | 0 |  |  |  |
| customer_role | smallint | 2 | 0 |  |  |  |
| title | varchar | 10 | 1 |  |  |  |
| first_name | varchar | 20 | 1 |  |  |  |
| last_name | varchar | 20 | 1 |  |  |  |
| address_1 | varchar | 40 | 1 |  |  |  |
| address_2 | varchar | 40 | 1 |  |  |  |
| city | varchar | 40 | 1 |  |  |  |
| county | varchar | 40 | 1 |  |  |  |
| state | varchar | 40 | 1 |  |  |  |
| country | varchar | 40 | 1 |  |  |  |
| post_code | varchar | 20 | 1 |  |  |  |
| telephone_no1 | varchar | 16 | 1 |  |  |  |
| telephone_no2 | varchar | 16 | 1 |  |  |  |
| customer_no | numeric | 13 | 1 |  |  |  |
| row_sequence_no | numeric | 9 | 0 | YES |  |  |
| pos_tax_jurisdiction_code | varchar | 20 | 1 |  |  |  |
| fax | varchar | 16 | 1 |  |  |  |
| email_address | varchar | 50 | 1 |  |  |  |
| more_info_flag | tinyint | 1 | 1 |  |  |  |
| customer_sufficient | tinyint | 1 | 1 |  |  |  |
