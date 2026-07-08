# dbo.cl_check_import_file_list

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| file_id | int | 4 | 0 | YES |  |  |
| file_name | varchar | 80 | 1 |  |  |  |
| backup_folder | varchar | 20 | 1 |  |  |  |
| file_date | smalldatetime | 4 | 1 |  |  |  |
| record_count | int | 4 | 1 |  |  |  |
| ict_import_filename | varchar | 20 | 1 |  |  |  |
| validate_status | varchar | 20 | 1 |  |  |  |
