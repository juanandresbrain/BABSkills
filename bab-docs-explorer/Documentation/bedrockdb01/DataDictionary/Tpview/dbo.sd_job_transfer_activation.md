# dbo.sd_job_transfer_activation

**Database:** Tpview  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| sd_job_transfer_activation_id | int | 4 | 0 | YES |  |  |
| sd_job_id | int | 4 | 0 |  |  |  |
| scheduling_type | int | 4 | 0 |  |  |  |
| from_date_time | datetime | 8 | 0 |  |  |  |
| time_day_start | datetime | 8 | 0 |  |  |  |
| time_day_stop | datetime | 8 | 0 |  |  |  |
| activation_type | int | 4 | 0 |  |  |  |
| activation_scheduling_type | int | 4 | 0 |  |  |  |
| activation_date_time | datetime | 8 | 0 |  |  |  |
| activation_time_day_start | datetime | 8 | 0 |  |  |  |
| activation_time_day_stop | datetime | 8 | 0 |  |  |  |
| eod_scheduling | int | 4 | 0 |  |  |  |
| job_file_name | varchar | 255 | 0 |  |  |  |
| activation_file_only | int | 4 | 0 |  |  |  |
| last_modified | datetime | 8 | 0 |  |  |  |
