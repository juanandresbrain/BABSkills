# dbo.vwDW_WeekEndingWIP

**Database:** reportingservices_subscription  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_WeekEndingWIP"]
    dbo_date_dim(["dbo.date_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.date_dim |

## View Code

```sql
CREATE VIEW [dbo].[vwDW_WeekEndingWIP]
AS 

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

	Select 'PreviousFP' as Week,
d.fiscal_year,d.fiscal_quarter, d.fiscal_week, d.fiscal_period, d.week_of_period,d.actual_date 
	FROM dw.dbo.date_dim d WITH (NOLOCK) JOIN 

(select fiscal_year, fiscal_period,week_of_period
					  from dw.dbo.date_dim where actual_date = 
					  cast(convert(varchar(11),getdate(),101) as datetime)) CurrentFP
			ON CurrentFP.fiscal_year = d.fiscal_year
			and CurrentFP.fiscal_period = d.fiscal_period
			and CurrentFP.week_of_period = d.week_of_period
			and d.day_of_week = 7	
			WHERE CurrentFP.week_of_period = 1
/*
	SELECT 'PreviousFP' as Week,
d.fiscal_year,d.fiscal_quarter, d.fiscal_week, d.fiscal_period, d.week_of_period,d.actual_date 
	FROM dw.dbo.date_dim d WITH (NOLOCK) JOIN 
(Select --'PreviousFP' as Week,
d.fiscal_year,d.fiscal_quarter, d.fiscal_week, d.fiscal_period, d.week_of_period  --,d.actual_date 
	FROM dw.dbo.date_dim d WITH (NOLOCK) JOIN 
(select --fiscal_year, fiscal_period,
week_of_period,actual_date
					  from dw.dbo.date_dim where actual_date = 
					  cast(convert(varchar(11),getdate(),101) as datetime)) CurrentFP
			ON d.actual_date = dateadd(wk,-1,CurrentFP.actual_date)
			WHERE CurrentFP.week_of_period = 1) PreviousFP
			ON PreviousFP.fiscal_year = d.fiscal_year
			and PreviousFP.fiscal_period = d.fiscal_period
			and PreviousFP.week_of_period = d.week_of_period
			where d.day_of_week = 7	
*/
UNION

	Select 'PreviousFP' as Week,
d.fiscal_year,d.fiscal_quarter, d.fiscal_week, d.fiscal_period, d.week_of_period,d.actual_date 
	FROM dw.dbo.date_dim d WITH (NOLOCK) JOIN 
(Select --'PreviousFP' as Week,
d.fiscal_year,d.fiscal_quarter, d.fiscal_week, d.fiscal_period, d.week_of_period  --,d.actual_date 
	FROM dw.dbo.date_dim d WITH (NOLOCK) JOIN 
(select --fiscal_year, fiscal_period,
week_of_period,actual_date
					  from dw.dbo.date_dim where week_of_period = 1
					  and actual_date = dateadd(wk,-3,cast(convert(varchar(11),getdate(),101) as datetime 
					  ))) CurrentFP
			ON d.actual_date = dateadd(wk,-1,CurrentFP.actual_date)
			WHERE CurrentFP.week_of_period = 1) PreviousFP
			ON PreviousFP.fiscal_year = d.fiscal_year
			and PreviousFP.fiscal_period = d.fiscal_period
			and PreviousFP.week_of_period = d.week_of_period
			where d.day_of_week = 7	

--  select * from vwDW_WeekEnding


/*

UNION
	Select 'CurrentFP' as Week,
d.fiscal_year,d.fiscal_quarter, d.fiscal_week, d.fiscal_period, d.week_of_period,d.actual_date 
	FROM dw.dbo.date_dim d WITH (NOLOCK) JOIN 

(select fiscal_year, fiscal_period,week_of_period
					  from dw.dbo.date_dim where actual_date = 
					  dateadd(wk,-3,cast(convert(varchar(11),getdate(),101) as datetime))) CurrentFP
			ON CurrentFP.fiscal_year = d.fiscal_year
			and CurrentFP.fiscal_period = d.fiscal_period
			and CurrentFP.week_of_period = d.week_of_period
			and d.day_of_week = 7	
			WHERE CurrentFP.week_of_period > 1
*/
```

