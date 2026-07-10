# Accounting.spRpt_Transaction_RawSummaryFromStoreServer_ForSingleFiscalMonth_NonPickUpFromStore

**Database:** DWStaging  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["Accounting.spRpt_Transaction_RawSummaryFromStoreServer_ForSingleFiscalMonth_NonPickUpFromStore"]
    dbo_date_dim(["dbo.date_dim"]) --> SP
    dbo_Sales_GAAP_RawFromStoreServer(["dbo.Sales_GAAP_RawFromStoreServer"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.date_dim |
| dbo.Sales_GAAP_RawFromStoreServer |

## Stored Procedure Code

```sql
-- =============================================
-- Author:		Dan Tweedie 2020-10-05
-- =============================================
CREATE PROCEDURE [Accounting].[spRpt_Transaction_RawSummaryFromStoreServer_ForSingleFiscalMonth_NonPickUpFromStore]
	@FiscalYear INT
	, @FiscalPeriod INT
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

	SELECT 
		trs.location_code
		, trs.location_name
		, SUM(trs.net_sales) AS net_sales
	--FROM [Accounting].[Sales_GAAP_RawFromStoreServer] trs WITH(NOLOCK)
	from dw.dbo.Sales_GAAP_RawFromStoreServer trs
		INNER JOIN dw.dbo.date_dim dd WITH(NOLOCK)
			ON trs.date_key = dd.date_key
	WHERE dd.fiscal_year = @FiscalYear
		AND dd.fiscal_period = @FiscalPeriod
		and isBOSISorBOPIS = 0
	GROUP BY 
		trs.location_code
		, trs.location_name
END
```

