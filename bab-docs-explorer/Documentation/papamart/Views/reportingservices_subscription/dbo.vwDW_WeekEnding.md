# dbo.vwDW_WeekEnding

**Database:** reportingservices_subscription  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_WeekEnding"]
    dbo_date_dim(["dbo.date_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.date_dim |

## View Code

```sql
CREATE VIEW [dbo].[vwDW_WeekEnding]
AS 
/***********************************************************************************************
Object Name:	[vwDW_WeekEnding]

Author			Date			Comment

Gary Murrish	11/3/2010		ADDED CurrentFP and PreviousFP for the reports which run month

Purpose:		View used for to determine the date information for 'constant' words based
				upon the current date.
**********************************************************************************************/

	Select 'Previous' as Week, d.fiscal_year,d.fiscal_quarter, d.fiscal_week, d.fiscal_period, d.week_of_period,d.actual_date 
	FROM dw.dbo.date_dim d WITH (NOLOCK) JOIN 
(select fiscal_year, fiscal_week --fiscal_period,fiscal_quarter, week_of_period
					  from dw.dbo.date_dim where actual_date = 
					  dateadd(wk,-1,cast(convert(varchar(11),getdate(),101) as datetime))) PreviousWeekEnding
			ON PreviousWeekEnding.fiscal_year = d.fiscal_year
			and PreviousWeekEnding.fiscal_week = d.fiscal_week
			and d.day_of_week = 7	
UNION

	Select 'TwoWeeksAgo' as Week, d.fiscal_year,d.fiscal_quarter, d.fiscal_week, d.fiscal_period, d.week_of_period,d.actual_date 
	FROM dw.dbo.date_dim d WITH (NOLOCK) JOIN 
(select fiscal_year, fiscal_week --fiscal_period,fiscal_quarter, week_of_period
					  from dw.dbo.date_dim where actual_date = 
					  dateadd(wk,-2,cast(convert(varchar(11),getdate(),101) as datetime))) PreviousWeekEnding
			ON PreviousWeekEnding.fiscal_year = d.fiscal_year
			and PreviousWeekEnding.fiscal_week = d.fiscal_week
			and d.day_of_week = 7	
UNION

	Select 'Current' as Week,
d.fiscal_year,d.fiscal_quarter, d.fiscal_week, d.fiscal_period, d.week_of_period,d.actual_date 
	FROM dw.dbo.date_dim d WITH (NOLOCK) JOIN 
(select fiscal_year, fiscal_week --fiscal_period,fiscal_quarter, week_of_period
					  from dw.dbo.date_dim where actual_date = 
					  cast(convert(varchar(11),getdate(),101) as datetime)) CurrentWeekEnding
			ON CurrentWeekEnding.fiscal_year = d.fiscal_year
			and CurrentWeekEnding.fiscal_week = d.fiscal_week
			and d.day_of_week = 7	
UNION

	Select 'Next' as Week,
d.fiscal_year,d.fiscal_quarter, d.fiscal_week, d.fiscal_period, d.week_of_period,d.actual_date 
	FROM dw.dbo.date_dim d WITH (NOLOCK) JOIN 
(select fiscal_year, fiscal_week --fiscal_period,fiscal_quarter, week_of_period
					  from dw.dbo.date_dim where actual_date = 
					  dateadd(wk,1,cast(convert(varchar(11),getdate(),101) as datetime))) NextWeekEnding
			ON NextWeekEnding.fiscal_year = d.fiscal_year
			and NextWeekEnding.fiscal_week = d.fiscal_week
			and d.day_of_week = 7	
UNION

	Select 'CurrentFP' as Week,
d.fiscal_year,d.fiscal_quarter, d.fiscal_week, d.fiscal_period, d.week_of_period,d.actual_date 
	FROM dw.dbo.date_dim d WITH (NOLOCK) JOIN 

(select fiscal_year, fiscal_period,week_of_period
					  from dw.dbo.date_dim where actual_date = 
					  cast(convert(varchar(11),getdate(),101) as datetime)) CurrentFP
			ON CurrentFP.fiscal_year = d.fiscal_year
			and CurrentFP.fiscal_period = d.fiscal_period
			and CurrentFP.week_of_period = d.week_of_period
			and d.day_of_week = 7	
			WHERE CurrentFP.week_of_period > 1
UNION

	Select TOP 1 'PreviousFP' as Week,
d.fiscal_year,d.fiscal_quarter, d.fiscal_week, d.fiscal_period, d.week_of_period,d.actual_date 
	-- Get the record for the last day of the Prior Fiscal Period
	FROM dw.dbo.date_dim d
	WHERE (fiscal_year * 100 + fiscal_period) < 
		(-- Get the current month
		SELECT (fiscal_year * 100 + fiscal_period) AS GMPeriod
		FROM dw.dbo.date_dim TDAY WITH (NOLOCK)
		where TDAY.actual_date = 
			cast(convert(varchar(11),getdate(),101) as DATETIME)
			--'2010-04-15'
		)
	ORDER BY (fiscal_year * 100 + fiscal_period) DESC, d.date_key desc
```

