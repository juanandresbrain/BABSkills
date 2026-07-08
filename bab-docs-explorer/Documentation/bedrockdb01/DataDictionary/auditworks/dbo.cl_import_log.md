# dbo.cl_import_log

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| import_id | int | 4 | 0 | YES |  |  |
| cl_load_status | varchar | 20 | 1 |  |  |  |
| import_start | smalldatetime | 4 | 1 |  |  |  |
| import_end | smalldatetime | 4 | 1 |  |  |  |
| file_count | int | 4 | 1 |  |  |  |
| backup_folder | varchar | 20 | 1 |  |  |  |
| records_to_load | int | 4 | 1 |  |  |  |
| records_match_sa | int | 4 | 1 |  |  |  |
| not_in_sa | int | 4 | 1 |  |  |  |
