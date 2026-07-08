# dbo.to_bin

**Database:** auditworks  
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
| @hexvalue | nvarchar | 64 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql
CREATE FUNCTION dbo.to_bin (@hexvalue nvarchar(32))
returns binary(16)
AS
BEGIN
DECLARE

    @pos    int,
    @posval int,
    @length int,
    @hexpar nchar(1),
    @hexstr nchar(16),
    @outpar nvarchar(32),
    @outcnt int,
    @outbin binary(16)

    SELECT @pos = 1, @length = len(@hexvalue), @hexstr = '0123456789ABCDEF', @outcnt = 0, @outpar = ''

    WHILE (@pos < @length)
    BEGIN
      SELECT @outcnt = @outcnt + 1
    
      SELECT @hexpar = substring(@hexvalue,@pos,1)
      SELECT @posval = CHARINDEX(@hexpar,@hexstr)

      SELECT @posval = (@posval-1)*16
      SELECT @hexpar = substring(@hexvalue,@pos+1,1)    
      SELECT @posval = @posval + (CHARINDEX(@hexpar,@hexstr)-1)     
      
      SELECT @outpar = @outpar + nchar(@posval)
      
      SELECT @pos = @pos + 2
    END
    
    SELECT @outbin = cast(@outpar as binary)
    
    return @outbin
END
```

