# dbo.com_application

**Database:** Comm  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| location_id | int | 4 | 0 |  |  |  |
| device_id | int | 4 | 0 |  |  |  |
| application_id | int | 4 | 0 |  |  |  |
| register_id | int | 4 | 1 |  |  |  |
| application_type_id | int | 4 | 0 |  |  |  |
| add_info_1 | nvarchar | 40 | 1 |  |  |  |
| add_info_2 | nvarchar | 40 | 1 |  |  |  |
| add_info_3 | nvarchar | 40 | 1 |  |  |  |
| server_assigned_id | nvarchar | 100 | 0 |  |  |  |
| last_modified | datetime | 8 | 0 |  |  |  |
| row_id | int | 4 | 0 | YES |  |  |
| max_log_file_size | int | 4 | 1 |  |  |  |
| log_files_per_day | int | 4 | 1 |  |  |  |
| number_of_log_days | int | 4 | 1 |  |  |  |
