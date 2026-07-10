# dbo.dt_displayoaerror_u

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.dt_displayoaerror_u"]
    dbo_dt_displayoaerror(["dbo.dt_displayoaerror"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.dt_displayoaerror |

## Stored Procedure Code

```sql
CREATE PROCEDURE dbo.dt_displayoaerror_u
    @iObject int,
    @iresult int
as
	-- This procedure should no longer be called;  dt_displayoaerror should be called instead.
	-- Calls are forwarded to dt_displayoaerror to maintain backward compatibility.
	set nocount on
	exec dbo.dt_displayoaerror
		@iObject,
		@iresult
```

