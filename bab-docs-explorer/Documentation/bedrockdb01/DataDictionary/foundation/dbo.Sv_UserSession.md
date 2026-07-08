# dbo.Sv_UserSession

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| user_id | int | 4 | 0 |  |  |  |
| session_id | int | 4 | 0 |  |  |  |
| serial_no | int | 4 | 1 |  |  |  |
| app_id | int | 4 | 0 |  |  |  |
| db_group_id | int | 4 | 1 |  |  |  |
| target_session_id | int | 4 | 1 |  |  |  |
| target_serial_no | int | 4 | 1 |  |  |  |
| language_id | int | 4 | 1 |  |  |  |
