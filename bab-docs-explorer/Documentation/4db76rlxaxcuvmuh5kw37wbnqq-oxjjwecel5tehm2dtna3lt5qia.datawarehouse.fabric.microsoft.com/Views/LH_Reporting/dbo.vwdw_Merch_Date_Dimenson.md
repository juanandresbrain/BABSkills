# dbo.vwdw_Merch_Date_Dimenson

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwdw_Merch_Date_Dimenson"]
    dbo_date_dim(["dbo.date_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.date_dim |

## View Code

```sql
-- CREATE view dbo.vwdw_Merch_Date_Dimenson
-- as
-- SELECT *,
-- FROM LH_Mart.date_dim
-- WHERE date_key > 0


CREATE   VIEW dbo.vwdw_Merch_Date_Dimenson
AS

SELECT
    *,

    -- Fiscal Year Quarter
    CONCAT(
        '''',
        RIGHT(CAST(fiscal_year AS VARCHAR), 2),
        ' Q',
        CAST(fiscal_quarter AS VARCHAR)
    ) AS fiscalyearquarter,

    -- Fiscal Month
    CAST(fiscal_year AS VARCHAR)
        + ' '
        + RIGHT('0' + CAST(fiscal_period AS VARCHAR), 2)
        AS fiscalmonth,

    -- Fiscal Week
    CAST(fiscal_year AS VARCHAR)
        + ' '
        + RIGHT('0' + CAST(fiscal_week AS VARCHAR), 2)
        AS fiscalweek,

    -- Calendar Year Month
    CAST(year AS VARCHAR)
        + ' '
        + RIGHT('0' + CAST(month AS VARCHAR), 2)
        AS calenderyearmonth,

    -- First Month Name
    ''''
        + RIGHT(CAST(fiscal_year AS VARCHAR), 2)
        + ' '
        + CASE
            WHEN fiscal_period = 1 THEN 'Feb'
            WHEN fiscal_period = 2 THEN 'Mar'
            WHEN fiscal_period = 3 THEN 'Apr'
            WHEN fiscal_period = 4 THEN 'May'
            WHEN fiscal_period = 5 THEN 'Jun'
            WHEN fiscal_period = 6 THEN 'Jul'
            WHEN fiscal_period = 7 THEN 'Aug'
            WHEN fiscal_period = 8 THEN 'Sep'
            WHEN fiscal_period = 9 THEN 'Oct'
            WHEN fiscal_period = 10 THEN 'Nov'
            WHEN fiscal_period = 11 THEN 'Dec'
            WHEN fiscal_period = 12 THEN 'Jan'
            ELSE 'Other'
        END
        AS firstmonthname,

    -- Simple Date
    CONVERT(VARCHAR, actual_date, 101)
        AS simpledate,

    -- Fiscal Week Display
    ''''
        + RIGHT(CAST(fiscal_year AS VARCHAR), 2)
        + ' FW'
        + RIGHT('0' + CAST(fiscal_week AS VARCHAR), 2)
        AS fiscalweekdisplay,

    -- Calendar Month Name
    CAST(year AS VARCHAR)
        + ' '
        + CASE
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
        END
        AS calendermonthname,

    -- Season Key
    CAST(year AS VARCHAR)
        + CASE
            WHEN LOWER(season) = 'spring' THEN '1'
            ELSE '2'
          END
        AS seasonkey,

    -- Season Display
    season
        + ' '''
        + RIGHT(CAST(year AS VARCHAR), 2)
        AS seasondisplay,

    -- Time Calcs
    'Current Time'
        AS timecalcs,

    -- Fiscal Month Of Year
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
    END
    AS fiscalmonthofyear,

    -- Fiscal Quarter Of Year
    'Q' + CAST(fiscal_quarter AS VARCHAR)
        AS fiscalquarterofyear,

    -- Fiscal Week Of Year
    ' FW'
        + RIGHT('0' + CAST(fiscal_week AS VARCHAR), 2)
        AS fiscalweekofyear,

    -- Weekday Type
    CASE
        WHEN weekend_y_n = 'y' THEN 'Weekend'
        ELSE 'Weekday'
    END
    AS weekdaytype,

    -- Marketing Quarter Of Year
    CASE
        WHEN fiscal_period IN (1,2,3,4) THEN 'MQ1'
        WHEN fiscal_period IN (5,6) THEN 'MQ2'
```

