# dbo.get_oh_0_slpd_ty_$fn

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.get_oh_0_slpd_ty_$fn"]
    dbo_history_period(["dbo.history_period"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.history_period |

## Stored Procedure Code

```sql
create proc dbo.get_oh_0_slpd_ty_$fn  @dummy int, @dummy2 int
AS
declare @hist_period_id int

select @hist_period_id = history_period_id
from history_period 
where  CONVERT(SMALLDATETIME,CONVERT(CHAR(12),GETDATE(),109)) 
between start_date and end_date 

return isnull( @hist_period_id, 0);
```

