# dbo.Sv_UserSession

**Database:** fn_01  
**Server:** bedrockdb02  

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

## Referenced By Stored Procedures

- [fn_01: dbo.Sv_Login](../../StoredProcedures/fn_01/dbo.Sv_Login.md)
- [fn_01: dbo.Sv_Logout](../../StoredProcedures/fn_01/dbo.Sv_Logout.md)
- [fn_01: dbo.Target_Login](../../StoredProcedures/fn_01/dbo.Target_Login.md)
- [fn_01: dbo.Target_Logout](../../StoredProcedures/fn_01/dbo.Target_Logout.md)
- [smartlook_01: dbo.Sv_Login](../../StoredProcedures/smartlook_01/dbo.Sv_Login.md)
- [smartlook_01: dbo.Sv_Logout](../../StoredProcedures/smartlook_01/dbo.Sv_Logout.md)
- [smartlook_01: dbo.Target_Login](../../StoredProcedures/smartlook_01/dbo.Target_Login.md)
- [smartlook_01: dbo.Target_Logout](../../StoredProcedures/smartlook_01/dbo.Target_Logout.md)

