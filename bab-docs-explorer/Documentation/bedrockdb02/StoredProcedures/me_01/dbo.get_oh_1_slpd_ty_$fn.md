# dbo.get_oh_1_slpd_ty_$fn

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.get_oh_1_slpd_ty_$fn"]
    dbo_get_sl_pdoh__fn(["dbo.get_sl_pdoh_$fn"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.get_sl_pdoh_$fn |

## Stored Procedure Code

```sql
create proc dbo.get_oh_1_slpd_ty_$fn  @dummy int, @dummy2 int
AS
declare @hist_period_id int
Declare @pds int
Declare @yrs int

set @pds = 1
set @yrs = 0

EXEC @hist_period_id = get_sl_pdoh_$fn @pds, @yrs

return isnull( @hist_period_id, 0);
```

