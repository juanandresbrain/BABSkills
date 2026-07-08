# dbo.work_emp_attribute_template

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | tran_id_datatype | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| if_reject_reason | smallint | 2 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| transaction_date | smalldatetime | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| transaction_no | trno | 4 | 0 |  |  |  |
| transaction_series | nchar | 2 | 0 |  |  |  |
| entry_date_time | datetime | 8 | 0 |  |  |  |
| date_reject_id | tinyint | 1 | 0 |  |  |  |
| cashier_no | int | 4 | 1 |  |  |  |
| cashier_on_file | tinyint | 1 | 1 |  |  |  |
| employee_no | int | 4 | 1 |  |  |  |
| employee_on_file | tinyint | 1 | 1 |  |  |  |
| salesperson | int | 4 | 1 |  |  |  |
| salesperson_on_file | tinyint | 1 | 1 |  |  |  |
| salesperson2 | int | 4 | 1 |  |  |  |
| salesperson2_on_file | tinyint | 1 | 1 |  |  |  |
| original_salesperson_flag | tinyint | 1 | 1 |  |  |  |
| note_type | smallint | 2 | 1 |  |  |  |
| line_note | nvarchar | 6000 | 1 |  |  |  |
| user_defined_emp_on_file | tinyint | 1 | 1 |  |  |  |
| interface_id | tinyint | 1 | 1 |  |  |  |
| interface_status_flag | smallint | 2 | 1 |  |  |  |
| all_rejects_fixed | tinyint | 1 | 1 |  |  |  |
| PRMY_ORG_CHN_NUM | int | 4 | 1 |  |  |  |
| PRMY_ORG_CHN_NUM_2 | int | 4 | 1 |  |  |  |
| payroll_date | datetime | 8 | 1 |  |  |  |
