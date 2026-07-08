# dbo.work_cust_liab_ref_list

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| input_id | numeric | 9 | 0 |  |  |  |
| row_no | numeric | 9 | 0 |  |  |  |
| reference_type | tinyint | 1 | 0 |  |  |  |
| reference_no | nvarchar | 40 | 0 |  |  |  |
| key_store_no | int | 4 | 0 |  |  |  |
| action_amount | money | 8 | 0 |  |  |  |
| issuing_store_no | int | 4 | 1 |  |  |  |
| date_issued | smalldatetime | 4 | 1 |  |  |  |
| replacement_reference_no | nvarchar | 40 | 1 |  |  |  |
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
| employee_no | int | 4 | 1 |  |  |  |
| destination_store_no | int | 4 | 1 |  |  |  |
| action_date | smalldatetime | 4 | 1 |  |  |  |
| upc_no | numeric | 9 | 1 |  |  |  |
| pos_identifier | nvarchar | 40 | 1 |  |  |  |
| units | unit_datatype | 9 | 1 |  |  |  |
| expiry_days | smallint | 2 | 1 |  |  |  |
| outstanding_amount | money | 8 | 1 |  |  |  |
| trans_row_no | int | 4 | 1 |  |  |  |
| line_row_no | int | 4 | 1 |  |  |  |
| serial_no | nvarchar | 160 | 1 |  |  |  |
| document_type | tinyint | 1 | 1 |  |  |  |
| pos_identifier_type | tinyint | 1 | 1 |  |  |  |
