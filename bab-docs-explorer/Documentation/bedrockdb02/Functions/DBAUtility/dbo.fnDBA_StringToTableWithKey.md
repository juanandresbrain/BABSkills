# dbo.fnDBA_StringToTableWithKey

**Database:** DBAUtility  
**Server:** bedrockdb02  
**Function Type:** Table-Valued Function  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.fnDBA_StringToTableWithKey"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @Key | varchar | 128 | NO |
| @String | varchar | 2000 | NO |
| @Delimeter | char | 1 | NO |
| @TrimSpace | bit | 1 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql

CREATE FUNCTION [dbo].[fnDBA_StringToTableWithKey](
	@Key VARCHAR(128),
	@String    VARCHAR(2000) /* input string */,
	@Delimeter CHAR(1) /* delimiter */,
	@TrimSpace BIT /* kill whitespace? */
) 
RETURNS @Table TABLE(
	[Key] VARCHAR(128),
	[Val] VARCHAR(4000)
)
AS
BEGIN
-- =============================================================================================================
-- Name: fnDBA_StringToTableWithKey
--
-- Description:	Creates a "table" based on the Key and Value passed in.
-- The Value variable is split based on the Delimeter.

-- Output: Table with the key and values in each row
--
-- Dependencies: N/A
--
-- Revision History
--		Name:			Date:			Comments:
--		Shawn Burge		08/13/2012		Created based on existing function
--		Mike P			08/27/2012		Changed VARCHAR(MAX) to VARCHAR(2000)
 	 
----------------------------------------------------------------------------------------------------
--// Revision                                                                                //--
----------------------------------------------------------------------------------------------------
	DECLARE @Revision DATETIME
	SET @Revision = '08/27/2012'
----------------------------------------------------------------------------------------------------
	
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
				@Table ([Key],[Val])
			VALUES
				(@Key, @Val)
	END
	RETURN
END
```
