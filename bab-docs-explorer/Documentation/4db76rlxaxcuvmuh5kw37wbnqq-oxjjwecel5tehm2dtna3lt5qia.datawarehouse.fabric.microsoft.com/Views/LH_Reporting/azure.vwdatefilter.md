# azure.vwdatefilter

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["azure.vwdatefilter"]
    dbo_date_dim(["dbo.date_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.date_dim |

## View Code

```sql
CREATE VIEW [azure].[vwdatefilter]
AS
SELECT date_key
	,actual_date
	,fiscal_year
	,season
	,fiscal_quarter
	,fiscal_period
	,fiscal_week
	,month
	,year
	,month_name
	,day_of_month
	,day_of_year
	,day_name
	,weekend_y_n
	,day_of_week
	,week_of_period
	,week_of_quarter
	,period_of_quarter
	,day_id
	,holiday_period_code
	,week_id
	,period_id
	,quarter_id
	,org_fiscal_quarter
	,org_fiscal_period
	,org_fiscal_week
	,org_week_of_period
	,org_week_of_quarter
	,org_period_of_quarter
FROM LH_Mart.dbo.date_dim
WHERE fiscal_year BETWEEN (
				SELECT fiscal_year - 2
				FROM LH_Mart.dbo.date_dim
				WHERE actual_date >= GetDate() - 1
					AND actual_date < GetDate()
				)
		AND (
				SELECT fiscal_year
				FROM LH_Mart.dbo.date_dim
				WHERE actual_date >= GetDate() - 1
					AND actual_date < GetDate()
				)
```

