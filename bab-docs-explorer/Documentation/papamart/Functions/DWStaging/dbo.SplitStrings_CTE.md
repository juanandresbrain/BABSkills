# dbo.SplitStrings_CTE

**Database:** DWStaging  
**Server:** papamart  
**Function Type:** Table-Valued Function  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.SplitStrings_CTE"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @List | nvarchar | -1 | NO |
| @Delimiter | nvarchar | 510 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql
CREATE FUNCTION dbo.SplitStrings_CTE
(
   @List       NVARCHAR(MAX),
   @Delimiter  NVARCHAR(255)
)
RETURNS @Items TABLE (Item NVARCHAR(4000))
WITH SCHEMABINDING
AS
BEGIN
   DECLARE @ll INT = LEN(@List) + 1, @ld INT = LEN(@Delimiter);
 
   WITH a AS
   (
       SELECT
           [start] = 1,
           [end]   = COALESCE(NULLIF(CHARINDEX(@Delimiter, 
                       @List, 1), 0), @ll),
           [value] = SUBSTRING(@List, 1, 
                     COALESCE(NULLIF(CHARINDEX(@Delimiter, 
                       @List, 1), 0), @ll) - 1)
       UNION ALL
       SELECT
           [start] = CONVERT(INT, [end]) + @ld,
           [end]   = COALESCE(NULLIF(CHARINDEX(@Delimiter, 
                       @List, [end] + @ld), 0), @ll),
           [value] = SUBSTRING(@List, [end] + @ld, 
                     COALESCE(NULLIF(CHARINDEX(@Delimiter, 
                       @List, [end] + @ld), 0), @ll)-[end]-@ld)
       FROM a
       WHERE [end] < @ll
   )
   INSERT @Items SELECT [value]
   FROM a
   WHERE LEN([value]) > 0
   OPTION (MAXRECURSION 0);
 
   RETURN;
END
```

