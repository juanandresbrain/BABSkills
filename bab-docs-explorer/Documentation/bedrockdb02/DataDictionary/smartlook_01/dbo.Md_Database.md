# dbo.Md_Database

**Database:** smartlook_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| database_id | int | 4 | 0 | YES |  |  |
| database_name | varchar | 30 | 0 |  |  |  |
| server_name | varchar | 30 | 0 |  |  |  |
| database_label_1 | varchar | 30 | 0 |  |  |  |
| database_label_2 | varchar | 30 | 0 |  |  |  |
| database_description_1 | varchar | 255 | 1 |  |  |  |
| database_description_2 | varchar | 255 | 1 |  |  |  |
| db_alias_id | int | 4 | 0 |  |  |  |
| db_group_id | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.Md_AddImplementation](../../StoredProcedures/fn_01/dbo.Md_AddImplementation.md)
- [smartlook_01: dbo.Md_AddImplementation](../../StoredProcedures/smartlook_01/dbo.Md_AddImplementation.md)

