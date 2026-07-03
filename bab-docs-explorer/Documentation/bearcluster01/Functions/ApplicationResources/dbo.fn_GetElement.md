# dbo.fn_GetElement

**Database:** ApplicationResources  
**Server:** bearcluster01  
**Function Type:** Scalar Function  
**Returns:** int(4)  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.fn_GetElement"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @ord | int | 4 | NO |
| @str | varchar | 8000 | NO |
| @delim | varchar | 1 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql
-- =============================================
-- Author:		Ben Barud
-- Create date: 2017-04-25
-- Description:	http://www.karpach.com/Get-asp-net-profile-value-MS-SQL-database-using-T-SQL.htm
-- =============================================
CREATE FUNCTION dbo.fn_GetElement
(
@ord AS INT,
@str AS VARCHAR(8000),
@delim AS VARCHAR(1) )
 
RETURNS INT
AS
BEGIN
  -- If input is invalid, return null.
  IF @str IS NULL
      OR LEN(@str) = 0
      OR @ord IS NULL
      OR @ord < 1
      -- @ord > [is the] expression that calculates the number of elements.
      OR @ord > LEN(@str) - LEN(REPLACE(@str, @delim, '')) + 1
    RETURN NULL
  DECLARE @pos AS INT, @curord AS INT
  SELECT @pos = 1, @curord = 1
  -- Find next element's start position and increment index.
  WHILE @curord < @ord
    SELECT
      @pos    = CHARINDEX(@delim, @str, @pos) + 1,
      @curord = @curord + 1
  RETURN
  CAST(SUBSTRING(@str, @pos, CHARINDEX(@delim, @str + @delim, @pos) - @pos) AS INT)
END
```
