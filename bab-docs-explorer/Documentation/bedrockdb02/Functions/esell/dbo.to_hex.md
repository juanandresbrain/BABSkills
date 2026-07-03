# dbo.to_hex

**Database:** esell  
**Server:** bedrockdb02  
**Function Type:** Scalar Function  
**Returns:** varchar(32)  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.to_hex"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @binvalue | binary | 16 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql
CREATE FUNCTION [dbo].[to_hex] (@binvalue binary(16))
returns varchar(32)
AS

/* 
  Name : dbo.to_hex
  Desc : Returns a hex number as a string that corresponds to the binary value that was passed in.

  HISTORY:   

  Date     Name       Defect# Desc
  Mar28,06 Ian        DV-1333 Author
  
*/

BEGIN
DECLARE

    @pos    int,
    @posval int,
    @length int,
    @binpar int,
    @hexstr char(16),
    @outhex varchar(32)

    SELECT @pos = 1, @length = len(@binvalue), @hexstr = '0123456789ABCDEF', @outhex=''

    WHILE (@pos <= @length)
    BEGIN
    
      SELECT @binpar = convert(int,substring(@binvalue,@pos,1))
      
      SELECT @posval = convert(int,@binpar/16)
     
      SELECT @outhex = @outhex + substring(@hexstr,@posval+1,1)

      SELECT @posval = @binpar - (@posval*16)

      SELECT @outhex = @outhex + substring(@hexstr,@posval+1,1)

      SELECT @pos = @pos + 1

    END
        
    RETURN @outhex
END
```
