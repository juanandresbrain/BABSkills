# dbo.ecp_import_transaction

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| period_end_datetime | datetime | 8 | 0 |  |  |  |
| employee_no | int | 4 | 0 |  |  |  |
| employee_transaction_role | nvarchar | 40 | 0 |  |  |  |
| transaction_commission_code | nvarchar | 40 | 0 |  |  |  |
| item_commission_code | nvarchar | 40 | 0 |  |  |  |
| transaction_amount | money | 8 | 0 |  |  |  |
| transaction_units | unit_datatype | 9 | 1 |  |  |  |
| commission_amount | money | 8 | 1 |  |  |  |
| transaction_store_no | int | 4 | 1 |  |  |  |
| employee_last_name | nvarchar | 200 | 1 |  |  |  |
| employee_first_name | nvarchar | 200 | 1 |  |  |  |
| entry_id | numeric | 9 | 0 | YES |  |  |
