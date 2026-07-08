# dbo.export_info

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| stream_no | tinyint | 1 | 0 |  |  |  |
| interface_id | tinyint | 1 | 0 |  |  |  |
| export_procedure_name | nvarchar | 60 | 1 |  |  |  |
| export_table_name | nvarchar | 60 | 1 |  |  |  |
| export_table_reclen | smallint | 2 | 1 |  |  |  |
| export_bcp_fmt_name | nvarchar | 60 | 1 |  |  |  |
| export_file_prefix | nvarchar | 60 | 1 |  |  |  |
| export_file_suffix | nvarchar | 60 | 1 |  |  |  |
| export_destination_path | nvarchar | 510 | 1 |  |  |  |
| ftp_flag | tinyint | 1 | 1 |  |  |  |
| ftp_host | nvarchar | 510 | 1 |  |  |  |
| ftp_hid | nvarchar | 100 | 1 |  |  |  |
| ftp_HPWD | nvarchar | 100 | 1 |  |  |  |
| max_retry | tinyint | 1 | 0 |  |  |  |
| current_retry | tinyint | 1 | 0 |  |  |  |
| include_timestamp | tinyint | 1 | 0 |  |  |  |
| current_copy | tinyint | 1 | 0 |  |  |  |
| copy_qty_required | tinyint | 1 | 0 |  |  |  |
| export_completed | tinyint | 1 | 0 |  |  |  |
| export_format | tinyint | 1 | 0 |  |  |  |
| dest_company_code | nvarchar | 510 | 1 |  |  |  |
| add_BOM | smallint | 2 | 0 |  |  |  |
