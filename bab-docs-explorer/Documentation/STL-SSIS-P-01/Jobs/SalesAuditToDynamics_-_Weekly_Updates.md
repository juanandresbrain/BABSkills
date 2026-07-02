# Job: SalesAuditToDynamics - Weekly Updates

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["SalesAuditToDynamics - Weekly Updates"]
    JOB --> Dynamically_Update_SSIS___SalesAuditToDynamicsStaging____Parameter___Days_to_Go_Back_and_Include_1["Step 1: Dynamically Update SSIS - SalesAuditToDynamicsStaging  - Parameter - Days to Go Back and Include [TSQL]"]`n    JOB --> PreFlight_Check___Legacy_AW_to_DW_Job_2["Step 2: PreFlight Check - Legacy AW to DW Job [TSQL]"]`n    JOB --> PreFlight_Check___SalesAuditToDynamics___Master_Job_3["Step 3: PreFlight Check - SalesAuditToDynamics - Master Job [TSQL]"]`n    JOB --> SSIS___SalesAuditToDynamicsDWFacts_4["Step 4: SSIS - SalesAuditToDynamicsDWFacts [SSIS]"]`n    JOB --> SSIS___SalesAuditToDynamicsStaging_5["Step 5: SSIS - SalesAuditToDynamicsStaging [SSIS]"]`n    JOB --> SSIS___SalesAuditToDynamicsPackageAPI_Parallel_6["Step 6: SSIS - SalesAuditToDynamicsPackageAPI_Parallel [SSIS]"]`n    JOB --> Job_Completion_Notification_7["Step 7: Job Completion Notification [TSQL]"]`n```

## Steps

### Step 1: Dynamically Update SSIS - SalesAuditToDynamicsStaging  - Parameter - Days to Go Back and Include
**Subsystem:** TSQL  

```sql
-- This Script is designed to check for first day of the current period   -- Then update the sql agent job step to set the days to go back and days to include parameters  for the SalesAuditToDynamics - Weekly Updates SSIS Step   -- We may not want to update any transactions from the previous period.   -- Added 4/20/2023    Declare @FirstDate date  Declare @DaysBack varchar (10)  Declare @Job_id NVARCHAR(MAX)  Declare @Step_id NVARCHAR(MAX)  Declare @Command NVARCHAR(MAX)  Declare @Sql NVARCHAR(MAX)    set @FirstDate =    (    select min(actual_date) as FirstDateOfCurrentPeriod    from papamart.dw.dbo.date_dim    where period_id = (select period_id from papamart.dw.dbo.date_dim where actual_date = cast (getdate() as date))   )    set @DaysBack = (select cast (DATEDIFF(dd,@FirstDate, cast(getdate() as date)) as varchar))       set @job_id = (select job_id from msdb.dbo.sysjobs where name = 'SalesAuditToDynamics - Weekly Updates')      set @step_id =    (    SELECT step_id           FROM msdb.dbo.sysjobsteps    WHERE 1=1    and job_id = @job_id    and step_name = 'SSIS - SalesAuditToDynamicsStaging'   )        set @Command =   (  '/ISSERVER "\"\SSISDB\WMS\SalesAuditToDynamicsStaging\SalesAuditToDynamicsStaging.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10166 /Par "\"DaysToGoBack(Int32)\"";'+@DaysBack+' /Par "\"DaysToInclude(Int32)\"";'+@DaysBack+' /Par ExecuteUpdateMergeFlow;Yes /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E'  )        SET @SQL =  '  EXEC msdb.dbo.sp_update_jobstep   @job_id=N''' +  @Job_id + ''',' + '  @step_id=' + @Step_id + ' , '+  '@command=N''' + @command + '' + char(39)     --To View Commands and Table   --print @command  --print @daysback  --print @sql    --SELECT   --step_id,  --step_name,  --subsystem,  --command,  --output_file_name,  --proxy_id,   --job_id  --FROM msdb.dbo.sysjobsteps  --WHERE 1=1  --and job_id = @job_id  --and step_id = @step_id  --ORDER BY job_id, step_id    -- Executes the Update   exec sp_executesql @sql  
```

### Step 2: PreFlight Check - Legacy AW to DW Job
**Subsystem:** TSQL  

```sql
-- Checks to See if Legagy AW to DW SSIS Is running (typically 2am - 6am Window)   -- If it is, it will raise an error and the sql agent step will be configured to try again     use SSISDB     If    (    select count (*)     --e.status,     --e.end_time,     --e.*     from catalog.executions e    WHERE 1=1     and e.project_name = 'SalesAuditToDWStaging'    and E.end_time IS NULL      and e.execution_id in (select max(execution_id) as execution_id from catalog.executions where project_name='SalesAuditToDWStaging') -- Most Recent Execution Only     --and e.status not in (2,5) -- Shouldn't be necessary with if end time with end time null filter    --The status of the operation.  ; The possible values are created (1), running (2), canceled (3), failed (4), pending (5), ended unexpectedly (6), succeeded (7), stopping (8), and completed (9).       )     <> 0       RAISERROR ('The Legacy SalesAuditToDWStaging SSIS is currently running. Will Retry.',16,1)    else     Print 'Proceed with Job Run'       
```

### Step 3: PreFlight Check - SalesAuditToDynamics - Master Job
**Subsystem:** TSQL  

```sql
-- Checks to See if SalesAuditToDynamics - Daily Job is running before proceeding  set nocount  on  Declare @JobId varchar (max)   set @JobId =    (    select s.job_id     from sysjobs s     --where s.[name] = 'Loyalty Customer and Transaction Hourly ETL' -- Testing Purposes    where s.[name] = 'SalesAuditToDynamics - Master Job' -- Job Name You want To Check Is Running   )      exec [dbo].[sp_get_composite_job_info_tc] @job_id = @JobId -- Truncates and Loads  TempJobTable    --select * from  TempJobTable  --Validation Purposes        If    (  select   case when current_execution_status = 4     then 'Proceed'    else 'TryAgainLater'    end as status  from TempJobTable   --where current_execution_status  <> 4 -- Idle Status Code - Not running     )  = 'TryAgainLater'      RAISERROR ('The SalesAuditToDynamics - Daily Job is currently running. Will Retry.',16,1)    else     Print 'Proceed with Weekly Job Run'
```

### Step 4: SSIS - SalesAuditToDynamicsDWFacts
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\DW\SalesAuditToDynamicsDWFacts\SalesAuditToDynamicsDWFacts.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10148 /Par "\"DaysToGoBack(Int32)\"";31 /Par "\"DaysToInclude(Int32)\"";31 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 5: SSIS - SalesAuditToDynamicsStaging
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\SalesAuditToDynamicsStaging\SalesAuditToDynamicsStaging.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10166 /Par "\"DaysToGoBack(Int32)\"";13 /Par "\"DaysToInclude(Int32)\"";13 /Par ExecuteUpdateMergeFlow;Yes /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 6: SSIS - SalesAuditToDynamicsPackageAPI_Parallel
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\SalesAuditToDynamicsPackageAPI_Parallel\SalesAuditToDynamicsPackageAPI_Parallel.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10167 /Par "\"DaysToGoBack(Int32)\"";31 /Par "\"DaysToInclude(Int32)\"";31 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 7: Job Completion Notification
**Subsystem:** TSQL  

```sql
exec spEmailSQLAgentJobCompletion   @ProcessName = 'SalesAuditToDynamics - Weekly Updates',   @SQLAgent = 'SalesAuditToDynamics - Weekly Updates',  @Recipients = 'biadmin@buildabear.com'
```


