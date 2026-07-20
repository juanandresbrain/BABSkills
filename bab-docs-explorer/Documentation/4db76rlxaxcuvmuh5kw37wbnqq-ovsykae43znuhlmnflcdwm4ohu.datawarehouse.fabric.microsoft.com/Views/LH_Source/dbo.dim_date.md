# dbo.dim_date

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.dim_date"]
    VIEW --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## View Code

```sql
CREATE   VIEW dbo.dim_date AS WITH d10 AS (     SELECT n FROM (VALUES(0),(1),(2),(3),(4),(5),(6),(7),(8),(9)) AS t(n) ), tally AS (     SELECT TOP (DATEDIFF(day, CAST('2018-01-01' AS date), CAST('2030-12-31' AS date)) + 1)            ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) - 1 AS day_offset       FROM d10 a CROSS JOIN d10 b CROSS JOIN d10 c CROSS JOIN d10 d ), calendar AS (     SELECT DATEADD(day, day_offset, CAST('2018-01-01' AS date)) AS calendar_date       FROM tally ) SELECT     calendar_date,     YEAR(calendar_date)                                                         AS year_no,     DATEPART(quarter, calendar_date)                                            AS quarter_no,     MONTH(calendar_date)                                                        AS month_no,     DATENAME(month, calendar_date)                                              AS month_name,     DAY(calendar_date)                                                          AS day_of_month,     /* ISO 8601 week-day: Monday=1..Sunday=7 */     ((DATEPART(weekday, calendar_date) + @@DATEFIRST + 5) % 7) + 1              AS day_of_week_iso,     /* US convention: Sunday=1..Saturday=7 (matches AuditWorks dbo.get_day_of_week) */     ((DATEPART(weekday, calendar_date) + @@DATEFIRST - 1) % 7) + 1              AS day_of_week_us,     DATENAME(weekday, calendar_date)                                            AS day_of_week_name,     DATEPART(iso_week, calendar_date)                                           AS week_of_year_iso,     CASE WHEN DATENAME(weekday, calendar_date) IN ('Saturday','Sunday') THEN 1          ELSE 0     END                                                                         AS is_weekend,     YEAR(calendar_date)                                                         AS fiscal_year,  /* TODO: NRF 4-5-4 if BBW uses retail calendar */     YEAR(calendar_date) * 100 + MONTH(calendar_date)                            AS yyyymm,     YEAR(calendar_date) * 10000 + MONTH(calendar_date) * 100 + DAY(calendar_date) AS yyyymmdd   FROM calendar;
```

