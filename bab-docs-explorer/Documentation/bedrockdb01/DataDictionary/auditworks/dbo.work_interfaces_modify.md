# dbo.work_interfaces_modify

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| process_id | binary | 16 | 0 |  |  |  |
| interface_id | tinyint | 1 | 0 |  |  |  |
| update_timing | smallint | 2 | 0 |  |  |  |
| upc_check | tinyint | 1 | 0 |  |  |  |
| customer_liability_check | tinyint | 1 | 0 |  |  |  |
| credit_card_check | tinyint | 1 | 0 |  |  |  |
| employee_no_check | tinyint | 1 | 0 |  |  |  |
| customer_info_check | tinyint | 1 | 0 |  |  |  |
| store_check | tinyint | 1 | 0 |  |  |  |
| interface_status | tinyint | 1 | 0 |  |  |  |
| exception_jurisdiction_check | tinyint | 1 | 0 |  |  |  |
| tax_default_check | tinyint | 1 | 0 |  |  |  |
| reference_no_check | tinyint | 1 | 0 |  |  |  |
| purchasing_employee_check | tinyint | 1 | 1 |  |  |  |
| cashier_check | tinyint | 1 | 1 |  |  |  |
| payroll_employee_check | tinyint | 1 | 1 |  |  |  |
| applicability_method | tinyint | 1 | 1 |  |  |  |
| line_modified_flag | tinyint | 1 | 1 |  |  |  |
| all_modifications_relevant | tinyint | 1 | 1 |  |  |  |
| work_tb_entry_date_time | datetime | 8 | 1 |  |  |  |
