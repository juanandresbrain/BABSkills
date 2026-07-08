# dbo.Tr_PollFileHistory

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| id | int | 4 | 0 |  |  |  |
| dir_id | int | 4 | 0 |  |  |  |
| filename | varchar | 30 | 0 |  |  |  |
| output_mask | varchar | 30 | 1 |  |  |  |
| execution_id | int | 4 | 1 |  |  |  |
| file_size | int | 4 | 0 |  |  |  |
| transactions | int | 4 | 1 |  |  |  |
| status | int | 4 | 0 |  |  |  |
| translate_type | int | 4 | 1 |  |  |  |
| translate_version | int | 4 | 1 |  |  |  |
| start_time | datetime | 8 | 0 |  |  |  |
| history_date_time | datetime | 8 | 0 |  |  |  |
