# dbo.fn_calc_age

**Database:** DBAUtility  
**Server:** papamart  
**Function Type:** Scalar Function  
**Returns:** tinyint(1)  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.fn_calc_age"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @birthdate | smalldatetime | 4 | NO |
| @todate | smalldatetime | 4 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql
CREATE FUNCTION fn_calc_age 
	(@birthdate smalldatetime,
      @todate smalldatetime)
RETURNS tinyint 
AS
BEGIN
     DECLARE @age smallint
     SELECT @age=datediff(yy,@birthdate,@todate)+ 
            CASE WHEN left(convert(varchar(10),@birthdate,101),6)+convert(varchar(4),year(@todate))>@todate
            THEN -1 
            ELSE 0 
            END
     IF @age<0 SET @age=0
     RETURN @age
END
```

