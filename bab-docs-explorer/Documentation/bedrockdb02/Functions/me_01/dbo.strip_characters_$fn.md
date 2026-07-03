# dbo.strip_characters_$fn

**Database:** me_01  
**Server:** bedrockdb02  
**Function Type:** Scalar Function  
**Returns:** nvarchar  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.strip_characters_$fn"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @input_string | nvarchar | -1 | NO |
| @match_expression | nvarchar | 510 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql


CREATE FUNCTION [dbo].[strip_characters_$fn]
( @input_string NVARCHAR(MAX), @match_expression NVARCHAR(255) )
RETURNS NVARCHAR(MAX)
AS
BEGIN

    SET @match_expression =  N'%['+@match_expression+N']%'

    WHILE PatIndex(@match_expression, @input_string) > 0
        SET @input_string = Stuff(@input_string, PatIndex(@match_expression, @input_string), 1, N'')

    RETURN @input_string

END
```
