# dbo.import_availability

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| import_id | numeric | 5 | 0 |  |  |  |
| import_control_file | nvarchar | 60 | 0 |  |  |  |
| import_file_suffix | nvarchar | 60 | 1 |  |  |  |
| from_document_release_no | nvarchar | 40 | 0 |  |  |  |
| to_document_release_no | nvarchar | 40 | 1 |  |  |  |
| import_description | nvarchar | 140 | 0 |  |  |  |
| import_table_name | nvarchar | 60 | 1 |  |  |  |
| import_procedure_name | nvarchar | 60 | 0 |  |  |  |
| import_format_name | nvarchar | 60 | 1 |  |  |  |
| import_priority | numeric | 5 | 1 |  |  |  |
| load_data_via_secondary_db | nchar | 2 | 0 |  |  |  |
| preprocessing_command | nvarchar | 60 | 0 |  |  |  |
