# dbo.get_curr_slpd_$fn

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.get_curr_slpd_$fn"]
    dbo_calendar_week(["dbo.calendar_week"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar_week |

## Stored Procedure Code

```sql
create proc dbo.get_curr_slpd_$fn 
 @dummy int, @dummy2 int


AS

Declare @curr_period_id  int




SELECT @curr_period_id = calendar_period_id 
FROM calendar_week
WHERE CONVERT(SMALLDATETIME,CONVERT(CHAR(12),GETDATE(),109)) BETWEEN calendar_week_start_date AND calendar_week_end_date;


return isnull( @curr_period_id, 0);
```

