# dbo.work_ecp_period_export3

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| pay_period_end_datetime | varchar | 10 | 0 |  |  |  |
| home_store_no | int | 4 | 1 |  |  |  |
| employee_no | int | 4 | 0 |  |  |  |
| commission_export_group_code | nvarchar | 40 | 0 |  |  |  |
| commission_amount | numeric | 9 | 0 |  |  |  |
| pay_period_start_datetime | varchar | 10 | 0 |  |  |  |
| employee_last_name | nvarchar | 100 | 1 |  |  |  |
| employee_first_name | nvarchar | 100 | 1 |  |  |  |
| employee_transaction_role_desc | nvarchar | 510 | 1 |  |  |  |
