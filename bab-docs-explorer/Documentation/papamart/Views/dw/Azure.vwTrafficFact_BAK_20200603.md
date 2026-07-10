# Azure.vwTrafficFact_BAK_20200603

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["Azure.vwTrafficFact_BAK_20200603"]
    dbo_date_dim(["dbo.date_dim"]) --> VIEW
    Azure_NewDateDim(["Azure.NewDateDim"]) --> VIEW
    SHPR_TRK_TRFC_FCT(["SHPR_TRK_TRFC_FCT"]) --> VIEW
    dbo_SHPR_TRK_TRFC_FCT(["dbo.SHPR_TRK_TRFC_FCT"]) --> VIEW
    dbo_Store_Dim(["dbo.Store_Dim"]) --> VIEW
    dbo_StoreCompDetail_Dim(["dbo.StoreCompDetail_Dim"]) --> VIEW
    dbo_time_dim(["dbo.time_dim"]) --> VIEW
    Azure_vwDateFilter(["Azure.vwDateFilter"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.date_dim |
| Azure.NewDateDim |
| SHPR_TRK_TRFC_FCT |
| dbo.SHPR_TRK_TRFC_FCT |
| dbo.Store_Dim |
| dbo.StoreCompDetail_Dim |
| dbo.time_dim |
| Azure.vwDateFilter |

## View Code

```sql
CREATE VIEW [Azure].[vwTrafficFact_BAK_20200603] AS
-- =============================================================================================================
-- Name: [Azure].[vwTraffic]
--
-- Description: Traffic by store and hour.  
--
--
-- Dependencies: 
--
-- Revision History
--		Name:				Date:			Comments:
--		Tim Bytnar			4/11/2018		Initial creation
--
-- =============================================================================================================
WITH HasDailyTraffic (StoreKey, DateKey, HasDailyTraffic) AS (
	SELECT 
		s.STR_KEY,
		ndd.Date_Key,
		CASE WHEN SUM(s.EXITS) = 0 THEN 0
			ELSE 1
		END
	FROM SHPR_TRK_TRFC_FCT s
	INNER JOIN DW.dbo.date_dim d
		ON d.date_key=s.DT_KEY
	INNER JOIN DW.Azure.NewDateDim ndd
		ON d.actual_date = ndd.Date_Key
	WHERE
		(s.ENTERS <> 0
		OR s.EXITS <> 0)
		AND d.actual_date>=DATEADD(day, -7, DATEADD(year, -2, DATEADD(yy, DATEDIFF(yy, 0, GETDATE()), 0)))
	GROUP BY 
		s.STR_KEY,
		ndd.Date_Key
	)
SELECT  sd.store_id AS StoreKey,
		CAST(dd.actual_date AS DATE) AS TrafficDate,
		td.hour AS TrafficHour,
	    SUM(sttf.EXITS) AS Traffic,
		h.HasDailyTraffic -- This field is used in "Traffic" transaction counts - when we only count transactions for stores that have traffic during that day.  Critical for conversion calcs.
FROM
	DW.dbo.SHPR_TRK_TRFC_FCT sttf 
	INNER JOIN Azure.vwDateFilter dd 
		ON dd.date_key = sttf.DT_KEY
	INNER JOIN DW.dbo.time_dim td 
		ON td.time_key = sttf.TM_KEY
	LEFT JOIN DW.dbo.StoreCompDetail_Dim cmp 
		ON cmp.store_key = sttf.STR_KEY AND cmp.date_key = sttf.DT_KEY
	INNER JOIN DW.dbo.Store_Dim sd
		ON sd.store_key=sttf.STR_KEY
	INNER JOIN DW.Azure.NewDateDim ndd
		ON dd.actual_date = ndd.Date_Key
	INNER JOIN HasDailyTraffic h
		ON h.StoreKey=sttf.STR_KEY
		AND h.DateKey=ndd.date_key
WHERE
	(sttf.ENTERS <> 0
	OR sttf.EXITS <> 0)
	
GROUP BY sd.store_id,
		 dd.actual_date,
		 td.hour,
		 h.HasDailyTraffic
```

