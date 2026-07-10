# dbo.vwBO_date_dim

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwBO_date_dim"]
    dbo_date_dim(["dbo.date_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.date_dim |

## View Code

```sql
CREATE VIEW [dbo].[vwBO_date_dim]
AS

	SELECT *
		,'''' + RIGHT(cast(fiscal_year as varchar), 2) + ' ' + 'Q' + cast(fiscal_quarter as varchar) as FiscalYearQuarter
		,cast(fiscal_year as varchar) + ' ' + RIGHT('0' + cast(fiscal_period as varchar), 2) as FiscalMonth
		,cast(fiscal_year as varchar) + ' ' + RIGHT('0' + cast(fiscal_week as varchar), 2) as FiscalWeekKey
		,cast(year as varchar) + ' ' + RIGHT('0' + cast(month as varchar), 2) as CalendarYearMonth
		,'''' + RIGHT(CAST(fiscal_year AS varchar), 2) + ' ' +
			CASE
				WHEN fiscal_period = 1 THEN 'Jan'
				WHEN fiscal_period = 2 THEN 'Feb'
				WHEN fiscal_period = 3 THEN 'Mar'
				WHEN fiscal_period = 4 THEN 'Apr'
				WHEN fiscal_period = 5 THEN 'May'
				WHEN fiscal_period = 6 THEN 'Jun'
				WHEN fiscal_period = 7 THEN 'Jul'
				WHEN fiscal_period = 8 THEN 'Aug'
				WHEN fiscal_period = 9 THEN 'Sep'
				WHEN fiscal_period = 10 THEN 'Oct'
				WHEN fiscal_period = 11 THEN 'Nov'
				WHEN fiscal_period = 12 THEN 'Dec'
				ELSE 'Other'
			END as FiscalMonthName
		,CONVERT(varchar, actual_date, 101) as SimpleDate
		,'''' + RIGHT(CAST(fiscal_year AS varchar), 2) + ' FW' + RIGHT('0' + cast(fiscal_week as varchar), 2) as FiscalWeekDisplay
		,CAST(year AS varchar) + ' ' +
			CASE
				WHEN month = 1 THEN 'Jan'
				WHEN month = 2 THEN 'Feb'
				WHEN month = 3 THEN 'Mar'
				WHEN month = 4 THEN 'Apr'
				WHEN month = 5 THEN 'May'
				WHEN month = 6 THEN 'Jun'
				WHEN month = 7 THEN 'Jul'
				WHEN month = 8 THEN 'Aug'
				WHEN month = 9 THEN 'Sep'
				WHEN month = 10 THEN 'Oct'
				WHEN month = 11 THEN 'Nov'
				WHEN month = 12 THEN 'Dec'
				ELSE 'Other'
			END as CalendarMonthName
		,cast(year as varchar) +
			CASE
				WHEN LOWER(season) = 'spring' THEN '1'
				ELSE '2'
			END as SeasonKey
		,season + ' ''' + RIGHT(cast(year as varchar), 2) as SeasonDisplay
		,N'Current Time' as [Time Calcs]
	FROM dbo.date_dim
	WHERE date_key > 0
```

