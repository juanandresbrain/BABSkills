# dbo.awl_customer

**Database:** auditworks_work  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_no | int | 4 | 0 |  |  |  |
| register_no | int | 4 | 0 |  |  |  |
| entry_date_time | datetime | 8 | 0 |  |  |  |
| transaction_series | nchar | 2 | 0 |  |  |  |
| transaction_no | int | 4 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| customer_role | smallint | 2 | 0 |  |  |  |
| title | nvarchar | 20 | 1 |  |  |  |
| first_name | nvarchar | 40 | 1 |  |  |  |
| last_name | nvarchar | 80 | 1 |  |  |  |
| address_1 | nvarchar | 80 | 1 |  |  |  |
| address_2 | nvarchar | 80 | 1 |  |  |  |
| city | nvarchar | 80 | 1 |  |  |  |
| county | nvarchar | 80 | 1 |  |  |  |
| state | nvarchar | 80 | 1 |  |  |  |
| country | nvarchar | 80 | 1 |  |  |  |
| post_code | nvarchar | 40 | 1 |  |  |  |
| telephone_no1 | nvarchar | 32 | 1 |  |  |  |
| telephone_no2 | nvarchar | 32 | 1 |  |  |  |
| customer_no | numeric | 9 | 1 |  |  |  |
| row_sequence_no | numeric | 9 | 0 | YES |  |  |
| pos_tax_jurisdiction_code | nvarchar | 40 | 1 |  |  |  |
| fax | nvarchar | 32 | 1 |  |  |  |
| email_address | nvarchar | 100 | 1 |  |  |  |
| more_info_flag | tinyint | 1 | 1 |  |  |  |
| customer_sufficient | tinyint | 1 | 1 |  |  |  |
