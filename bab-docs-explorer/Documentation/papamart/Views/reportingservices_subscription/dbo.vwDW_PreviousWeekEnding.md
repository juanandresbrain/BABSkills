# dbo.vwDW_PreviousWeekEnding

**Database:** reportingservices_subscription  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_PreviousWeekEnding"]
    dbo_date_dim(["dbo.date_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.date_dim |

## View Code

```sql
CREATE VIEW dbo.vwDW_PreviousWeekEnding
AS 
	Select d.fiscal_year,d.fiscal_quarter, d.fiscal_week, d.fiscal_period, d.week_of_period,d.actual_date 
	FROM dw.dbo.date_dim d WITH (NOLOCK) JOIN 
(select fiscal_year, fiscal_week --fiscal_period,fiscal_quarter, week_of_period
					  from dw.dbo.date_dim where actual_date = 
					  dateadd(wk,-1,cast(convert(varchar(11),getdate(),101) as datetime))) PreviousWeekEnding
			ON PreviousWeekEnding.fiscal_year = d.fiscal_year
			and PreviousWeekEnding.fiscal_week = d.fiscal_week
			WHERE d.day_of_week = 7
```

