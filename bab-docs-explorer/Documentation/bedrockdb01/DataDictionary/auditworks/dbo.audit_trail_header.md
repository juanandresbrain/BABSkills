# dbo.audit_trail_header

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| entry_id | numeric | 9 | 0 | YES |  |  |
| entry_date | smalldatetime | 4 | 0 |  |  |  |
| table_name | varchar | 30 | 0 |  |  |  |
| table_key | varchar | 255 | 0 |  |  |  |
| table_key_descr | varchar | 255 | 0 |  |  |  |
| user_name | varchar | 50 | 0 |  |  |  |
| action | tinyint | 1 | 0 |  |  |  |
| function_no | tinyint | 1 | 0 |  |  |  |
| store_no | int | 4 | 1 |  |  |  |
| register_no | smallint | 2 | 1 |  |  |  |
| transaction_date | smalldatetime | 4 | 1 |  |  |  |
| date_reject_id | tinyint | 1 | 1 |  |  |  |
| transaction_no | trno | 4 | 1 |  |  |  |
| transaction_series | char | 1 | 1 |  |  |  |
| entry_date_time | datetime | 8 | 1 |  |  |  |
| cashier_no | int | 4 | 1 |  |  |  |
| reference_type | tinyint | 1 | 1 |  |  |  |
| rule_id | varchar | 3 | 1 |  |  |  |
| reference_no | varchar | 20 | 1 |  |  |  |
| comment_id | numeric | 9 | 1 |  |  |  |
| till_no | smallint | 2 | 1 |  |  |  |
