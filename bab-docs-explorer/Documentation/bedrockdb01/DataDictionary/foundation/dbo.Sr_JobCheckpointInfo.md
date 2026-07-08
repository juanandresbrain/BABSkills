# dbo.Sr_JobCheckpointInfo

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| job_id | int | 4 | 0 |  |  |  |
| execution_id | int | 4 | 0 |  |  |  |
| checkpoint_no | int | 4 | 0 |  |  |  |
| checkpoint_info | text | 16 | 1 |  |  |  |
| record_time | datetime | 8 | 0 |  |  |  |
