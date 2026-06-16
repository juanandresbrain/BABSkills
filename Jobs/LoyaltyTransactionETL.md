# Job: LoyaltyTransactionETL

**Enabled:** Yes  
**Description:** No Description

## Architecture Diagram

```mermaid
flowchart LR
    JOB["LoyaltyTransactionETL"]
    JOB --> Check_to_Make_Sure_Daily_Job_Ran_1["Step 1: Check to Make Sure Daily Job Ran [TSQL]"]`n    JOB --> LoyaltyTransactionETL_2["Step 2: LoyaltyTransactionETL [SSIS]"]`n    JOB --> Run_Azure_Trigger_3["Step 3: Run Azure Trigger [TSQL]"]`n```

## Steps

### Step 1: Check to Make Sure Daily Job Ran
**Subsystem:** TSQL  

```sql
if    (    select count(*)    --select J.name, msdb.dbo.agent_datetime(h.run_date, h.run_time)    from [STL-SSIS-P-02].msdb.dbo.sysjobs j    join [STL-SSIS-P-02].msdb.dbo.sysjobhistory h      on j.job_id = h.job_id      and h.step_id = 0 --job outcome    where j.name='CRMLoyaltyETL_daily'    and datediff(dd, msdb.dbo.agent_datetime(h.run_date, h.run_time), getdate()) = 0    and h.run_status = '1' -- Succeeded -- Added Jul 1 2025   ) = 0      RAISERROR ('SQL - [stl-ssis-p-02] SQL Agent ''CRMLoyaltyETL_daily'' has not completed running today, so the Hourly job cannot start yet.', 18,1);    
```

### Step 2: LoyaltyTransactionETL
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\Loyalty\LoyaltyTransactionETL\LoyaltyTransactionETL.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10168 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 3: Run Azure Trigger
**Subsystem:** TSQL  

```sql
EXEC [stl-ssis-p-02].msdb.dbo.sp_start_job @job_name='CRMLoyaltyETL_hourly'  
```


