# Job: WebOrderInboundDemandExtract_ForPowerBI

**Enabled:** Yes  
**Description:** No longer runs the step to run AzureProcessing_WebOrderInboundDemandTracking because this runs hourly via WebDemandTracking

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WebOrderInboundDemandExtract_ForPowerBI"]
    JOB --> WebOrderInboundDemandExtract_1["Step 1: WebOrderInboundDemandExtract [SSIS]"]`n    JOB --> WebOrderInboundDemandExtract_MergeIntoHistoricalTable_2["Step 2: WebOrderInboundDemandExtract_MergeIntoHistoricalTable [TSQL]"]`n    JOB --> AzureProcessing_WebOrderInboundDemandTracking_3["Step 3: AzureProcessing_WebOrderInboundDemandTracking [TSQL]"]`n    JOB --> AzureProcessing_WebOrderData_4["Step 4: AzureProcessing_WebOrderData [TSQL]"]`n    JOB --> Job_Completion_Notice_5["Step 5: Job Completion Notice [TSQL]"]`n```

## Steps

### Step 1: WebOrderInboundDemandExtract
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\Azure\WebOrderInboundDemandExtract\WebOrderInboundDemandExtract.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10096 /Par "\"DaysToGoBack(Int32)\"";3 /Par "\"DaysToInclude(Int32)\"";3 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: WebOrderInboundDemandExtract_MergeIntoHistoricalTable
**Subsystem:** TSQL  

```sql
-- Temporary step added to accomdate data requests for PDP Redesign project    EXEC PAPAMART.DWStaging.dbo.spMergeWebOrderInboundDemandTrackingFactsV2_TEMP2;
```

### Step 3: AzureProcessing_WebOrderInboundDemandTracking
**Subsystem:** TSQL  

```sql
EXEC [stl-ssis-p-02].msdb.dbo.sp_start_job @job_name='AzureProcessing_WebOrderInboundDemandTracking'  
```

### Step 4: AzureProcessing_WebOrderData
**Subsystem:** TSQL  

```sql
EXEC [stl-ssis-p-02].msdb.dbo.sp_start_job @job_name='AzureProcessing_WebOrderData'  
```

### Step 5: Job Completion Notice
**Subsystem:** TSQL  

```sql
exec spEmailSQLAgentJobCompletion   @ProcessName = 'Power BI DailyInbound Demand Tracking',   @SQLAgent = 'WebOrderInboundDemandExtract_ForPowerBI',  @Recipients = 'biadmin@buildabear.com'
```


