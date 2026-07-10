# dbo.vwScorecardDate_Dim

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwScorecardDate_Dim"]
    date_dim(["date_dim"]) --> VIEW
    dbo_date_dim(["dbo.date_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| date_dim |
| dbo.date_dim |

## View Code

```sql
CREATE    VIEW dbo.vwScorecardDate_Dim
AS


SELECT 	--date_key, 
	getdate() as currentDateTime,
	(select week_id from date_dim where actual_date >= dateadd(d,-1,getdate()) and actual_date <= getdate()) as current_week_id,
	(select period_id from date_dim where actual_date >= dateadd(d,-1,getdate()) and actual_date <= getdate()) as current_period_id,
	(select max(period_id) from date_dim where week_id = 
		(select week_id-1 
		 from date_dim 
		 where actual_date >= dateadd(d,-1,getdate()) and actual_date <= getdate() 
		)
		) as previous_week_period_id,
	a.week_id,
	a.weekendingdate,
	a.ttlDaysInPeriod,
	a.ttlWeekendDays,
	a.ttlWeekDays,
	fiscal_year, 
	season, 
	fiscal_quarter, 
	fiscal_period, 
	fiscal_week, 
	week_of_period, 
	week_of_quarter, 
	period_of_quarter,
	period_id, 
	quarter_id



FROM 
(
select 	week_id, 
	max(actual_date) as weekendingdate,
	count(date_key) as ttlDaysInPeriod,
	sum(CASE WHEN weekend_y_n = 'y' THEN 1 ELSE 0 END) as ttlWeekendDays,
	sum(CASE WHEN weekend_y_n = 'n' THEN 1 ELSE 0 END) as ttlWeekDays

from dbo.date_dim

-- WHERE fiscal_year = 2005 
-- and fiscal_period = 3

group by week_id
) a

JOIN date_dim dd on a.week_id = dd.week_id and dd.day_of_week = 7
-- WHERE fiscal_year = 2005 
-- and period_id = @curFP
```

