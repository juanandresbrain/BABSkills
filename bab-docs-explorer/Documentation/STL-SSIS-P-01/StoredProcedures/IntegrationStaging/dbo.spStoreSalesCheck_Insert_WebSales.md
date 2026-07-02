# dbo.spStoreSalesCheck_Insert_WebSales

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spStoreSalesCheck_Insert_WebSales"]
    dbo_NSBTranslate_batch(["dbo.NSBTranslate_batch"]) --> SP
    dbo_NSBTranslate_logTrans(["dbo.NSBTranslate_logTrans"]) --> SP
    dbo_StoreSalesCheck_StoreSales(["dbo.StoreSalesCheck_StoreSales"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.NSBTranslate_batch |
| dbo.NSBTranslate_logTrans |
| dbo.StoreSalesCheck_StoreSales |

## Stored Procedure Code

```sql
-- =============================================================================================================
-- Name: spStoreSalesCheck_Insert_WebSales
--
-- Description:	
--		Pulls the previous days sales for stores related to the NSBTranslate - i.e., web sales. 
--		
-- Revision History
--		Name:			Date:			Comments:
---		Dan Tweedie		2017-10-09		New query against new settlement tables
-- =============================================================================================================

CREATE PROCEDURE [dbo].[spStoreSalesCheck_Insert_WebSales]
AS
BEGIN

SET NOCOUNT ON;

declare @startDate date, @endDate date

set @startDate = cast(getdate()-1 as date)
set @endDate = cast(getdate()-1 as date)
--set @startDate = cast(getdate()-2 as date)
--set @endDate = cast(getdate()-2 as date)

insert into StoreSalesCheck_StoreSales (store_id, sales_date, units, sales, datestamp)
select 
	lt.sStore,
	CONVERT(char,lt.dTimeStamp,101),
	SUM(lt.iUnits) ,
	SUM(lt.mAmount),
	getdate()
from [STL-SQLAAG-P-01].BABWeCommerce.dbo.NSBTranslate_logTrans lt
  join [STL-SQLAAG-P-01].BABWeCommerce.dbo.NSBTranslate_batch b on lt.sBatchID=b.sBatchID
where b.bSentToAW = 1 
	AND cast(b.dTimeStamp as date) between @startDate and @endDate
	AND cast(lt.dTimeStamp as date) between @startDate and @endDate
and lt.sStore in ('13', '2013')
group by lt.sStore, CONVERT(char,lt.dTimeStamp,101)




END

dbo,spTruncateTnAStaging,-- =============================================
-- Author:		Tim Bytnar
-- Create date: 5/17/2017
-- Description:	This proc simply truncates any staging table involved with the Time and Attendance SSIS package.
-- =============================================
CREATE PROCEDURE spTruncateTnAStaging 

AS
BEGIN
    TRUNCATE TABLE [dbo].[BABW_TnA_Staging]
END
```

