# dbo.work_voucher

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| reference_type | tinyint | 1 | 0 |  |  |  |
| reference_no | nvarchar | 40 | 0 |  |  |  |
| key_store_no | int | 4 | 0 |  |  |  |
| date_issued | smalldatetime | 4 | 0 |  |  |  |
| issuing_store_no | int | 4 | 0 |  |  |  |
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
| customer_no | numeric | 13 | 1 |  |  |  |
| pos_tax_jurisdiction_code | nvarchar | 40 | 1 |  |  |  |
| fax | nvarchar | 32 | 1 |  |  |  |
| email_address | nvarchar | 100 | 1 |  |  |  |
| synch_flag | tinyint | 1 | 0 |  |  |  |
| pos_status | tinyint | 1 | 0 |  |  |  |
| pos_amount_1 | money | 8 | 0 |  |  |  |
| pos_amount_2 | money | 8 | 0 |  |  |  |
| pos_amount_3 | money | 8 | 0 |  |  |  |
| as_of_date | datetime | 8 | 1 |  |  |  |
| entry_type | nchar | 2 | 0 |  |  |  |
