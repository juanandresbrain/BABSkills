# Job: MERCH ADMIN - Check On PL0004000 - Issue Documents Job

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** In Jan 2017 we ran into a scenario where the Issue Documents job on PipeApp01 was hung on a step for a couple of days. This prevented promotion DCNs from flowing to stores. Which ultimately caused pricing issues at POS. This alert is to notify MerchAdmin if the Pipeline Job has not completed in the last 2 hours.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCH ADMIN - Check On PL0004000 - Issue Documents Job"]
    JOB --> UNO_1["Step 1: UNO [TSQL]"]`n```

## Steps

### Step 1: UNO
**Subsystem:** TSQL  

```sql
IF (Object_ID('tempdb..#TC_Pipe1') IS NOT NULL) DROP TABLE #TC_Pipe1
SELECT instance_id, msdb.dbo.agent_datetime(run_date,run_time) as Last_Run_Date_Time
into #TC_Pipe1
from pipeapp01.msdb.dbo.SysJobHistory
where job_id = '1A3C3503-4843-417E-8299-AB0301102F88' -- Issue Documents SQL Agent Job
and step_id = '0' -- Step 0 Indicates Successful Completion of Agent Job 


IF (Object_ID('tempdb..#TC_Pipe2') IS NOT NULL) DROP TABLE #TC_Pipe2
select  DATEDIFF(hh, Max(Last_Run_Date_Time), getdate()) as Hours_Since -- Last 
into #TC_Pipe2
from #TC_Pipe1

-- select * from #TC_Pipe2

if 
(select count (*) from #TC_Pipe2 where Hours_Since > 2 ) > 0 

Begin 

EXEC bedrockdb02.msdb.dbo.sp_send_dbmail
	--@recipients = 'merchadmin@buildabear.com',
	--@recipients = 'TimC@buildabear.com',
	@recipients = 'EntSysSupport@buildabear.com',
	@subject = 'The Pipeline Job PL0004000 - Issue Documents - Has Not Completed in Over 2 Hours!',
	@importance= 'HIGH',
@body = 
'This job is responsible for generating DCNs for stores and completing price change documents.

The job is scheduled to run everyday and every hour from 8am to 8 p.m.

This long duration may indicate the job is hung.

Please investigate this immediately!',

	@profile_name = 'MerchAdmin'
	
End
```


