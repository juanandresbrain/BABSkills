# dbo.Sl_Md_Topic

**Database:** fn_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.Sl_Md_Topic"]
    dbo_Md_Topic(["dbo.Md_Topic"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Md_Topic |

## View Code

```sql
create view [dbo].[Sl_Md_Topic] 
(topic_id, topic_label_1, topic_label_2, topic_description_1, topic_description_2, system_from_version, system_to_version, data_source_name, user_name, user_password, delete_proc_name, md_version, md_instdate, md_scriptdate, extension_manager, resource_id, sec_app_id, sec_root_key)
AS SELECT topic_id, topic_label_1, topic_label_2, topic_description_1, topic_description_2, system_from_version, system_to_version, data_source_name, user_name, user_password, delete_proc_name, md_version, md_instdate, md_scriptdate, extension_manager, resource_id, sec_app_id, sec_root_key
FROM fn_01.dbo.Md_Topic
```

