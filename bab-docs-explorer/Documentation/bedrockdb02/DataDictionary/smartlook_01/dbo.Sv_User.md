# dbo.Sv_User

**Database:** smartlook_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| user_id | int | 4 | 0 | YES |  |  |
| user_name | varchar | 30 | 0 |  |  |  |
| user_fullname | varchar | 30 | 1 |  |  |  |
| user_level | smallint | 2 | 0 |  |  |  |
| topic_id | int | 4 | 0 |  |  |  |
| flags | char | 20 | 0 |  |  |  |
| mail_user_name | varchar | 150 | 1 |  |  |  |
| mail_password | varchar | 30 | 1 |  |  |  |
| logo_filename | varchar | 255 | 1 |  |  |  |
| check_mail_interval | smallint | 2 | 0 |  |  |  |
| user_password | varchar | 60 | 1 |  |  |  |
| user_status | smallint | 2 | 1 |  |  |  |
| email_address | varchar | 80 | 1 |  |  |  |
| language_id | int | 4 | 1 |  |  |  |
| pc_language_id | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.Sv_Admin_AddUserToSv18](../../StoredProcedures/fn_01/dbo.Sv_Admin_AddUserToSv18.md)
- [fn_01: dbo.Sv_UpdateNextID](../../StoredProcedures/fn_01/dbo.Sv_UpdateNextID.md)
- [fn_01: dbo.Web_AddUser](../../StoredProcedures/fn_01/dbo.Web_AddUser.md)
- [smartlook_01: dbo.Sv_Admin_AddUserToSv18](../../StoredProcedures/smartlook_01/dbo.Sv_Admin_AddUserToSv18.md)
- [smartlook_01: dbo.Sv_UpdateNextID](../../StoredProcedures/smartlook_01/dbo.Sv_UpdateNextID.md)
- [smartlook_01: dbo.Web_AddUser](../../StoredProcedures/smartlook_01/dbo.Web_AddUser.md)

