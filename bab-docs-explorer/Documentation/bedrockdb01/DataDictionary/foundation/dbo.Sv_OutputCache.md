# dbo.Sv_OutputCache

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| cache_file_id | int | 4 | 0 |  |  |  |
| view_id | int | 4 | 0 |  |  |  |
| query_id | int | 4 | 0 |  |  |  |
| period_id | int | 4 | 0 |  |  |  |
| db_group_id | int | 4 | 0 |  |  |  |
| security_query_id | int | 4 | 0 |  |  |  |
| dynamic_query | varchar | 255 | 1 |  |  |  |
| qparameters_bag | varchar | 255 | 1 |  |  |  |
| created_datetime | datetime | 8 | 0 |  |  |  |
| valid_until | datetime | 8 | 0 |  |  |  |
| locked | bit | 1 | 0 |  |  |  |
