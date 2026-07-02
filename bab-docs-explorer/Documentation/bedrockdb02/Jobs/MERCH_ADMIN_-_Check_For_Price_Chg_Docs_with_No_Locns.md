# Job: MERCH ADMIN - Check For Price Chg Docs with No Locns

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Checks for PCDs without locations associated with them. If there are no locations, this will cause DCN generation issues.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCH ADMIN - Check For Price Chg Docs with No Locns"]
    JOB --> Uno_1["Step 1: Uno [TSQL]"]`n```

## Steps

### Step 1: Uno
**Subsystem:** TSQL  

```sql
if (object_id('tempdb.. ##PCD1') is not null) drop table ##PCD1

select *
into ##PCD1
from price_change
where price_change_id in 
(
select price_change_id from price_change
except
select price_change_id from price_change_location
)
and approval_status = '2'
and state_no <> '8'
and price_change_id <> '1222' -- Omitting this as it's really old and none of the styles are active.
order by create_date desc

if (select count (*) from ##PCD1) > 0 

Begin

EXEC bedrockdb02.msdb.dbo.sp_send_dbmail
	@recipients = 'MerchAdmin@buildabear.com',
	@subject = 'Possible Price Change Docs WITHOUT Locations!',
	@body = 'There may be be Price Change Documents WITHOUT locations associated with them, which will cause DCN generation issues. Please investigate.

',
	@query = 'select price_change_no, effective_from_date from ##PCD1 order by effective_from_date desc',
	@profile_name = 'MerchAdmin'
end
	


MERCH ADMIN - Check On PipeApp01 SQL Server Agent	Yes	This Job was born out of an issue on approx 8/23/2016 where the SQL Agent Service did not start properly after a reboot on PipeApp01 
 If the SQL Server Agent is not running, the job will attempt to start the service and will e-mail MerchAdmin that the service was stopped. 
	1	uno	TSQL	
-- This Job was born out of an issue on approx 8/23/2016 where the SQL Agent Service did not start properly after a reboot on PipeApp01 
-- If the SQL Server Agent is not running, the job will attempt to start the service and will e-mail MerchAdmin that the service was stopped. 

set nocount on 

IF (Object_ID('tempdb..#ServiceStatus') IS NOT null) DROP TABLE #ServiceStatus
Create TABLE #ServiceStatus 
(Current_Service_State nvarchar(50))

INSERT INTO #ServiceStatus 
EXEC pipeapp01.master.dbo.xp_servicecontrol N'querystate',N'SQLServerAGENT'



if (select count(*) from #ServiceStatus where Current_Service_State = 'Stopped.') = 1 

Begin 

	EXEC pipeapp01.master.dbo.xp_servicecontrol N'start',N'SQLServerAGENT'

	EXEC bedrockdb02.msdb.dbo.sp_send_dbmail
	@recipients = 'MerchAdmin@buildabear.com',
	@subject = 'SQL Server Agent service Was Stopped on PipeApp01',
	@body = 'The SQL Server Agent service was in a stopped state on PipeApp01.
The job that generates this e-mail should have started the service.
Please ensure the service is now running.
This alert was brough to you by the following job:
MERCH ADMIN - Check On PipeApp01 SQL Server Agent on bedrockdb02. ',
	@profile_name = 'MerchAdmin'

	
End
```


