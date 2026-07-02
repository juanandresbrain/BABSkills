# dbo.Sv_UserTopic

**Database:** smartlook_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| user_id | int | 4 | 0 | YES |  |  |
| topic_id | int | 4 | 0 | YES |  |  |
| view_id | int | 4 | 0 |  |  |  |
| query_id | int | 4 | 0 |  |  |  |
| period_id | int | 4 | 0 |  |  |  |
| sec_query_id | int | 4 | 0 |  |  |  |
| db_group_id | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.Sv_Admin_AddUserToTopic](../../StoredProcedures/fn_01/dbo.Sv_Admin_AddUserToTopic.md)
- [fn_01: dbo.Web_AddUser](../../StoredProcedures/fn_01/dbo.Web_AddUser.md)
- [smartlook_01: dbo.Sv_Admin_AddUserToTopic](../../StoredProcedures/smartlook_01/dbo.Sv_Admin_AddUserToTopic.md)
- [smartlook_01: dbo.Web_AddUser](../../StoredProcedures/smartlook_01/dbo.Web_AddUser.md)

