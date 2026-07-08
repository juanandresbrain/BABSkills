# dbo.FNDTN_ADD_USER_SSN_PS

**Database:** foundation  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.FNDTN_ADD_USER_SSN_PS"]
    FNDTN_SCRTY_SSN(["FNDTN_SCRTY_SSN"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| FNDTN_SCRTY_SSN |

## Stored Procedure Code

```sql
create proc dbo.FNDTN_ADD_USER_SSN_PS @sessionId varchar (255), @userId int, @pid int, @machineName varchar (30)
AS 
	insert into FNDTN_SCRTY_SSN (SSN_ID, USER_ID, APP_ID, CMPNY_ID, CRNT_MDL, CRNT_ITEM, STRT_TIME, PID, MCHN_NAME, LAST_VLDTN)
	select Convert(uniqueidentifier, @sessionId), @userId, 0, 0, null, 0, getdate (), @pid, @machineName, getdate ()
```

