# dbo.av_payroll_detail

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| av_transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| employee_no | int | 4 | 1 |  |  |  |
| payroll_date | datetime | 8 | 1 |  |  |  |
| employee_payroll_id | nvarchar | 18 | 1 |  |  |  |
| employee_type | nchar | 8 | 1 |  |  |  |
| payroll_entry_type | smallint | 2 | 1 |  |  |  |
| transaction_date | smalldatetime | 4 | 1 |  |  |  |
