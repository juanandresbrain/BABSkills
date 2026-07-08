# dbo.trace_media_rec_report

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
| rdl_number | int | 4 | 1 |  |  |  |
| rec_types | nvarchar | 400 | 1 |  |  |  |
| bal_methods | nvarchar | 400 | 1 |  |  |  |
| bal_ents | nvarchar | 400 | 1 |  |  |  |
| combine_all_dates | int | 4 | 1 |  |  |  |
| store_no | int | 4 | 1 |  |  |  |
| cashier_no | int | 4 | 1 |  |  |  |
| rec_date | smalldatetime | 4 | 1 |  |  |  |
| run_as_trace_execution_time | datetime | 8 | 1 |  |  |  |
