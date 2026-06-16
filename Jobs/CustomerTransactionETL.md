# Job: CustomerTransactionETL

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["CustomerTransactionETL"]
    JOB --> Wait_Until_6AM_to_Run_1["Step 1: Wait Until 6AM to Run [TSQL]"]`n    JOB --> Check_for_Transaction_Facts_Loaded__fail_if_not__2["Step 2: Check for Transaction_Facts Loaded (fail if not) [TSQL]"]`n    JOB --> CRMCustomerDim_update_from_inbound_3["Step 3: CRMCustomerDim_update_from_inbound [TSQL]"]`n    JOB --> wait_4["Step 4: wait [TSQL]"]`n    JOB --> CustomerTransactionETL_5["Step 5: CustomerTransactionETL [SSIS]"]`n    JOB --> LoyaltyTransactionETL_6["Step 6: LoyaltyTransactionETL [SSIS]"]`n    JOB --> Start_Job____ServiceCloud_CustomerDim_Upsert_7["Step 7: Start Job -> ServiceCloud_CustomerDim_Upsert [TSQL]"]`n    JOB --> Start_Job____CRMLoyaltyETL_daily_8["Step 8: Start Job -> CRMLoyaltyETL_daily [TSQL]"]`n    JOB --> start_a360_job_9["Step 9: start a360 job [TSQL]"]`n    JOB --> ProcessCubeCRM___If_Necessary_10["Step 10: ProcessCubeCRM - If Necessary [TSQL]"]`n    JOB --> Start_Job___AzureProcessing_CRMTransactionFacts_11["Step 11: Start Job - AzureProcessing_CRMTransactionFacts [TSQL]"]`n    JOB --> JobCompletionNotice_12["Step 12: JobCompletionNotice [TSQL]"]`n```

## Steps

### Step 1: Wait Until 6AM to Run
**Subsystem:** TSQL  

```sql
while (select datepart(hh, getdate()))<6  begin   waitfor delay '00:01:00'      if (select datepart(hh, getdate()))>=6   break    else   Continue  end
```

### Step 2: Check for Transaction_Facts Loaded (fail if not)
**Subsystem:** TSQL  

```sql
IF (Object_ID('tempdb..#SSISHistory') IS NOT NULL) DROP TABLE #SSISHistory  select    e.folder_name,   e.project_name,   e.package_name,   e.environment_name,   ex.executable_name,   exs.execution_path,   exs.start_time,   exs.end_time,   CONVERT(TIME,DATEADD (ms, exs.execution_duration, 0)) as Duration,   case exs.execution_result     when 0 then 'Success'    when 1 then 'Failure'    when 2 then 'Completion'    when 3 then 'Cancelled'   end as execution_result,   exs.execution_value  into #SSISHistory  from SSISDB.internal.executions e  join SSISDB.internal.executable_statistics exs on e.execution_id=exs.execution_id  join SSISDB.internal.executables ex    on exs.executable_id=ex.executable_id   and e.project_lsn=ex.project_version_lsn  where 1=1  and datediff(dd, cast(exs.start_time as date), getdate())=0  and e.package_name='SalesAuditToDWStaging.dtsx'  --and exs.execution_path='\SalesAuditToDWStaging\SEQ - Merge Fact Tables\Build Transaction_Facts'  and ex.executable_name='Merge Transaction_Facts'  and exs.execution_result=0  order by exs.start_time    if (select count(*) from #SSISHistory) =0    RAISERROR ('SQL - Build Transaction Facts not yet completed', 18,1);    
```

### Step 3: CRMCustomerDim_update_from_inbound
**Subsystem:** TSQL  

```sql
EXEC [stl-ssis-p-02].msdb.dbo.sp_start_job @job_name='CRMCustomerDim_update_from_inbound'
```

### Step 4: wait
**Subsystem:** TSQL  

```sql
waitfor delay '00:30:00'
```

### Step 5: CustomerTransactionETL
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\CRM\CustomerTransactionETL\CustomerTransactionETL.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10024 /Par "\"DaysToGoBack(Int32)\"";10 /Par "\"DaysToInclude(Int32)\"";10 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 6: LoyaltyTransactionETL
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\Loyalty\LoyaltyTransactionETL\LoyaltyTransactionETL.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10168 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";3 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 7: Start Job -> ServiceCloud_CustomerDim_Upsert
**Subsystem:** TSQL  

```sql
EXEC [stl-ssis-p-02].msdb.dbo.sp_start_job @job_name='Azure_CustomerDim_trigger'
```

### Step 8: Start Job -> CRMLoyaltyETL_daily
**Subsystem:** TSQL  

```sql
EXEC [stl-ssis-p-02].msdb.dbo.sp_start_job @job_name='CRMLoyaltyETL_daily'
```

### Step 9: start a360 job
**Subsystem:** TSQL  

```sql
EXEC sp_start_job @job_name='CRM_SalesForceDataExtensionExportA360'
```

### Step 10: ProcessCubeCRM - If Necessary
**Subsystem:** TSQL  

```sql
--IF CUBE MEASURES ALREADY PROCESSED AND IT IS BEFORE 6:30AM, PROCESS THE CRM MEASURES AGAIN -- ALL CUBE MEASURES NORMALLY PROCESSES WITH SALES -- SO IF IT DIDN'T PROCESS, IT WILL  if (    select count(*) ProcessRunCount    from sysjobs j with (nolock)    join sysjobhistory h with (nolock)     on j.job_id = h.job_id      and datediff(dd, msdb.dbo.agent_datetime(h.run_date, h.run_time), getdate()) = 0      and h.step_id = 0 --job outcome     and h.run_status=1    where j.name='ProcessCubeMeasures'   ) > 0   and convert(varchar, getdate(), 108) <= '06:45:00'  BEGIN   EXEC sp_start_job @job_name='ProcessCubeCRM'  END
```

### Step 11: Start Job - AzureProcessing_CRMTransactionFacts
**Subsystem:** TSQL  

```sql
EXEC [stl-ssis-p-02].msdb.dbo.sp_start_job @job_name='AzureProcessing_CRMTransactionFacts'
```

### Step 12: JobCompletionNotice
**Subsystem:** TSQL  

```sql
exec spEmailSQLAgentJobCompletion   @ProcessName = 'CRM to DW Customer-Transaction ETL (phase one)',   @SQLAgent = 'CustomerTransactionETL',  @Recipients = 'biadmin@buildabear.com'
```


