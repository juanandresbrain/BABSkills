# dbo.to_hex

**Database:** auditworks  
**Server:** bedrockdb01  
**Function Type:** Scalar Function  
**Returns:** nvarchar(64)  

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
CREATE FUNCTION dbo.to_hex (@binvalue binary(16))
returns nvarchar(32)
AS
BEGIN
DECLARE

    @pos    int,
    @posval int,
    @length int,
    @binpar int,
    @hexstr nchar(16),
    @outhex nvarchar(32)

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
        
    return @outhex
END
```

