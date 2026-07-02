# dbo.Md_DatabaseGroup

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| db_group_id | int | 4 | 0 | YES |  |  |
| db_group_label_1 | varchar | 30 | 0 |  |  |  |
| db_group_label_2 | varchar | 30 | 0 |  |  |  |
| db_group_description_1 | varchar | 255 | 1 |  |  |  |
| db_group_description_2 | varchar | 255 | 1 |  |  |  |
| data_source_name | varchar | 60 | 1 |  |  |  |
| user_name | varchar | 60 | 1 |  |  |  |
| user_password | varchar | 60 | 1 |  |  |  |
| vdb_name | varchar | 30 | 1 |  |  |  |
| topic_id | int | 4 | 0 |  |  |  |
| file_dsn_info | text | 16 | 1 |  |  |  |
| server_name | varchar | 60 | 1 |  |  |  |
| group_type | int | 4 | 1 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |
| sec_company_id | int | 4 | 1 |  |  |  |
| sec_product_id | varchar | 30 | 1 |  |  |  |
| sec_app_id | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.Md_AddImplementation](../../StoredProcedures/fn_01/dbo.Md_AddImplementation.md)
- [fn_01: dbo.Sv_Admin_AddUserToTopic](../../StoredProcedures/fn_01/dbo.Sv_Admin_AddUserToTopic.md)
- [smartlook_01: dbo.Md_AddImplementation](../../StoredProcedures/smartlook_01/dbo.Md_AddImplementation.md)
- [smartlook_01: dbo.Sv_Admin_AddUserToTopic](../../StoredProcedures/smartlook_01/dbo.Sv_Admin_AddUserToTopic.md)

