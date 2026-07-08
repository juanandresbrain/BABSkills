# dbo.TO_BIGHEX

**Database:** COMM_EVENT  
**Server:** bedrockdb01  
**Function Type:** Scalar Function  
**Returns:** varchar(8000)  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.TO_BIGHEX"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @binvalue | varbinary | 4000 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql
CREATE FUNCTION [dbo].[TO_BIGHEX] (@binvalue varbinary(4000)) RETURNS varchar(8000)
AS
BEGIN
DECLARE    	@pos    int,
    		@posval int,
    		@length int,
    		@binpar int,
    		@hexstr char(16),
    		@outhex varchar(8000)
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

