# dbo.spSQLJobHistoryEmailBAK20200228

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spSQLJobHistoryEmailBAK20200228"]
    dbo_agent_datetime(["dbo.agent_datetime"]) --> SP
    dbo_sp_send_dbmail(["dbo.sp_send_dbmail"]) --> SP
    dbo_sysjobhistory(["dbo.sysjobhistory"]) --> SP
    dbo_sysjobs(["dbo.sysjobs"]) --> SP
    tmpEmlSQLJobHistory(["tmpEmlSQLJobHistory"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.agent_datetime |
| dbo.sp_send_dbmail |
| dbo.sysjobhistory |
| dbo.sysjobs |
| tmpEmlSQLJobHistory |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spSQLJobHistoryEmailBAK20200228]

as

-- =====================================================================================================
-- Name: spSQLJobHistoryEmail
--
-- Description:	Sends emails to report sql agent job status for specific set of high priority jobs
--
-- Syntax:  EXEC [dbo].[spSQLJobHistoryEmail_TB021418]
--
-- Input: N/A
--
-- Output: 
--
-- Dependencies: 
--
-- Revision History
--		Name:			Date:			Comments:
--		Dan Tweedie		07/25/2016		created proc
--		Dan Tweedie		08/12/2016		added DOMO datasets
--		Dan Tweedie		09/10/2016		Added isnull handling for left join on the Domo jobs section (commented below)
--		Dan Tweedie		09/23/2016		Added handling for Saturday afternoon rebuild of these Domo datasets:
--										DW.DiscountFact
--										DW.TransactionFact
--										DW.TransactionDetailFact
--										DW.TransactionFact Store Day Summary
--										DW.TransactionFactProduct
--										The rebuilds are starting at noon and this query will run on Saturday night at 7pm (also daily at 7am to look for the daily updates)
--		Dan Tweedie		10/06/2016		Added new CRM and NameMe datasets
--		Dan Tweedie		10/28/2016		Added text alert for failed status
--		Dan Tweedie		11/2/2016		Removed ExperianFootfall_ExportDaily_DataExtract
--		Tim Bytnar		2/14/2018		Temporarily disabling the DOMO datasets monitoring while the API issue persists
--		Dan Tweedie		2018-09-26		Completely removed references to Domo
--		Dan Tweedie		2019-03-18		Removed old ca/uk labor job, added new UltiPro labor job 
-- =====================================================================================================

set nocount on

Declare @Recip varchar(100)


IF (Object_ID('DW..tmpEmlSQLJobHistory') IS NOT NULL) DROP TABLE tmpEmlSQLJobHistory

;
with 
ServerJobs as
	(
		select 'BABWSCORE01' as servername, name, job_id 
		from babwscore01.msdb.dbo.sysjobs 
		union 
		select 'KERMODE' as servername, name, job_id 
		from kermode.msdb.dbo.sysjobs
		union 
		select 'PAPAMART' as servername, name, job_id 
		from papamart.msdb.dbo.sysjobs
		union 
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
						'HR_UTA_ETL',
						'Workbrain HOO Import'
					) then 'Labor' 
				when name in 
					(
						'ShopperTrak Export Daily',
						'ShopperTrak Traffic DailyImport'
					) then 'Traffic'
				when name in
					(
						--'EmailFactsETL',
						'Process Sales Cube - CRM Info',
						'CustomerTransactionETL',
						'ExactTargetDownloadAndProcess'
					) then 'Guest Load'
				when name in 
					(
						'AuditWorksImport_Transactions_VAT_Part1of3',
						'AuditWorksImport_Transactions_VAT_Part2of3',
						'AuditWorksImport_Transactions_VAT_Part3of3',
						'AuditWorksImport_Transactions_VAT_Part3Branch',
						'Process Sales Cube and Run Workbrain Export'
					) then 'AW Sales'
				when name in
					(
						'DWSales_DimensionImport',
						'DM/DW Sync Coupon Dim - CRITICAL'
					) then 'Dimensions'
				when name in 
					(
						'FranchiseeFilesImport'
					) then 'Franchisee'
				
				end as 'DataSet'
				
		from Serverjobs
	)
select 
	j.servername as server,
	j.name as 'JobName',
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
into tmpEmlSQLJobHistory
From JOBS j
left join babwscore01.msdb.dbo.sysjobhistory h 
	on j.job_id = h.job_id 
	and h.step_id = 0 --job outcome
	and 
		(
			( --jobs ran yesterday on/after 5pm
				datediff(dd, msdb.dbo.agent_datetime(h.run_date, h.run_time), getdate()-1) = 0
				and datepart(hh, msdb.dbo.agent_datetime(run_date, run_time)) > 16
			) -- or jobs ran today
			or datediff(dd, msdb.dbo.agent_datetime(h.run_date, h.run_time), getdate()) = 0
		)
where j.servername = 'BABWSCORE01'
and j.DataSet in 
	(
		'Labor',
		'Traffic',
		'Guest Load',
		'AW Sales',
		'Dimensions',
		'Franchisee'
	)

UNION

select 
	j.servername as server,
	j.name as 'JobName',
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
From JOBS j
left join KERMODE.msdb.dbo.sysjobhistory h 
	on j.job_id = h.job_id 
	and h.step_id = 0 --job outcome
	and 
		(
			( --jobs ran yesterday on/after 5pm
				datediff(dd, msdb.dbo.agent_datetime(h.run_date, h.run_time), getdate()-1) = 0
				and datepart(hh, msdb.dbo.agent_datetime(run_date, run_time)) > 16
			) -- or jobs ran today
			or datediff(dd, msdb.dbo.agent_datetime(h.run_date, h.run_time), getdate()) = 0
		)
where j.servername = 'KERMODE'
and j.DataSet in 
	(
		'Labor',
		'Traffic',
		'Guest Load',
		'AW Sales',
		'Dimensions',
		'Franchisee'
	)

UNION

select 
	j.servername as server,
	j.name as 'JobName',
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
From JOBS j
left join papamart.msdb.dbo.sysjobhistory h 
	on j.job_id = h.job_id 
	and h.step_id = 0 --job outcome
	and 
		(
			( --jobs ran yesterday on/after 5pm
				datediff(dd, msdb.dbo.agent_datetime(h.run_date, h.run_time), getdate()-1) = 0
				and datepart(hh, msdb.dbo.agent_datetime(run_date, run_time)) > 16
			) -- or jobs ran today
			or datediff(dd, msdb.dbo.agent_datetime(h.run_date, h.run_time), getdate()) = 0
		)
where j.servername = 'PAPAMART'
and j.DataSet in 
	(
		'Labor',
		'Traffic',
		'Guest Load',
		'AW Sales',
		'Dimensions',
		'Franchisee'
	)
UNION

select 
	j.servername as server,
	j.name as 'JobName',
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
From JOBS j
left join [STL-SSIS-P-01].msdb.dbo.sysjobhistory h 
	on j.job_id = h.job_id 
	and h.step_id = 0 --job outcome
	and 
		(
			( --jobs ran yesterday on/after 5pm
				datediff(dd, msdb.dbo.agent_datetime(h.run_date, h.run_time), getdate()-1) = 0
				and datepart(hh, msdb.dbo.agent_datetime(run_date, run_time)) > 16
			) -- or jobs ran today
			or datediff(dd, msdb.dbo.agent_datetime(h.run_date, h.run_time), getdate()) = 0
		)
where j.servername = 'STL-SSIS-P-01'
and j.DataSet in 
	(
		'Labor',
		'Traffic',
		'Guest Load',
		'AW Sales',
		'Dimensions',
		'Franchisee'
	)

order by RunDateTime, JobName


delete from tmpEmlSQLJobHistory where DataSet is null

;
	with Succeeded as
		(
			select JobName, cast(RunDateTime as datetime) as RunDateTime 
			from tmpEmlSQLJobHistory
			where run_status = 'Succeeded'
		)
	delete t
	from tmpEmlSQLJobHistory t
	join Succeeded s on t.JobName = s.JobName 
	where t.run_status <> 'Succeeded' 
	and cast(t.RunDateTime as datetime) < s.RunDateTime 
	;
--=====================================================================================================================================
--=====================================================================================================================================

if (select count(*) from tmpEmlSQLJobHistory) > 0
BEGIN
	
		
			declare @text nvarchar(max)

			declare @LaborStat varchar(4),
					@TrafficStat varchar(4),
					@GuestLoadStat varchar(4),
					@SalesStat varchar(4),
					@DimStat varchar(4),
					@FranchStat varchar(4),
					@SequenceCheck varchar(4),
					@Subj varchar(100)
	
 
			if (
					select count(*) from tmpEmlSQLJobHistory j
						where j.DataSet = 'Labor' 
							and 
							(
								(
									(j.Run_Status <> 'Succeeded' or j.Run_Status is NULL) 
										and
									j.JobName not in (select jj.JobName from tmpEmlSQLJobHistory jj where jj.DataSet = 'Labor' and jj.Run_Status = 'Succeeded' and jj.RunDateTime > j.RunDateTime ) --in case we ran the job again after it failed
								) 

							)
				) > 0 
		
				set @LaborStat = 'Fail' else set @LaborStat = 'Pass'

			if (
					select count(*) from tmpEmlSQLJobHistory j
						where j.DataSet = 'Traffic' 
							and (
								(
									(j.Run_Status <> 'Succeeded' or j.Run_Status is NULL) 
										and
									j.JobName not in (select jj.JobName from tmpEmlSQLJobHistory jj where jj.DataSet = 'Traffic' and jj.Run_Status = 'Succeeded' and jj.RunDateTime > j.RunDateTime )--in case we ran the job again after it failed
								)
								)
				) > 0

				set @TrafficStat = 'Fail' else set @TrafficStat = 'Pass'

			if (
					select count(*) from tmpEmlSQLJobHistory j
						where j.DataSet = 'Guest Load' 
							and (
								(
									(j.Run_Status <> 'Succeeded' or j.Run_Status is NULL) 
										and
									j.JobName not in (select jj.JobName from tmpEmlSQLJobHistory jj where jj.DataSet = 'Guest Load' and jj.Run_Status = 'Succeeded' and jj.RunDateTime > j.RunDateTime )--in case we ran the job again after it failed
								)
								)
				) > 0
				set @GuestLoadStat = 'Fail' else set @GuestLoadStat = 'Pass'

			if (
					select count(*) from tmpEmlSQLJobHistory j
						where j.DataSet = 'AW Sales' 
							and 
								(
								(
									(j.Run_Status <> 'Succeeded' or j.Run_Status is NULL) 
										and
									j.JobName not in (select jj.JobName from tmpEmlSQLJobHistory jj where jj.DataSet = 'AW Sales' and jj.Run_Status = 'Succeeded' and jj.RunDateTime > j.RunDateTime )--in case we ran the job again after it failed
								)
								)
				) > 0
				set @SalesStat = 'Fail' else set @SalesStat = 'Pass'

			if (
					select count(*) from tmpEmlSQLJobHistory j
						where j.DataSet = 'Dimensions' 
							and 
								(
								(
									(j.Run_Status <> 'Succeeded' or j.Run_Status is NULL) 
										and
									j.JobName not in (select jj.JobName from tmpEmlSQLJobHistory jj where jj.DataSet = 'Dimensions' and jj.Run_Status = 'Succeeded' and jj.RunDateTime > j.RunDateTime )--in case we ran the job again after it failed
								)
								)
				) > 0
				set @DimStat = 'Fail' else set @DimStat = 'Pass'

				if (
					select count(*) from tmpEmlSQLJobHistory j
						where j.DataSet = 'Franchisee' 
							and 
								(
								(
									(j.Run_Status <> 'Succeeded' or j.Run_Status is NULL) 
										and
									j.JobName not in (select jj.JobName from tmpEmlSQLJobHistory jj where jj.DataSet = 'Franchisee' and jj.Run_Status = 'Succeeded' and jj.RunDateTime > j.RunDateTime )--in case we ran the job again after it failed
								) 
								)
				) > 0
				set @FranchStat = 'Fail' else set @FranchStat = 'Pass'
		

			set @text = '<H1><font face =arial> BI Team Morning Critical Job Status </font> </H1>' +
				'<font face =arial size = 2> These jobs are critical to our reporting environment and must run successfully each morning before 7am.' +
				'<br> The query captures the run history from 5pm the previous day, until today at query run time. 
				<br> 
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
									when 'Labor' then @LaborStat
									when 'Traffic' then @TrafficStat
									when 'Guest Load' then @GuestLoadStat
									when 'AW Sales' then @SalesStat
									when 'Dimensions' then @DimStat
									when 'Franchisee' then @FranchStat
								end, ''
							from tmpEmlSQLJobHistory jh
							--left join #PassFail pf on jh.DataSet = pf.DataSet and jh.JobName = pf.JobName
							group by jh.DataSet--, pf.condition
							order by jh.Dataset
						  FOR XML PATH('tr'), TYPE 
				) AS NVARCHAR(MAX) ) +
				'</font></table>
				<br>'
				+
				'<font face =arial size = 2> <b> LABOR </b> </font>' +
				'<br>' +
				'<table border="1">' +
				'<font face =arial size = 2>' + 
				'<tr><th>SERVER</th><th>JOB NAME</th><th>DATETIME</th><th>DURATION</th><th>STATUS</th></tr>' +
				CAST ( ( SELECT td = server,'',
								td = jobName, '',
								td = isnull(RunDateTime, 0), '',
								td = isnull(RunDurationMinutes, ''), '',
								td = Run_Status, ''
						  from tmpEmlSQLJobHistory
						  where DataSet = 'Labor'
						  order by RunDateTime
						  FOR XML PATH('tr'), TYPE 
				) AS NVARCHAR(MAX) ) +
				'</font></table>
				<br>' 
				+
				'<font face =arial size = 2> <b> TRAFFIC </b> </font>' +
				'<br>' +
				'<table border="1">' +
				'<font face =arial size = 2>' + 
				'<tr><th>SERVER</th><th>JOB NAME</th><th>DATETIME</th><th>DURATION</th><th>STATUS</th></tr>' +
				CAST ( ( SELECT td = server,'',
								td = jobName, '',
								td = isnull(RunDateTime, 0), '',
								td = isnull(RunDurationMinutes, ''), '',
								td = Run_Status, ''
						  from tmpEmlSQLJobHistory
						  where DataSet = 'Traffic'
						  order by RunDateTime
						  FOR XML PATH('tr'), TYPE 
				) AS NVARCHAR(MAX) ) +
				'</font></table>
				<br>' 
				+
				'<font face =arial size = 2> <b> SALES </b> </font>' +
				'<br>' +
				'<table border="1">' +
				'<font face =arial size = 2>' + 
				'<tr><th>SERVER</th><th>JOB NAME</th><th>DATETIME</th><th>DURATION</th><th>STATUS</th></tr>' +
				CAST ( ( SELECT td = server,'',
								td = jobName, '',
								td = isnull(RunDateTime, 0), '',
								td = isnull(RunDurationMinutes, ''), '',
								td = Run_Status, ''
						  from tmpEmlSQLJobHistory
						  where DataSet = 'AW Sales'
						  order by RunDateTime
						  FOR XML PATH('tr'), TYPE 
				) AS NVARCHAR(MAX) ) +
				'</font></table>
				<br>' +
				'<font face =arial size = 2> <b> Guest Load </b> </font>' +
				'<br>' +
				'<table border="1">' +
				'<font face =arial size = 2>' + 
				'<tr><th>SERVER</th><th>JOB NAME</th><th>DATETIME</th><th>DURATION</th><th>STATUS</th></tr>' +
				CAST ( ( SELECT td = server,'',
								td = jobName, '',
								td = isnull(RunDateTime, 0), '',
								td = isnull(RunDurationMinutes, ''), '',
								td = Run_Status, ''
						  from tmpEmlSQLJobHistory
						  where DataSet = 'Guest Load'
						  order by RunDateTime
						  FOR XML PATH('tr'), TYPE 
				) AS NVARCHAR(MAX) ) +
				'</font></table>
				<br>' +
				'<font face =arial size = 2> <b> DIMENSIONS </b> </font>' +
				'<br>' +
				'<table border="1">' +
				'<font face =arial size = 2>' + 
				'<tr><th>SERVER</th><th>JOB NAME</th><th>DATETIME</th><th>DURATION</th><th>STATUS</th></tr>' +
				CAST ( ( SELECT td = server,'',
								td = jobName, '',
								td = isnull(RunDateTime, 0), '',
								td = isnull(RunDurationMinutes, ''), '',
								td = Run_Status, ''
						  from tmpEmlSQLJobHistory
						  where DataSet = 'Dimensions'
						  order by RunDateTime
						  FOR XML PATH('tr'), TYPE 
				) AS NVARCHAR(MAX) ) +
				'</font></table>
				<br>' +
				'<font face =arial size = 2> <b> FRANCHISEE </b> </font>' +
				'<br>' +
				'<table border="1">' +
				'<font face =arial size = 2>' + 
				'<tr><th>SERVER</th><th>JOB NAME</th><th>DATETIME</th><th>DURATION</th><th>STATUS</th></tr>' +
				CAST ( ( SELECT td = server,'',
								td = jobName, '',
								td = isnull(RunDateTime, 0), '',
								td = isnull(RunDurationMinutes, ''), '',
								td = Run_Status, ''
						  from tmpEmlSQLJobHistory
						  where DataSet = 'Franchisee'
						  order by RunDateTime
						  FOR XML PATH('tr'), TYPE 
				) AS NVARCHAR(MAX) ) +
				'</font></table>
				<br>
				<font face =arial size = 2>This report was generated by papamart.DW.dbo.spSQLJobHistoryEmail, which was executed from Kermode SQL Agent: CRITICAL JOB WATCH - - BI TEAM SANITY CHECK.</font>
				<br>
				<br>'

			if 
					@LaborStat = 'Fail'
					or
					@TrafficStat = 'Fail' 
					or
					@GuestLoadStat = 'Fail' 
					or
					@SalesStat = 'Fail' 
					or
					@DimStat = 'Fail' 
					or
					@FranchStat = 'Fail'
					or
					@SequenceCheck = 'Fail'
		
				select 
					@subj = 'BI Team Morning Critical Job Status: Fail',
					@Recip = 'BIAdminTextAlert@buildabear.com'
			else

				select 
					@subj = 'BI Team Morning Critical Job Status: Pass',
					@Recip = 'biadmin@buildabear.com'
		

			exec msdb.dbo.sp_send_dbmail
				@profile_name = 'biadmin',
				@recipients = @Recip, --'biadmin@buildabear.com',
				@body = @text,
				@subject = @subj,
				@body_format = 'HTML'


		
END
```

