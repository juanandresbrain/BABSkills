# dbo.Md_QueueKey

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| queue_id | int | 4 | 0 |  |  |  |
| key_sequence | smallint | 2 | 0 |  |  |  |
| key_type | smallint | 2 | 0 |  |  |  |
| key_length | smallint | 2 | 0 |  |  |  |
| key_label | varchar | 30 | 0 |  |  |  |
| key_position | smallint | 2 | 0 |  |  |  |
| key_precision | smallint | 2 | 1 |  |  |  |
