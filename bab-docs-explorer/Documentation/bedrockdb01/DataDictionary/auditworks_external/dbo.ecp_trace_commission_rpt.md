# dbo.ecp_trace_commission_rpt

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| execution_datetime | datetime | 8 | 0 |  |  |  |
| select_from_date | datetime | 8 | 1 |  |  |  |
| select_to_date | datetime | 8 | 1 |  |  |  |
| empl_calendar_level_list | nvarchar | 8000 | 1 |  |  |  |
| select_transaction_role_list | nvarchar | 8000 | 1 |  |  |  |
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
| include_transaction_role | tinyint | 1 | 1 |  |  |  |
| include_item_commission_code | tinyint | 1 | 1 |  |  |  |
| include_commission_rate | tinyint | 1 | 1 |  |  |  |
| include_trans_commission_code | tinyint | 1 | 1 |  |  |  |
| language_id | smallint | 2 | 1 |  |  |  |
| user_name | nvarchar | 60 | 1 |  |  |  |
| user_id | numeric | 9 | 1 |  |  |  |
| store_access_table_name | nvarchar | 200 | 1 |  |  |  |
| include_zero_rate | tinyint | 1 | 1 |  |  |  |
| select_home_store_list | nvarchar | -1 | 1 |  |  |  |
| select_home_store_from | int | 4 | 1 |  |  |  |
| select_home_store_to | int | 4 | 1 |  |  |  |
| terminated_employees | tinyint | 1 | 1 |  |  |  |
| include_trans_store | tinyint | 1 | 1 |  |  |  |
| date_selection_calendar_level | int | 4 | 1 |  |  |  |
| date_range_type | nvarchar | 60 | 1 |  |  |  |
| include_selling_area | tinyint | 1 | 1 |  |  |  |
| employee_no | int | 4 | 1 |  |  |  |
| top_X | smallint | 2 | 1 |  |  |  |
