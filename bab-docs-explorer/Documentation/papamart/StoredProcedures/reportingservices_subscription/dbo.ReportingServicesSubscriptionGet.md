# dbo.ReportingServicesSubscriptionGet

**Database:** reportingservices_subscription  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.ReportingServicesSubscriptionGet"]
    vw_Reporting_SundayMerch(["vw_Reporting_SundayMerch"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| vw_Reporting_SundayMerch |

## Stored Procedure Code

```sql
-- =============================================
-- Author:		Zac Doerr
-- Create date: Oct 17 2008	
-- Description:	Gather all reporting service subscriptions with a given caption for the Sunday Merch Reports
-- =============================================

-- Modifications
--	7/28/2012	G Murrish	Changed the Query so that it only gets the report for the Sunday Merch Reports
CREATE PROCEDURE [dbo].[ReportingServicesSubscriptionGet]
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

SELECT 
	ReportId,
	FileName,
	Path,
	FileExtension,
	ReportingServiceReportName
FROM vw_Reporting_SundayMerch

END
```

