# dbo.export_format_10052010

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| interface_id | tinyint | 1 | 0 |  |  |  |
| export_format | tinyint | 1 | 0 |  |  |  |
| export_format_description | varchar | 255 | 0 |  |  |  |
| export_procedure_name | varchar | 30 | 1 |  |  |  |
| export_bcp_fmt_name | varchar | 30 | 1 |  |  |  |
| export_table_name | varchar | 30 | 1 |  |  |  |
| export_table_reclen | smallint | 2 | 1 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |
| export_file_prefix | varchar | 30 | 1 |  |  |  |
| export_file_suffix | varchar | 30 | 1 |  |  |  |
| export_destination_path | varchar | 255 | 1 |  |  |  |
| ftp_flag | smallint | 2 | 1 |  |  |  |
| ftp_host | varchar | 30 | 1 |  |  |  |
| ftp_hid | varchar | 30 | 1 |  |  |  |
| ftp_HPWD | varchar | 30 | 1 |  |  |  |
| auto_set_posting_request | tinyint | 1 | 0 |  |  |  |
| max_retry_qty | tinyint | 1 | 0 |  |  |  |
| stream_no | tinyint | 1 | 0 |  |  |  |
| include_timestamp | tinyint | 1 | 0 |  |  |  |
| copy_no | tinyint | 1 | 0 |  |  |  |
| if_export_code | smallint | 2 | 1 |  |  |  |
