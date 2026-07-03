# esell.fGetDelimitedLocationValues

**Database:** esell  
**Server:** bedrockdb02  
**Function Type:** Table-Valued Function  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["esell.fGetDelimitedLocationValues"]
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
--END fGetDelimitedAttributeValues

--START fGetDelimitedLocationValues
CREATE FUNCTION [esell].[fGetDelimitedLocationValues](@DelimitedString NVARCHAR(MAX))
RETURNS @tempLocations TABLE
     (
      locationId      INT
     )
AS 

--Function Name: fGetDelimitedLocationValues
--
--  Description: This function will return a table containing the individual locations from a comma seperated list of locations. 
--
--  Parameters:
--             IN Parameter(s):
--                 1. DelimitedString  - comma seperated list of location ids.
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
--

BEGIN
DECLARE    @element  INT,
           @index  INT,
           @locationIdString VARCHAR(100)
          
SET @index = 1
SET @element = 1
SET @DelimitedString = @DelimitedString + ','

--Within while loop the temporary table @tempLocations is filled up with individual rows of location id's, for the arbitrary limit of 1000. 
WHILE @element <> 0 
BEGIN
     SET @element = CHARINDEX(',', @DelimitedString)
     IF @element <> 0
	     BEGIN
			INSERT INTO @tempLocations (locationId)
			SELECT CONVERT(INT,SUBSTRING(@DelimitedString, 1, @element - 1))
						
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
