# dbo.sd_job

**Database:** Comm  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| sd_job_id | int | 4 | 0 |  |  |  |
| job_id | nvarchar | 108 | 0 |  |  |  |
| job_name | nvarchar | 80 | 0 |  |  |  |
| job_description | nvarchar | 100 | 0 |  |  |  |
| creation_date_time | datetime | 8 | 0 |  |  |  |
| job_version | nvarchar | 20 | 0 |  |  |  |
| new_script | int | 4 | 0 |  |  |  |
| inventory_job_machine | nvarchar | 60 | 0 |  |  |  |
| inventory_job_path | nvarchar | 510 | 0 |  |  |  |
| job_type | int | 4 | 0 |  |  |  |
| command_name | nvarchar | 200 | 0 |  |  |  |
| command_download | int | 4 | 0 |  |  |  |
| command_path | nvarchar | 510 | 0 |  |  |  |
| command_parameters | nvarchar | 510 | 0 |  |  |  |
| database_type | int | 4 | 0 |  |  |  |
| database_name | nvarchar | 510 | 0 |  |  |  |
| database_user | nvarchar | 40 | 0 |  |  |  |
| database_password | nvarchar | 80 | 0 |  |  |  |
| run_as_user | nvarchar | 80 | 0 |  |  |  |
| run_as_password | nvarchar | 80 | 0 |  |  |  |
| reboot | int | 4 | 0 |  |  |  |
| end_of_life_days | int | 4 | 0 |  |  |  |
| max_run_time | int | 4 | 0 |  |  |  |
| hidden_flag | int | 4 | 0 |  |  |  |
| last_modified | datetime | 8 | 0 |  |  |  |
