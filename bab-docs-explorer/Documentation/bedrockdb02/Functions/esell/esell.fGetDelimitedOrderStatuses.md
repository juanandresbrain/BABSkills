# esell.fGetDelimitedOrderStatuses

**Database:** esell  
**Server:** bedrockdb02  
**Function Type:** Table-Valued Function  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["esell.fGetDelimitedOrderStatuses"]
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
--END fGetDelimitedNoStockReasonIds

--START fGetDelimitedOrderStatuses
CREATE FUNCTION [esell].[fGetDelimitedOrderStatuses](@DelimitedString NVARCHAR(MAX))
RETURNS @tempOrderStatues TABLE
     (
        orderStatus  VARCHAR(100)
     )
AS 

--Function Name: fGetDelimitedOrderStatuses
--
--  Description: This function will return a table containing the individual order status values from a comma seperated list of order statuses. 
--
--
--  Parameters:
--             IN Parameter(s):
--                 1. DelimitedString  - comma seperated list of order statuses.
--  Returns : 
--				Table containing records of individual order status.
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
 
--Within while loop the temporary table @tempOrderStatues is filled up with individual rows of order statuses, for the arbitrary limit of 1000.
WHILE @element <> 0 
BEGIN
     SET @element = CHARINDEX(',', @DelimitedString)
     IF @element <> 0
		BEGIN
			INSERT INTO @tempOrderStatues (OrderStatus)
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
