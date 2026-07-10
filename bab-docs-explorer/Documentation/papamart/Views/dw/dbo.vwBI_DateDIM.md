# dbo.vwBI_DateDIM

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwBI_DateDIM"]
    dbo_date_dim(["dbo.date_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.date_dim |

## View Code

```sql
CREATE view [dbo].[vwBI_DateDIM]

as
	SELECT 
		cast(actual_date as date) as ActualDate,
		fiscal_year as FiscalYear,
		fiscal_quarter as FiscalQuarter,
		fiscal_period as FiscalPeriod,
		fiscal_week as FiscalWeek,
		concat('''',right(fiscal_year,2), ' Q', fiscal_quarter) as FiscalQuarterDisplay,
		concat('''',right(fiscal_year,2), ' P', fiscal_period) as FiscalPeriodDisplayName,
		concat('''',right(fiscal_year,2), ' FW', fiscal_week) as FiscalWeekDisplay,
		year as CalendarYear,
		month as CalendarMonth,
		CAST(year AS varchar) + ' ' +
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
			END as CalendarMonthName,
		day_name as DayName,
		day_of_week as DayOfWeek,
		day_of_month as DayOfCalendarMonth,
		day_of_year as DayOfCalendarYear

	
	FROM dbo.date_dim
	WHERE actual_date>=DATEADD(year, -2, DATEADD(yy, DATEDIFF(yy, 0, GETDATE()), 0))
```

