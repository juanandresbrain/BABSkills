# dbo.view_sl_fp_year_period

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_sl_fp_year_period"]
    dbo_calendar_date(["dbo.calendar_date"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar_date |

## View Code

```sql
create view dbo.view_sl_fp_year_period
	( curr_year_period, prev_year_period)
AS
SELECT
	(merch_year*100 + merch_period) curr_year_period,
	((merch_year*100-1) + merch_period) prev_year_period
FROM calendar_date cd
WHERE
cd.calendar_date = CONVERT(SMALLDATETIME,CONVERT(CHAR(12),GETDATE(),109))
```

