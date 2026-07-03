# dbo.ufn_RemoveString

**Database:** ma_01  
**Server:** bedrockdb02  
**Function Type:** Scalar Function  
**Returns:** varchar(1000)  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.ufn_RemoveString"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @Input | varchar | 1000 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql
CREATE Function [dbo].[ufn_RemoveString]
(@Input VARCHAR(1000))
RETURNS VARCHAR (1000)
AS
BEGIN
       DECLARE @String INT
       SET @String = PATINDEX('%[&#@.''''$%^!`~;:<>/\?()_+=*"{}|,-[]%', REPLACE(@InPut, ']', ''))
 
       WHILE @String > 0
       BEGIN
              SET @Input = STUFF(REPLACE(@InPut, ']', ''), @String, 1, '')
              SET @String = PATINDEX('%[&#@.''''$%^!`~;:<>/\?()_+=*"{}|,-[]%', REPLACE(@InPut, ']', ''))
       END
       RETURN REPLACE(@InPut, ']', '')
END
```
