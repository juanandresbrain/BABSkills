# dbo.fnGetNearestStoreFromLatLonZipDate

**Database:** dw  
**Server:** papamart  
**Function Type:** Scalar Function  
**Returns:** float(8)  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.fnGetNearestStoreFromLatLonZipDate"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @Lat | real | 4 | NO |
| @Lon | real | 4 | NO |
| @Date | datetime | 8 | NO |
| @Zip | varchar | 10 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql
CREATE        function [dbo].[fnGetNearestStoreFromLatLonZipDate](
@Lat float(15), @Lon float(15), @Date datetime, @Zip varchar(10))
returns float
AS
BEGIN

DECLARE @storeID int

-- seriously doubt this was being used because tmpziptop didn't exist -- dlr 10/17/2007

/*
IF ISNUMERIC(Substring(@Zip,1,3))=1 --US Zip
  BEGIN
	select @storeID =
	(
		select 
		top 1 s.store_id
		from store_dim s 

		where s.store_id > 0 and s.store_id < 400 and s.store_id not in (0, 8, 17, 13, 136, 155, 179, 180, 209, 212, 242, 272, 1513)
-- changed 	04/14/2007 	dlr
--		where s.store_id > 0 and s.store_id < 2000 and s.store_id not in (0, 8, 17, 13, 136, 155, 179, 180, 209, 212, 242, 470, 471, 473, 480, 482, 485, 486, 489, 950, 960, 975, 980, 990)
			and s.Opening_Date <= @Date
			and (s.Closing_date > @Date or s.Closing_date is NULL)
			and store_id in (select store_id from tmpziptop where postal_code=@Zip and @Date between start_date and end_date)
		order by dw.dbo.fnCalcDistance(@Lat, @Lon, s.latitude, s.longitude) asc
	)
  END
ELSE  --Canada Postal Code
  BEGIN
	SET @Zip = Substring(@Zip,1,3)  --will get top 3 stores based on FSA

	select @storeID =
	(
		select 
		top 1 s.store_id
		from store_dim s 
		where s.store_id > 0 and s.store_id < 400 and s.store_id not in (0, 8, 17, 13, 136, 155, 179, 180, 209, 212, 242, 272, 1513)
-- changed 	04/14/2007 	dlr
--		where s.store_id > 0 and s.store_id < 2000 and s.store_id not in (0, 8, 17, 13, 136, 155, 179, 180, 209, 212, 242, 470, 471, 473, 480, 482, 485, 486, 489, 950, 960, 975, 980, 990)
			and s.Opening_Date <= @Date
			and (s.Closing_date > @Date or s.Closing_date is NULL)
			and store_id in (select store_id from tmpziptop where postal_code=@Zip and @Date between start_date and end_date)
		order by dw.dbo.fnCalcDistance(@Lat, @Lon, s.latitude, s.longitude) asc
	)
  END	
*/


RETURN @storeID
END
```

