# Job: WMS_cycleCount_ETL

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WMS_cycleCount_ETL"]
    JOB --> WMS_CycleCountETL_1["Step 1: WMS_CycleCountETL [SSIS]"]`n    JOB --> Start_Job___AzureProcessing_WMS_CycleCount_2["Step 2: Start Job - AzureProcessing_WMS_CycleCount [TSQL]"]`n```

## Steps

### Step 1: WMS_CycleCountETL
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\WMS_CycleCountETL\WMS_CycleCountETL.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10118 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: Start Job - AzureProcessing_WMS_CycleCount
**Subsystem:** TSQL  

```sql
EXEC [stl-ssis-p-02].msdb.dbo.sp_start_job @job_name='AzureProcessing_WMS_CycleCount'
```


