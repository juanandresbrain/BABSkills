# dbo.employee_hour_transaction

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| payroll_date | datetime | 8 | 0 |  |  |  |
| employee_no | int | 4 | 0 |  |  |  |
| hours | money | 8 | 0 |  |  |  |
| transaction_id | numeric | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| if_entry_no | numeric | 9 | 0 |  |  |  |
| current_flag | tinyint | 1 | 0 |  |  |  |
| empl_hour_summary_id | numeric | 9 | 1 |  |  |  |
| shift_start_datetime | datetime | 8 | 0 |  |  |  |
| shift_end_datetime | datetime | 8 | 0 |  |  |  |
