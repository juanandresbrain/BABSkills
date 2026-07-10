# dbo.fn_split_inline_cte

**Database:** DBAUtility  
**Server:** papamart  
**Function Type:** Inline Table-Valued Function  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.fn_split_inline_cte"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @list | nvarchar | -1 | NO |
| @delimiter | nchar | 2 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql
CREATE FUNCTION [dbo].[fn_split_inline_cte]
 (@list  NVARCHAR(MAX),
  @delimiter NCHAR(1) = ',') 
    RETURNS TABLE 
AS

RETURN
    WITH cte_list([BeginChar], [EndChar]) AS (
        SELECT [BeginChar] = CONVERT(BIGINT, 1), [EndChar] = CHARINDEX(@delimiter, @list + @delimiter)
    UNION ALL
        SELECT [BeginChar] = [EndChar] + 1, [EndChar] = CHARINDEX(@delimiter, @list + @delimiter, [EndChar] + 1)
    FROM cte_list
        WHERE  [EndChar] > 0
    )
    SELECT LTRIM(RTRIM(SUBSTRING(@list, [BeginChar],
        CASE WHEN [EndChar] > 0 THEN [EndChar] - [BeginChar] ELSE 0 END))) AS [ParsedValue]
    FROM cte_list
        WHERE [EndChar] > 0 ;
```

