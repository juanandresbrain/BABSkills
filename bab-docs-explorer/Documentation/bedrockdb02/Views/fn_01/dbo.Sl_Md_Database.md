# dbo.Sl_Md_Database

**Database:** fn_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.Sl_Md_Database"]
    dbo_Md_Database(["dbo.Md_Database"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Md_Database |

## View Code

```sql
create view [dbo].[Sl_Md_Database] 

(
	database_id,
	database_name,
	server_name,
	database_label_1,
	database_label_2,
	database_description_1,
	database_description_2,
	db_alias_id,
	db_group_id
)
AS SELECT 
	database_id,
	database_name,
	server_name,
	database_label_1,
	database_label_2,
	database_description_1,
	database_description_2,
	db_alias_id,
	db_group_id
FROM fn_01.dbo.Md_Database
```

