# dbo.ecp_trace_commission_subrpt2

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| execution_datetime | datetime | 8 | 0 |  |  |  |
| drill_down_column | nvarchar | 60 | 1 |  |  |  |
| select_from_date | datetime | 8 | 1 |  |  |  |
| select_to_date | datetime | 8 | 1 |  |  |  |
| empl_calendar_level_list | nvarchar | 8000 | 1 |  |  |  |
| employee_trans_role_desc | nvarchar | 8000 | 1 |  |  |  |
| select_store_list | nvarchar | 8000 | 1 |  |  |  |
| select_store_from | int | 4 | 1 |  |  |  |
| select_store_to | int | 4 | 1 |  |  |  |
| select_employee_list | nvarchar | -1 | 1 |  |  |  |
| select_employee_from | int | 4 | 1 |  |  |  |
| select_employee_to | int | 4 | 1 |  |  |  |
| select_selling_area_list | nvarchar | 8000 | 1 |  |  |  |
| select_selling_area_from | int | 4 | 1 |  |  |  |
| select_selling_area_to | int | 4 | 1 |  |  |  |
| select_primary_position_list | nvarchar | 8000 | 1 |  |  |  |
| language_id | smallint | 2 | 1 |  |  |  |
| user_name | nvarchar | 60 | 1 |  |  |  |
| other_store_flag | tinyint | 1 | 1 |  |  |  |
| other_selling_area_flag | tinyint | 1 | 1 |  |  |  |
| employee_trans_role | nvarchar | 40 | 1 |  |  |  |
