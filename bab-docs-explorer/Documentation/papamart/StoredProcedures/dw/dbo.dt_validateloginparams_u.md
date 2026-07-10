# dbo.dt_validateloginparams_u

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.dt_validateloginparams_u"]
    dbo_dt_validateloginparams(["dbo.dt_validateloginparams"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.dt_validateloginparams |

## Stored Procedure Code

```sql
create proc dbo.dt_validateloginparams_u
    @vchLoginName  nvarchar(255),
    @vchPassword   nvarchar(255)
as

	-- This procedure should no longer be called;  dt_validateloginparams should be called instead.
	-- Calls are forwarded to dt_validateloginparams to maintain backward compatibility.
	set nocount on
	exec dbo.dt_validateloginparams
		@vchLoginName,
		@vchPassword
```

