# Job: StoreForcePosSalesExport_OncePerDay

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["StoreForcePosSalesExport_OncePerDay"]
    JOB --> Stop_Half_Hourly_Job_If_Running_1["Step 1: Stop Half Hourly Job If Running [TSQL]"]`n    JOB --> Check_for_Dupes_2["Step 2: Check for Dupes [TSQL]"]`n    JOB --> Check_to_See_if_Transaction_Facts_is_Loaded_3["Step 3: Check to See if Transaction Facts is Loaded [TSQL]"]`n    JOB --> Check_for_Transaction_Facts_vs_vwDW_Transactions_Cube_V3_4["Step 4: Check for Transaction Facts vs vwDW_Transactions_Cube_V3 [TSQL]"]`n    JOB --> HR_StoreForcePosSalesExtractSSIS_5["Step 5: HR_StoreForcePosSalesExtractSSIS [SSIS]"]`n    JOB --> Delete_Old_Files_6["Step 6: Delete Old Files [TSQL]"]`n    JOB --> Process_Completion_Notification_7["Step 7: Process Completion Notification [TSQL]"]`n    JOB --> Start_Job_StoreForcePosSalesExport_Every30Minutes_8["Step 8: Start Job StoreForcePosSalesExport_Every30Minutes [TSQL]"]`n```

## Steps

### Step 1: Stop Half Hourly Job If Running
**Subsystem:** TSQL  

```sql
declare @run int  select @run = 1    exec spSQLAGentStopLongRunningJob   @Job= 'StoreForcePosSalesExport_Every30Minutes',   @Runtime = @run,   @Rec = 'dant@buildabear.com'
```

### Step 2: Check for Dupes
**Subsystem:** TSQL  

```sql
select    StoreCode,   DateRaw,   Slot  into #dupes  from papamart.dw.dbo.HR_StoreForcePosSalesFact  group by    StoreCode,   DateRaw,   Slot  having count(*) >1    if (select count(*) from #dupes) >0    begin     delete sf   from papamart.dw.dbo.HR_StoreForcePosSalesFact sf   join #dupes d     on sf.StoreCode=d.StoreCode    and sf.DateRaw=d.DateRaw    and sf.Slot=d.Slot    end
```

### Step 3: Check to See if Transaction Facts is Loaded
**Subsystem:** TSQL  

```sql
IF (Object_ID('tempdb..#SSISHistory') IS NOT NULL) DROP TABLE #SSISHistory  select    e.folder_name,   e.project_name,   e.package_name,   e.environment_name,   ex.executable_name,   exs.execution_path,   exs.start_time,   exs.end_time,   CONVERT(TIME,DATEADD (ms, exs.execution_duration, 0)) as Duration,   case exs.execution_result     when 0 then 'Success'    when 1 then 'Failure'    when 2 then 'Completion'    when 3 then 'Cancelled'   end as execution_result,   exs.execution_value  into #SSISHistory  from SSISDB.internal.executions e  join SSISDB.internal.executable_statistics exs on e.execution_id=exs.execution_id  join SSISDB.internal.executables ex    on exs.executable_id=ex.executable_id   and e.project_lsn=ex.project_version_lsn  where 1=1  and datediff(dd, cast(exs.start_time as date), getdate())=0  and e.package_name='SalesAuditToDWStaging.dtsx'  --and exs.execution_path='\SalesAuditToDWStaging\SEQ - Merge Fact Tables\Build Transaction_Facts'  and ex.executable_name='Merge Transaction_Facts'  and exs.execution_result=0  order by exs.start_time    if (select count(*) from #SSISHistory) =0    RAISERROR ('SQL - Build Transaction Facts not yet completed', 18,1);        /*  IF (Object_ID('tempdb..#SQLJobHistory') IS NOT NULL) DROP TABLE #SQLJobHistory      select       j.name as 'JobName',   cast(msdb.dbo.agent_datetime(run_date, run_time) as datetime)  as 'RealRunDateTime',   convert(varchar, msdb.dbo.agent_datetime(run_date, run_time), 100)  as 'RunDateTime',   ((run_duration/10000*3600 + (run_duration/100)%100*60 + run_duration%100 + 31 ) / 60)            as 'RunDurationMinutes',   case h.run_status    when 0 then 'Failed'    when 1 then 'Succeeded'    when 2 then 'Retry'    when 3 then 'Canceled'    when NULL then 'No History'   end as Run_Status,   h.step_id,   h.step_name  into #SQLJobHistory  From [STL-SQL-P-04\SQL2008R2].msdb.dbo.sysjobs j  left join [STL-SQL-P-04\SQL2008R2].msdb.dbo.sysjobhistory h    on j.job_id = h.job_id    --and h.step_id = 0 --job outcome   and datediff(dd, msdb.dbo.agent_datetime(h.run_date, h.run_time), getdate()) = 0  where j.name='AuditWorksImport_Transactions_VAT_Part2of3'  and h.step_name='SQL - Build Transaction Facts'  order by h.step_id      ----===================================================================     ;   with    MaxDate as    (     select JobName, max(RealRunDateTime) RealRunDateTime     from #SQLJobHistory     group by JobName    )   delete jh   from #SQLJobHistory jh   join MaxDate md     on jh.JobName=md.JobName     and jh.RealRunDateTime<>md.RealRunDateTime   ;      if (select count(*) from #SQLJobHistory where Run_status='Succeeded') =0    RAISERROR ('SQL - Build Transaction Facts not yet completed', 18,1);    */
```

### Step 4: Check for Transaction Facts vs vwDW_Transactions_Cube_V3
**Subsystem:** TSQL  

```sql
select    cast(dd.actual_date as date) TransactionDate,   sd.store_id,   sum(tf.gaap_sales_amount) GaapSales,   sum(tf.store_sales_amount) StoreSales  INTO #tranFacts  from papamart.dw.dbo.transaction_facts tf  join papamart.dw.dbo.store_dim sd on tf.store_key=sd.store_key  join papamart.dw.dbo.date_dim dd on tf.date_key=dd.date_key   where cast(dd.actual_date as date) >= getdate()-45  group by    cast(dd.actual_date as date),   sd.store_id    select    cast(dd.actual_date as date) TransactionDate,   sd.store_id,   sum(tf.gaap_sales_amount) GaapSales,   sum(tf.store_sales_amount) StoreSales  INTO #tranFactsCube  from papamart.dw.dbo.vwDW_Transactions_Cube_V3 tf  join papamart.dw.dbo.store_dim sd on tf.store_key=sd.store_key  join papamart.dw.dbo.date_dim dd on tf.date_key=dd.date_key   where cast(dd.actual_date as date) >= getdate()-45  group by    cast(dd.actual_date as date),   sd.store_id      if (    select count(*)    from #tranFacts tf    full outer join #tranFactsCube tfc      on isnull(tf.TransactionDate,'3030-12-31')=isnull(tfc.TransactionDate, '3030-12-31')     and isnull(tf.store_id,0)=isnull(tf.store_id,0)     and isnull(tf.GaapSales,0)=isnull(tf.GaapSales,0)    where tf.TransactionDate is null    or tfc.TransactionDate is null   )>0    RAISERROR ('SQL - transaction_facts<>vwDW_Transactions_Cube_V3', 18,1);  
```

### Step 5: HR_StoreForcePosSalesExtractSSIS
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\StoreForce\HR_StoreForcePosSalesExtract\HR_StoreForcePosSalesExtract.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10041 /Par "\"DaysToGoBack(Int32)\"";10 /Par "\"DaysToInclude(Int32)\"";9 /Par StoreForcePOSSalesExtractRunType;NormalRun /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 6: Delete Old Files
**Subsystem:** TSQL  

```sql
exec spDeleteOldFiles_StoreForcePosSalesExtract
```

### Step 7: Process Completion Notification
**Subsystem:** TSQL  

```sql
exec spEmailSQLAgentJobCompletion   @ProcessName = 'Storeforce Daily Reload',   @SQLAgent = 'StoreForcePosSalesExport_OncePerDay',  @Recipients = 'biadmin@buildabear.com'
```

### Step 8: Start Job StoreForcePosSalesExport_Every30Minutes
**Subsystem:** TSQL  

```sql
EXEC sp_start_job @job_name='StoreForcePosSalesExport_Every30Minutes'
```


