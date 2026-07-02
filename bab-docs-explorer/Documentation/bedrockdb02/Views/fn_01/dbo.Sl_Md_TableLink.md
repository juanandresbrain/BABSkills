# dbo.Sl_Md_TableLink

**Database:** fn_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.Sl_Md_TableLink"]
    dbo_Md_TableLink(["dbo.Md_TableLink"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Md_TableLink |

## View Code

```sql
create view [dbo].[Sl_Md_TableLink] 
(
	from_table_id,
	from_exp,
	join_exp,
	to_table_id,
	to_exp,
	temp_table_id,
	temp_join_exp,
	from_temp_exp,
	temp_to_exp)
AS SELECT 	from_table_id,
	from_exp,
	join_exp,
	to_table_id,
	to_exp,
	temp_table_id,
	temp_join_exp,
	from_temp_exp,
	temp_to_exp
FROM fn_01.dbo.Md_TableLink
```

