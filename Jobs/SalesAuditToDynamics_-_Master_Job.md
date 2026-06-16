# Job: SalesAuditToDynamics - Master Job

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["SalesAuditToDynamics - Master Job"]
    JOB --> PreFlight_Check___Legacy_AW_to_DW_Job_1["Step 1: PreFlight Check - Legacy AW to DW Job [TSQL]"]`n    JOB --> PreFlight_Check___SalesAuditToDynamics___Weekly_Updates_Job_2["Step 2: PreFlight Check - SalesAuditToDynamics - Weekly Updates Job [TSQL]"]`n    JOB --> SSIS___SalesAuditToDynamicsDWFacts_3["Step 3: SSIS - SalesAuditToDynamicsDWFacts [SSIS]"]`n    JOB --> SSIS___SalesAuditToDynamicsStaging_4["Step 4: SSIS - SalesAuditToDynamicsStaging [SSIS]"]`n    JOB --> SSIS___SalesAuditToDynamicsPackageAPI_Parallel_5["Step 5: SSIS - SalesAuditToDynamicsPackageAPI_Parallel [SSIS]"]`n    JOB --> Trigger_ADF_Pipeline___Promotion_Studio_Discount_Facts_6["Step 6: Trigger ADF Pipeline - Promotion Studio Discount Facts [TSQL]"]`n```

## Steps

### Step 1: PreFlight Check - Legacy AW to DW Job
**Subsystem:** TSQL  

```sql
-- Checks to See if Legagy AW to DW SSIS Is running (typically 2am - 6am Window)   -- If it is, it will raise an error and the sql agent step will be configured to try again     use SSISDB     If    (    select count (*)     --e.status,     --e.end_time,     --e.*     from catalog.executions e    WHERE 1=1     and e.project_name = 'SalesAuditToDWStaging'    and E.end_time IS NULL      and e.execution_id in (select max(execution_id) as execution_id from catalog.executions where project_name='SalesAuditToDWStaging') -- Most Recent Execution Only     --and e.status not in (2,5) -- Shouldn't be necessary with if end time with end time null filter    --The status of the operation.  ; The possible values are created (1), running (2), canceled (3), failed (4), pending (5), ended unexpectedly (6), succeeded (7), stopping (8), and completed (9).       )     <> 0       RAISERROR ('The Legacy SalesAuditToDWStaging SSIS is currently running. Will Retry.',16,1)    else     Print 'Proceed with Job Run'       
```

### Step 2: PreFlight Check - SalesAuditToDynamics - Weekly Updates Job
**Subsystem:** TSQL  

```sql
-- Checks to See if SalesAuditToDynamics - Weekly Updates Job is running before proceeding  set nocount  on  Declare @JobId varchar (max)   set @JobId =    (    select s.job_id     from sysjobs s     --where s.[name] = 'Loyalty Customer and Transaction Hourly ETL' -- Testing Purposes    where s.[name] = 'SalesAuditToDynamics - Weekly Updates' -- Job Name You want To Check Is Running   )      exec [dbo].[sp_get_composite_job_info_tc] @job_id = @JobId -- Truncates and Loads  TempJobTable    --select * from  TempJobTable  Validation Purpose        If    (  select   case when current_execution_status = 4     then 'Proceed'    else 'TryAgainLater'    end as status  from TempJobTable   --where current_execution_status  <> 4 -- Idle Status Code - Not running     )  = 'TryAgainLater'      RAISERROR ('The SalesAuditToDynamics - Weekly Updates Job is currently running. Will Retry.',16,1)    else     Print 'Proceed with Daily Job Run'
```

### Step 3: SSIS - SalesAuditToDynamicsDWFacts
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\DW\SalesAuditToDynamicsDWFacts\SalesAuditToDynamicsDWFacts.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10148 /Par "\"DaysToGoBack(Int32)\"";3 /Par "\"DaysToInclude(Int32)\"";3 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";1 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 4: SSIS - SalesAuditToDynamicsStaging
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\SalesAuditToDynamicsStaging\SalesAuditToDynamicsStaging.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10166 /Par "\"DaysToGoBack(Int32)\"";3 /Par "\"DaysToInclude(Int32)\"";3 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";1 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 5: SSIS - SalesAuditToDynamicsPackageAPI_Parallel
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\SalesAuditToDynamicsPackageAPI_Parallel\SalesAuditToDynamicsPackageAPI_Parallel.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10167 /Par "\"DaysToGoBack(Int32)\"";3 /Par "\"DaysToInclude(Int32)\"";3 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 6: Trigger ADF Pipeline - Promotion Studio Discount Facts
**Subsystem:** TSQL  

```sql
EXEC sp_start_job @job_name='AzureProcessing_DiscountFacts'
```


