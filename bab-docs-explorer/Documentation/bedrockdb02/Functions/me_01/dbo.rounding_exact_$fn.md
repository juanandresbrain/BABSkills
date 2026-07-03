# dbo.rounding_exact_$fn

**Database:** me_01  
**Server:** bedrockdb02  
**Function Type:** Scalar Function  
**Returns:** float(8)  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.rounding_exact_$fn"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @number_to_round | float | 8 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql


CREATE FUNCTION rounding_exact_$fn (@number_to_round float)
RETURNS float
AS
-----------------------------------------------------------------------------------------------------------------------------
--	Main Query: Create Function
--	History:
--	Date		By who		Bug number and description
--	Feb. 17		Feng		156574 when using a % off method the system is rounding up instead of down
-----------------------------------------------------------------------------------------------------------------------------

BEGIN
	RETURN ROUND(CAST(@number_to_round AS DECIMAL(12,5)),2)

END
```
