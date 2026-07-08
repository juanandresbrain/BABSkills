# dbo.sd_job_capture_log

**Database:** Comm  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| row_id | int | 4 | 0 |  |  |  |
| sd_job_id | int | 4 | 0 |  |  |  |
| capture_log_name | nvarchar | 510 | 0 |  |  |  |
| capture_log_action | int | 4 | 0 |  |  |  |
| capture_log_action_delay | int | 4 | 0 |  |  |  |
| last_modified | datetime | 8 | 0 |  |  |  |
