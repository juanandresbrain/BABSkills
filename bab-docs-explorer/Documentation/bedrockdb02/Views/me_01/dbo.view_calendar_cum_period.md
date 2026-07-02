# dbo.view_calendar_cum_period

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_calendar_cum_period"]
    dbo_calendar_period(["dbo.calendar_period"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar_period |

## View Code

```sql
create view dbo.view_calendar_cum_period 
( period, cum_period ) 
AS 
SELECT cp.calendar_period_id period, cp1.calendar_period_id cum_period  
FROM calendar_period cp, calendar_period cp1  
WHERE cp.calendar_year_id = cp1.calendar_year_id  
AND cp.calendar_period_code >= cp1.calendar_period_code
```

