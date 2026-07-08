# dbo.sd_config

**Database:** Comm  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| inventory_machine | nvarchar | 60 | 0 |  |  |  |
| inventory_root_path | nvarchar | 510 | 0 |  |  |  |
| output_machine | nvarchar | 60 | 0 |  |  |  |
| output_path | nvarchar | 510 | 0 |  |  |  |
| input_machine | nvarchar | 60 | 0 |  |  |  |
| input_path | nvarchar | 510 | 0 |  |  |  |
| job_backup_days | int | 4 | 0 |  |  |  |
| daily_info_file_backups | int | 4 | 0 |  |  |  |
| max_run_time_eod | int | 4 | 0 |  |  |  |
| last_modified | datetime | 8 | 0 |  |  |  |
