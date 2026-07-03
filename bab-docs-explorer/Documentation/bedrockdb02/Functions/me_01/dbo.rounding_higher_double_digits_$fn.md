# dbo.rounding_higher_double_digits_$fn

**Database:** me_01  
**Server:** bedrockdb02  
**Function Type:** Scalar Function  
**Returns:** float(8)  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.rounding_higher_double_digits_$fn"]
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


CREATE FUNCTION rounding_higher_double_digits_$fn (@number_to_round float)
RETURNS float
AS
BEGIN 
	declare @diff_sign int
			,@adjustedTenths int
	select @diff_sign = sign(CAST((@number_to_round*100 + 0.001) as int) % 10 - CAST((@number_to_round*10 + 0.001) as int) % 10  )
	select @adjustedTenths = CAST((@number_to_round*10 + 0.001) as int) % 10 -- get tenths
			  -- add 1 to the tenths if hundreds are higher (0.56 -> 0.66, 0.54 -> 0.55), idea is add @x*(sign(@x + 1)) where @x indicates if hundreds are higher (1) or lower(-1) or equal(0) to the tents
			  + @diff_sign*(sign(@diff_sign + 1))
	RETURN FLOOR(@number_to_round) + @adjustedTenths * 0.1 + @adjustedTenths * 0.01
END
```
