# dbo.employee_transaction_role

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| employee_transaction_role | nvarchar | 40 | 0 |  |  |  |
| employee_transaction_role_desc | nvarchar | 510 | 0 |  |  |  |
| identified_in_transaction_flag | tinyint | 1 | 0 |  |  |  |
| cashier_flag | tinyint | 1 | 0 |  |  |  |
| salesperson_flag | tinyint | 1 | 0 |  |  |  |
| salesperson2_flag | tinyint | 1 | 0 |  |  |  |
| salesperson_note_type | smallint | 2 | 1 |  |  |  |
| salesperson_line_note | nvarchar | 40 | 1 |  |  |  |
| salesperson2_note_type | smallint | 2 | 1 |  |  |  |
| salesperson2_line_note | nvarchar | 40 | 1 |  |  |  |
| transaction_role_note_type | smallint | 2 | 1 |  |  |  |
| track_in_commission_flag | tinyint | 1 | 0 |  |  |  |
| track_in_productivity_flag | tinyint | 1 | 0 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |
| rtn_salesperson_flag | tinyint | 1 | 1 |  |  |  |
| rtn_salesperson2_flag | tinyint | 1 | 1 |  |  |  |
| salesperson_note_type_optional | tinyint | 1 | 0 |  |  |  |
| salespersn2_note_type_optional | tinyint | 1 | 0 |  |  |  |
| report_sort_sequence | int | 4 | 0 |  |  |  |
| commission_export_column_no | tinyint | 1 | 0 |  |  |  |
| remap_from_transaction_role | nvarchar | 40 | 1 |  |  |  |
| remap_on_presence_of_tran_role | nvarchar | 40 | 1 |  |  |  |
| commission_export_group_code | nvarchar | 40 | 1 |  |  |  |
