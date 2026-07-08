# dbo.import_cust_liability_BJB20250923

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| rule_id | nvarchar | 6 | 0 |  |  |  |
| reference_no | nvarchar | 40 | 1 |  |  |  |
| date_issued | smalldatetime | 4 | 1 |  |  |  |
| action_amount | money | 8 | 0 |  |  |  |
| issuing_store_no | numeric | 9 | 0 |  |  |  |
| upc_no | numeric | 9 | 1 |  |  |  |
| pos_identifier | nvarchar | 40 | 1 |  |  |  |
| units | unit_datatype | 9 | 1 |  |  |  |
| customer_no | numeric | 13 | 1 |  |  |  |
| employee_no | int | 4 | 1 |  |  |  |
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
| pos_tax_jurisdiction_code | nvarchar | 40 | 1 |  |  |  |
| telephone_no1 | nvarchar | 32 | 1 |  |  |  |
| telephone_no2 | nvarchar | 32 | 1 |  |  |  |
| fax | nvarchar | 32 | 1 |  |  |  |
| email_address | nvarchar | 100 | 1 |  |  |  |
| replacement_reference_no | nvarchar | 40 | 1 |  |  |  |
| destination_store_no | int | 4 | 1 |  |  |  |
| expiry_date | nvarchar | 20 | 1 |  |  |  |
| date_issued_formatted | nvarchar | 20 | 1 |  |  |  |
| export_flag | tinyint | 1 | 1 |  |  |  |
| import_row_id | numeric | 9 | 0 | YES |  |  |
| import_batch_id | numeric | 9 | 1 |  |  |  |
| currency_code | nvarchar | 6 | 1 |  |  |  |
| serial_no | nvarchar | 160 | 1 |  |  |  |
| pos_identifier_type | tinyint | 1 | 1 |  |  |  |
