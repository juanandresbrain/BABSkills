# dbo.cust_liability

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| cust_liability_entry_no | numeric | 9 | 0 | YES |  |  |
| reference_type | tinyint | 1 | 0 |  |  |  |
| reference_no | nvarchar | 40 | 0 |  |  |  |
| key_store_no | int | 4 | 1 |  |  |  |
| date_issued | smalldatetime | 4 | 1 |  |  |  |
| issuing_store_no | int | 4 | 0 |  |  |  |
| tracking_id | smallint | 2 | 1 |  |  |  |
| liability_amount | money | 8 | 0 |  |  |  |
| receivable_amount | money | 8 | 0 |  |  |  |
| amount_3 | money | 8 | 0 |  |  |  |
| amount_4 | money | 8 | 0 |  |  |  |
| amount_5 | money | 8 | 0 |  |  |  |
| amount_6 | money | 8 | 0 |  |  |  |
| amount_7 | money | 8 | 0 |  |  |  |
| amount_8 | money | 8 | 0 |  |  |  |
| amount_9 | money | 8 | 0 |  |  |  |
| amount_10 | money | 8 | 0 |  |  |  |
| stocked_amount | money | 8 | 1 |  |  |  |
| stocked_flag | smallint | 2 | 0 |  |  |  |
| stocked_stolen_flag | smallint | 2 | 1 |  |  |  |
| issued_flag | smallint | 2 | 0 |  |  |  |
| stolen_from_cust_flag | smallint | 2 | 0 |  |  |  |
| forfeited_flag | smallint | 2 | 0 |  |  |  |
| assumed_completion_date | smalldatetime | 4 | 1 |  |  |  |
| reopen_date | smalldatetime | 4 | 1 |  |  |  |
| last_modified_by_aw | datetime | 8 | 1 |  |  |  |
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
| expiry_date | smalldatetime | 4 | 1 |  |  |  |
| original_amount | money | 8 | 1 |  |  |  |
| pos_status | tinyint | 1 | 0 |  |  |  |
| pos_amount_1 | money | 8 | 1 |  |  |  |
| pos_amount_2 | money | 8 | 1 |  |  |  |
| pos_amount_3 | money | 8 | 1 |  |  |  |
| last_modified_by_pos | datetime | 8 | 1 |  |  |  |
| employee_no | int | 4 | 1 |  |  |  |
| last_synched | datetime | 8 | 1 |  |  |  |
| last_client_activity_date | smalldatetime | 4 | 1 |  |  |  |
| date_4 | smalldatetime | 4 | 1 |  |  |  |
