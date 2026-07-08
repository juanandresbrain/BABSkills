# dbo.Md_Topic

**Database:** foundation  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| topic_id | int | 4 | 0 |  |  |  |
| topic_label_1 | varchar | 60 | 0 |  |  |  |
| topic_label_2 | varchar | 60 | 0 |  |  |  |
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
| topic_label_resource_name | nvarchar | 510 | 1 |  |  |  |
| topic_lcid | nvarchar | 510 | 1 |  |  |  |
| topic_desc_resource_name | nvarchar | 510 | 1 |  |  |  |
