# dbo.ecp_import_hours

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| period_end_datetime | datetime | 8 | 0 |  |  |  |
| employee_no | int | 4 | 0 |  |  |  |
| hours | money | 8 | 0 |  |  |  |
| payroll_entry_hour_type_alpha | nvarchar | 40 | 0 |  |  |  |
| payroll_entry_position | nvarchar | 8 | 1 |  |  |  |
| payroll_entry_selling_area_no | int | 4 | 1 |  |  |  |
| employee_last_name | nvarchar | 200 | 1 |  |  |  |
| employee_first_name | nvarchar | 200 | 1 |  |  |  |
| store_no | int | 4 | 1 |  |  |  |
| shift_start_datetime | datetime | 8 | 1 |  |  |  |
| entry_id | numeric | 9 | 0 | YES |  |  |
