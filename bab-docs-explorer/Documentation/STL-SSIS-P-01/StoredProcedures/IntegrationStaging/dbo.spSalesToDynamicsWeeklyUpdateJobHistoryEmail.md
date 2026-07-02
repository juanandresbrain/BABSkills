# dbo.spSalesToDynamicsWeeklyUpdateJobHistoryEmail

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spSalesToDynamicsWeeklyUpdateJobHistoryEmail"]
    dbo_agent_datetime(["dbo.agent_datetime"]) --> SP
    dbo_date_dim(["dbo.date_dim"]) --> SP
    dbo_jh(["dbo.jh"]) --> SP
    dbo_SalesToDynamicsWeeklyUpdateSQLJobHistory(["dbo.SalesToDynamicsWeeklyUpdateSQLJobHistory"]) --> SP
    dbo_sp_send_dbmail(["dbo.sp_send_dbmail"]) --> SP
    dbo_sysjobhistory(["dbo.sysjobhistory"]) --> SP
    dbo_sysjobs(["dbo.sysjobs"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.agent_datetime |
| dbo.date_dim |
| dbo.jh |
| dbo.SalesToDynamicsWeeklyUpdateSQLJobHistory |
| dbo.sp_send_dbmail |
| dbo.sysjobhistory |
| dbo.sysjobs |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spSalesToDynamicsWeeklyUpdateJobHistoryEmail]

as


set nocount on

declare @CheckDateStart date
select @CheckDateStart=
	case 
		when datename(weekday, getdate())='Saturday'
			then cast(getdate() as date)
		else max(cast(actual_date as date)) 
	end
from papamart.dw.dbo.date_dim 
where cast(actual_date as date) < cast(getdate() as date)
and datename(weekday,actual_date)='Saturday'


if (select count(*) from SalesToDynamicsWeeklyUpdateSQLJobHistory where datediff(dd, InsertDate, getdate()) <> 0) > 0
	begin

		delete from SalesToDynamicsWeeklyUpdateSQLJobHistory 
		where datediff(dd, InsertDate, getdate()) <> 0
	end


IF (Object_ID('tempdb..#SalesToDynamicsWeeklyUpdateSQLJobHistory') IS NOT NULL) DROP TABLE #SalesToDynamicsWeeklyUpdateSQLJobHistory

;
with 
ServerJobs as
	(
		
		select 'STL-SSIS-P-01' as servername, name, job_id 
		from [STL-SSIS-P-01].msdb.dbo.sysjobs
	
	),
JOBS as
	(
		select 
			servername,
			name, 
			job_id,
			case 
				when name in 
					(
						'SalesAuditToDynamics - Weekly Updates'
						
						
					) then 'Sales Audit To Dynamics - Weekly Updates' 
				end as 'DataSet'
				
		from Serverjobs
	)

select 
	j.servername as server,
	j.name as 'JobName',
	cast(msdb.dbo.agent_datetime(run_date, run_time) as datetime)  as 'RealRunDateTime',
	convert(varchar, msdb.dbo.agent_datetime(run_date, run_time), 100)  as 'RunDateTime',
	((run_duration/10000*3600 + (run_duration/100)%100*60 + run_duration%100 + 31 ) / 60) 
         as 'RunDurationMinutes',
	case h.run_status
		when 0 then 'Failed'
		when 1 then 'Succeeded'
		when 2 then 'Retry'
		when 3 then 'Canceled'
		when NULL then 'No History'
	end as Run_Status,
	j.DataSet
into #SalesToDynamicsWeeklyUpdateSQLJobHistory
From JOBS j
left join [STL-SSIS-P-01].msdb.dbo.sysjobhistory h 
	on j.job_id = h.job_id 
	and h.step_id = 0 --job outcome
	and cast(msdb.dbo.agent_datetime(h.run_date, h.run_time) as date) >= @CheckDateStart
where j.servername = 'STL-SSIS-P-01'
and j.DataSet in 
	(
		'Sales Audit To Dynamics - Weekly Updates'
	)



----===================================================================

	;
	with 
	MaxDate as
		(
			select [server], JobName, max(RealRunDateTime) RealRunDateTime
			from #SalesToDynamicsWeeklyUpdateSQLJobHistory
			group by server, JobName
		)
	delete jh
	from #SalesToDynamicsWeeklyUpdateSQLJobHistory jh
	join MaxDate md 
		on jh.[server]=md.[server] 
		and jh.JobName=md.JobName 
		and jh.RealRunDateTime<>md.RealRunDateTime
	;

-----
	;
	merge into SalesToDynamicsWeeklyUpdateSQLJobHistory as target 
	using #SalesToDynamicsWeeklyUpdateSQLJobHistory as source
		on 
			target.[Server]=source.[server]
			and 
			target.JobName=source.JobName
			and 
			target.DataSet=source.DataSet
	when matched 
		and
			isnull(target.Run_Status,'x') <> 'Succeeded'
			--and 	
			--(
			--	isnull(target.RunDateTime,convert(varchar, getdate(), 100))<>isnull(source.RunDateTime,convert(varchar, getdate(), 100))
			--	OR
			--	isnull(target.Run_Status,'x')<>isnull(source.Run_Status,'x')
			--)
	then update
		set 
			target.RunDateTime=source.RunDateTime,
			target.RunDurationMinutes=source.RunDurationMinutes,
			target.Run_Status=source.Run_Status,
			target.UpdateDate=getdate()
	when not matched by target
	then insert
		(
			[Server],
			JobName,
			DataSet,
			RunDateTime,
			RunDurationMinutes,
			Run_Status,
			InsertDate
		)
		values
		(
			source.[Server],
			source.JobName,
			source.DataSet,
			source.RunDateTime,
			source.RunDurationMinutes,
			source.Run_Status,
			getdate()
		)
	;
----

;
	with Succeeded as
		(
			select JobName, cast(RunDateTime as datetime) as RunDateTime 
			from SalesToDynamicsWeeklyUpdateSQLJobHistory
			where run_status = 'Succeeded'
		)
	delete t
	from SalesToDynamicsWeeklyUpdateSQLJobHistory t
	join Succeeded s on t.JobName = s.JobName 
	where t.run_status <> 'Succeeded' 
	and cast(t.RunDateTime as datetime) < s.RunDateTime 
;
--=====================================================================================================================================
--=====================================================================================================================================

if (select count(*) from SalesToDynamicsWeeklyUpdateSQLJobHistory) > 0
BEGIN
	
			Declare @Recip varchar(100),
					@text nvarchar(max),
					@SalesExtract varchar(4),
					@FileExport varchar(4),
					@SequenceCheck varchar(4),
					@Subj varchar(100)
	
		
		
 
			if (
					select count(*) from SalesToDynamicsWeeklyUpdateSQLJobHistory j
						where j.DataSet = 'Sales Audit To Dynamics - Weekly Updates'
							and 
							(
								(
									(j.Run_Status <> 'Succeeded' or j.Run_Status is NULL) 
										and
									j.JobName not in (select jj.JobName from SalesToDynamicsWeeklyUpdateSQLJobHistory jj where jj.DataSet = 'Sales Audit To Dynamics - Weekly Updates' and jj.Run_Status = 'Succeeded' and jj.RunDateTime > j.RunDateTime ) --in case we ran the job again after it failed
								) 

							)
				) > 0 
		
				set @SalesExtract = 'Fail' else set @SalesExtract = 'Pass'
		
			set @text = '<H1><font face =arial> Sales to Dynamics Weekly Updates - Critical Job Status </font> </H1>' +
				'<font face =arial size = 2> This job must run successfully each Saturday in order to ensure that all sales are pushed to Dynamics.
				<br>
				<b>Please consult with Tim Callahan for next steps</b>' +
				'<br> 
				</font><br><br>' +
				'<br>' + 
				'<font face =arial size = 2> <b> SUMMARY </b> </font>' +
				'<br>' +
				'<table border="1">' +
				'<font face =arial size = 2>' + 
				'<tr><th>DATASET</th><th>PASS / FAIL</th></tr>' +
				CAST ( ( SELECT distinct
								td = jh.Dataset,'',
								td = case jh.DataSet 
									when 'Sales Audit To Dynamics - Weekly Updates' 
										then @SalesExtract
								end, ''
							from SalesToDynamicsWeeklyUpdateSQLJobHistory jh
							--left join #PassFail pf on jh.DataSet = pf.DataSet and jh.JobName = pf.JobName
							group by jh.DataSet--, pf.condition
							order by jh.Dataset
						  FOR XML PATH('tr'), TYPE 
				) AS NVARCHAR(MAX) ) +
				'</font></table>
				<br>'
				+
				'<font face =arial size = 2> <b> Sales Audit To Dynamics - Weekly Updates </b> </font>' +
				'<br>' +
				'<table border="1">' +
				'<font face =arial size = 2>' + 
				'<tr><th>SERVER</th><th>JOB NAME</th><th>DATETIME</th><th>DURATION</th><th>STATUS</th></tr>' +
				CAST ( ( SELECT td = server,'',
								td = jobName, '',
								td = isnull(RunDateTime, 0), '',
								td = isnull(RunDurationMinutes, ''), '',
								td = Run_Status, ''
						  from SalesToDynamicsWeeklyUpdateSQLJobHistory
						  where DataSet = 'Sales Audit To Dynamics - Weekly Updates' 
						  order by RunDateTime
						  FOR XML PATH('tr'), TYPE 
				) AS NVARCHAR(MAX) ) +
				'</font></table>
				<br>' +
				'<br>
				<font face =arial size = 2>This report was generated by stl-ssis-p-01.IntegrationStaging.dbo.spSalesToDynamicsWeeklyUpdateJobHistoryEmail, which was executed from STL-SSIS-P-01 SQL Agent: SalesToDynamics-CRITICAL_JOB_CHECK.</font>
				<br>
				<br>'

			if 
					@SalesExtract = 'Fail'
					or
					@FileExport = 'Fail' 
					
				select 
					@subj = 'Sales Audit to Dynamics Weekly Updates - Critical Job Status: Fail',
					@Recip = 'BIAdminTextAlert@buildabear.com'
			else

				select 
					@subj = 'Sales Audit to Dynamics Weekly Updates - Job Status: Pass',
					@Recip = 'biadmin@buildabear.com'
		
	
			exec msdb.dbo.sp_send_dbmail
				@profile_name = 'biadmin',
				@recipients = @Recip, 
				@body = @text,
				@subject = @subj,
				@body_format = 'HTML'


		
END


dbo,spSQLAGentStopLongRunningJob,CREATE proc [dbo].[spSQLAGentStopLongRunningJob]
	@Job varchar(500),
	@Runtime int,
	@Rec varchar(1000)

as


--currently running sql agent jobs
IF (Object_ID('tempdb..#LongRunningJob') IS NOT null) DROP TABLE #LongRunningJob
SELECT
    ja.job_id,
    j.name AS job_name,
    ja.start_execution_date,      
    ISNULL(last_executed_step_id,0)+1 AS current_executed_step_id,
    Js.step_name,
	datediff(mi, ja.start_execution_date, getdate()) RunningMinutes
into #LongRunningJob
FROM msdb.dbo.sysjobactivity ja 
LEFT JOIN msdb.dbo.sysjobhistory jh ON ja.job_history_id = jh.instance_id
JOIN msdb.dbo.sysjobs j ON ja.job_id = j.job_id
JOIN msdb.dbo.sysjobsteps js
    ON ja.job_id = js.job_id
    AND ISNULL(ja.last_executed_step_id,0)+1 = js.step_id
WHERE
  ja.session_id = (
    SELECT TOP 1 session_id FROM msdb.dbo.syssessions ORDER BY agent_start_date DESC
  )
AND start_execution_date is not null
AND stop_execution_date is null
and j.name = @Job --'CRM_SalesForceDataExtensionExport'
and datediff(mi, ja.start_execution_date, getdate())>= @Runtime --30


if (select count(*) from #LongRunningJob) > 0
begin
	EXEC msdb.dbo.sp_stop_job @Job

	declare
		@bod varchar(1000),  
		@sub varchar(1000) 

	select 
		@bod= 'The SQL Agent Job ' + cast(@JOB as varchar(500)) + ' was halted due to having been running for longer than ' + cast(@Runtime as varchar) + ' minutes.',
		@sub= 'SQL Long Running Job Stopped: ' + cast(@JOB as varchar(500))

	exec msdb.dbo.sp_send_dbmail
		@profile_name = 'biadmin',
		@recipients = @Rec,-- 'dant@buildabear.com',
		@body = @bod,
		@subject = @sub ,
		@body_format = 'HTML'

	if @Job= 'StoreForcePosSalesExport_Every30Minutes' and datepart(hh, getdate())<>5 
	EXEC msdb.dbo.sp_start_job @job_name='HangingSQLConnectionCheck_MasterController'

	--if (select count(*) from #LongRunningJob where job_name='StoreForcePosSalesExport_Every30Minutes' and datepart(hh, getdate()) >9 ) > 0 --
	--begin
	--	EXEC msdb.dbo.sp_start_job @job_name='StoreForcePOSSalesExport_MergeAndFileOnly'
	--end

end
```

