# dbo.fnComputeDecimalAge

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  
**Function Type:** Scalar Function  
**Returns:** decimal(5)  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.fnComputeDecimalAge"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @BirthDate | datetime | 8 | NO |
| @MarkDate | datetime | 8 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql
CREATE FUNCTION fnComputeDecimalAge(@BirthDate DATETIME = NULL,@MarkDate DATETIME) RETURNS DECIMAL(4, 1) AS BEGIN 	--IF @MarkDate IS NULL SET @MarkDate = current_timestamp() 	 	DECLARE @age DECIMAL(4, 1) 	DECLARE @fromDatetodayyear DATETIME 	--SET @fromDatetodayyear = LEFT(CONVERT(VARCHAR(10),@BirthDate,101),6)+CONVERT(VARCHAR(4),YEAR(@MarkDate)) 	--SET @fromDatetodayyear = DATEADD(year, DATEDIFF(year, @BirthDate, @MarkDate), @BirthDate) 	 	SELECT @age= 		CASE 			WHEN @BirthDate IS NULL 				THEN -1.0 			WHEN @BirthDate >= @MarkDate 				THEN 0.0 			ELSE CAST(DATEDIFF(yy,@BirthDate,@MarkDate) AS DECIMAL(5, 2))  				+ CASE  					WHEN @fromDatetodayyear > @MarkDate 						THEN FLOOR(-CAST(DATEDIFF(dd,@MarkDate,@fromDatetodayyear) AS DECIMAL(5, 2))/36.522)/10  					ELSE CAST(DATEDIFF(dd,@fromDatetodayyear,@MarkDate) AS DECIMAL(5, 2))/365.22  				END 		END 	--IF @age<0 SET @age=0.0 	RETURN @age END
```

