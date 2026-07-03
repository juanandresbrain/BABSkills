# esell.fGetDelimitedNoStockReasonIds

**Database:** esell  
**Server:** bedrockdb02  
**Function Type:** Table-Valued Function  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["esell.fGetDelimitedNoStockReasonIds"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @DelimitedString | nvarchar | -1 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql
--END fGetDelimitedLocationValues

--START fGetDelimitedNoStockReasonIds
CREATE FUNCTION [esell].[fGetDelimitedNoStockReasonIds](@DelimitedString NVARCHAR(MAX))
RETURNS @tempNoStockReasonIds TABLE
     (
      NoStockReasonId      INT
     )
AS 

--Function Name: fGetDelimitedNoStockReasonIds
--
--  Description: Description: This function will return a table containing the individual no stock reason ids from a comma seperated list of no stock reasons. 
--
--
--  Parameters:
--             IN Parameter(s):
--                 1. DelimitedString  - comma seperated list of no stock reason ids.
--  Returns : 
--				Table containing records of individual no stock reason ids.
--
--  Author: OBernal
--
--  Date: 22-October-2012
--
--  Revisions:
--
--  Notes: 

BEGIN
DECLARE    @element  INT
          ,@index  INT
          
SET @index = 1
SET @element = 1
SET @DelimitedString = @DelimitedString + ','

--Within while loop the temporary table @tempNoStockReasonIds is filled up with individual rows of no stock reason id's, for the arbitrary limit of 1000.  
WHILE @element <> 0
BEGIN
     SET @element=CHARINDEX(',', @DelimitedString)
     IF @element <> 0
		BEGIN
		  INSERT INTO @tempNoStockReasonIds (NoStockReasonId)
          SELECT CONVERT(INT, SUBSTRING(@DelimitedString,1,@element - 1))
          
          SET @DelimitedString = RIGHT(@DelimitedString, LEN(@DelimitedString) - @element)
		END
     ELSE IF @element = 0
	    BEGIN 
			BREAK
		END

	SET @index = @index + 1
END
RETURN
END
```
