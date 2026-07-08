# dbo.work_cust_liab_in

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_id | binary | 16 | 0 |  |  |  |
| reference_no | nvarchar | 40 | 0 |  |  |  |
| reference_type | tinyint | 1 | 0 |  |  |  |
| key_store_no | int | 4 | 0 |  |  |  |
| liability_amount_in | money | 8 | 0 |  |  |  |
| receivable_amount_in | money | 8 | 0 |  |  |  |
| amount_3_in | money | 8 | 0 |  |  |  |
| amount_4_in | money | 8 | 0 |  |  |  |
| amount_5_in | money | 8 | 0 |  |  |  |
| amount_6_in | money | 8 | 0 |  |  |  |
| amount_7_in | money | 8 | 0 |  |  |  |
| amount_8_in | money | 8 | 0 |  |  |  |
| amount_9_in | money | 8 | 0 |  |  |  |
| amount_10_in | money | 8 | 0 |  |  |  |
| stocked_amount_in | money | 8 | 0 |  |  |  |
| stocked_flag_in | smallint | 2 | 0 |  |  |  |
| stocked_stolen_flag_in | smallint | 2 | 0 |  |  |  |
| issued_flag_in | smallint | 2 | 0 |  |  |  |
| stolen_from_cust_flag_in | smallint | 2 | 0 |  |  |  |
| forfeited_flag_in | smallint | 2 | 0 |  |  |  |
| entry_count_in | int | 4 | 0 |  |  |  |
