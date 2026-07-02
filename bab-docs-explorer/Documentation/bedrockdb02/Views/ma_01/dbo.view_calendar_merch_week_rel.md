# dbo.view_calendar_merch_week_rel

**Database:** ma_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_calendar_merch_week_rel"]
    dbo_calendar_merch_week(["dbo.calendar_merch_week"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar_merch_week |

## View Code

```sql
create view dbo.view_calendar_merch_week_rel



as
select o.merch_year, o.merch_week, merch_period,
(select count (*) from calendar_merch_week d
                 where (d.merch_year * 100 + d.merch_week ) <= (o.merch_year * 100 + o.merch_week ) ) relative_week
from calendar_merch_week o
```

