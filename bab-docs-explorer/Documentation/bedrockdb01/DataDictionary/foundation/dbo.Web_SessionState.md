# dbo.Web_SessionState

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| session_id | numeric | 9 | 0 |  |  |  |
| user_id | int | 4 | 0 |  |  |  |
| topic_id | int | 4 | 0 |  |  |  |
| db_group_id | int | 4 | 0 |  |  |  |
| sub_system | varchar | 20 | 0 |  |  |  |
| nav_level | int | 4 | 0 |  |  |  |
| format_id | int | 4 | 0 |  |  |  |
| language_id | int | 4 | 0 |  |  |  |
| start_time | datetime | 8 | 0 |  |  |  |
| authenticated_topics | varchar | 255 | 1 |  |  |  |
