# dbo.Md_Topic

**Database:** smartlook_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| topic_id | int | 4 | 0 | YES |  |  |
| topic_label_1 | varchar | 30 | 0 |  |  |  |
| topic_label_2 | varchar | 30 | 0 |  |  |  |
| topic_description_1 | varchar | 255 | 1 |  |  |  |
| topic_description_2 | varchar | 255 | 1 |  |  |  |
| system_from_version | float | 8 | 0 |  |  |  |
| system_to_version | float | 8 | 0 |  |  |  |
| data_source_name | varchar | 60 | 1 |  |  |  |
| user_name | varchar | 60 | 1 |  |  |  |
| user_password | varchar | 60 | 1 |  |  |  |
| delete_proc_name | varchar | 40 | 1 |  |  |  |
| md_version | varchar | 30 | 1 |  |  |  |
| md_instdate | datetime | 8 | 1 |  |  |  |
| md_scriptdate | datetime | 8 | 1 |  |  |  |
| extension_manager | varchar | 80 | 1 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |
| sec_app_id | int | 4 | 1 |  |  |  |
| sec_root_key | varchar | 10 | 1 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.Md_LoadLanguage](../../StoredProcedures/fn_01/dbo.Md_LoadLanguage.md)
- [smartlook_01: dbo.Md_LoadLanguage](../../StoredProcedures/smartlook_01/dbo.Md_LoadLanguage.md)

