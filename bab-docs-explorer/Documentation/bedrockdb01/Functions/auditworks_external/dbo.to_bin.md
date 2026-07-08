# dbo.to_bin

**Database:** auditworks_external  
**Server:** bedrockdb01  
**Function Type:** Scalar Function  
**Returns:** binary(16)  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.to_bin"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @hexvalue | varchar | 32 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql
CREATE FUNCTION [dbo].[to_bin] (@hexvalue varchar(32))
returns binary(16)
AS

/* 
  Name : dbo.to_bin
  Desc : Returns a binary number that corresponds to the hex value that was passed in.

  HISTORY:   

  Date     Name       Defect# Desc
  Mar28,06 Ian        DV-1333 Author
  
*/

BEGIN
DECLARE

    @pos    int,
    @posval int,
    @length int,
    @hexpar char(1),
    @hexstr char(16),
    @outpar varchar(32),
    @outcnt int,
    @outbin binary(16)

    SELECT @pos = 1, @length = len(@hexvalue), @hexstr = '0123456789ABCDEF', @outcnt = 0, @outpar = ''

    WHILE (@pos < @length)
    BEGIN
      SELECT @outcnt = @outcnt + 1
    
      SELECT @hexpar = substring(@hexvalue,@pos,1)
      SELECT @posval = charindex(@hexpar,@hexstr)

      SELECT @posval = (@posval-1)*16
      SELECT @hexpar = substring(@hexvalue,@pos+1,1)    
      SELECT @posval = @posval + (charindex(@hexpar,@hexstr)-1)     
      
      SELECT @outpar = @outpar + char(@posval)
      
      SELECT @pos = @pos + 2
    END
    
    SELECT @outbin = cast(@outpar as binary)
    
    RETURN @outbin
END
```

