# dbo.view_calendar_merch_pd_rel

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_calendar_merch_pd_rel"]
    dbo_calendar_merch_period(["dbo.calendar_merch_period"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar_merch_period |

## View Code

```sql
create view dbo.view_calendar_merch_pd_rel



as
select (o.merch_year * 100 + o.merch_period)merch_year_pd,
(select count (*) from calendar_merch_period d
                 where (d.merch_year * 100 + d.merch_period ) <= (o.merch_year * 100 + o.merch_period ) ) relative_period
from calendar_merch_period o
```

