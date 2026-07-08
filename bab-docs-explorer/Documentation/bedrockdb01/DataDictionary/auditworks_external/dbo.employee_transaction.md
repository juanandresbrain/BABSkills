# dbo.employee_transaction

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| employee_no | int | 4 | 0 |  |  |  |
| employee_transaction_role | nvarchar | 40 | 0 |  |  |  |
| transaction_id | numeric | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| if_entry_no | numeric | 9 | 0 |  |  |  |
| current_flag | tinyint | 1 | 0 |  |  |  |
| empl_trans_summary_id | numeric | 9 | 1 |  |  |  |
| posting_datetime | datetime | 8 | 1 |  |  |  |
| reversal_flag | tinyint | 1 | 1 |  |  |  |
| reassigned_flag | tinyint | 1 | 1 |  |  |  |
