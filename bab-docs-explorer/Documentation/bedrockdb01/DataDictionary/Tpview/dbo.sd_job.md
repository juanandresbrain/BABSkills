# dbo.sd_job

**Database:** Tpview  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| sd_job_id | int | 4 | 0 | YES |  |  |
| job_id | varchar | 54 | 0 |  |  |  |
| job_name | varchar | 40 | 0 |  |  |  |
| job_description | varchar | 50 | 0 |  |  |  |
| creation_date_time | datetime | 8 | 0 |  |  |  |
| job_version | varchar | 10 | 0 |  |  |  |
| new_script | int | 4 | 0 |  |  |  |
| inventory_job_machine | varchar | 30 | 0 |  |  |  |
| inventory_job_path | varchar | 255 | 0 |  |  |  |
| job_type | int | 4 | 0 |  |  |  |
| command_name | varchar | 100 | 0 |  |  |  |
| command_download | int | 4 | 0 |  |  |  |
| command_path | varchar | 255 | 0 |  |  |  |
| command_parameters | varchar | 255 | 0 |  |  |  |
| database_type | int | 4 | 0 |  |  |  |
| database_name | varchar | 255 | 0 |  |  |  |
| database_user | varchar | 20 | 0 |  |  |  |
| database_password | varchar | 40 | 0 |  |  |  |
| run_as_user | varchar | 40 | 0 |  |  |  |
| run_as_password | varchar | 40 | 0 |  |  |  |
| reboot | int | 4 | 0 |  |  |  |
| end_of_life_days | int | 4 | 0 |  |  |  |
| max_run_time | int | 4 | 0 |  |  |  |
| hidden_flag | int | 4 | 0 |  |  |  |
| last_modified | datetime | 8 | 0 |  |  |  |
