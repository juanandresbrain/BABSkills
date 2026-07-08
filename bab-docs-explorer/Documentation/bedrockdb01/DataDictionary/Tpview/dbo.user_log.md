# dbo.user_log

**Database:** Tpview  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| user_id | int | 4 | 0 |  |  |  |
| action_type | int | 4 | 0 |  |  |  |
| action_table_name | varchar | 30 | 0 |  |  |  |
| action_row_id | int | 4 | 0 |  |  |  |
| action_time | datetime | 8 | 0 |  |  |  |
