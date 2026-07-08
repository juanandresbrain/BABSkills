# dbo.master_table_subscription

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| interface_id | tinyint | 1 | 0 |  |  |  |
| table_name | varchar | 30 | 0 |  |  |  |
| export_module_name | varchar | 255 | 0 |  |  |  |
| last_modification_datetime | datetime | 8 | 0 |  |  |  |
| last_export_datetime | datetime | 8 | 0 |  |  |  |
| export_status | tinyint | 1 | 0 |  |  |  |
| sequence_no | smallint | 2 | 1 |  |  |  |
| update_timing | smallint | 2 | 1 |  |  |  |
| export_table_name | varchar | 30 | 1 |  |  |  |
| export_bcp_fmt_name | varchar | 30 | 1 |  |  |  |
| export_file_prefix | varchar | 30 | 1 |  |  |  |
| export_file_suffix | varchar | 30 | 1 |  |  |  |
| last_retrieval_datetime | datetime | 8 | 1 |  |  |  |
| active_flag | tinyint | 1 | 0 |  |  |  |
