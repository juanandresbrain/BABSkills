# dbo.interface_directory_lookup

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| interface_id | tinyint | 1 | 0 |  |  |  |
| update_timing | smallint | 2 | 0 |  |  |  |
| upc_check | tinyint | 1 | 0 |  |  |  |
| credit_card_check | tinyint | 1 | 0 |  |  |  |
| employee_no_check | tinyint | 1 | 0 |  |  |  |
| customer_info_check | tinyint | 1 | 0 |  |  |  |
| exception_jurisdiction_check | tinyint | 1 | 0 |  |  |  |
| live_date | smalldatetime | 4 | 1 |  |  |  |
| interface_voided_transactions | tinyint | 1 | 0 |  |  |  |
| tax_default_check | tinyint | 1 | 0 |  |  |  |
| store_check | tinyint | 1 | 0 |  |  |  |
| edit_mass_update_flag | tinyint | 1 | 0 |  |  |  |
| applicability_method | tinyint | 1 | 0 |  |  |  |
| purchasing_employee_check | tinyint | 1 | 0 |  |  |  |
| cashier_check | tinyint | 1 | 0 |  |  |  |
| payroll_employee_check | tinyint | 1 | 0 |  |  |  |
| reference_no_check | tinyint | 1 | 0 |  |  |  |
| customer_liability_check | tinyint | 1 | 0 |  |  |  |
| all_modifications_relevant | tinyint | 1 | 0 |  |  |  |
