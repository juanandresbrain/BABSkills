# dbo.spCalcDistance

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spCalcDistance"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
CREATE  procedure  dbo.spCalcDistance 

@Lat1 as float, 
@Lon1 as float, 
@Lat2 as float, 
@Lon2 as float, 
@distance  float output

AS
BEGIN
    DECLARE @a float, @result float, @error int
    select @a = 57.2958
    
    IF @Lat1 IS NOT NULL AND @Lon1 IS NOT NULL
        BEGIN
            IF @Lat1 = @Lat2 AND @Lon1 = @Lon2
                select @distance = 0
            ELSE
            BEGIN
            select @distance = 3958.75 * ACos(Sin(@Lat1/@a) * Sin(@Lat2/@a) + 
                        Cos(@Lat1/@a) * Cos(@Lat2/@a)*Cos(@Lon2/@a - @Lon1/@a))
            select @error = @@ERROR
            if @error != 0
                select @distance = NULL
            END
        END
    RETURN @error
END
```

