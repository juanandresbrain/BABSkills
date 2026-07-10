# dbo.fn_String_To_Table

**Database:** dw  
**Server:** papamart  
**Function Type:** Table-Valued Function  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.fn_String_To_Table"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @String | varchar | -1 | NO |
| @Delimeter | char | 1 | NO |
| @TrimSpace | bit | 1 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql
CREATE FUNCTION [dbo].[fn_String_To_Table](@String    VARCHAR(MAX),
/* input string */                         @Delimeter CHAR(1),
/* delimiter */                            @TrimSpace BIT
                                           ) /* kill whitespace? */
RETURNS @Table TABLE(
	[Val] VARCHAR(4000)
)
AS
BEGIN
	DECLARE @Val VARCHAR(4000)
	WHILE LEN(@String) > 0
	BEGIN
		SET @Val = left(@String,
		isnull(nullif(CHARINDEX(@Delimeter, @String) - 1, -1),
		LEN(@String)))
		SET @String = substring(@String,
		isnull(nullif(CHARINDEX(@Delimeter, @String), 0),
		LEN(@String)) + 1, LEN(@String))
		IF @TrimSpace = 1
			SET @Val = LTRIM(RTRIM(@Val))
		-- Eliminate Duplicates			
		IF EXISTS (SELECT 1
				   FROM
					   @Table
				   WHERE
					   Val = @Val)
			-- If it is, do nothing
			SET @Val = @Val
		ELSE
			-- If it isn't, then add it to the table
			INSERT
			INTO
				@Table ([Val])
			VALUES
				(@Val)
	END
	RETURN
END
```

