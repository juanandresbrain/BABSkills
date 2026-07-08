# dbo.ecp_trace_productivity_rpt2

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| execution_datetime | datetime | 8 | 0 |  |  |  |
| select_from_date | datetime | 8 | 1 |  |  |  |
| select_to_date | datetime | 8 | 1 |  |  |  |
| empl_calendar_level_list | nvarchar | 6000 | 1 |  |  |  |
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
| select_primary_positionlist | nvarchar | 6000 | 1 |  |  |  |
| comparison_type | smallint | 2 | 1 |  |  |  |
| comparison_limited | tinyint | 1 | 1 |  |  |  |
| language_id | smallint | 2 | 1 |  |  |  |
| self_compare | tinyint | 1 | 1 |  |  |  |
| user_name | nvarchar | 60 | 1 |  |  |  |
| filter_clause | nvarchar | 6000 | 1 |  |  |  |
| order_clause | nvarchar | 6000 | 1 |  |  |  |
| user_id | numeric | 9 | 1 |  |  |  |
| store_access_table_name | nvarchar | 200 | 1 |  |  |  |
| select_home_store_list | nvarchar | 6000 | 1 |  |  |  |
| select_home_store_from | int | 4 | 1 |  |  |  |
| select_home_store_to | int | 4 | 1 |  |  |  |
| terminated_employees | tinyint | 1 | 1 |  |  |  |
| subtotal_qty | tinyint | 1 | 1 |  |  |  |
| compare_role | tinyint | 1 | 1 |  |  |  |
| include_comment | tinyint | 1 | 1 |  |  |  |
| merch_sale_amt | money | 8 | 1 |  |  |  |
| merch_sale_disc_amt | money | 8 | 1 |  |  |  |
| merch_sale_units | money | 8 | 1 |  |  |  |
| merch_sale_trans_qty | money | 8 | 1 |  |  |  |
| merch_rtn_amt | money | 8 | 1 |  |  |  |
| merch_rtn_units | money | 8 | 1 |  |  |  |
| merch_rtn_trans_qty | money | 8 | 1 |  |  |  |
| serv_sale_amt | money | 8 | 1 |  |  |  |
| serv_rtn_amt | money | 8 | 1 |  |  |  |
| productive_selling_hours | money | 8 | 1 |  |  |  |
| productive_non_selling_hours | money | 8 | 1 |  |  |  |
| non_productive_hours | money | 8 | 1 |  |  |  |
| comment | nvarchar | 6000 | 1 |  |  |  |
| comment_private | nvarchar | 6000 | 1 |  |  |  |
| private_comment_access | tinyint | 1 | 1 |  |  |  |
| exclude_private_comment | tinyint | 1 | 1 |  |  |  |
| merge_calendar_dates | tinyint | 1 | 1 |  |  |  |
| comp_row_level_only | tinyint | 1 | 1 |  |  |  |
| date_selection_calendar_level | int | 4 | 1 |  |  |  |
| date_range_type | nvarchar | 60 | 1 |  |  |  |
| employee_no | int | 4 | 1 |  |  |  |
| reference_amt_type_list | nvarchar | 6000 | 1 |  |  |  |
| top_X | smallint | 2 | 1 |  |  |  |
| reference_amt_only | tinyint | 1 | 1 |  |  |  |
| include_auto_adj_basis | tinyint | 1 | 1 |  |  |  |
| run_as_trace_execution_time | datetime | 8 | 1 |  |  |  |
| columns_selected | nvarchar | 6000 | 1 |  |  |  |
