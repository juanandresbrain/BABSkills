# dbo.trace_sos_overshort_trend

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| execution_datetime | datetime | 8 | 0 |  |  |  |
| store_group_table_name | nvarchar | 80 | 1 |  |  |  |
| language_id | int | 4 | 1 |  |  |  |
| from_date | smalldatetime | 4 | 1 |  |  |  |
| to_date | smalldatetime | 4 | 1 |  |  |  |
| group_by | int | 4 | 1 |  |  |  |
| rec_type | nvarchar | 400 | 1 |  |  |  |
| tender | nvarchar | 800 | 1 |  |  |  |
| drill_cashier | nvarchar | 400 | 1 |  |  |  |
| drill_store | nvarchar | 400 | 1 |  |  |  |
| ve | tinyint | 1 | 1 |  |  |  |
| rec_date | smalldatetime | 4 | 1 |  |  |  |
| cashier_query_list | varchar | 8000 | 1 |  |  |  |
| home_store_query_list | varchar | 8000 | 1 |  |  |  |
| cashier_active_status | smallint | 2 | 1 |  |  |  |
| convert_to_base | tinyint | 1 | 1 |  |  |  |
| currency_code | char | 3 | 1 |  |  |  |
| include_summary_records | tinyint | 1 | 1 |  |  |  |
| drill_reg_loc | nvarchar | 1000 | 1 |  |  |  |
| selling_area_list | varchar | 8000 | 1 |  |  |  |
| run_as_trace_execution_time | datetime | 8 | 1 |  |  |  |
