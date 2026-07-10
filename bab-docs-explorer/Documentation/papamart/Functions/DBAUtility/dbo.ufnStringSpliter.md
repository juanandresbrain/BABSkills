# dbo.ufnStringSpliter

**Database:** DBAUtility  
**Server:** papamart  
**Function Type:** Table-Valued Function  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.ufnStringSpliter"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @vcDelimitedString | varchar | 8000 | NO |
| @vcDelimiter | varchar | 100 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql
CREATE FUNCTION dbo.ufnStringSpliter (@vcDelimitedString 		varchar(8000),
				     @vcDelimiter			varchar(100) )
/**************************************************************************
DESCRIPTION: Accepts a delimited string and splits it at the specified
		delimiter points.  Returns the individual items as a table data
		type with the ElementID field as the array index and the Element
		field as the data

PARAMETERS:
		@vcDelimitedString		- The string to be split
		@vcDelimiter			- String containing the delimiter where
							delimited string should be split

RETURNS:
		Table data type containing array of strings that were split with
		the delimiters removed from the source string

USAGE:
		SELECT ElementID, Element FROM Split('2|9', '|') ORDER BY ElementID

AUTHOR:	
DATE: 	
MODIFICATION HISTORY:
	WHO		DATE		DESCRIPTION
	---		----------	---------------------------------------------------

***************************************************************************/
RETURNS @tblArray TABLE 
   (
	ElementID	smallint	IDENTITY(1,1),  --Array index
   	Element		varchar(1000)			--Array element contents
   )
AS
BEGIN

	DECLARE 
	@siIndex					smallint,
	@siStart					smallint,
	@siDelSize					smallint


	SET @siDelSize	= LEN(@vcDelimiter)
	--loop through source string and add elements to destination table array
	WHILE LEN(@vcDelimitedString) > 0
	BEGIN
		SET @siIndex = CHARINDEX(@vcDelimiter, @vcDelimitedString)
		IF @siIndex = 0
		BEGIN
			INSERT INTO @tblArray VALUES(@vcDelimitedString)
			BREAK
		END
		ELSE
		BEGIN
			INSERT INTO @tblArray VALUES(SUBSTRING(@vcDelimitedString, 1,@siIndex - 1))
			SET @siStart = @siIndex + @siDelSize
			SET @vcDelimitedString = SUBSTRING(@vcDelimitedString, @siStart , LEN(@vcDelimitedString) - @siStart + 1)
		END
	END
	
	RETURN
END
```

