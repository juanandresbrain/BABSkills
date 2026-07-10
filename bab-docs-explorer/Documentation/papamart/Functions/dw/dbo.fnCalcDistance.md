# dbo.fnCalcDistance

**Database:** dw  
**Server:** papamart  
**Function Type:** Scalar Function  
**Returns:** float(8)  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.fnCalcDistance"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @Lat1 | float | 8 | NO |
| @Lon1 | float | 8 | NO |
| @Lat2 | float | 8 | NO |
| @Lon2 | float | 8 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql
CREATE  FUNCTION dbo.fnCalcDistance 
            (@Lat1 as float, @Lon1 as float, @Lat2 as float, @Lon2 as float) 
RETURNS float
AS
BEGIN
            DECLARE @a float, @result float, @error int
            select @a = 57.2958
            
            IF @Lat1 IS NOT NULL AND @Lon1 IS NOT NULL
                        BEGIN
                                    IF @Lat1 = @Lat2 AND @Lon1 = @Lon2
                                                select @result = 0
                                    ELSE
                                    BEGIN
                                    select @result = 3958.75 * ACos(Sin(@Lat1/@a) * Sin(@Lat2/@a) + 
                                                Cos(@Lat1/@a) * Cos(@Lat2/@a)*Cos(@Lon2/@a - @Lon1/@a))
                                    select @error = @@ERROR
                                    if @error != 0
                                                select @result = NULL
                                    END
                        END
            RETURN @result
END
```

