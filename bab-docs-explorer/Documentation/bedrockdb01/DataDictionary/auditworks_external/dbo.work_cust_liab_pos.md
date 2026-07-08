# dbo.work_cust_liab_pos

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_id | binary | 16 | 0 |  |  |  |
| reference_no | nvarchar | 40 | 0 |  |  |  |
| reference_type | tinyint | 1 | 0 |  |  |  |
| glc_type | tinyint | 1 | 0 |  |  |  |
| tracking_id | smallint | 2 | 0 |  |  |  |
| amount | money | 8 | 0 |  |  |  |
| line_action | tinyint | 1 | 0 |  |  |  |
| expiry_date | smalldatetime | 4 | 1 |  |  |  |
| first_name | nvarchar | 40 | 1 |  |  |  |
| last_name | nvarchar | 40 | 1 |  |  |  |
| telephone_no1 | nvarchar | 32 | 1 |  |  |  |
| customer_no | numeric | 13 | 1 |  |  |  |
| entry_date_time | smalldatetime | 4 | 1 |  |  |  |
| issued_amount | money | 8 | 1 |  |  |  |
| redeemed_amount | money | 8 | 1 |  |  |  |
| forfeited_amount | money | 8 | 1 |  |  |  |
| stocked_amount | money | 8 | 1 |  |  |  |
| stocked_stolen_amount | money | 8 | 1 |  |  |  |
| stolen_amount | money | 8 | 1 |  |  |  |
| transaction_void_flag | smallint | 2 | 1 |  |  |  |
| interface_control_flag | numeric | 9 | 1 |  |  |  |
