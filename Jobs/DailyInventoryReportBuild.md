# Job: DailyInventoryReportBuild

**Enabled:** Yes  
**Description:** Note Aug 1 2025: Changed the schedule from daily at 9am to daily at 6am. This is to allow this to be run during the Azure Analysis scalling to S4 Window. This data seems mostly dependent on merchandising and Web Order Processing data.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["DailyInventoryReportBuild"]
    JOB --> LoadData_1["Step 1: LoadData [SSIS]"]`n    JOB --> Process_unshipped_data_2["Step 2: Process unshipped data [SSIS]"]`n    JOB --> Start_Job___AzureProcessing_DailyInventory_3["Step 3: Start Job - AzureProcessing_DailyInventory [TSQL]"]`n    JOB --> Job_Completion_Notice_4["Step 4: Job Completion Notice [TSQL]"]`n```

## Steps

### Step 1: LoadData
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\Azure\DailyInventoryPowerBI\DailyInventoryPowerBI.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10085 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: Process unshipped data
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\Azure\DailyInventory_Unshipped\DailyInventory_Unshipped.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10090 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 3: Start Job - AzureProcessing_DailyInventory
**Subsystem:** TSQL  

```sql
EXEC [stl-ssis-p-02].msdb.dbo.sp_start_job @job_name='AzureProcessing_DailyInventory'
```

### Step 4: Job Completion Notice
**Subsystem:** TSQL  

```sql
exec spEmailSQLAgentJobCompletion   @ProcessName = 'Daily Inventory Report Data Stage',   @SQLAgent = 'DailyInventoryReportBuild',  @Recipients = 'biadmin@buildabear.com'
```


