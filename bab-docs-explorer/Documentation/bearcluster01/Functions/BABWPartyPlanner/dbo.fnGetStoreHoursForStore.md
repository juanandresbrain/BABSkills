# dbo.fnGetStoreHoursForStore

**Database:** BABWPartyPlanner  
**Server:** bearcluster01  
**Function Type:** Inline Table-Valued Function  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.fnGetStoreHoursForStore"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @StoreNumber | int | 4 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql
-- =============================================
-- Author:		Tim Bytnar
-- Create date: 7/27/2017
-- Description:	This is used by the PartyPlanner database to retrive tabular store hours for the website.
-- =============================================
CREATE FUNCTION fnGetStoreHoursForStore 
(	
	-- Add the parameters for the function here
	@StoreNumber int = 0
	 
)
RETURNS TABLE 
AS
RETURN 
(
	WITH StoreOpenHoursRaw 
	AS
	(
		SELECT sd.STR_NUM as StoreNumber,
			   CASE
		   			WHEN (sohd.DY_OF_WK_ID = 1) THEN 'Sunday'
					WHEN (sohd.DY_OF_WK_ID = 2) THEN 'Monday'
					WHEN (sohd.DY_OF_WK_ID = 3) THEN 'Tuesday'
					WHEN (sohd.DY_OF_WK_ID = 4) THEN 'Wednesday'
					WHEN (sohd.DY_OF_WK_ID = 5) THEN 'Thursday'
					WHEN (sohd.DY_OF_WK_ID = 6) THEN 'Friday'
					WHEN (sohd.DY_OF_WK_ID = 7) THEN 'Saturday'
			   END AS 'DayOfWeek',
			   CAST(STRT_TM as time(0)) as StartTime
		FROM [Kodiak].[BABWMstrData].[dbo].STR_OPRNL_HR_DIM sohd
		LEFT JOIN [Kodiak].[BABWMstrData].dbo.STR_DIM sd
			ON sohd.STR_ID = sd.STR_ID
		WHERE sd.STR_NUM = @StoreNumber
	),PivotOpenHours
	AS
	(
		SELECT StoreNumber,Sunday as 'SundayOpen',Monday as 'MondayOpen',Tuesday as 'TuesdayOpen',Wednesday as 'WednesdayOpen',Thursday as 'ThursdayOpen',Friday as 'FridayOpen',Saturday as 'SaturdayOpen'
		FROM StoreOpenHoursRaw
		PIVOT
		(
			MIN(StartTime)
			FOR DayOfWeek IN (Sunday,Monday,Tuesday,Wednesday,Thursday,Friday,Saturday)
		) AS p
	),StoreClosedHoursRaw 
	AS
	(
		SELECT sd.STR_NUM as StoreNumber,
			   CASE
		   			WHEN (sohd.DY_OF_WK_ID = 1) THEN 'Sunday'
					WHEN (sohd.DY_OF_WK_ID = 2) THEN 'Monday'
					WHEN (sohd.DY_OF_WK_ID = 3) THEN 'Tuesday'
					WHEN (sohd.DY_OF_WK_ID = 4) THEN 'Wednesday'
					WHEN (sohd.DY_OF_WK_ID = 5) THEN 'Thursday'
					WHEN (sohd.DY_OF_WK_ID = 6) THEN 'Friday'
					WHEN (sohd.DY_OF_WK_ID = 7) THEN 'Saturday'
			   END AS 'DayOfWeek',
			   CAST(END_TM as time(0)) as EndTime
		FROM [Kodiak].[BABWMstrData].dbo.STR_OPRNL_HR_DIM sohd
		LEFT JOIN [Kodiak].[BABWMstrData].dbo.STR_DIM sd
			ON sohd.STR_ID = sd.STR_ID
		WHERE sd.STR_NUM = @StoreNumber
	),PivotClosedHours
	AS
	(
		SELECT StoreNumber,Sunday as 'SundayClose',Monday as 'MondayClose',Tuesday as 'TuesdayClose',Wednesday as 'WednesdayClose',Thursday as 'ThursdayClose',Friday as 'FridayClose',Saturday as 'SaturdayClose'
		FROM StoreClosedHoursRaw
		PIVOT
		(
			MIN(EndTime)
			FOR DayOfWeek IN (Sunday,Monday,Tuesday,Wednesday,Thursday,Friday,Saturday)
		) AS p
	)

	SELECT 
		po.StoreNumber
	   ,po.SundayOpen
	   ,po.MondayOpen
	   ,po.TuesdayOpen
	   ,po.WednesdayOpen
	   ,po.ThursdayOpen
	   ,po.FridayOpen
	   ,po.SaturdayOpen
	   ,pc.SundayClose
	   ,pc.MondayClose
	   ,pc.TuesdayClose
	   ,pc.WednesdayClose
	   ,pc.ThursdayClose
	   ,pc.FridayClose
	   ,pc.SaturdayClose
	FROM PivotOpenHours po
	left join PivotClosedHours pc on po.StoreNumber = pc.StoreNumber


)
```
