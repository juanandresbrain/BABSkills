# dbo.employee_hour_summary

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| empl_hour_summary_id | numeric | 9 | 0 | YES |  |  |
| calendar_level | smallint | 2 | 0 |  |  |  |
| period_end_datetime | datetime | 8 | 0 |  |  |  |
| pay_period_end_datetime | datetime | 8 | 0 |  |  |  |
| employee_no | int | 4 | 0 |  |  |  |
| primary_position | nvarchar | 8 | 0 |  |  |  |
| primary_selling_area_no | int | 4 | 0 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| payroll_entry_hour_type | smallint | 2 | 1 |  |  |  |
| payroll_entry_position | nvarchar | 8 | 0 |  |  |  |
| payroll_entry_selling_area_no | int | 4 | 1 |  |  |  |
| productive_selling_hours | money | 8 | 0 |  |  |  |
| productive_non_selling_hours | money | 8 | 0 |  |  |  |
| non_productive_hours | money | 8 | 0 |  |  |  |
| home_store_no | int | 4 | 1 |  |  |  |
| relationship_set_id | numeric | 9 | 1 |  |  |  |
| attributed_traffic_count | money | 8 | 1 |  |  |  |
