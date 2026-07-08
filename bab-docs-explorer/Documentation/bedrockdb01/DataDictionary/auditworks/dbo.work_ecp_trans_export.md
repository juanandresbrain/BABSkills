# dbo.work_ecp_trans_export

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | numeric | 9 | 0 |  |  |  |
| if_entry_no | numeric | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| pay_period_date | datetime | 8 | 0 |  |  |  |
| transaction_store_no | int | 4 | 0 |  |  |  |
| transaction_commission_code | nvarchar | 40 | 0 |  |  |  |
| transaction_net_amount | money | 8 | 0 |  |  |  |
| transaction_discount_amount | money | 8 | 0 |  |  |  |
| transaction_units | numeric | 9 | 0 |  |  |  |
| store_commission_code | nvarchar | 40 | 1 |  |  |  |
| item_commission_code | nvarchar | 40 | 1 |  |  |  |
| cashier_no | int | 4 | 0 |  |  |  |
| salesperson | int | 4 | 1 |  |  |  |
| salesperson2 | int | 4 | 1 |  |  |  |
| interface_control_flag | numeric | 9 | 0 |  |  |  |
| max_serial_no | numeric | 9 | 0 |  |  |  |
| rtn_salesperson | int | 4 | 1 |  |  |  |
| rtn_salesperson2 | int | 4 | 1 |  |  |  |
| employee_transaction_role | nvarchar | 40 | 1 |  |  |  |
| commission_amount | money | 8 | 1 |  |  |  |
| reference_type | tinyint | 1 | 1 |  |  |  |
