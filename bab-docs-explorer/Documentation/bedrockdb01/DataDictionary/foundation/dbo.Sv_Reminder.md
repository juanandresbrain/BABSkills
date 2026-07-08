# dbo.Sv_Reminder

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| remind_id | int | 4 | 0 |  |  |  |
| user_id | int | 4 | 0 |  |  |  |
| remind_user_id | int | 4 | 0 |  |  |  |
| remind_action | smallint | 2 | 0 |  |  |  |
| action_target | int | 4 | 0 |  |  |  |
| app_id | int | 4 | 0 |  |  |  |
| remind_date | datetime | 8 | 0 |  |  |  |
| remind_msg | varchar | 250 | 1 |  |  |  |
| view_flag | bit | 1 | 0 |  |  |  |
