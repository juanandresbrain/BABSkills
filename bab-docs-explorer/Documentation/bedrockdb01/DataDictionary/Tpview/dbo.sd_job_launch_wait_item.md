# dbo.sd_job_launch_wait_item

**Database:** Tpview  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| row_id | int | 4 | 0 | YES |  |  |
| sd_job_id | int | 4 | 0 |  |  |  |
| wait_time | int | 4 | 0 |  |  |  |
| wait_type | int | 4 | 0 |  |  |  |
| wait_key | varchar | 255 | 0 |  |  |  |
| wait_key_action | int | 4 | 0 |  |  |  |
| wait_key_action_delay | int | 4 | 0 |  |  |  |
| last_modified | datetime | 8 | 0 |  |  |  |
