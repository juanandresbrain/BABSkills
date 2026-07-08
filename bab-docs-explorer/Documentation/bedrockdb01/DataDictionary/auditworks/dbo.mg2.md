# dbo.mg2

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| reference_type | tinyint | 1 | 0 |  |  |  |
| reference_no | varchar | 20 | 0 |  |  |  |
| key_store_no | int | 4 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| process_no | smallint | 2 | 0 |  |  |  |
| process_key | numeric | 9 | 0 |  |  |  |
| posting_date | datetime | 8 | 0 |  |  |  |
| transaction_category | tinyint | 1 | 0 |  |  |  |
| entry_date_time | datetime | 8 | 0 |  |  |  |
| transaction_void_flag | smallint | 2 | 0 |  |  |  |
| interface_control_flag | tinyint | 1 | 1 |  |  |  |
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
| stocked_amount | money | 8 | 0 |  |  |  |
| stocked_flag | smallint | 2 | 0 |  |  |  |
| stocked_stolen_flag | smallint | 2 | 0 |  |  |  |
| issued_flag | smallint | 2 | 0 |  |  |  |
| stolen_from_cust_flag | smallint | 2 | 0 |  |  |  |
| forfeited_flag | smallint | 2 | 0 |  |  |  |
