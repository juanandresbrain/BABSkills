# dbo.Sv_Statistic

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| exec_id | int | 4 | 0 |  |  |  |
| view_id | int | 4 | 0 |  |  |  |
| query_id | int | 4 | 0 |  |  |  |
| period_id | int | 4 | 0 |  |  |  |
| folder_id | int | 4 | 0 |  |  |  |
| topic_id | int | 4 | 0 |  |  |  |
| user_id | int | 4 | 0 |  |  |  |
| rows_count | int | 4 | 0 |  |  |  |
| cols_count | smallint | 2 | 0 |  |  |  |
| drill_count | int | 4 | 0 |  |  |  |
| table_count | smallint | 2 | 0 |  |  |  |
| drilled_to | bit | 1 | 0 |  |  |  |
| user_cancelled | bit | 1 | 0 |  |  |  |
| data_view_type | char | 1 | 0 |  |  |  |
| start_date_time | datetime | 8 | 0 |  |  |  |
| loading_time | int | 4 | 0 |  |  |  |
| prepare_time | int | 4 | 0 |  |  |  |
| exec_time | int | 4 | 0 |  |  |  |
| retreive_time | int | 4 | 0 |  |  |  |
| usage_time | int | 4 | 0 |  |  |  |
