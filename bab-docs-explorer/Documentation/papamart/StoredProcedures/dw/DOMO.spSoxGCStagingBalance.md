# DOMO.spSoxGCStagingBalance

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["DOMO.spSoxGCStagingBalance"]
    staging_ReconUK(["staging.ReconUK"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| staging.ReconUK |

## Stored Procedure Code

```sql
CREATE PROCEDURE [DOMO].[spSoxGCStagingBalance]
@Fiscal_Year int,
@AuditQuarter int
AS

-- =============================================================================================================
-- Name: [DOMO].[spSoxGCStagingBalance]
--
-- Description: Sox StagingGiftCard Balance Reporting to DOMO.
-- 
--
--
-- Dependencies: 
--
-- Revision History
--		Name:				Date:			Comments:
--		Brian Byas			9/8/2016		Initial creation
-- =============================================================================================================




WITH StagingBalance (Fiscal_Year,AuditQuarter,ActivationMid,NumCards,OutstandingBalance) AS (
		
		/*
		-- Sox Staging GiftCard Balance Reporting
		*/
	
	
		SELECT
		@Fiscal_year AS Fiscal_Year,
		@AuditQuarter AS AuditQuarter,			
		ru.ActivationMid,	
		COUNT(*) AS NumCards,	
		SUM(ru.OutstandingBalance) AS OutstandingBalance	
	FROM		
		SOX.staging.ReconUK ru WITH (NOLOCK)	
	GROUP BY ru.ActivationMid		

		)


		SELECT * FROM StagingBalance
		ORDER BY ActivationMid


















dbo,spRPT_Product_TransWithSKUs2,-- =====================================================================================================
-- Name: spRPT_Product_TransWithSKUs2
--
-- Description:	Pulls transaction data from the data warehouse for specific SKUs
--
-- Input:	
--			@fromDate			datetime	Sets date range
--			@thruDate			datetime	
--			@selSKUs			varchar(MAX) A comma delimited list of SKUs
--
-- Output: Resultset 
--			
--
-- Dependencies: None
--
-- Revision History
--		Name:			Date:			Comments:
--		Shawn Burge		03/21/2012		Initial Release
-- =====================================================================================================
CREATE PROCEDURE [dbo].[spRPT_Product_TransWithSKUs2]
	@fromDate DATETIME,
	@thruDate DATETIME,
	@selSKUs VARCHAR(MAX)
AS
BEGIN
	SET NOCOUNT ON;

	SET @fromDate = CAST(FLOOR(CAST(@fromDate AS FLOAT)) AS DATETIME);
	SET @thruDate = CAST(FLOOR(CAST(@thruDate AS FLOAT)) AS DATETIME);

	DECLARE @fromDateKey INT
	DECLARE @thruDateKey INT

	SET @fromDateKey = (SELECT date_key FROM date_dim WITH (NOLOCK) WHERE actual_date = @fromDate);
	SET @thruDateKey = (SELECT date_key FROM date_dim WITH (NOLOCK) WHERE actual_date = @thruDate);

	SELECT store_id, fiscal_year, fiscal_week, Transaction_Type, ISNULL(CLNSD_GST_ID, 0) AS CLNSD_GST_ID, partyflag, skucount AS [ActualSkuCount], merchandiseunits,
		COUNT(transaction_id) AS [NumberOfTransactions], SUM(skuCount) AS [SkuCount],
		SUM(merchandiseunits) AS [TotalUnits], SUM(animalunits) AS [AnimalUnits],
		SUM(LineCount) AS [LineCount], SUM(GaapSales) AS [GAAPSales],
		SUM(unitGrossAmount) AS [UnitGrossAmount], SUM(unitdiscamount) AS [UnitDiscountAmount]
	FROM (
		SELECT trig.transaction_id, sd.store_id, dd.fiscal_year, dd.fiscal_week , dt.transaction_type,
			trig.selectedUnits as skuCount, dt.MerchandiseUnits, dt.LineCount, dt.AnimalUnits, dt.GaapSales,
			dt.UnitGrossAmount, dt.UnitDiscAmount, dt.PartyFlag, ctsf.CLNSD_GST_ID
			FROM (
				SELECT transaction_id, SUM(tdf.units) AS selectedUnits FROM	transaction_detail_facts tdf WITH (NOLOCK)
					WHERE product_key IN (
						SELECT product_key FROM product_dim pd WITH (NOLOCK)
							WHERE sku IN (SELECT [Val] FROM dw.dbo.fn_String_To_Table(@selSKUs, ',', 1))
						)
						AND date_key BETWEEN @fromDateKey AND @thruDateKey
					GROUP BY transaction_id) trig
			INNER JOIN vwDW_Transactions dt WITH (NOLOCK)
				ON trig.transaction_id = dt.transaction_id
			INNER JOIN date_dim dd WITH (NOLOCK)
				ON dd.date_key = dt.date_key
			INNER JOIN store_dim sd WITH (NOLOCK)
				ON sd.store_key = dt.store_key
			LEFT JOIN CRM_TRN_SUM_FACT ctsf WITH (NOLOCK)
				ON ctsf.TDF_TRN_ID = trig.transaction_id
	) A
	GROUP BY store_id, fiscal_year, fiscal_week, Transaction_Type, ISNULL(CLNSD_GST_ID, 0), partyflag, skucount, merchandiseunits
	ORDER BY store_id, fiscal_year, fiscal_week, Transaction_Type, ISNULL(CLNSD_GST_ID, 0), partyflag, skucount, merchandiseunits
END
```

