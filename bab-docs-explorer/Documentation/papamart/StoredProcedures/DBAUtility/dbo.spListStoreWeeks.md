# dbo.spListStoreWeeks

**Database:** DBAUtility  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spListStoreWeeks"]
    dbo_vwStore_dim(["dbo.vwStore_dim"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.vwStore_dim |

## Stored Procedure Code

```sql
CREATE PROCEDURE dbo.spListStoreWeeks AS

DECLARE @Start_date datetime,
	@end_date datetime,
	@begin_week datetime,
	@end_week datetime,
	@begin_count int,
	@end_count int

SET NOCOUNT ON

CREATE TABLE #listweeks
(begin_week datetime,
 end_week datetime)

SELECT  @Start_date=MIN(opening_date) 
FROM dw.dbo.vwStore_dim  --could be replaced with store dim table

SELECT @end_date=getdate()


SELECT @begin_count=CASE datename(dw,@Start_date)
			WHEN 'Sunday'    THEN 0
			WHEN 'Monday'    THEN -1
			WHEN 'Tuesday'   THEN -2
			WHEN 'Wednesday' THEN -3
			WHEN 'Thursday'  THEN -4
			WHEN 'Friday'    THEN -5 
			WHEN 'Saturday'  THEN -6
			END

SELECT @begin_week=dateadd(dd,@begin_count,@Start_date)

SELECT @end_count=CASE datename(dw,@Start_date)
			WHEN 'Sunday'    THEN 6
			WHEN 'Monday'    THEN 5
			WHEN 'Tuesday'   THEN 4
			WHEN 'Wednesday' THEN 3
			WHEN 'Thursday'  THEN 2
			WHEN 'Friday'    THEN 1
			WHEN 'Saturday'  THEN 0
			END

SELECT @end_week=dateadd(dd,@end_count,@Start_date)
 




WHILE @begin_week<=@end_date
BEGIN
	INSERT INTO  #listweeks
	(begin_week, end_week)
	SELECT @begin_week,@end_week

	SELECT @begin_week=dateadd(wk,1,@begin_week)
	SELECT @end_week=dateadd(wk,1,@end_week)
END

SELECT begin_week, end_week
FROM #listweeks

DROP TABLE #listweeks
```

