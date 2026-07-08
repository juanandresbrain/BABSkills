# dbo.import_info

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| import_id | numeric | 5 | 0 |  |  |  |
| import_file_prefix | nvarchar | 60 | 0 |  |  |  |
| import_file_suffix | nvarchar | 60 | 0 |  |  |  |
| import_description | nvarchar | 140 | 0 |  |  |  |
| import_table_name | nvarchar | 60 | 0 |  |  |  |
| import_procedure_name | nvarchar | 60 | 0 |  |  |  |
| import_format_name | nvarchar | 60 | 0 |  |  |  |
| import_time_stamp | nvarchar | 60 | 0 |  |  |  |
| load_data_via_secondary_db | nchar | 2 | 0 |  |  |  |
| preprocessing_command | nvarchar | 60 | 0 |  |  |  |
