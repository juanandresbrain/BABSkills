# dbo.spRpt_Balancing_ByDay

**Database:** DWStaging  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spRpt_Balancing_ByDay"]
    dbo_Balancing_Source(["dbo.Balancing_Source"]) --> SP
    dbo_Balancing_Target(["dbo.Balancing_Target"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Balancing_Source |
| dbo.Balancing_Target |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[spRpt_Balancing_ByDay]
-- =============================================================================================================
-- Name: spRpt_Balancing_ByDay
--
-- Description:	
--	Generate the recordset to print the balancing by Day. This extracts the information on a day by day
--		basis from the Balancing tables.
--
-- Input:		
--
-- Output: 
--
-- Dependencies: 
--
-- Revision History
--		Name:			Date:			Comments:
--		Gary Murrish	4/17/2013		Created

-- =============================================================================================================
AS

	SET NOCOUNT ON


	IF OBJECT_ID('tempdb..#tmpSource') IS NOT NULL
	BEGIN
		DROP TABLE #tmpSource
	END

	SELECT
		bs.Transaction_Date,
		SUM(bs.GAAPSales) + SUM(ISNULL(bs.VATAmount, 0)) AS AWGAAPSales
	INTO #tmpSource
	FROM
		DWStaging.dbo.Balancing_Source bs WITH (NOLOCK)
	GROUP BY bs.Transaction_Date

	IF OBJECT_ID('tempdb..#tmpTarget') IS NOT NULL
	BEGIN
		DROP TABLE #tmpTarget
	END

	SELECT
		bt.Transaction_Date,
		SUM(bt.GAAPSales) AS DWGAAPSales
	INTO #tmpTarget
	FROM
		DWStaging.dbo.Balancing_Target bt WITH (NOLOCK)
	GROUP BY bt.Transaction_Date

	SELECT
		s.Transaction_Date,
		s.AWGAAPSales,
		ISNULL(t.dwGAAPSales, 0) AS DWAGGPSales,
		s.AWGAAPSales - ISNULL(t.dwGAAPSales, 0) AS Difference
	FROM
		#tmpSource s WITH (NOLOCK)
		LEFT JOIN #tmpTarget t WITH (NOLOCK)
			ON s.Transaction_Date = t.Transaction_Date
	UNION ALL
	SELECT
		t.Transaction_Date,
		ISNULL(s.AWGAAPSales, 0) AS AWGAAPSales,
		t.dwGAAPSales AS DWAGGPSales,
		ISNULL(s.AWGAAPSales, 0) - ISNULL(t.dwGAAPSales, 0) AS Difference
	FROM
		#tmpTarget t WITH (NOLOCK)
		LEFT JOIN #tmpSource s WITH (NOLOCK)
			ON s.Transaction_Date = t.Transaction_Date
	WHERE
		s.Transaction_Date IS NULL
```

