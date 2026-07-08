# dbo.awt_payroll_detail

**Database:** auditworks_work  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| entry_date_time | datetime | 8 | 0 |  |  |  |
| transaction_series | char | 1 | 0 |  |  |  |
| transaction_no | int | 4 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| employee_no | int | 4 | 0 |  |  |  |
| payroll_date | smalldatetime | 4 | 1 |  |  |  |
| employee_payroll_id | varchar | 9 | 1 |  |  |  |
| employee_type | char | 1 | 0 |  |  |  |
| payroll_entry_type | smallint | 2 | 0 |  |  |  |
| row_sequence_no | numeric | 9 | 0 | YES |  |  |
| transaction_id | numeric | 9 | 1 |  |  |  |
