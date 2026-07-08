# dbo.sd_job_capture_log

**Database:** Tpview  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| row_id | int | 4 | 0 | YES |  |  |
| sd_job_id | int | 4 | 0 |  |  |  |
| capture_log_name | varchar | 255 | 0 |  |  |  |
| capture_log_action | int | 4 | 0 |  |  |  |
| capture_log_action_delay | int | 4 | 0 |  |  |  |
| last_modified | datetime | 8 | 0 |  |  |  |
