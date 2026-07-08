# dbo.GET_MIN

**Database:** COMM_EVENT  
**Server:** bedrockdb01  
**Function Type:** Scalar Function  
**Returns:** bigint(8)  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.GET_MIN"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @firstValue | bigint | 8 | NO |
| @secondValue | bigint | 8 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql
CREATE FUNCTION [dbo].[GET_MIN](@firstValue bigint, @secondValue bigint) RETURNS bigint
AS
BEGIN
if @firstValue < @secondValue
   return @firstValue
return @secondValue
END
```

