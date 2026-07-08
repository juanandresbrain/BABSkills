# dbo.Md_QueueDef

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| queue_id | int | 4 | 0 |  |  |  |
| topic_id | int | 4 | 0 |  |  |  |
| description_1 | varchar | 255 | 0 |  |  |  |
| description_2 | varchar | 255 | 0 |  |  |  |
| keep_hours | int | 4 | 0 |  |  |  |
| table_id | int | 4 | 0 |  |  |  |
| delete_proc_name | varchar | 40 | 1 |  |  |  |
