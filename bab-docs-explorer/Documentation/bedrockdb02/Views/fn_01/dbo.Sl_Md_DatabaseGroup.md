# dbo.Sl_Md_DatabaseGroup

**Database:** fn_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.Sl_Md_DatabaseGroup"]
    dbo_Md_DatabaseGroup(["dbo.Md_DatabaseGroup"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Md_DatabaseGroup |

## View Code

```sql
CREATE VIEW [dbo].[Sl_Md_DatabaseGroup] (db_group_id,db_group_label_1,db_group_label_2,db_group_description_1,db_group_description_2,data_source_name,user_name,user_password,vdb_name,topic_id,file_dsn_info,server_name,group_type,resource_id,sec_company_id)
AS SELECT db_group_id,db_group_label_1,db_group_label_2,db_group_description_1,db_group_description_2,data_source_name,user_name,user_password,vdb_name,topic_id,file_dsn_info,server_name,group_type,resource_id,sec_company_id
FROM fn_01.dbo.Md_DatabaseGroup
```

