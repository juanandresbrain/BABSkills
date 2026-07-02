# Job: PLM_ExtractedFilesProcessing

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["PLM_ExtractedFilesProcessing"]
    JOB --> PLM_ExtractedFilesProcessing_1["Step 1: PLM_ExtractedFilesProcessing [SSIS]"]`n```

## Steps

### Step 1: PLM_ExtractedFilesProcessing
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\PLM_ExtractedFilesProcessing\PLM_ExtractedFilesProcessing.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10159 /Par ToEmailAddresses;"\"SantiagoB@buildabear.com;DorisM@buildabear.com\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


