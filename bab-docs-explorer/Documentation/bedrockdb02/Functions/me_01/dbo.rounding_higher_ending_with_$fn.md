# dbo.rounding_higher_ending_with_$fn

**Database:** me_01  
**Server:** bedrockdb02  
**Function Type:** Scalar Function  
**Returns:** float(8)  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.rounding_higher_ending_with_$fn"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @number_to_round | float | 8 | NO |
| @ending_with | float | 8 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql


CREATE FUNCTION rounding_higher_ending_with_$fn (@number_to_round float, @ending_with float)
RETURNS float
AS
BEGIN
	RETURN FLOOR(@number_to_round + (0.99 - @ending_with)) + @ending_with
END
```
