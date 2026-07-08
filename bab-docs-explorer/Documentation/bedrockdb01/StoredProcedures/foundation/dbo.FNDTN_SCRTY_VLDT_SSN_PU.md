# dbo.FNDTN_SCRTY_VLDT_SSN_PU

**Database:** foundation  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.FNDTN_SCRTY_VLDT_SSN_PU"]
    FNDTN_SCRTY_SSN(["FNDTN_SCRTY_SSN"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| FNDTN_SCRTY_SSN |

## Stored Procedure Code

```sql
create proc dbo.FNDTN_SCRTY_VLDT_SSN_PU 
@sessionId binary(16)
AS 
	update FNDTN_SCRTY_SSN 
	set LAST_VLDTN = getdate ()
	WHERE SSN_ID = @sessionId
```

