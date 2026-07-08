# dbo.Sl_Md_TableLink3Ways

**Database:** foundation  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.Sl_Md_TableLink3Ways"]
    dbo_Md_TableLink3Ways(["dbo.Md_TableLink3Ways"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Md_TableLink3Ways |

## View Code

```sql
create view dbo.Sl_Md_TableLink3Ways 
(
	topic_id,
	from_table_id,
	middle_table_id1,
	to_table_id,
	exclusive_count
)
AS SELECT 
	topic_id,
	from_table_id,
	middle_table_id1,
	to_table_id,
	exclusive_count
FROM foundation.dbo.Md_TableLink3Ways
```

