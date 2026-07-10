# dbo.udf_ProperCase

**Database:** dw  
**Server:** papamart  
**Function Type:** Scalar Function  
**Returns:** varchar(7999)  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.udf_ProperCase"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @x | varchar | 7999 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql
CREATE FUNCTION udf_ProperCase (@x varchar(7999))
RETURNS varchar(7999)
AS
  BEGIN

	DECLARE @y int
	SET @y = 1
	
	SELECT @x = UPPER(SUBSTRING(@x,1,1))+LOWER(SUBSTRING(@x,2,LEN(@x)-1))+' '
	
	WHILE @y < LEN(@x)
	  BEGIN
		SELECT @y=CHARINDEX(' ',@x,@y)
		SELECT @x=SUBSTRING(@x,1,@y)+UPPER(SUBSTRING(@x,@y+1,1))+SUBSTRING(@x,@y+2,LEN(@x)-@y+1)	
		SELECT @y=@y+1
	  END
	RETURN @x
END
```

