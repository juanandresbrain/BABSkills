# dbo.FNDTN_LOCK_SSN_PU

**Database:** foundation  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.FNDTN_LOCK_SSN_PU"]
    FNDTN_SCRTY_SSN(["FNDTN_SCRTY_SSN"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| FNDTN_SCRTY_SSN |

## Stored Procedure Code

```sql
create proc dbo.FNDTN_LOCK_SSN_PU @sessionId binary(16)
AS
BEGIN

   declare @rc int	

   update FNDTN_SCRTY_SSN 
      set LCKD = 1
    where SSN_ID = @sessionId

   SELECT @rc=isnull(@@rowcount,0)
   
   return @rc

END
```

