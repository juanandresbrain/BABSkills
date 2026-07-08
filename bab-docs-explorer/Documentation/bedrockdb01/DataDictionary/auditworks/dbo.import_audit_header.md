# dbo.import_audit_header

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| entry_id | numeric | 9 | 0 |  |  |  |
| entry_date | smalldatetime | 4 | 0 |  |  |  |
| table_name | nvarchar | 60 | 0 |  |  |  |
| table_key | nvarchar | 510 | 0 |  |  |  |
| table_key_descr | nvarchar | 510 | 0 |  |  |  |
| user_name | nvarchar | 100 | 0 |  |  |  |
| action | tinyint | 1 | 0 |  |  |  |
| function_no | tinyint | 1 | 0 |  |  |  |
| store_no | int | 4 | 1 |  |  |  |
| register_no | smallint | 2 | 1 |  |  |  |
| transaction_date | smalldatetime | 4 | 1 |  |  |  |
| date_reject_id | tinyint | 1 | 1 |  |  |  |
| transaction_no | trno | 4 | 1 |  |  |  |
| transaction_series | nchar | 2 | 1 |  |  |  |
| entry_date_time | datetime | 8 | 1 |  |  |  |
| cashier_no | int | 4 | 1 |  |  |  |
| reference_type | smallint | 2 | 1 |  |  |  |
| rule_id | nvarchar | 6 | 1 |  |  |  |
| reference_no | nvarchar | 40 | 1 |  |  |  |
