# dbo.work_cust_liab_final

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_id | binary | 16 | 0 |  |  |  |
| reference_type | tinyint | 1 | 0 |  |  |  |
| reference_no | nvarchar | 40 | 0 |  |  |  |
| key_store_no | int | 4 | 0 |  |  |  |
| tracking_id | smallint | 2 | 0 |  |  |  |
| default_issuing_date | smalldatetime | 4 | 0 |  |  |  |
| default_issuing_store_no | int | 4 | 0 |  |  |  |
| issuing_date | smalldatetime | 4 | 1 |  |  |  |
| issuing_store_no | int | 4 | 1 |  |  |  |
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
| expiry_days | smallint | 2 | 1 |  |  |  |
| liability_amount | money | 8 | 0 |  |  |  |
| receivable_amount | money | 8 | 0 |  |  |  |
| updated_receivable_amount | money | 8 | 0 |  |  |  |
| amount_3 | money | 8 | 0 |  |  |  |
| amount_4 | money | 8 | 0 |  |  |  |
| amount_5 | money | 8 | 0 |  |  |  |
| amount_6 | money | 8 | 0 |  |  |  |
| amount_7 | money | 8 | 0 |  |  |  |
| amount_8 | money | 8 | 0 |  |  |  |
| amount_9 | money | 8 | 0 |  |  |  |
| amount_10 | money | 8 | 0 |  |  |  |
| stocked_amount | money | 8 | 0 |  |  |  |
| stocked_flag | smallint | 2 | 0 |  |  |  |
| stocked_stolen_flag | smallint | 2 | 0 |  |  |  |
| issued_flag | smallint | 2 | 0 |  |  |  |
| stolen_from_cust_flag | smallint | 2 | 0 |  |  |  |
| forfeited_flag | smallint | 2 | 0 |  |  |  |
| max_transaction_date | smalldatetime | 4 | 1 |  |  |  |
| existing_entry | tinyint | 1 | 0 |  |  |  |
| assumed_completion_date | smalldatetime | 4 | 1 |  |  |  |
| reopen_date | smalldatetime | 4 | 1 |  |  |  |
| employee_no | int | 4 | 1 |  |  |  |
| interface_control_flag | tinyint | 1 | 1 |  |  |  |
| reassignment_flag | tinyint | 1 | 1 |  |  |  |
| updated_liability_amount | money | 8 | 1 |  |  |  |
| last_client_activity_date | smalldatetime | 4 | 1 |  |  |  |
| date_4 | smalldatetime | 4 | 1 |  |  |  |
| expiry_date | smalldatetime | 4 | 1 |  |  |  |
