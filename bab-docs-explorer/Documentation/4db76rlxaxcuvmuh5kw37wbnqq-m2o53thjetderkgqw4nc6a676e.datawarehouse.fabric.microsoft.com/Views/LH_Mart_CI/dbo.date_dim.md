# dbo.date_dim

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.date_dim"]
    dbo_date_dim(["dbo.date_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.date_dim |

## View Code

```sql
;

CREATE VIEW dbo.date_dim AS SELECT date_key, actual_date, fiscal_year, season COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS season, 
fiscal_quarter, fiscal_period, fiscal_week, month, year, month_name COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS month_name, day_of_month, 
day_of_year, day_name COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS day_name, weekend_y_n COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS weekend_y_n, 
day_of_week, week_of_period, week_of_quarter, period_of_quarter, day_id, holiday_period_code COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS holiday_period_code,
week_id, period_id, quarter_id, org_fiscal_quarter, org_fiscal_period, org_fiscal_week, org_week_of_period, org_week_of_quarter,
org_period_of_quarter FROM LH_Mart.dbo.date_dim;
```

