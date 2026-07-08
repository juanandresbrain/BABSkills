# dbo.vwDW_Tender_Dim

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_Tender_Dim"]
    dbo_line_object(["dbo.line_object"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.line_object |

## View Code

```sql
CREATE VIEW [dbo].[vwDW_Tender_Dim]
AS
SELECT cast([line_object] as varchar(5)) AS tender_code
      ,cast(substring([line_object_description], 1, 50) as varchar(50)) AS tender_desc
  FROM [auditworks].[dbo].[line_object] with (nolock)
 WHERE [line_object_type] = 6
```

