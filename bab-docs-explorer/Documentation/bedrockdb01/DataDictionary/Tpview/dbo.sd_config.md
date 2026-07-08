# dbo.sd_config

**Database:** Tpview  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| inventory_machine | varchar | 30 | 0 |  |  |  |
| inventory_root_path | varchar | 255 | 0 |  |  |  |
| output_machine | varchar | 30 | 0 |  |  |  |
| output_path | varchar | 255 | 0 |  |  |  |
| input_machine | varchar | 30 | 0 |  |  |  |
| input_path | varchar | 255 | 0 |  |  |  |
| job_backup_days | int | 4 | 0 |  |  |  |
| daily_info_file_backups | int | 4 | 0 |  |  |  |
| max_run_time_eod | int | 4 | 0 |  |  |  |
| last_modified | datetime | 8 | 0 |  |  |  |
