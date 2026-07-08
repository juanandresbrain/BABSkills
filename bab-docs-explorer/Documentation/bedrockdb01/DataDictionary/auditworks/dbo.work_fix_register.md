# dbo.work_fix_register

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_id | binary | 16 | 0 |  |  |  |
| transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| logical_trading_date | smalldatetime | 4 | 0 |  |  |  |
| entry_date_time | datetime | 8 | 0 |  |  |  |
| employee_no | int | 4 | 1 |  |  |  |
| cashier_no | int | 4 | 0 |  |  |  |
| closeout_date | smalldatetime | 4 | 1 |  |  |  |
| work_tb_entry_date_time | datetime | 8 | 1 |  |  |  |
