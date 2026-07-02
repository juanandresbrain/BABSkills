# Job: AzureProcessingSummary_MorningValidation

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** Job is not scheduled because it is called from kermode job CRITICAL JOB WATCH - - BI TEAM SANITY CHECK (we should move that job to stl-ssis-p-01)

## Architecture Diagram

```mermaid
flowchart LR
    JOB["AzureProcessingSummary_MorningValidation"]
    JOB --> AzurePartitionsMetaDownload_1["Step 1: AzurePartitionsMetaDownload [SSIS]"]`n    JOB --> spEmailAzureProcessSummary_MorningValidation_2["Step 2: spEmailAzureProcessSummary_MorningValidation [TSQL]"]`n```

## Steps

### Step 1: AzurePartitionsMetaDownload
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\Azure\AzurePartitionsMetaDownload\AzurePartitionsMetaDownload.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10124 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: spEmailAzureProcessSummary_MorningValidation
**Subsystem:** TSQL  

```sql
exec papamart.dwstaging.dbo.spEmailAzureProcessSummary_MorningValidation
```


