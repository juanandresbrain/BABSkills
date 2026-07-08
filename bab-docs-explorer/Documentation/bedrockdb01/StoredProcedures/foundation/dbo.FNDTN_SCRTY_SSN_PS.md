# dbo.FNDTN_SCRTY_SSN_PS

**Database:** foundation  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.FNDTN_SCRTY_SSN_PS"]
    FNDTN_SCRTY_SSN(["FNDTN_SCRTY_SSN"]) --> SP
    FNDTN_SCRTY_SSN_LOG(["FNDTN_SCRTY_SSN_LOG"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| FNDTN_SCRTY_SSN |
| FNDTN_SCRTY_SSN_LOG |

## Stored Procedure Code

```sql
create proc dbo.FNDTN_SCRTY_SSN_PS 
@SessionId varchar(255),
@status int
AS 
DECLARE @HistoryPollID int

	INSERT INTO FNDTN_SCRTY_SSN_LOG (SSN_ID, USER_ID, STRT_TIME, END_TIME, MCHN_NAME, PID, STS)
	     SELECT Convert(uniqueidentifier, @SessionId), USER_ID, STRT_TIME, getdate (), MCHN_NAME, PID, @status
	       FROM FNDTN_SCRTY_SSN
	      WHERE SSN_ID = @SessionId

	DELETE FNDTN_SCRTY_SSN
	 WHERE SSN_ID = Convert(uniqueidentifier, @SessionId)
```

