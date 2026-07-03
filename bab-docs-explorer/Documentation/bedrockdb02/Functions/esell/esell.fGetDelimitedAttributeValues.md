# esell.fGetDelimitedAttributeValues

**Database:** esell  
**Server:** bedrockdb02  
**Function Type:** Table-Valued Function  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["esell.fGetDelimitedAttributeValues"]
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
--END GETSKUDEMANDREPORTLOCATION--


--START fGetDelimitedAttributeValues
CREATE FUNCTION [esell].[fGetDelimitedAttributeValues](@DelimitedString NVARCHAR(MAX))
RETURNS @tempLocationAttributeIds TABLE
     (
        locationAttributeId  VARCHAR(100)
     )
AS 

--Function Name: fGetDelimitedAttributeValues
--
--  Description: This function will return a table containing the individual location attribute values from a comma seperated list of location attribute values. 
--
--
--  Parameters:
--             IN Parameter(s):
--                 1. DelimitedString  - comma seperated list of location attribute ids.
--  Returns : 
--				Table containing records of individual location attribute ids.
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
 
--Within while loop the temporary table @tempLocationAttributeIds is filled up with individual rows of location attribute id's, for the arbitrary limit of 1000.
WHILE @element <> 0
BEGIN
     SET @element = CHARINDEX(',', @DelimitedString)
     IF @element <> 0
		BEGIN
			INSERT INTO @tempLocationAttributeIds (locationAttributeId)
			SELECT SUBSTRING(@DelimitedString, 1, @element - 1)
			
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
