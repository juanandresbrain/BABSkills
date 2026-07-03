# dbo.rounding_lower_multple_of_$fn

**Database:** me_01  
**Server:** bedrockdb02  
**Function Type:** Scalar Function  
**Returns:** float(8)  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.rounding_lower_multple_of_$fn"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @number_to_round | float | 8 | NO |
| @multiple_of | float | 8 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql


CREATE FUNCTION rounding_lower_multple_of_$fn (@number_to_round float, @multiple_of float)
RETURNS float
AS
BEGIN
	RETURN case (cast(((@number_to_round - FLOOR(@number_to_round)) * 100) as int ) / cast(((@multiple_of + 0.001) * 100) as int))
			WHEN 0 -- fraction part lower than multiple, need to go to the max in the lower integer
				THEN FLOOR(@number_to_round) - 1 + (cast(((0.99) * 100) as int ) / cast(((@multiple_of + 0.001) * 100) as int)) * @multiple_of 
			ELSE   -- get the integer part of the price + number of times the value fits in the fraction part * fraction part  
				FLOOR(@number_to_round) + (cast(((@number_to_round - FLOOR(@number_to_round)) * 100) as int ) / cast(((@multiple_of + 0.001) * 100) as int)) * @multiple_of
		END
END
```
