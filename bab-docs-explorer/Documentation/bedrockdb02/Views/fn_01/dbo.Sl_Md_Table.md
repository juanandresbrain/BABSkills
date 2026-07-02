# dbo.Sl_Md_Table

**Database:** fn_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.Sl_Md_Table"]
    dbo_Md_Table(["dbo.Md_Table"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Md_Table |

## View Code

```sql
create view [dbo].[Sl_Md_Table] 
(
	table_id,
	table_name,
	pre_code,
	post_code,
	db_alias_id,
	topic_id,
	apply_period,
	multiple_names,
	priority,
	note,
	where_clause)
AS SELECT table_id,
	table_name,
	pre_code,
	post_code,
	db_alias_id,
	topic_id,
	apply_period,
	multiple_names,
	priority,
	note,
	where_clause
FROM fn_01.dbo.Md_Table
```

