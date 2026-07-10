# dbo.vw_StyleSummary_Any_Week

**Database:** reportingservices_subscription  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vw_StyleSummary_Any_Week"]
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
CREATE VIEW [dbo].[vw_StyleSummary_Any_Week]
AS

select ss.SortType as SortType
	,ss.Division
	,ss.Caption
	,'[Date].[Fiscal].[Fiscal Week].&[' + CAST(dd.fiscal_year AS varchar) + ' ' + right('0'+CAST(dd.fiscal_week AS varchar),2) + ']' AS Fiscal
	,'FileName'=
			case
				when ss.sorttype='SS' Then 'TOTAL'
				WHEN ss.sorttype='H' Then 'HILO'
			END +' '+ss.caption+' '+right('0'+cast(datepart(mm,getdate()) as varchar),2)+'-'+right('0'+cast(datepart(dd,getdate()) as varchar),2)+'-'+cast(datepart(yy,getdate()) 
		as varchar)
	,'\\sharebear1\Groups\Planning\MANLEY' as Path
	, 'PDF' as FileExtension
	, CAST(dd.fiscal_year AS varchar) + ' ' + right('0'+CAST(dd.fiscal_week AS varchar),2) as fiscal_week
	from dw.dbo.date_dim dd
	cross join ReportingServices_Subscription.dbo.StyleSummary ss
	group by ss.SortType
		,ss.Division
		,ss.Caption
		,dd.fiscal_year
		,dd.fiscal_week


/*
select * from dw..date_dim where actual_date = '05/28/2008'    grant select on [vw_StyleSummary_Any_Week] to link_readonly

select * from [vw_StyleSummary_Any_Week] where fiscal_week = '2008 22'

select * from dbo.StyleSummary

SELECT *  FROM [reportingservices_subscription].[dbo].[vw_StyleSummary]

select * from [reportingservices_subscription].[dbo].[vw_StyleSummary_Any_Week] where fiscal_week = '2008 22'
*/
```

