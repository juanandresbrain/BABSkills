# dbo.spEmailTrafficProcessSummary

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spEmailTrafficProcessSummary"]
    ExperianFootfall_CompanyHierarchyStoreMapping(["ExperianFootfall.CompanyHierarchyStoreMapping"]) --> SP
    date_dim(["date_dim"]) --> SP
    dbo_DATE_DIM(["dbo.DATE_DIM"]) --> SP
    dbo_ShopperTrackFact(["dbo.ShopperTrackFact"]) --> SP
    dbo_ShopperTrackStage(["dbo.ShopperTrackStage"]) --> SP
    dbo_sp_send_dbmail(["dbo.sp_send_dbmail"]) --> SP
    store_dim(["store_dim"]) --> SP
    dbo_STORE_DIM(["dbo.STORE_DIM"]) --> SP
    Store_Shoppertrak_Open_Dim(["Store_Shoppertrak_Open_Dim"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| ExperianFootfall.CompanyHierarchyStoreMapping |
| date_dim |
| dbo.DATE_DIM |
| dbo.ShopperTrackFact |
| dbo.ShopperTrackStage |
| dbo.sp_send_dbmail |
| store_dim |
| dbo.STORE_DIM |
| Store_Shoppertrak_Open_Dim |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spEmailTrafficProcessSummary]


as 

-- =====================================================================================================
-- Name: spEmailTrafficProcessSummary
--
-- Description:	Sends email summary of the traffic data processed from Experian and Shoppertrack
--
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		11/02/2015		Created Proc
--		Brian Byas		9/8/2016		Added Actual vs Inputed percentages
--		Tim Callahan	5/21/2020		Proc overhauled to account for:
--											New staging and fact tables
--											Handling when a store traffic source has not been not defined
--											Handling when an expected store had no data in the traffic file
--		Tim Callahan	6/3/2020		Added additional filter to Data_Ind_Nm CTE 
--										This is to account for UK stores\time difference that caused duplicate entries
-- =====================================================================================================

set nocount on


IF (Object_ID('tempdb..#TrafficSummary') IS NOT NULL) DROP TABLE #TrafficSummary;


--DECLARE @ActualDate AS DATE;
--SET @ActualDate=GETDATE()-1;
--DECLARE @DT AS INT;
--SELECT @DT=convert(int, convert(varchar(10), @ActualDate, 112));

WITH Data_Ind_Nm (StoreID, InputedInd) AS (
		SELECT DISTINCT sd.STORE_ID, tf.DataIndicatorName
		FROM [dw].[dbo].[ShopperTrackFact] tf
		INNER JOIN [dw].[dbo].[STORE_DIM] sd
			ON sd.STORE_KEY=tf.StoreKey
		INNER JOIN [dw].[dbo].[DATE_DIM] dd
			ON dd.DATE_KEY=tf.DateKey
		WHERE dd.Date_Key = (select distinct date_key from date_dim where actual_date = cast (GETDATE ()-1 as date))
		--AND tf.DataIndicatorName='Inputed' -- Why this filter ??
		and cast (InsertDate as date) = cast (getdate() as date)  -- Only included Records inserted today added 6/3/2020 by Tim C
		),
	TrafficFact (StoreID, SumEnters, SumExits) AS (
		SELECT sd.STORE_ID, sum(t.enters), sum(t.exits)
		FROM [dw].[dbo].[ShopperTrackFact] t
		INNER JOIN [dw].[dbo].[STORE_DIM] sd
			ON sd.STORE_KEY=t.StoreKey
		INNER JOIN [dw].[dbo].[DATE_DIM] dd
			ON dd.DATE_KEY=t.DateKey
		WHERE dd.Date_Key = (select distinct date_key from date_dim where actual_date = cast (GETDATE ()-1 as date)) -- Added 5/21/2020		
		GROUP BY sd.STORE_ID
		),
	 TrafficSTG (StoreID, SumEnters, SumExits) AS (
		SELECT sd.store_id, sum(t.enters), sum(t.exits)
		FROM [DWStaging].[dbo].[ShopperTrackStage] t
		INNER JOIN [dw].[dbo].[STORE_DIM] sd
			on sd.store_key=t.StoreKey
		WHERE t.DateKey = (select distinct date_key from date_dim where actual_date = cast (GETDATE ()-1 as date))		
		AND t.ShopperTrakOrgId not like '4____'
		GROUP BY sd.store_id
		),
	TrafficVendor (StoreID, IsShopperTrak, IsFootFall) AS (
		SELECT DISTINCT SiteIdentity, IsShopperTrak, IsFootFall 
		FROM  DWStaging.ExperianFootfall.CompanyHierarchyStoreMapping
		),
	IncludedStores (StoreID) AS (
		SELECT DISTINCT sd.store_id
		FROM store_dim sd
		INNER JOIN Store_Shoppertrak_Open_Dim sod
			ON sod.store_key=sd.store_key
		LEFT OUTER JOIN date_dim dd1
			ON dd1.date_key=sod.date_key_from
		LEFT OUTER JOIN date_dim dd2
			ON dd2.date_key=sod.date_key_thru
		WHERE GETDATE() BETWEEN ISNULL(dd1.actual_date,'1/1/1900') AND ISNULL(dd2.actual_date,'12/31/2999')
		AND (sd.closing_date>GETDATE() OR sd.closing_date IS NULL)
		),
	PercentActuals (storeID,PctActuals,PctInputed)AS (
	SELECT 
      sd.store_id  
	  ,CAST(CAST(COUNT(CASE WHEN DataIndicatorName = 'Actual' THEN 1 ELSE NULL END)AS numeric) / CAST(COUNT(EXITS) AS int)AS decimal(18,2)) AS PctAcutals
	  ,CAST(CAST(COUNT(CASE WHEN DataIndicatorName = 'Inputed' THEN 1 ELSE NULL END)AS numeric) / CAST(COUNT(EXITS) AS int)AS decimal(18,2)) AS PctInputed
		FROM [dw].[dbo].[ShopperTrackFact] SF INNER JOIN
			[dw].[dbo].[store_dim] sd ON
				sf.StoreKey = sd.store_key
			INNER JOIN [dw].[dbo].[DATE_DIM] dd
			ON dd.DATE_KEY=sf.DateKey
		WHERE dd.Date_Key = (select distinct date_key from date_dim where actual_date = cast (GETDATE ()-1 as date))
		
	GROUP BY sd.store_id)

SELECT	DISTINCT 
		inc.StoreID AS AllStores
		,CASE	WHEN tv.IsFootFall=1 THEN 'FootFall'
				WHEN tv.IsShopperTrak=1 THEN 'ShopperTrack'
		 END AS DataSource
		,ts.StoreID AS StageStore
		,ts.SumEnters AS StageSumEnters
		,ts.SumExits AS StageSumExits
		,tf.StoreID AS FactStore
		,tf.SumEnters AS FactSumEnters
		,tf.SumExits AS FactSumExits
		,ts.SumEnters-tf.SumEnters AS MissingEnters
		,ts.SumExits-tf.SumExits AS MissingExits
		,CASE WHEN di.InputedInd IS NULL THEN 'No Data in File' ELSE di.InputedInd END AS InputedInd
		,pa.PctActuals
		,pa.PctInputed
INTO #TrafficSummary
FROM IncludedStores inc
LEFT OUTER JOIN TrafficSTG ts
		ON ts.StoreID=inc.StoreID
LEFT OUTER JOIN TrafficFact tf
		ON tf.StoreID=inc.StoreID
LEFT OUTER JOIN TrafficVendor tv
		ON tv.StoreID=inc.StoreID
LEFT OUTER JOIN Data_Ind_Nm di
		ON di.StoreID=inc.StoreID
LEFT OUTER JOIN PercentActuals pa
		ON pa.StoreID=inc.StoreID
ORDER BY inc.StoreID; 

declare @text nvarchar(max)

select @text = '<font face = arial size = 2> ' +
				'<B>TRAFFIC PROCESS SUMMARY - (SHOPPERTRACK AND EXPERIAN)</B>' + 
				'<BR>' +
				'<BR>' +
				'<table border="1">' +
				'<font face =arial size = 2>' +
				'<tr><th>LOCATION</th><th>TRAFFIC SOURCE</th><th>STAGED ENTERS</th><th>STAGED EXITS</th><th>POSTED FACT ENTERS</th><th>POSTED FACT EXITS</th><th>MISSING ENTERS</th><th>MISSING EXITS</th><th>INPUT METHOD</th><th>ACTUAL %</th><th>INPUTED %</th></tr>'+
					CAST ( ( SELECT td = right(('0000' + cast (AllStores as varchar)), 4), '',
									td = isnull(DataSource,'NOT MAPPED'), '',
									td = isnull(StageSumEnters,0), '',
									td = isnull(StageSumExits,0), '',
									td = isnull(FactSumEnters,0), '',
									td = isnull(FactSumExits,0), '',
									td = isnull(MissingEnters,0), '',
									td = isnull(MissingExits,0), '',
									td = isnull(InputedInd, 'NULL'), '',
									td = isnull(CAST(CAST(PctActuals*100 AS decimal(18,0)) AS varchar(4)),''), '',
									td = isnull(CAST(CAST( PctInputed*100 AS decimal(18,0)) AS varchar(4)),''),''
								from #TrafficSummary
								order by 
									CASE WHEN (isnull(FactSumExits,0)=0 OR isnull(FactSumExits,0) IS NULL) 
										THEN 'No' 
										ELSE 'Yes' 
									END, 
									right(('0000' + cast (AllStores as varchar)), 4)
								FOR XML PATH('tr'), TYPE 
					) AS NVARCHAR(MAX) ) +
					'</font></table></font></p></p>
					<br>
					<br>
					<br>'


exec msdb.dbo.sp_send_dbmail
	@profile_name = 'biadmin',
	@recipients = 'biadmin@buildabear.com;ChadV@buildabear.com;scottp@buildabear.com;BenD@buildabear.com;ColleenD@buildabear.co.uk;AnnieS@buildabear.com;IT-ServiceDesk@buildabear.com;KaseyP@buildabear.com',
	--@recipients = 'TimC@buildabear.com',
	@body = @text,
	@subject= 'Traffic Process Summary', 
	@body_format = 'HTML'
```

