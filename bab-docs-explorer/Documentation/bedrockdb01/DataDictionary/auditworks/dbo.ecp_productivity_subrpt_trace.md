# dbo.ecp_productivity_subrpt_trace

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| execution_datetime | datetime | 8 | 0 |  |  |  |
| drill_down_column | nvarchar | 60 | 1 |  |  |  |
| select_from_date | datetime | 8 | 1 |  |  |  |
| select_to_date | datetime | 8 | 1 |  |  |  |
| select_calendar_level | int | 4 | 1 |  |  |  |
| select_transaction_role_list | nvarchar | 6000 | 1 |  |  |  |
| select_store_list | nvarchar | 6000 | 1 |  |  |  |
| select_store_from | int | 4 | 1 |  |  |  |
| select_store_to | int | 4 | 1 |  |  |  |
| select_employee_list | nvarchar | 6000 | 1 |  |  |  |
| select_employee_from | int | 4 | 1 |  |  |  |
| select_employee_to | int | 4 | 1 |  |  |  |
| select_selling_area_list | nvarchar | 6000 | 1 |  |  |  |
| select_selling_area_from | int | 4 | 1 |  |  |  |
| select_selling_area_to | int | 4 | 1 |  |  |  |
| select_primary_position_list | nvarchar | 6000 | 1 |  |  |  |
| language_id | smallint | 2 | 1 |  |  |  |
| user_name | nvarchar | 60 | 1 |  |  |  |
| select_home_store_list | nvarchar | 6000 | 1 |  |  |  |
| select_home_store_from | int | 4 | 1 |  |  |  |
| select_home_store_to | int | 4 | 1 |  |  |  |
| terminated_employees | tinyint | 1 | 1 |  |  |  |
| employee_group_code_start | nvarchar | 40 | 1 |  |  |  |
| employee_group_code_end | nvarchar | 40 | 1 |  |  |  |
| relationship_type | nvarchar | 40 | 1 |  |  |  |
| user_id | numeric | 9 | 1 |  |  |  |
| unlimited_comparison_type | smallint | 2 | 1 |  |  |  |
| all_transaction_roles | tinyint | 1 | 1 |  |  |  |
| employee_no | int | 4 | 1 |  |  |  |
