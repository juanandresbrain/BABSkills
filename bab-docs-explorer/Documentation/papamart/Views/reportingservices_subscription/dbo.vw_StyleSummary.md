# dbo.vw_StyleSummary

**Database:** reportingservices_subscription  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vw_StyleSummary"]
    dbo_date_dim(["dbo.date_dim"]) --> VIEW
    dbo_StyleSummary(["dbo.StyleSummary"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.date_dim |
| dbo.StyleSummary |

## View Code

```sql
CREATE VIEW [dbo].[vw_StyleSummary]
AS
select ss.SortType as 'SortType',ss.Division,ss.Caption,
'[Date].[Fiscal].[Fiscal Week].&[' + CAST(dd.fiscal_year AS varchar) + ' ' + right('0'+CAST(dd.fiscal_week AS varchar),2) + ']' AS 'Fiscal',
'FileName'=
case
	when ss.sorttype='SS' Then 'TOTAL'
	WHEN ss.sorttype='H' Then 'HILO'
END +' '+ss.caption+' '+right('0'+cast(datepart(mm,getdate()) as varchar),2)+'-'+right('0'+cast(datepart(dd,getdate()) as varchar),2)+'-'+cast(datepart(yy,getdate()) as varchar),
--'\\ursamajor\shared\it\jll' as Path,
'\\sharebear1\Groups\Planning\MANLEY' as Path,
--'\\babwpas01\c$\Merch Style PDFs' as Path,
'PDF' as FileExtension
from dw.dbo.date_dim dd,ReportingServices_Subscription.dbo.StyleSummary ss
where dd.actual_date = (SELECT DATEADD(d, -7, CAST(CONVERT(varchar(10),GETDATE(),101) AS smalldatetime)))
```

