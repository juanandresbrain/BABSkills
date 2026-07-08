# dbo.dayend_workload_restore

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| dayend_process_id | tinyint | 1 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| sales_date | smalldatetime | 4 | 0 |  |  |  |
| date_reject_id | tinyint | 1 | 0 |  |  |  |
| store_audit_status | smallint | 2 | 0 |  |  |  |
| merchandise_year_no | smallint | 2 | 0 |  |  |  |
| merchandise_month_no | tinyint | 1 | 0 |  |  |  |
| gl_company | int | 4 | 0 |  |  |  |
| tax_jurisdiction | char | 5 | 0 |  |  |  |
| store_deposit_destination | smallint | 2 | 0 |  |  |  |
| tax_strip_flag | tinyint | 1 | 1 |  |  |  |
| log_tax_override | tinyint | 1 | 1 |  |  |  |
