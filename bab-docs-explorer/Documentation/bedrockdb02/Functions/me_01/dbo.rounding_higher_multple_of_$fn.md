# dbo.rounding_higher_multple_of_$fn

**Database:** me_01  
**Server:** bedrockdb02  
**Function Type:** Scalar Function  
**Returns:** float(8)  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.rounding_higher_multple_of_$fn"]
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


CREATE FUNCTION rounding_higher_multple_of_$fn (@number_to_round float, @multiple_of float)
RETURNS float
AS
BEGIN
	RETURN case cast ((cast(((@number_to_round - FLOOR(@number_to_round)) * 100) as int ) / cast(((@multiple_of + 0.001) * 100) as int) + 1) * @multiple_of as int )
		when 0 -- fraction does not overflow into the next integer
			then FLOOR(@number_to_round) -- integer part of the price 
						+ (cast(((@number_to_round - FLOOR(@number_to_round)) * 100) as int ) / cast(((@multiple_of + 0.001) * 100) as int)  -- how many times the value (multiple) fits in the decimal part
						+ (sign((cast(((@number_to_round - FLOOR(@number_to_round)) * 100) as int ) % cast(((@multiple_of + 0.001) * 100) as int) ))) -- add 1 if it is not already multiple of the value
						) * @multiple_of -- multiply the number times it fits by the value
		else -- next highest multiple is in the next integer, must get the next integer + one multiple of the value 
			FLOOR(@number_to_round) + 1 + @multiple_of
		END
END
```
