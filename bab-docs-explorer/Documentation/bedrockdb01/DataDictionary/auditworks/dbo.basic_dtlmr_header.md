# dbo.basic_dtlmr_header

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| if_entry_no | if_entry_datatype | 9 | 0 |  |  |  |
| transaction_category | tinyint | 1 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| register_no | smallint | 2 | 0 |  |  |  |
| transaction_date | char | 8 | 0 |  |  |  |
| transaction_no | trno | 4 | 0 |  |  |  |
| entry_time | char | 4 | 0 |  |  |  |
| cashier_no | int | 4 | 0 |  |  |  |
| transaction_void_flag | smallint | 2 | 0 |  |  |  |
| media_count_flag | tinyint | 1 | 0 |  |  |  |
| tender_total | int | 4 | 0 |  |  |  |
| employee_no | int | 4 | 1 |  |  |  |
| transaction_code | char | 1 | 0 |  |  |  |
| subsystem | char | 15 | 0 |  |  |  |
| interface_control_flag | numeric | 9 | 1 |  |  |  |
| transaction_series | char | 1 | 1 |  |  |  |
