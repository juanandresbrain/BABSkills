# Job: FlashGaapSales_AzureProcessing

**Enabled:** No  
**Description:** Disabled because job is called from FlashGaapSales job on Kermode  In addition to processing the Azure FlashGaapSales table in the FlashGaapSales model, it will also call the job on stl-ssis-p-02 which will process the FlashGaapSales table on the BABW-DW model.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["FlashGaapSales_AzureProcessing"]
    JOB --> FlashGaapSales_AzureProcessing_1["Step 1: FlashGaapSales_AzureProcessing [SSIS]"]`n    JOB --> AzureProcessing_FlashGaapSales_2["Step 2: AzureProcessing_FlashGaapSales [TSQL]"]`n```

## Steps

### Step 1: FlashGaapSales_AzureProcessing
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\Azure\FlashGaapSales_AzureProcessing\FlashGaapSales_AzureProcessing.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10084 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: AzureProcessing_FlashGaapSales
**Subsystem:** TSQL  

```sql
EXEC [stl-ssis-p-02].msdb.dbo.sp_start_job @job_name='AzureProcessing_FlashGaapSales'
```


