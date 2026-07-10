# dbo.spRpt_Balancing_ForDayAndStore

**Database:** DWStaging  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spRpt_Balancing_ForDayAndStore"]
    Balancing_Source(["Balancing_Source"]) --> SP
    dbo_date_dim(["dbo.date_dim"]) --> SP
    dbo_store_dim(["dbo.store_dim"]) --> SP
    dbo_Transaction_Facts(["dbo.Transaction_Facts"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Balancing_Source |
| dbo.date_dim |
| dbo.store_dim |
| dbo.Transaction_Facts |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[spRpt_Balancing_ForDayAndStore]
	-- =============================================================================================================
	-- Name: spRpt_Balancing_ForDayAndStore
	--
	-- Description:	
	--	Generate the recordset to print the balancing by Day. This extracts the information for a day and store
	--		by transaction
	--		basis from the Balancing tables.
	--
	-- Input:	
	--		forDate - Date of the day to list
	--		store_no - Store Number to list	
	--
	-- Output: 
	--
	-- Dependencies: 
	--
	-- Revision History
	--		Name:			Date:			Comments:
	--		Gary Murrish	4/17/2013		Created

	-- =============================================================================================================
	@forDate datetime,
	@store_no int
AS

	SET NOCOUNT ON


	DECLARE @dateKey int
	SELECT
		@dateKey = date_key
	FROM
		dw.dbo.date_dim dd WITH (NOLOCK)
	WHERE
		dd.actual_date = @forDate

	DECLARE @storeKey int
	SELECT
		@storeKey = sd.store_key
	FROM
		dw.dbo.store_dim sd WITH (NOLOCK)
	WHERE
		sd.store_id = @store_no

	IF OBJECT_ID('tempdb..#tmpSource') IS NOT NULL
	BEGIN
		DROP TABLE #tmpSource
	END

	SELECT
		bs.Transaction_Date,
		bs.Store_No,
		bs.transaction_id,
		SUM(bs.gaapsales) + SUM(ISNULL(bs.VATAmount, 0)) AS gaapsales
	INTO #tmpSource
	FROM
		Balancing_Source bs WITH (NOLOCK)
	WHERE
		bs.Store_No = @store_no
		AND bs.Transaction_Date = @forDate
	GROUP BY	bs.Transaction_Date,
				bs.Store_No,
				bs.transaction_id

	SELECT
		@forDate AS transaction_date,
		@store_no AS Store_no,
		ISNULL(s.GAAPSales, 0) AS AWGAAPSales,
		tf.GAAP_sales_amount AS DWGAAPSales,
		tf.GAAP_sales_amount - ISNULL(s.GAAPSales, 0) AS Difference,
		tf.transaction_id

	FROM
		dw.dbo.Transaction_Facts tf WITH (NOLOCK)
		LEFT JOIN #tmpSource s WITH (NOLOCK)
			ON tf.transaction_id = s.transaction_id
	WHERE
		tf.GAAP_sales_amount <> ISNULL(s.GAAPSales, 0)
		AND tf.store_key = @storeKey
		AND tf.date_key = @dateKey
	UNION ALL
	SELECT
		@forDate AS transaction_date,
		@store_no AS Store_no,
		ISNULL(s.GAAPSales, 0) AS AWGAAPSales,
		ISNULL(tf.GAAP_sales_amount, 0) AS DWGAAPSales,
		ISNULL(tf.GAAP_sales_amount, 0) - ISNULL(s.GAAPSales, 0) AS Difference,
		tf.transaction_id

	FROM
		#tmpSource s WITH (NOLOCK)
		LEFT JOIN dw.dbo.Transaction_Facts tf WITH (NOLOCK)
			ON tf.transaction_id = s.transaction_id
	WHERE
		tf.transaction_id IS NULL
```

