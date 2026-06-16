# Job: AzurePartitionMetaDownload

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["AzurePartitionMetaDownload"]
    JOB --> AzurePartitionsMetaDownload_1["Step 1: AzurePartitionsMetaDownload [SSIS]"]`n```

## Steps

### Step 1: AzurePartitionsMetaDownload
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\Azure\AzurePartitionsMetaDownload\AzurePartitionsMetaDownload.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10124 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


