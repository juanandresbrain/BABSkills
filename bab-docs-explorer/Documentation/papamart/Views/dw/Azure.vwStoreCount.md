# Azure.vwStoreCount

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["Azure.vwStoreCount"]
    Azure_NewDateDim(["Azure.NewDateDim"]) --> VIEW
    Azure_OnHand(["Azure.OnHand"]) --> VIEW
    Azure_vwDateFilter(["Azure.vwDateFilter"]) --> VIEW
    Azure_vwProducts(["Azure.vwProducts"]) --> VIEW
    Azure_vwStoreCountbyWeek(["Azure.vwStoreCountbyWeek"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| Azure.NewDateDim |
| Azure.OnHand |
| Azure.vwDateFilter |
| Azure.vwProducts |
| Azure.vwStoreCountbyWeek |

## View Code

```sql
CREATE VIEW [Azure].[vwStoreCount]
AS
WITH 
P AS 
	(
		SELECT        
			ProductKey, 
			CASE LEFT(style, 1) 
				WHEN 0 THEN 'NA' 
				WHEN '1' THEN 'CA' 
				WHEN '4' THEN 'EU' 
				WHEN '8' THEN 'AS' 
			END AS Jurisdiction
        FROM Azure.vwProducts
	), 
d AS
    (
		SELECT
			Azure.OnHand.ProductKey, 
			Azure.OnHand.workYear, 
			Azure.OnHand.workweek, 
			SUM(Azure.OnHand.OnHandCost) AS Cost, 
			SUM(Azure.OnHand.OnHand) AS Units, 
			Azure.NewDateDim.Date_Key
      FROM Azure.OnHand 
	  INNER JOIN Azure.NewDateDim 
		ON Azure.OnHand.workYear = RIGHT(Azure.NewDateDim.Fiscal_Year, 4) 
		AND Azure.OnHand.workweek = CAST(Azure.NewDateDim.Fiscal_Week_Of_Year_key AS int) 
		AND Azure.NewDateDim.Fiscal_Day_Of_Week_Key = 1
      WHERE (Azure.OnHand.Inv_Status = 'Available')
      GROUP BY 
		Azure.OnHand.ProductKey, 
		Azure.OnHand.workYear, 
		Azure.OnHand.workweek, 
		Azure.NewDateDim.Date_Key
		--having sum(onHand) > 0
	),
PreStage as 
	(
		SELECT        
			P_1.ProductKey, 
			cast(C.actual_date as date) AS ActualDate, 
			C.store_count AS StoreCount, 
			--ISNULL(d_1.Cost / d_1.Units, 0) AS UnitCost
			isnull(d_1.Cost / nullif(d_1.Units, 0),0) AS UnitCost
			--,
			--CASE 
			--	WHEN C.TradingGroup IN ('US','CA') THEN 'North America'
			--	WHEN C.TradingGroup IN ('UK','DK','IE','CN') THEN 'Europe'
			--END AS TradingGroup
		 FROM  P AS P_1 
		 INNER JOIN Azure.vwStoreCountbyWeek AS C ON P_1.Jurisdiction = C.TradingGroup 
		 INNER JOIN Azure.vwDateFilter AS f ON C.actual_date = f.actual_date 
		 LEFT OUTER JOIN d AS d_1 
			ON P_1.ProductKey = d_1.ProductKey 
			AND f.actual_date = d_1.Date_Key
	)
--select
--	ps.ProductKey,
--	nwd.date_key as ActualDate,
--	ps.StoreCount,
--	ps.UnitCost
--from PreStage ps
--join azure.newdatedim dd on ps.ActualDate=dd.date_key
--join azure.newdatedim nwd on dd.fiscal_week=nwd.fiscal_week
select *
from PreStage
```

