# dbo.vwDW_LineObj_Store_Lookup

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_LineObj_Store_Lookup"]
    dbo_line_object(["dbo.line_object"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.line_object |

## View Code

```sql
CREATE VIEW [dbo].[vwDW_LineObj_Store_Lookup]
AS
SELECT DISTINCT
	  cast([line_object] as int)  [STS_line_object]
      ,case
	   when [line_object_description] like '%#%' 
		  then cast(substring([line_object_description], charindex('#', [line_object_description]) + 1, 10) as int)
	   else
		  cast(0 as int)
	  end [StoreNo]
                    ,cast([line_object] as int)  [Beehive_line_object]
  FROM [dbo].[line_object] with (nolock)
 WHERE line_object_type in (3,6) AND line_object > 600
```

