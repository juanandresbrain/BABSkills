# dbo.generateCurrentDateInformation

**Database:** reportingservices_subscription  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.generateCurrentDateInformation"]
    CurrentDateInformation(["CurrentDateInformation"]) --> SP
    dbo_date_dim(["dbo.date_dim"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| CurrentDateInformation |
| dbo.date_dim |

## Stored Procedure Code

```sql
-- =============================================
-- Author:		Gary Murrish
-- Create date: 10/10/2012
--			This stored procedures will generate the record
--			in CurrentDateInformation based upon the 
--			date provided
-- Modifications
--		Changed the format of Fiscal Quarter Name 2014-01-13
-- =============================================
CREATE PROCEDURE [dbo].[generateCurrentDateInformation]
    @asOfDate DATETIME = NULL
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

	TRUNCATE TABLE CurrentDateInformation
	IF @asOfDate IS NULL
	BEGIN
		SET @asOfDate = cast(convert(VARCHAR(10), getdate(), 101) AS DATETIME)
	END

	DECLARE @prior_FY INT
	DECLARE @prior_FW INT
	DECLARE @prior_FQ int
	DECLARE @prior_FQ_Value int
	DECLARE @prior_FP INT
	DECLARE @prior_FW_EndingDate DATETIME

	DECLARE @this_FY INT
	DECLARE @this_FW INT
	DECLARE @this_FQ INT
	DECLARE @this_FP INT

	-- Get the prior week information
	SELECT @prior_FQ = fiscal_year * 10 + fiscal_quarter
		 , @prior_FP = fiscal_year * 100 + fiscal_period
		 , @prior_FY = fiscal_year
		 , @prior_FW = fiscal_week
		 , @prior_FQ_Value = dd.fiscal_quarter
	FROM
		dw.dbo.date_dim dd WITH (NOLOCK)
	WHERE
		dd.actual_date = dateadd(D, -7, @asOfDate)

	SELECT @prior_FW_EndingDate = max(actual_date)
	FROM
		dw.dbo.date_dim dd WITH (NOLOCK)
	WHERE
		dd.fiscal_year = @prior_FY
		AND dd.fiscal_week = @prior_fw


	-- Get the current week information
	SELECT @this_FQ = fiscal_year * 10 + fiscal_quarter
		 , @this_FP = fiscal_year * 100 + fiscal_period
		 , @this_FY = fiscal_year
		 , @this_FW = fiscal_week
	FROM
		dw.dbo.date_dim dd WITH (NOLOCK)
	WHERE
		dd.actual_date = @asofDate

	INSERT INTO CurrentDateInformation ([MDX Fiscal]
									  , Fiscal
									  , [MDX Fiscal Week]
									  , weekEndingDate
									  , isEndFiscalQuarter
									  , isEndFiscalPeriod
									  , FiscalPeriod
									  , FiscalYear
									  , FWSuffix
									  , FPSuffix
									  , FQSuffix)
	SELECT '[Date].[Fiscal].[Fiscal Week].&[' + cast(@prior_FY AS VARCHAR) + ' ' + right('0' + cast(@prior_FW AS VARCHAR), 2) + ']' AS 'MDX Fiscal'
		 , cast(@prior_FY AS VARCHAR) + ' ' + right('0' + cast(@prior_FW AS VARCHAR), 2) AS 'Fiscal'
		 , '[Date].[Fiscal Week].&[' + cast(@prior_FY AS VARCHAR) + ' ' + right('0' + cast(@prior_fw AS VARCHAR), 2) + ']' AS 'MDX Fiscal Week'
		 , convert(VARCHAR(10), @prior_FW_EndingDate, 120) AS weekEndingDate
		 , CASE
			   WHEN @prior_FQ <> @this_FQ THEN
				   1
			   ELSE
				   0
		   END AS isEndFiscalQuarter
		 , CASE
			   WHEN @prior_FP <> @this_FP THEN
				   1
			   ELSE
				   0
		   END AS isEndFiscalPeriod
		 , @prior_FP AS FiscalPeriod
		 , @prior_FY AS FiscalYear
		 , '-' + cast(@prior_FY AS VARCHAR) + 'FW' + right('00' + cast(@prior_FW AS VARCHAR), 2)
		 , '-' + cast(@prior_FY AS VARCHAR) + 'FP' + right('00' + cast(@prior_FP AS VARCHAR), 2)
		 , '-' + cast(@prior_FY AS VARCHAR) + 'FQ' + cast(@prior_FQ_value AS VARCHAR)
END
```

