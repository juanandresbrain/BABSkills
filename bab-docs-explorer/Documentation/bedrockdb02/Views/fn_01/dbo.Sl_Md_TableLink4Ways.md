# dbo.Sl_Md_TableLink4Ways

**Database:** fn_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.Sl_Md_TableLink4Ways"]
    dbo_Md_TableLink4Ways(["dbo.Md_TableLink4Ways"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Md_TableLink4Ways |

## View Code

```sql
create view [dbo].[Sl_Md_TableLink4Ways] 
(
	topic_id,
	from_table_id,
	middle_table_id1,
	middle_table_id2,
	to_table_id,
	exclusive_count
)
AS SELECT 
	topic_id,
	from_table_id,
	middle_table_id1,
	middle_table_id2,
	to_table_id,
	exclusive_count
FROM fn_01.dbo.Md_TableLink4Ways
```

