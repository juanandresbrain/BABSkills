# dbo.Sv_Reminder

**Database:** smartlook_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| remind_id | int | 4 | 0 | YES |  |  |
| user_id | int | 4 | 0 |  |  |  |
| remind_user_id | int | 4 | 0 | YES |  |  |
| remind_action | smallint | 2 | 0 |  |  |  |
| action_target | int | 4 | 0 |  |  |  |
| app_id | int | 4 | 0 |  |  |  |
| remind_date | datetime | 8 | 0 |  |  |  |
| remind_msg | varchar | 250 | 1 |  |  |  |
| view_flag | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.Sv_UpdateNextID](../../StoredProcedures/fn_01/dbo.Sv_UpdateNextID.md)
- [smartlook_01: dbo.Sv_UpdateNextID](../../StoredProcedures/smartlook_01/dbo.Sv_UpdateNextID.md)

