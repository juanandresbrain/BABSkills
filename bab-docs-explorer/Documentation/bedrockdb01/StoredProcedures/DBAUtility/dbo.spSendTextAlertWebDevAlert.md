# dbo.spSendTextAlertWebDevAlert

**Database:** DBAUtility  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spSendTextAlertWebDevAlert"]
    dbo_sp_send_dbmail(["dbo.sp_send_dbmail"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sp_send_dbmail |

## Stored Procedure Code

```sql
CREATE procedure [dbo].[spSendTextAlertWebDevAlert]
(
	@TextSubject varchar(35),
	@BodyOfText varchar(110)
)
as

--declare @importance varchar(100)
--set @importance = 'Low'	--'Low','Normal','High', defaults to 'Normal'

declare @subjectToSend varchar(50)
set @subjectToSend = 'Web Developer ALERT: ' + @TextSubject

EXEC msdb.dbo.sp_send_dbmail @recipients='3144066121@txt.att.net;3146206144@messaging.sprintpcs.com;3144063104@txt.att.net;3142399869@txt.att.net'
--EXEC msdb.dbo.sp_send_dbmail @recipients='3144400230@txt.att.net'
    ,@subject = @subjectToSend
    ,@body = @BodyOfText
	,@body_format = 'TEXT' --'HTML' or 'TEXT', defaults to 'TEXT'
	,@from_address='WebDevAlert@buildabear.com'
	,@importance='High';
```

