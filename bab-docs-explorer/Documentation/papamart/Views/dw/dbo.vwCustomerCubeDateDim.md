# dbo.vwCustomerCubeDateDim

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwCustomerCubeDateDim"]
    dbo_date_dim(["dbo.date_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.date_dim |

## View Code

```sql
CREATE view [dbo].[vwCustomerCubeDateDim]

AS

SELECT        
	date_key as DateKey, 
	cast(actual_date as date) ActualDate, 
	fiscal_year as FiscalYear, 
	fiscal_quarter as FiscalQuarter ,
	fiscal_period as FiscalPeriod,
	fiscal_week as FiscalWeek,
	year as CalendarYear, 
	month_name as MonthName, 
	day_of_month as DayOfMonth, 
	day_name as DayName, 
	day_id as DayID,
	dense_rank() over (order by fiscal_year, fiscal_week) as WeekID,
	dense_rank() over (order by fiscal_year, fiscal_period) as PeriodID,
	dense_rank() over(order by fiscal_year, fiscal_quarter) as QuarterID,
	dense_rank() over (order by year, month_name) as MonthNameID,
	dense_rank() over (order by year, month_name, day_of_month) as DayOfMonthID
FROM  dbo.date_dim with (nolock)
where fiscal_year >= 2014
--or date_key = 0
```

