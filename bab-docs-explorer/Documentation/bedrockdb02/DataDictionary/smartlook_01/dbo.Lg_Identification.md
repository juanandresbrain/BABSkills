# dbo.Lg_Identification

**Database:** smartlook_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| language_id | int | 4 | 0 | YES |  |  |
| english_desc | varchar | 30 | 1 |  |  |  |
| display_desc | varchar | 30 | 1 |  |  |  |
| active_flag | tinyint | 1 | 0 |  |  |  |
| column_position | tinyint | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.Md_LoadLanguage](../../StoredProcedures/fn_01/dbo.Md_LoadLanguage.md)
- [fn_01: dbo.Sv_Admin_AddUserToSv18](../../StoredProcedures/fn_01/dbo.Sv_Admin_AddUserToSv18.md)
- [fn_01: dbo.Web_AddUser](../../StoredProcedures/fn_01/dbo.Web_AddUser.md)
- [smartlook_01: dbo.Md_LoadLanguage](../../StoredProcedures/smartlook_01/dbo.Md_LoadLanguage.md)
- [smartlook_01: dbo.Sv_Admin_AddUserToSv18](../../StoredProcedures/smartlook_01/dbo.Sv_Admin_AddUserToSv18.md)
- [smartlook_01: dbo.Web_AddUser](../../StoredProcedures/smartlook_01/dbo.Web_AddUser.md)

