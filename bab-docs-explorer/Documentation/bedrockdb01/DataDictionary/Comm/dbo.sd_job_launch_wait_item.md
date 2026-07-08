# dbo.sd_job_launch_wait_item

**Database:** Comm  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| row_id | int | 4 | 0 |  |  |  |
| sd_job_id | int | 4 | 0 |  |  |  |
| wait_time | int | 4 | 0 |  |  |  |
| wait_type | int | 4 | 0 |  |  |  |
| wait_key | nvarchar | 510 | 0 |  |  |  |
| wait_key_action | int | 4 | 0 |  |  |  |
| wait_key_action_delay | int | 4 | 0 |  |  |  |
| last_modified | datetime | 8 | 0 |  |  |  |
