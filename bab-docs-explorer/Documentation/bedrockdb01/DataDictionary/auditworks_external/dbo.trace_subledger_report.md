# dbo.trace_subledger_report

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| execution_datetime | datetime | 8 | 0 |  |  |  |
| store_group_table_name | nvarchar | 80 | 1 |  |  |  |
| language_id | int | 4 | 1 |  |  |  |
| from_date | smalldatetime | 4 | 1 |  |  |  |
| to_date | smalldatetime | 4 | 1 |  |  |  |
| include_date | tinyint | 1 | 1 |  |  |  |
| include_store | tinyint | 1 | 1 |  |  |  |
| include_object_action | tinyint | 1 | 1 |  |  |  |
| convert_to_base | tinyint | 1 | 1 |  |  |  |
| currency_code | char | 3 | 1 |  |  |  |
| trans_category_restriction | varchar | 8000 | 1 |  |  |  |
| object_action_restriction | varchar | 8000 | 1 |  |  |  |
| gl_account_restriction | varchar | 8000 | 1 |  |  |  |
| run_as_trace_execution_time | datetime | 8 | 1 |  |  |  |
| unit_of_measure_restriction | varchar | 8000 | 1 |  |  |  |
