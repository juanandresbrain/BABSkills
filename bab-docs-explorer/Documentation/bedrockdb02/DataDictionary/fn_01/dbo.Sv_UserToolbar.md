# dbo.Sv_UserToolbar

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| user_id | int | 4 | 0 | YES |  |  |
| topic_id | int | 4 | 0 | YES |  |  |
| item_sequence | smallint | 2 | 0 | YES |  |  |
| button_id | int | 4 | 0 |  |  |  |
| button_info | varchar | 255 | 1 |  |  |  |
| button_help | varchar | 80 | 1 |  |  |  |
| app_id | int | 4 | 1 |  |  |  |

