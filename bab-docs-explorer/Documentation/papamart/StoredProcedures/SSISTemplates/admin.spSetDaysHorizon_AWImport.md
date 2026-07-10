# admin.spSetDaysHorizon_AWImport

**Database:** SSISTemplates  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["admin.spSetDaysHorizon_AWImport"]
    admin_configurations(["admin.configurations"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| admin.configurations |

## Stored Procedure Code

```sql
-- =============================================================================================================
-- Name: spSetDaysHorizon_AWImport
--
-- Description:	
--		Set the number of days to pull from Auditworks and import into the Datawarehouse
--
-- Input:
--		None
--
-- Output: 
--		Updates the associated records in the Configuration for the SSIS packages
--
-- Dependencies: 
--
--
-- Revision History
--		Name:				Date:			Comments:
--		Gary Murrish		12/26/2014		Changed to permanently process 20 days due to performance reasons
--		Gary Murrish		6/9/2014		Changed to permanently process 30 days due to performance reasons
--		Gary Murrish		6/6/2014		Changed to permanently process 45 days per Jack McCormick
--		Gary Murrish		4/8/2014		Removed temporary force of March 2014
--		Gary Murrish		4/3/2014		Temporarily force all of March 2014 to be processed....
--		Gary Murrish		8/15/2013		created
-- =============================================================================================================
CREATE PROCEDURE [admin].[spSetDaysHorizon_AWImport]
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

	DECLARE @daysHorizon int

	--DECLARE @asOfDate datetime
	--SET @asOfDate = dw.dbo.fnDateOnly(GETDATE())

	--DECLARE @fiscalYear int
	--DECLARE @fiscalPeriod int
	--DECLARE @lastDayOfPeriod int
	--DECLARE @firstDayOfPeriod int
	--DECLARE @todayDay int
	--DECLARE @todayName varchar(20)
	--DECLARE @daysLeftInMonth int



	--SELECT
	--	@fiscalYear = fiscal_year,
	--	@fiscalPeriod = fiscal_period,
	--	@todayDay = date_key,
	--	@todayName = day_name
	--FROM
	--	dw.dbo.date_dim WITH (NOLOCK)
	--WHERE
	--	actual_date = @asOfDate

	--SELECT
	--	@lastDayOfPeriod = MAX(dd.date_key),
	--	@firstDayOfPeriod = MIN(dd.date_key)
	--FROM
	--	dw.dbo.date_dim dd WITH (NOLOCK)
	--WHERE
	--	dd.fiscal_year = @fiscalYear
	--	AND dd.fiscal_period = @fiscalPeriod


	--SET @daysLeftInMonth = @lastDayOfPeriod - @todayDay + 1

	--IF @daysLeftInMonth <= 3 OR (@todayName IN ('THURSDAY', 'FRIDAY', 'SATURDAY') AND @daysLeftInMonth < 14)
	--	SET @daysHorizon = @todayDay - @firstDayOfPeriod + 1
	--ELSE
	--	SET @daysHorizon = 15

	SET @daysHorizon = 35
	
	UPDATE x
		SET ConfiguredValue = @daysHorizon
	FROM
		[SSISTemplates].[admin].[configurations] x
	WHERE (ConfigurationFilter = 'Load Discount Results from DW' AND PackagePath = '\Package.Variables[User::DaysHorizon].Properties[Value]')
	OR (ConfigurationFilter = 'AW Copy to Staging' AND PackagePath = '\Package.Variables[User::DaysHorizon].Properties[Value]')
	OR (ConfigurationFilter = 'Giftcard Extract AW' AND PackagePath = '\Package.Variables[User::DaysHorizon].Properties[Value]')
END
```

