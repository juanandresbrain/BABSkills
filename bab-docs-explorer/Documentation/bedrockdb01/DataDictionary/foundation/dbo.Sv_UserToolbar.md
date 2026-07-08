# dbo.Sv_UserToolbar

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| user_id | int | 4 | 0 |  |  |  |
| topic_id | int | 4 | 0 |  |  |  |
| item_sequence | smallint | 2 | 0 |  |  |  |
| button_id | int | 4 | 0 |  |  |  |
| button_info | varchar | 255 | 1 |  |  |  |
| button_help | varchar | 80 | 1 |  |  |  |
| app_id | int | 4 | 1 |  |  |  |
