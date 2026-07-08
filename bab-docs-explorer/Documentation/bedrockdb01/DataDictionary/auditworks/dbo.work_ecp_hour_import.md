# dbo.work_ecp_hour_import

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_id | numeric | 9 | 0 |  |  |  |
| if_entry_no | numeric | 9 | 0 |  |  |  |
| line_id | numeric | 5 | 0 |  |  |  |
| payroll_date | datetime | 8 | 0 |  |  |  |
| calendar_level | smallint | 2 | 0 |  |  |  |
| period_end_datetime | datetime | 8 | 0 |  |  |  |
| pay_period_end_datetime | datetime | 8 | 0 |  |  |  |
| calendar_level_seq | smallint | 2 | 0 |  |  |  |
| employee_no | int | 4 | 0 |  |  |  |
| primary_position | nvarchar | 8 | 1 |  |  |  |
| primary_selling_area_no | int | 4 | 1 |  |  |  |
| store_no | int | 4 | 0 |  |  |  |
| payroll_entry_hour_type | smallint | 2 | 1 |  |  |  |
| payroll_entry_position | nvarchar | 8 | 1 |  |  |  |
| payroll_entry_selling_area_no | int | 4 | 1 |  |  |  |
| productive_selling_hours | money | 8 | 0 |  |  |  |
| productive_non_selling_hours | money | 8 | 0 |  |  |  |
| non_productive_hours | money | 8 | 0 |  |  |  |
| interface_control_flag | numeric | 9 | 0 |  |  |  |
| empl_hour_summary_id | numeric | 9 | 1 |  |  |  |
| new_flag | tinyint | 1 | 1 |  |  |  |
| home_store_no | int | 4 | 1 |  |  |  |
| relationship_set_id | numeric | 9 | 1 |  |  |  |
| shift_start_datetime | datetime | 8 | 0 |  |  |  |
| shift_end_datetime | datetime | 8 | 0 |  |  |  |
| attributed_traffic_count | money | 8 | 1 |  |  |  |
| period_start_date | datetime | 8 | 1 |  |  |  |
| last_trans_version_flag | tinyint | 1 | 0 |  |  |  |
| wehi_id | numeric | 9 | 0 | YES |  |  |
