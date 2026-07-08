# dbo.export_format_20190606

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| interface_id | tinyint | 1 | 0 |  |  |  |
| export_format | tinyint | 1 | 0 |  |  |  |
| export_format_description | nvarchar | 510 | 0 |  |  |  |
| export_procedure_name | nvarchar | 60 | 1 |  |  |  |
| export_bcp_fmt_name | nvarchar | 60 | 1 |  |  |  |
| export_table_name | nvarchar | 60 | 1 |  |  |  |
| export_table_reclen | smallint | 2 | 1 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |
| export_file_prefix | nvarchar | 60 | 1 |  |  |  |
| export_file_suffix | nvarchar | 60 | 1 |  |  |  |
| export_destination_path | nvarchar | 510 | 1 |  |  |  |
| ftp_flag | smallint | 2 | 1 |  |  |  |
| ftp_host | nvarchar | 510 | 1 |  |  |  |
| ftp_hid | nvarchar | 100 | 1 |  |  |  |
| ftp_HPWD | nvarchar | 100 | 1 |  |  |  |
| auto_set_posting_request | tinyint | 1 | 0 |  |  |  |
| max_retry_qty | tinyint | 1 | 0 |  |  |  |
| stream_no | tinyint | 1 | 0 |  |  |  |
| include_timestamp | tinyint | 1 | 0 |  |  |  |
| copy_no | tinyint | 1 | 0 |  |  |  |
| if_export_code | smallint | 2 | 1 |  |  |  |
| batch_size | int | 4 | 1 |  |  |  |
| add_BOM | smallint | 2 | 0 |  |  |  |
