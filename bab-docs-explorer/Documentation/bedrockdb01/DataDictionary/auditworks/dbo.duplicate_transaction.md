# dbo.duplicate_transaction

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| date_reject_id | tinyint | 1 | 0 |  |  |  |
| entry_date_time | datetime | 8 | 0 |  |  |  |
| transaction_series | nchar | 2 | 0 |  |  |  |
| transaction_no | trno | 4 | 0 |  |  |  |
| cashier_no | int | 4 | 0 |  |  |  |
| transaction_category | tinyint | 1 | 0 |  |  |  |
| tender_total | money | 8 | 0 |  |  |  |
| verified | tinyint | 1 | 0 |  |  |  |
| support_call_id | nvarchar | 60 | 1 |  |  |  |
| verified_date | smalldatetime | 4 | 1 |  |  |  |
| verification_remark | nvarchar | 510 | 1 |  |  |  |
| verified_by_user_id | int | 4 | 1 |  |  |  |
| override_flag | tinyint | 1 | 1 |  |  |  |
