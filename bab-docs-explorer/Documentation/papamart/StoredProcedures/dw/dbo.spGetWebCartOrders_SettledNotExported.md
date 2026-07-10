# dbo.spGetWebCartOrders_SettledNotExported

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spGetWebCartOrders_SettledNotExported"]
    dbo_OrderGroup(["dbo.OrderGroup"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.OrderGroup |

## Stored Procedure Code

```sql
--exec spGetWebCartOrders_SettledNotExported_BAK
CREATE   procedure [dbo].[spGetWebCartOrders_SettledNotExported]
as


IF  EXISTS (SELECT * FROM dbo.sysobjects WHERE id = OBJECT_ID(N'[dbo].[tmpAWT_SettledNotExported]') AND OBJECTPROPERTY(id, N'IsUserTable') = 1)
DROP TABLE [dbo].[tmpAWT_SettledNotExported]


--UNEXPORTED PROBLEM
select SendToSalesExport
	, order_number
	, SiteCode
	, SendToSettlement
	, DateSentToSettlement
	, order_status_code
	, Convert(varchar(8), DateSentToSettlement, 1) 
		+ ' ' 
		+ Cast(Datepart(hour, DateSentToSettlement) as varchar(2)) 
		+ ':' 
		+ Cast(Datepart(minute, DateSentToSettlement) as varchar(2)) 
		as SettleDate
into tmpAWT_SettledNotExported
from Bearwebdb.webcart_commerce.dbo.OrderGroup WITH(NOLOCK)
where 
sendToSalesExport NOT in (2,3)
and sendtosettlement in (2,3) 
and datesenttosettlement < DateAdd(minute, -60,getdate())
order by SendToSalesExport, DateSentToSettlement







dbo,spAdjustedWeeks,-- =============================================
-- Author:	Ian Wallace	
-- Create date: 7/30/2019
-- Description: labor factors from dw & hoo from kodiak 
-- =============================================
CREATE PROCEDURE spAdjustedWeeks 
	-- Add the parameters for the stored procedure here
	@year int, 
	@week int
AS
BEGIN
	
	SET NOCOUNT ON;

 
;WITH cteMdmHoo (STR_NUM, hoo) AS
(
select STR_NUM = CASE WHEN len(STR_NUM) = 1 THEN '0000' + cast(STR_NUM as nvarchar)
				WHEN len(STR_NUM) = 1 THEN '0000' + cast(STR_NUM as nvarchar)
				WHEN len(STR_NUM) = 2 THEN '000' + cast(STR_NUM as nvarchar)
				WHEN len(STR_NUM) = 3 THEN '00' + cast(STR_NUM as nvarchar)
				WHEN len(STR_NUM) = 4 THEN '0' + cast(STR_NUM as nvarchar)
				WHEN len(STR_NUM) = 5 THEN cast(STR_NUM as nvarchar)
				END, 
sum(isnull(hoursSched,0))-72 from [KODIAK].[BABWMstrData].[dbo].[HOO_DW] 
where cast(substring(yearWeek,1,4) as int) = @year and Country = 'US'
and yearWeek = CASE WHEN len(@week) = 1 THEN cast(@year as varchar) + '0' + cast(@week as varchar) 
ELSE cast(@year as varchar) + cast(@week as varchar) END group by STR_NUM
)
select aVeAw.store, aVeAw.year, aVeAw.week, aVeAw.startDate, aVeAw.dpc, aVeAw.law, 
isnull(cteMdmHoo.hoo,0.00) as 'hoo',
aVeAw.eqv, aVeAw.spp, aVeAw.msc, aVeAw.ffh, aVeAw.wbt_id
from [dbo].[ActualVEarnedAdjustedWeeks] aVeAw 
left outer join cteMdmHoo on cteMdmHoo.STR_NUM = aVeAw.store
where aVeAw.year =  @year and aVeAw.week = @week order by store asc


END
```

